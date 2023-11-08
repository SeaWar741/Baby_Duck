import sys
from antlr4 import *
from antlr4 import TerminalNode
from utils.BabyDuckLexer import BabyDuckLexer
from utils.BabyDuckParser import BabyDuckParser
from utils.BabyDuckListener import BabyDuckListener   
from utils.BabyDuckVisitor import BabyDuckVisitor
from antlr4.tree.Trees import Trees
from semanticAnalyzer import SemanticAnalyzer
from semanticTable import DirFunc, VarTable



class Visitor(BabyDuckVisitor):
    def __init__(self):
        self.temp_counter = 0
        self.quadruples = []
        self.operand_stack = []
        self.operator_stack = []
        self.type_stack = []
        self.jump_stack = []
        self.precedence = {
            "(": 1,
            "+": 2,
            "-": 2,
            "*": 3,
            "/": 3,
        }
        self.Semantics = {
            'int': {
                'int': {
                    '+': 'int',
                    '-': 'int',
                    '*': 'int',
                    '/': 'int'
                },
                'float': {
                    '+': 'float',
                    '-': 'float',
                    '*': 'float',
                    '/': 'float'
                }
            },
            'float': {
                'int': {
                    '+': 'float',
                    '-': 'float',
                    '*': 'float',
                    '/': 'float'
                },
                'float': {
                    '+': 'float',
                    '-': 'float',
                    '*': 'float',
                    '/': 'float'
                }
            }
        }
        

    def printQuadruples(self):
        print("Quadruples")
        for i, quad in enumerate(self.quadruples):
            print(f"{i}: {quad}")

    def printStacks(self):
        print("Operand Stack")
        print(self.operand_stack)
        print("Operator Stack")
        print(self.operator_stack)
        print("Type Stack")
        print(self.type_stack)
        print("Jump Stack")
        print(self.jump_stack)

    def new_temporary(self):
        # Generate a new temporary variable
        temp_var = f"t{self.temp_counter}"
        self.temp_counter += 1
        return temp_var
    
    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False
        
    def check_semantic_cube(self, left_type, right_type, operator):
        """
        Check the semantic cube for the result type of an operation
        given the types of the left and right operands and the operator.
        """
        if left_type in self.Semantics and right_type in self.Semantics[left_type]:
            if operator in self.Semantics[left_type][right_type]:
                return self.Semantics[left_type][right_type][operator]
        raise TypeError(f"Incompatible types: {left_type} {operator} {right_type}")

    def process_operator(self):
        """
        Process the operator at the top of the operator stack by generating a quadruple.
        """
        right_operand = self.operand_stack.pop()
        right_type = self.type_stack.pop()
        left_operand = self.operand_stack.pop()
        left_type = self.type_stack.pop()
        operator = self.operator_stack.pop()

        # Check types using the semantic cube
        result_type = self.check_semantic_cube(left_type, right_type, operator)

        temp_var = self.new_temporary()
        self.generate_quadruple(operator, left_operand, right_operand, temp_var)
        self.operand_stack.append(temp_var)
        self.type_stack.append(result_type)  # Push the result type onto the type stack

    def generate_quadruple(self, operator, left_operand, right_operand, result):
        # Create a quadruple tuple and add it to the list of quadruples
        quadruple = (operator, left_operand, right_operand, result)
        self.quadruples.append(quadruple)

        # After adding the quadruple to the list, we need to handle the jump stack
        # for control flow operations like if-else and loops.
        if operator in ['JMPF', 'JMP', 'JMPT']:
            self.jump_stack.append(len(self.quadruples) - 1)

    def visitCte(self, ctx: BabyDuckParser.CteContext):
        # Return the text of the constant
        return ctx.getText()
    
    def visitUnary_expression(self, ctx: BabyDuckParser.Unary_expressionContext):
        print("Unary Expression")
        #split the operator and operand
        operator = ctx.getChild(0).getText()
        operand = self.visit(ctx.factor())

        #generate quadruple
        temp_var = self.new_temporary()
        self.generate_quadruple(operator, operand, None, temp_var)

        #append to operand stack
        self.operand_stack.append(temp_var)

        return temp_var
    
    def visitParenthesized_expression(self, ctx: BabyDuckParser.Parenthesized_expressionContext):
        return self.visit(ctx.expression())


    def visitFactor(self, ctx: BabyDuckParser.FactorContext):
        if ctx.parenthesized_expression():
            return self.visit(ctx.parenthesized_expression())
        elif ctx.unary_expression():
            return self.visit(ctx.unary_expression())
            
        else:
            # Handle ID or cte
            operand = ctx.getChild(0).getText()
            self.operand_stack.append(operand)
        
        #return last part of operand or none
        return self.operand_stack[-1]
    
    def visitExp(self, ctx: BabyDuckParser.ExpContext):
        print(ctx.getText())
        left = self.visit(ctx.termino(0))
        
        for i in range(1, len(ctx.termino())):
            operator = ctx.getChild(2 * i - 1).getText() #iterate on list of all children. gets the operator which is always second element each iterator
            right = self.visit(ctx.termino(i))
            
            if right is not None:
                #create new temporary
                temp_var = self.new_temporary()
                #generate quadruple
                self.generate_quadruple(operator, left, right, temp_var)
                
                #result is new temporary
                left = temp_var


        # Return the last operand, which is the result of the expression.
        return left

    def process_operator(self):
        right_operand = self.operand_stack.pop()
        left_operand = self.operand_stack.pop()
        operator = self.operator_stack.pop()
        temp_var = self.new_temporary()
        self.generate_quadruple(operator, left_operand, right_operand, temp_var)
        self.operand_stack.append(temp_var)

    def visitVar(self, ctx: BabyDuckParser.VarsContext):
        # Visit the expression to evaluate it and push the result onto the operand stack
        value = self.visit(ctx.expression())
        # The ID to which the value is assigned
        var_id = ctx.ID().getText()
        # Generate a quadruple for the assignment
        self.generate_quadruple('=', value, None, var_id)

    def visitTermino(self, ctx: BabyDuckParser.TerminoContext):
        result = self.visit(ctx.factor(0))

        for i in range(1, len(ctx.factor())):
            operator = ctx.getChild(2 * i - 1).getText()
            right = self.visit(ctx.factor(i))

            if right is not None:
                #create new temporary
                temp_var = self.new_temporary()
                #generate quadruple
                self.generate_quadruple(operator, result, right, temp_var)
                
                #result is new temporary
                result = temp_var   
        
        return result


    def visitAssign(self, ctx: BabyDuckParser.AssignContext):
        # Visit the expression to evaluate it and push the result onto the operand stack
        value = self.visit(ctx.expression())
        # The ID to which the value is assigned
        var_id = ctx.ID().getText()
        # Generate a quadruple for the assignment
        self.generate_quadruple('=', value, None, var_id)


    def visitExpression(self, ctx: BabyDuckParser.ExpressionContext):
        print(ctx.getText())
        if ctx.getChildCount() == 1:
            # If there is only one child, visit it and return the result
            return self.visit(ctx.exp(0))
        
        #visit left and right. Second is the operator
        elif ctx.getChildCount == 3:
            print(ctx.getText())
            left = self.visit(ctx.exp(0))
            right = self.visit(ctx.exp(1))

            operator = ctx.RELOP().getText()

            temp_var = self.new_temporary()

            self.generate_quadruple(operator, left, right, temp_var)

            #append to operand stack
            self.operand_stack.append(temp_var)

            return temp_var
        
        else:
            #if structure is wrong then error
            self.printQuadruples()
            raise ValueError(f"Unexpected expression format: {ctx.getText()}")





    

    def visitPrint(self, ctx: BabyDuckParser.PrintContext):
        # Visit all expressions or strings to be printed
        for print_item in ctx.expression() + ctx.STRING():
            # Check if print_item is an instance of TerminalNode, which is used for tokens
            if isinstance(print_item, TerminalNode):
                item = print_item.getText()
            else:
                item = self.visit(print_item)
            # Generate a quadruple for the print operation
            self.generate_quadruple('PRINT', item, None, None)




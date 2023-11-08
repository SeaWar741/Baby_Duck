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
        self.temp_counter = 0
        self.label_counter = 0
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
        
    #--------------------------------------------------------------
    #UTILITY METHODS
    #--------------------------------------------------------------

    def printQuadruples(self):
        print("Quadruples")
        for i, quad in enumerate(self.quadruples):
            print(f"{i}: {quad}")

    def printStacks(self):
        print("\nOperand Stack")
        print(self.operand_stack)

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
        # Create a quadruple list and add it to the list of quadruples
        quadruple = [operator, left_operand, right_operand, result]
        self.quadruples.append(quadruple)

        # After adding the quadruple to the list, we need to handle the jump stack
        # for control flow operations like if-else and loops.
        if operator in ['JMPF', 'JMP', 'JMPT']:
            self.jump_stack.append(len(self.quadruples) - 1)
    
    def new_label_or_placeholder(self, type):
        prefix = "L" if type == "label" else "P"
        value = f"{prefix}{self.label_counter}"
        self.label_counter += 1
        return value

    def backpatch(self, placeholder, label):
        for i, quad in enumerate(self.quadruples):
            if quad[3] == placeholder:
                # Convert the tuple to a list, make the change, then convert back to a tuple
                quad_list = list(quad)
                quad_list[3] = label
                self.quadruples[i] = tuple(quad_list)

    def backpatch2(self, placeholder, label):
        for i, quad in enumerate(self.quadruples):
            if quad[3] == placeholder:
                self.quadruples[i][3] = label

    #--------------------------------------------------------------
    #MiSCELANEOUS METHODS
    #--------------------------------------------------------------

    def visitCte(self, ctx: BabyDuckParser.CteContext):
        # Return the text of the constant
        return ctx.getText()
    
    def process_operator(self):
        right_operand = self.operand_stack.pop()
        left_operand = self.operand_stack.pop()
        operator = self.operator_stack.pop()
        temp_var = self.new_temporary()
        self.generate_quadruple(operator, left_operand, right_operand, temp_var)
        self.operand_stack.append(temp_var)

    def visitExpression(self, ctx: BabyDuckParser.ExpressionContext):
        
        if ctx.getChildCount() == 1:
            # If there is only one child, visit it and return the result
            return self.visit(ctx.exp(0))
        
        #visit left and right. Second is the operator
        elif ctx.getChildCount() == 3 and isinstance(ctx.getChild(1), BabyDuckParser.RelopContext):
            left = self.visit(ctx.exp(0))
            right = self.visit(ctx.exp(1))

            operator = ctx.relop().getText()

            temp_var = self.new_temporary()

            self.generate_quadruple(operator, left, right, temp_var)

            #append to operand stack
            self.operand_stack.append(temp_var)

            return temp_var
        
        else:
            #if structure is wrong then error
            raise ValueError(f"Unexpected expression format: {ctx.getText()}")


    #--------------------------------------------------------------
    #ARITHMETIC METHODS
    #--------------------------------------------------------------

    def visitExp(self, ctx: BabyDuckParser.ExpContext):
        terminos = ctx.termino()
        terminos_length = len(terminos)
        left = self.visit(terminos[0])
        
        for i in range(1, terminos_length):
            operator = ctx.getChild(2 * i - 1).getText()  # Gets the operator
            right = self.visit(terminos[i])
            
            if right is not None:
                # Create new temporary
                temp_var = self.new_temporary()
                # Generate quadruple
                self.generate_quadruple(operator, left, right, temp_var)
                
                # Result is new temporary
                left = temp_var

        # Return the last operand, which is the result of the expression.
        return left

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

    #--------------------------------------------------------------
    #LINEAR CONTROL FLOW METHODS
    #--------------------------------------------------------------

    def visitAssign(self, ctx: BabyDuckParser.AssignContext):
        # Visit the expression to evaluate it and push the result onto the operand stack
        value = self.visit(ctx.expression())
        # The ID to which the value is assigned
        var_id = ctx.ID().getText()
        # Generate a quadruple for the assignment
        self.generate_quadruple('=', value, None, var_id)

    def visitVar(self, ctx: BabyDuckParser.VarsContext):
        # Visit the expression to evaluate it and push the result onto the operand stack
        value = self.visit(ctx.expression())
        # The ID to which the value is assigned
        var_id = ctx.ID().getText()
        # Generate a quadruple for the assignment
        self.generate_quadruple('=', value, None, var_id)



    #--------------------------------------------------------------
    #NON-LINEAR CONTROL FLOW  METHODS
    #--------------------------------------------------------------

    def visitF_call(self, ctx: BabyDuckParser.F_callContext): 
        function_name = ctx.ID().getText()
        arg_count = 0
        args = ctx.expression()  # Get the list of expressions passed as arguments

        # Check if there are arguments
        if args:
            arg_count = len(args)

            for arg in args:
                arg_result = self.visit(arg)
                self.generate_quadruple("param", arg_result, None, None)

        self.generate_quadruple("call", function_name, arg_count, None)
        return None

    def visitCondition(self, ctx):
        condition = self.visit(ctx.expression())

        # Generate a placeholder for the false jump
        false_placeholder = self.new_label_or_placeholder("placeholder")

        # Generate the quadruple for the conditional jump
        self.quadruples.append(("if_false", condition, None, false_placeholder))

        # Visit the body of the if statement
        self.visit(ctx.body(0))

        end_if_placeholder = None
        if ctx.else_():
            # Generate a placeholder for the end of the if block
            end_if_placeholder = self.new_label_or_placeholder("placeholder")

            # Generate the quadruple to jump to the end of the if block
            self.quadruples.append(("goto", None, None, end_if_placeholder))

        # Backpatch the false jump with the actual label
        false_jump_label = self.new_label_or_placeholder("label")
        self.backpatch(false_placeholder, false_jump_label)

        if ctx.else_():
            # Visit the else body
            self.visit(ctx.body(1))

            # Backpatch the end if jump with the actual label
            end_if_label = self.new_label_or_placeholder("label")
            self.backpatch(end_if_placeholder, end_if_label)

    def visitCycle(self, ctx: BabyDuckParser.CycleContext):
        print("Entering cycle")
        # Generate the start label for the loop and push it onto the jump stack
        start_label = self.new_label_or_placeholder("label")
        self.jump_stack.append(("start", start_label))
        self.generate_quadruple("label", start_label, None, None)

        # Visit the expression to evaluate the loop's condition
        condition_result = self.visit(ctx.expression())

        # Generate a placeholder for the exit label and push it onto the jump stack
        exit_label_placeholder = self.new_label_or_placeholder("placeholder")
        self.jump_stack.append(("end", exit_label_placeholder))

        # Generate an 'if_false' quadruple that will jump to the exit label if the condition is false
        exit_index = self.generate_quadruple("if_false", condition_result, None, exit_label_placeholder)

        # Visit the body of the loop
        self.visit(ctx.body())

        # Generate a 'goto' quadruple to jump back to the start of the loop
        self.generate_quadruple("goto", start_label, None, None)

        # Generate the end label for the loop
        end_label = self.new_label_or_placeholder("")
        self.generate_quadruple("label", end_label, None, None)

        # Backpatch the 'if_false' jump to the end label
        self.backpatch2(exit_index, end_label)

        # Backpatch any 'end' jumps that are still on the jump stack
        while self.jump_stack and self.jump_stack[-1][0] == "end":
            _, placeholder = self.jump_stack.pop()
            self.backpatch2(placeholder, end_label)

        # The cycle does not produce a value, so return None
        return None

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



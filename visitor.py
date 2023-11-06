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
        self.temp_counter = 1
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
        for quad in self.quadruples:
            print(quad)

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

    def visitCte(self, ctx: BabyDuckParser.CteContext):
        # Return the text of the constant
        return ctx.getText()

    def visitFactor(self, ctx: BabyDuckParser.FactorContext):
        if ctx.parenthesized_expression():
            return self.visit(ctx.parenthesized_expression())
        elif ctx.unary_expression():
            return self.visit(ctx.unary_expression())
        else:
            # Handle ID or cte
            operand = ctx.ID().getText() if ctx.ID() else ctx.cte().getText()
            self.operand_stack.append(operand)
            return operand
    
    def visitExp(self, ctx: BabyDuckParser.ExpContext):
        left = self.visit(ctx.termino(0))
        
        for i in range(1, len(ctx.termino())):
            operator = ctx.getChild(2 * i - 1).getText()
            right = self.visit(ctx.termino(i))
            
            # Check operator precedence and handle stack accordingly
            while (self.operator_stack and
                self.precedence[self.operator_stack[-1]] >= self.precedence[operator]):
                self.process_operator()

            self.operator_stack.append(operator)
            self.operand_stack.append(right)

        # Process any remaining operators
        while self.operator_stack:
            self.process_operator()

        return self.operand_stack[-1]

    def process_operator(self):
        right_operand = self.operand_stack.pop()
        left_operand = self.operand_stack.pop()
        operator = self.operator_stack.pop()
        temp_var = self.new_temporary()
        self.generate_quadruple(operator, left_operand, right_operand, temp_var)
        self.operand_stack.append(temp_var)

    def visitUnaryExpression(self, ctx: BabyDuckParser.Unary_expressionContext):
        operator = ctx.getChild(0).getText()
        operand = self.visit(ctx.factor())

        # Check if the operand is a constant or a variable
        if isinstance(operand, (int, float)):
            # If it's a constant, apply the unary operator directly
            if operator == '-':
                value = -operand
            elif operator == '+':
                value = operand
            # Push the result onto the operand stack and return it
            self.operand_stack.append(value)
            return value
        else:
            # If it's not a constant (e.g., a variable or a temporary), generate a quadruple
            temp_var = self.new_temporary()
            self.generate_quadruple(operator, operand, None, temp_var)
            
            # Push the result of the unary operation onto the operand stack
            self.operand_stack.append(temp_var)
            return temp_var


    def visitTermino(self, ctx: BabyDuckParser.TerminoContext):
        left = self.visit(ctx.factor(0))

        for i in range(1, len(ctx.factor())):
            operator = ctx.getChild(2 * i - 1).getText()
            right = self.visit(ctx.factor(i))

            while (self.operator_stack and
                self.precedence[self.operator_stack[-1]] >= self.precedence[operator]):
                self.process_operator()

            self.operator_stack.append(operator)
            self.operand_stack.append(right)

        while self.operator_stack:
            self.process_operator()

        return self.operand_stack[-1]

    def visitAssign(self, ctx: BabyDuckParser.AssignContext):
        # Visit the expression to evaluate it and push the result onto the operand stack
        value = self.visit(ctx.expression())
        # The ID to which the value is assigned
        var_id = ctx.ID().getText()
        # Generate a quadruple for the assignment
        self.generate_quadruple('=', value, None, var_id)

    def visitCondition(self, ctx: BabyDuckParser.ConditionContext):
        # Visit the expression for the condition
        self.visit(ctx.expression())
        # Generate a quadruple for the conditional jump
        false_jump_quad = self.new_temporary()
        self.generate_quadruple('JMPF', self.operand_stack.pop(), None, false_jump_quad)
        # Visit the body of the if statement
        self.visit(ctx.body(0))
        # If there is an else statement, handle the jump to the end of the block
        if ctx.else_():
            end_jump_quad = self.new_temporary()
            self.generate_quadruple('JMP', None, None, end_jump_quad)
            # Update the false jump quadruple to jump to the else body
            self.quadruples[int(false_jump_quad[1:]) - 1] = ('JMPF', self.quadruples[int(false_jump_quad[1:]) - 1][1], None, len(self.quadruples))
            # Visit the body of the else statement
            self.visit(ctx.body(1))
            # Update the end jump quadruple to jump to the end of the if-else block
            self.quadruples[int(end_jump_quad[1:]) - 1] = ('JMP', None, None, len(self.quadruples))
        else:
            # Update the false jump quadruple to jump to the end of the if block
            self.quadruples[int(false_jump_quad[1:]) - 1] = ('JMPF', self.quadruples[int(false_jump_quad[1:]) - 1][1], None, len(self.quadruples))

    def visitCycle(self, ctx: BabyDuckParser.CycleContext):
        # Mark the beginning of the cycle for potential jumps
        start_quad = len(self.quadruples)
        # Visit the body of the while loop
        self.visit(ctx.body())
        # Visit the expression for the loop condition
        self.visit(ctx.expression())
        # Generate a quadruple to jump back to the start if the condition is true
        self.generate_quadruple('JMPT', self.operand_stack.pop(), None, start_quad)

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


    def visitFCall(self, ctx: BabyDuckParser.F_callContext):
        # Visit all expressions to be passed as arguments
        arguments = [self.visit(expr) for expr in ctx.expression()]
        # Generate a quadruple for the function call
        # Assuming the function returns a value and it should be stored in a temporary variable
        result = self.new_temporary()
        self.generate_quadruple('CALL', ctx.ID().getText(), arguments, result)
        # Push the result of the function call onto the operand stack
        self.operand_stack.append(result)


    def fix_jump_targets(self):
        for index, quad in enumerate(self.quadruples):
            if quad[0] in ['JMPF', 'JMP', 'JMPT']:
                jump_target = quad[3]
                # Check if jump_target is a string and starts with 't'
                if isinstance(jump_target, str) and jump_target.startswith('t'):
                    # Extract the number from the temporary variable name
                    target_index = self.temp_counter - int(jump_target[1:])
                    # Update the quadruple with the actual jump target index
                    self.quadruples[index] = (quad[0], quad[1], quad[2], target_index)
                elif isinstance(jump_target, int):
                    # If jump_target is already an integer, no action is needed
                    pass
                else:
                    # Handle unexpected jump_target format
                    raise ValueError(f"Unexpected format for jump target: {jump_target}")

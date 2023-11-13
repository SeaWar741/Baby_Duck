from antlr4 import *
from antlr4 import TerminalNode
from utils.BabyDuckParser import BabyDuckParser
from utils.BabyDuckVisitor import BabyDuckVisitor



class Visitor(BabyDuckVisitor):
    def __init__(self,varTables,functions_directory):
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
                    '/': 'int',
                    '<': 'bool',
                    '>': 'bool',
                    '!=': 'bool',
                },
                'float': {
                    '+': 'float',
                    '-': 'float',
                    '*': 'float',
                    '/': 'float',
                    '<': 'bool',
                    '>': 'bool',
                    '!=': 'bool',
                }
            },
            'float': {
                'int': {
                    '+': 'float',
                    '-': 'float',
                    '*': 'float',
                    '/': 'float',
                    '<': 'bool',
                    '>': 'bool',
                    '!=': 'bool',
                },
                'float': {
                    '+': 'float',
                    '-': 'float',
                    '*': 'float',
                    '/': 'float',
                    '<': 'bool',
                    '>': 'bool',
                    '!=': 'bool',
                }
            }
        }
        self.scope = "Global"

        self.quadCounter = 0

        self.global_vars = varTables['Global'].df
        self.varTables = varTables
        self.functions_directory = functions_directory

        self.insert_initial_goto()




    #--------------------------------------------------------------
    #UTILITY METHODS
    #--------------------------------------------------------------

    def printQuadruples(self):
        print("Quadruples\n")
        for i, quad in enumerate(self.quadruples):
            print(f"{i}: {quad}")

    def printStacks(self):
        print("\nOperand Stack: ", len(self.operand_stack))
        print(self.operand_stack)
        print()

        print("Type Stack: ", len(self.type_stack))
        print(self.type_stack)
        print()

        print("Functions Directory: ")
        print(self.functions_directory)
        print()

    def new_temporary(self):
        # Generate a new temporary variable
        temp_var = f"_t{self.temp_counter}" #to avoid issues if user decides to use t# as a variable name
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
    

    def generate_quadruple(self, operator, left_operand, right_operand, result,typeResult=None):
        # Create a quadruple list and add it to the list of quadruples

        #implement the datatype for result
        quadruple = [operator, left_operand, right_operand, result, self.scope, typeResult]
        self.quadruples.append(quadruple)

        # After adding the quadruple to the list, we need to handle the jump stack
        # for control flow operations like if-else and loops.
        if operator in ['JMPF', 'JMP', 'JMPT']:
            self.jump_stack.append(len(self.quadruples) - 1)
        
        self.quadCounter += 1


    def process_operator(self):
        right_operand = self.operand_stack.pop()
        left_operand = self.operand_stack.pop()
        operator = self.operator_stack.pop()


        self.generate_quadruple(operator, left_operand, right_operand, temp_var, result_type)



    
    def new_label_or_placeholder(self, type):
        prefix = "L" if type == "LABEL" else "P" #labels and placeholders are continuous, meaning they share the counter
        value = f"{prefix}{self.label_counter}"
        self.label_counter += 1
        return value

    def backpatch(self, placeholder, LABEL):
        for i, quad in enumerate(self.quadruples):
            if quad[3] == placeholder:
                # Convert the tuple to a list, make the change, then convert back to a tuple
                quad_list = list(quad)
                quad_list[3] = LABEL
                self.quadruples[i] = tuple(quad_list)

    def backpatch2(self, placeholder, LABEL):
        for i, quad in enumerate(self.quadruples):
            if quad[3] == placeholder:
                self.quadruples[i][3] = LABEL

    def lookup_type_from_variable(self, variable_name):
        # Implement the logic to find the type from a variable name
        # Check in global variables
        if variable_name in self.global_vars['id-name'].values:
            return self.global_vars.loc[self.global_vars['id-name'] == variable_name]['type'].values[0]
        #check in other variable tables
        for scope, var_table in self.varTables.items():
            if variable_name in var_table.df['id-name'].values:
                return var_table.df.loc[var_table.df['id-name'] == variable_name]['type'].values[0]

    #--------------------------------------------------------------
    #MiSCELANEOUS METHODS
    #--------------------------------------------------------------

    def insert_initial_goto(self):
        # Crear un marcador de posición para la dirección de 'main'
        main_placeholder = self.new_label_or_placeholder("placeholder")
        # Insertar el cuádruplo 'GOTO' al principio de la lista
        self.generate_quadruple("GOTO", None, None, main_placeholder)
        return main_placeholder
    
    def visitCte(self, ctx: BabyDuckParser.CteContext):
        # Return the text of the constant
        cte_text = ctx.getText()


        return cte_text
    
    def process_operator(self):
        right_operand = self.operand_stack.pop()
        left_operand = self.operand_stack.pop()
        operator = self.operator_stack.pop()
        temp_var = self.new_temporary()

        
        self.operand_stack.append(temp_var)
        

        self.generate_quadruple(operator, left_operand, right_operand, temp_var, result_type)


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

            #append to operand stack
            self.operand_stack.append(temp_var)
            


            self.generate_quadruple(operator, left, right, temp_var)


            return temp_var
        
        else:
            #if structure is wrong then error
            raise ValueError(f"Unexpected expression format: {ctx.getText()}")
    
    def visitMainSection(self, ctx: BabyDuckParser.MainSectionContext):
        #print("Main Section")
        #change scope
        self.scope = "Global"
        #HERE PERFORM THE BACKPATCHING of the GOTO initial
        
        #if there are no other functions, then the placeholder is the first quadruple  
        if self.label_counter == 1: #when the counter was only used for the GOTO main THEN the placeholder is the first quadruple
            #self.backpatch2('P0', main_label)
            self.visit(ctx.body())
            # Generate a quadruple for the end of the program
            self.generate_quadruple("END", None, None, None)
        else:
            main_label = self.new_label_or_placeholder("LABEL")
            self.backpatch2('P0', main_label)
            self.visit(ctx.body())
            # Generate a quadruple for the end of the program
            self.generate_quadruple("END", None, None, None)

    def visitFuncs(self, ctx: BabyDuckParser.FuncsContext):
        #set scope
        self.scope = ctx.ID()[0].getText()
        self.functions_directory.loc[self.functions_directory['id-name'] == self.scope, 'starting_quad'] = self.quadCounter
        self.visit(ctx.body())

        #set the quadCounter as the first quadruple of the functiondirectory
        self.functions_directory.loc[self.functions_directory['id-name'] == self.scope, 'ending_quad'] = self.quadCounter

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

                # Result is new temporary
                left = temp_var

                # Generate quadruple
                self.generate_quadruple(operator, left, right, temp_var)
                


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
        
        #append to operand stack
        self.operand_stack.append(temp_var)

        

        self.generate_quadruple(operator, operand, None, temp_var)

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
        # The ID to which the value is assigned
        var_id = ctx.ID().getText()



        # Visit the expression to evaluate it and push the result onto the operand stack
        value = self.visit(ctx.expression())
        # Generate a quadruple for the assignment
        self.generate_quadruple('=', value, None, var_id)

    
    #--------------------------------------------------------------
    #NON-LINEAR CONTROL FLOW  METHODS
    #--------------------------------------------------------------

    def visitF_call(self, ctx: BabyDuckParser.F_callContext): 
        function_name = ctx.ID().getText()
        scope = function_name
        arg_count = 0
        args = ctx.expression()  # Get the list of expressions passed as arguments

        # Check if there are arguments
        if args:
            arg_count = len(args)

            for arg in args:
                arg_result = self.visit(arg)
                self.generate_quadruple("PARAM", arg_result, None, None)

        self.generate_quadruple("CALL", function_name, arg_count, None)
        return None

    def visitCondition(self, ctx):
        condition = self.visit(ctx.expression())

        # Generate a placeholder for the false jump
        false_placeholder = self.new_label_or_placeholder("placeholder")

        # Generate the quadruple for the conditional jump
        self.quadruples.append(("GOTO_F", condition, None, false_placeholder,None))

        # Visit the body of the if statement
        self.visit(ctx.body(0))

        end_if_placeholder = None
        if ctx.else_():
            # Generate a placeholder for the end of the if block
            end_if_placeholder = self.new_label_or_placeholder("placeholder")

            # Generate the quadruple to jump to the end of the if block
            self.quadruples.append(("GOTO", None, None, end_if_placeholder,None))

        # Backpatch the false jump with the actual LABEL
        false_jump_label = self.new_label_or_placeholder("LABEL")
        self.backpatch(false_placeholder, false_jump_label)

        if ctx.else_():
            # Visit the else body
            self.visit(ctx.body(1))

            # Backpatch the end if jump with the actual LABEL
            end_if_label = self.new_label_or_placeholder("LABEL")
            self.backpatch(end_if_placeholder, end_if_label)

    def visitCycle(self, ctx: BabyDuckParser.CycleContext):
        # Generate the start LABEL for the loop and push it onto the jump stack
        start_label = self.new_label_or_placeholder("LABEL")
        self.jump_stack.append(("start", start_label))
        self.generate_quadruple("LABEL", start_label, None, None)

        # Visit the expression to evaluate the loop's condition
        condition_result = self.visit(ctx.expression())

        # Generate a placeholder for the exit LABEL and push it onto the jump stack
        exit_label_placeholder = self.new_label_or_placeholder("placeholder")
        self.jump_stack.append(("end", exit_label_placeholder))

        # Generate an 'GOTO_F' quadruple that will jump to the exit LABEL if the condition is false
        exit_index = self.generate_quadruple("GOTO_F", condition_result, None, exit_label_placeholder)

        # Visit the body of the loop
        self.visit(ctx.body())

        # Generate a 'GOTO' quadruple to jump back to the start of the loop
        self.generate_quadruple("GOTO", start_label, None, None)

        # Generate the end LABEL for the loop
        end_label = self.new_label_or_placeholder("")
        self.generate_quadruple("LABEL", end_label, None, None)

        # Backpatch the 'GOTO_F' jump to the end LABEL
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



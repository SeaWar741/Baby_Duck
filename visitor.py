from antlr4 import *
from antlr4 import TerminalNode
from utils.BabyDuckParser import BabyDuckParser
from utils.BabyDuckVisitor import BabyDuckVisitor



class Visitor(BabyDuckVisitor):
    def __init__(self,var_tables,functions_directory,debug=False):
            """
            Initializes the Visitor object with the given parameters.

            Args:
            - var_tables: A dictionary containing the variable tables for each scope.
            - functions_directory: A dictionary containing the functions directory.
            - debug: A boolean indicating whether to enable debug mode or not.
            """
            self.temp_counter = 0
            self.quadruples = []
            self.operand_stack = []
            self.operator_stack = []
            self.type_dict = {}
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
            self.debug = debug
            self.functions_directory = functions_directory
            self.varTables = var_tables
            self.insert_initial_goto()




    #--------------------------------------------------------------
    #UTILITY METHODS
    #--------------------------------------------------------------

    def printQuadruples(self):
        print("Quadruples\n")
        for i, quad in enumerate(self.quadruples):
            print(f"{i}: {quad}")

    def printStacks(self):
        print("\nOperand Stack")
        print(self.operand_stack)
        print()
        #print("Type Dictionary")
        #print(self.type_dict)
        print("Function Directory")
        print(self.functions_directory)

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

    def process_operator(self):
        right_operand = self.operand_stack.pop()
        left_operand = self.operand_stack.pop()
        operator = self.operator_stack.pop()


        temp_var = self.new_temporary()
        self.operand_stack.append(temp_var)

        self.generate_quadruple(operator, left_operand, right_operand, temp_var)

    def generate_quadruple(self, operator, left_operand, right_operand, result,targetType=None):
        
        #print(f"({operator},{left_operand},{right_operand},{result},{self.scope},{targetType})")
        #print(self.operand_stack)
        #print(self.type_dict)
        # Create a quadruple list and add it to the list of quadruples
        quadruple = [operator, left_operand, right_operand, result, self.scope, targetType]
        self.quadruples.append(quadruple)

        # After adding the quadruple to the list, we need to handle the jump stack
        # for control flow operations like if-else and loops.
        if operator in ['JMPF', 'JMP', 'JMPT']:
            self.jump_stack.append(len(self.quadruples) - 1)

        self.quadCounter += 1
    
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
        # Check in variable tables
        for scope, var_table in self.varTables.items():
            if variable_name in var_table.df['id-name'].values:
                return var_table.df.loc[var_table.df['id-name'] == variable_name]['type'].values[0]


    def get_type(self, operand):
        if self.is_number(operand):
            return "int" if operand.isdigit() else "float"
        elif operand in self.type_dict:
            return self.type_dict[operand]
        else:
            #check if bool
            if operand == "true" or operand == "false":
                return "bool"
            else:
                return None



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
        return ctx.getText()
    
    def process_operator(self):
        """
        This method processes an operator by popping the right and left operands and the operator from their respective stacks.
        It then generates a new temporary variable and appends it to the operand stack. The method then checks if the types of the operands are compatible with the operator using the semantic cube. 
        The result type is appended to the type dictionary and a quadruple is generated.
        """
        right_operand = self.operand_stack.pop()
        left_operand = self.operand_stack.pop()
        operator = self.operator_stack.pop()
        temp_var = self.new_temporary()
        self.operand_stack.append(temp_var)

        #get type of operands
        left_type = self.get_type(left_operand)
        right_type = self.get_type(right_operand)
        
        

        #check if types are compatible with operator
        result_type = self.check_semantic_cube(left_type,right_type,operator)
        #append to type dict
        self.type_dict[temp_var] = result_type
        #generate quadruple
        self.generate_quadruple(operator, left_operand, right_operand, temp_var,result_type)



    def visitExpression(self, ctx: BabyDuckParser.ExpressionContext):
        """
        Visits an expression node in the AST and generates the corresponding quadruples.
        If the expression has only one child, it visits it and returns the result.
        If the expression has three children and the second one is a relational operator, it visits the left and right children,
        generates the corresponding quadruple and returns the temporary variable where the result is stored.
        If the expression has a different structure, it raises a ValueError.
        :param ctx: The expression node in the AST.
        :return: The temporary variable where the result is stored.
        """
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

            #get type of operands
            left_type = self.get_type(left)
            right_type = self.get_type(right)

            if self.debug:
                print(f"left: {left} right: {right} operator: {operator}")

            #check if types are compatible with operator
            result_type = self.check_semantic_cube(left_type,right_type,operator)
            #append to type dict
            self.type_dict[temp_var] = result_type
            #generate quadruple
            self.generate_quadruple(operator, left, right, temp_var,result_type)

            

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
        #set the starting quadruple for this function in the directory
        self.functions_directory.loc[self.functions_directory['id-name'] == self.scope,'starting_quad'] = self.quadCounter
        
        self.visit(ctx.body())
        
        #set the ending quadruple for this function in the directory
        self.functions_directory.loc[self.functions_directory['id-name'] == self.scope,'ending_quad'] = self.quadCounter

    #--------------------------------------------------------------
    #ARITHMETIC METHODS
    #--------------------------------------------------------------

    def visitExp(self, ctx: BabyDuckParser.ExpContext):
        """
        Visits an expression node in the abstract syntax tree and generates quadruples for it.
        :param ctx: The expression context to visit.
        :return: The result of the expression.
        """
        terminos = ctx.termino()
        terminos_length = len(terminos)
        left = self.visit(terminos[0])
        
        for i in range(1, terminos_length):
            operator = ctx.getChild(2 * i - 1).getText()  # Gets the operator
            right = self.visit(terminos[i])

            if right is not None:
                # Create new temporary
                temp_var = self.new_temporary()


                #get type of operands
                left_type = self.get_type(left)
                right_type = self.get_type(right)

                #check if types are compatible with operator
                result_type = self.check_semantic_cube(left_type,right_type,operator)

                #append to operand stack
                self.operand_stack.append(temp_var)

                #append to type dict
                self.type_dict[temp_var] = result_type

                # Generate quadruple
                self.generate_quadruple(operator, left, right, temp_var,result_type)
                
                # Result is new temporary
                left = temp_var

        # Return the last operand, which is the result of the expression.
        return left

    def visitTermino(self, ctx: BabyDuckParser.TerminoContext):
            """
            Visits the TerminoContext node and generates quadruples for the expression.

            Args:
            - ctx: BabyDuckParser.TerminoContext object representing the current context.

            Returns:
            - result: The result of the expression.
            """
            result = self.visit(ctx.factor(0))

            for i in range(1, len(ctx.factor())):
                operator = ctx.getChild(2 * i - 1).getText()
                right = self.visit(ctx.factor(i))

                if right is not None:
                    #create new temporary
                    temp_var = self.new_temporary()

                    #get type of right
                    right_type = self.get_type(right)

                    #append to the type dict
                    self.type_dict[temp_var] = right_type

                    #append to operand stack
                    self.operand_stack.append(temp_var)

                    #generate quadruple
                    self.generate_quadruple(operator, result, right, temp_var,right_type)
                    
                    #result is new temporary
                    result = temp_var   
            
            return result

    def visitFactor(self, ctx: BabyDuckParser.FactorContext):
            """
            Visits the Factor rule of the BabyDuck grammar and returns the result of the visit.

            :param ctx: The FactorContext object representing the current parse tree node.
            :return: The result of the visit.
            """
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
        """
        Visits a Unary Expression node in the parse tree and generates a quadruple for it.

        :param ctx: The Unary_expressionContext node in the parse tree.
        :return: The temporary variable generated for the expression.
        """
        if self.debug:
            print("Unary Expression")
        
        #split the operator and operand
        operator = ctx.getChild(0).getText()
        operand = self.visit(ctx.factor())

        #generate quadruple
        temp_var = self.new_temporary()


        self.generate_quadruple(operator, operand, None, temp_var,)

        return temp_var
    
    def visitParenthesized_expression(self, ctx: BabyDuckParser.Parenthesized_expressionContext):
        return self.visit(ctx.expression())

    #--------------------------------------------------------------
    #LINEAR CONTROL FLOW METHODS
    #--------------------------------------------------------------

    def visitAssign(self, ctx: BabyDuckParser.AssignContext):
        """
        Visits the AssignContext node and generates a quadruple for the assignment.
        :param ctx: The AssignContext node to visit.
        :return: None
        """
        # Visit the expression to evaluate it and push the result onto the operand stack
        value = self.visit(ctx.expression())
        # The ID to which the value is assigned
        var_id = ctx.ID().getText()

        # Get the type of the variable
        var_type = self.lookup_type_from_variable(var_id)

        #append to operand stack
        self.operand_stack.append(var_id)

        #append to type dict
        self.type_dict[var_id] = var_type
        
        # Generate a quadruple for the assignment
        self.generate_quadruple('=', value, None, var_id,var_type)

    def visitVar(self, ctx: BabyDuckParser.VarsContext):
        """
        Visits a variable context and generates a quadruple for the assignment.

        :param ctx: The variable context to visit.
        :type ctx: BabyDuckParser.VarsContext
        """
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
        """
        Visits a function call node in the parse tree and generates the corresponding quadruples.
        
        :param ctx: The parse tree node representing the function call.
        :type ctx: BabyDuckParser.F_callContext
        :return: None
        """
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
            """
            Visits the condition node of an if statement and generates the corresponding quadruples.

            :param ctx: The context node of the condition.
            :type ctx: antlr4.tree.Tree
            """
            condition = self.visit(ctx.expression())

            # Generate a placeholder for the false jump
            false_placeholder = self.new_label_or_placeholder("placeholder")

            # Generate the quadruple for the conditional jump
            self.quadruples.append(("GOTO_F", condition, None, false_placeholder))

            # Visit the body of the if statement
            self.visit(ctx.body(0))

            end_if_placeholder = None
            if ctx.else_():
                # Generate a placeholder for the end of the if block
                end_if_placeholder = self.new_label_or_placeholder("placeholder")

                # Generate the quadruple to jump to the end of the if block
                self.quadruples.append(("GOTO_T", None, None, end_if_placeholder))

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
        """
        Visits a cycle node in the parse tree and generates quadruples for it.

        :param ctx: The cycle context node in the parse tree.
        :return: None
        """
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
            """
            Visits all expressions or strings to be printed and generates a quadruple for the print operation.

            :param ctx: The print context to visit.
            """
            for print_item in ctx.expression() + ctx.STRING():
                if isinstance(print_item, TerminalNode):
                    item = print_item.getText()
                else:
                    item = self.visit(print_item)
                self.generate_quadruple('PRINT', item, None, None)


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
import pandas as pd


class Listener(BabyDuckListener):
    def __init__(self):
        self.dir_func = DirFunc()
        self.var_table = VarTable()
        self.scope_stack = ["Global"]  # Initialize with global scope

    def exitVars(self, ctx: BabyDuckParser.VarsContext):
        # Determine the scope
        if isinstance(ctx.parentCtx, BabyDuckParser.FuncsContext):
            scope = ctx.parentCtx.ID()[0].getText()
        else:
            scope = "Global"

        # Iterate over the children of the VarsContext
        for i, child in enumerate(ctx.children):
            # Check if the child is a COLON token, which indicates the start of a type
            if isinstance(child, TerminalNode) and child.getSymbol().type == BabyDuckLexer.COLON:
                # The next child should be the type
                var_type = ctx.children[i + 1].getText()
                # Now, extract the associated IDs for this type
                j = i - 1
                while j >= 0 and isinstance(ctx.children[j], TerminalNode) and (ctx.children[j].getSymbol().type == BabyDuckLexer.ID or ctx.children[j].getSymbol().type == BabyDuckLexer.COMMA):
                    if ctx.children[j].getSymbol().type == BabyDuckLexer.ID:
                        var_name = ctx.children[j].getText()
                        print(f"Added variable: {var_name} | type: {var_type} | scope: {scope}")
                        self.var_table.add_var(var_name, var_type, scope=scope)
                    j -= 1
                    

    def exitStatement(self, ctx: BabyDuckParser.StatementContext):
        # Capture the entire text of the statement
        statement_text = ctx.getText()

        # Determine the type of the statement

        #ASSIGN
        if ctx.assign():
            statement_type = "Assignment"
            var_name = ctx.assign().ID().getText()
            expression = ctx.assign().expression().getText()
            # Check if the variable is declared
            if not self.is_var_declared(var_name):
                raise ValueError(f"Error: Undeclared variable {var_name}")

            print(f"Variable Name: {var_name} | Expression: {expression}")

        #CONDITION
        elif ctx.condition():
            statement_type = "Condition (if-else)"
            condition_text = ctx.condition().expression().getText()
            true_body = ctx.condition().body(0).getText()  # Body when condition is true
            if ctx.condition().body(1):  # Check if there's an 'else' body
                false_body = ctx.condition().body(1).getText()  # Body when condition is false
            else:
                false_body = "None"
            print(f"Condition: {condition_text}")
            print(f"If True: {true_body}")
            print(f"If False: {false_body}")


        #CYCLE
        elif ctx.cycle():
            statement_type = "Cycle (while-do)"
            while_body = ctx.cycle().body().getText()  # Body of the while loop
            do_expression = ctx.cycle().expression().getText()  # Expression after the 'do' keyword
            print(f"While Body: {while_body}")
            print(f"Do Expression: {do_expression}")


        elif ctx.f_call():
            statement_type = "Function Call"
            func_name = ctx.f_call().ID().getText()
            func_params = []
            if ctx.f_call().expression():
                func_params = [param.getText() for param in ctx.f_call().expression()]
                
                print(f"Function Name: {func_name} | Parameters: {func_params}")
            else:
                print(f"Function Name: {func_name} | No Parameters")

        print("")

    
    def enterFuncs(self, ctx: BabyDuckParser.FuncsContext):
        # Push the function name to the scope stack when entering a function
        func_name = ctx.ID()[0].getText()
        self.scope_stack.append(func_name)

    def exitFuncs(self, ctx: BabyDuckParser.FuncsContext):
        # Extract the function name
        func_name = ctx.ID()[0].getText()

        # Check if the function is already in the directory of functions
        if func_name in self.dir_func.df["id-name"].values:
            #print(f"Error: Multiple declaration of function {func_name}")
            raise ValueError(f"Error: Multiple declaration of function {func_name}")
        else:
            # Add the function to the directory of functions
            self.dir_func.add_func(func_name, "void", scope="Local")

            # Create a subtable for the function
            func_var_table = VarTable()

            # Iterate over the children of the FuncsContext
            for i, child in enumerate(ctx.children):
                # Check if the child is a COLON token, which indicates the start of a type
                if isinstance(child, TerminalNode) and child.getSymbol().type == BabyDuckLexer.COLON:
                    # The next child should be the type
                    var_type = ctx.children[i + 1].getText()
                    # Now, extract the associated IDs for this type
                    j = i - 1
    
    def exitAssign(self, ctx: BabyDuckParser.AssignContext):
        # Check if the variable being assigned to is declared
        var_name = ctx.ID().getText()
        if not self.is_var_declared(var_name):
            raise ValueError(f"Error: Undeclared variable {var_name}")

    def is_var_declared(self, var_name):
        # Check if a variable is declared in the current scope or any outer scope
        for scope in reversed(self.scope_stack):
            if self.var_table.df[(self.var_table.df["id-name"] == var_name) & (self.var_table.df["scope"] == scope)].shape[0] > 0:
                return True
        return False


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

        # Generate a quadruple for the unary operation
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

            



def main(argv):
    # Leer el archivo de entrada
    input_stream = FileStream(argv[1])
    
    # Tokenizar el archivo de entrada
    lexer = BabyDuckLexer(input_stream)
    stream = CommonTokenStream(lexer)
    
    # Parsear el archivo de entrada
    parser = BabyDuckParser(stream)

    tree = parser.program()  # 'program' es la regla inicial de la gramática

    # Crea una instancia del Listener y pasa la instancia a ParseTreeWalker
    listener = Listener()
    walker = ParseTreeWalker()

    walker.walk(listener, tree)

    if(tree.exception is None):
        print("\n---------------------------------------------------------------------")
        print("SIN ERROES DE SINTAXIS")
        print("---------------------------------------------------------------------\n")

    print("Directory of Functions")
    print(listener.dir_func.df)
    print("\nVariable Table")
    print(listener.var_table.df)    
    print("\n---------------------------------------------------------------------")
    print("PARSING COMPLETE")
    print("---------------------------------------------------------------------\n")


    # Create a visitor instance
    visitor = Visitor()
    visitor.visit(tree)
    visitor.printQuadruples()

    

if __name__ == '__main__':
    main(sys.argv)

import sys
from antlr4 import *
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

    def visitFactor(self, ctx: BabyDuckParser.FactorContext):
        # Check if the factor is a parenthesized expression
        if ctx.LPAREN() and ctx.RPAREN():
            # A parenthesized expression should be evaluated on its own terms.
            print(ctx.expression().getText())
            return self.visit(ctx.expression())
        else:
            unary_op = None
            operand = None

            # Check if there is a unary operator present
            if ctx.MINUS() or ctx.PLUS():
                unary_op = ctx.MINUS().getText() if ctx.MINUS() else ctx.PLUS().getText()
                # The operand follows the unary operator, which is the next child
                operand = self.visitChildren(ctx)  # This will visit the child nodes of the context
            else:
                operand = ctx.getText()

            # If there's a unary operator, handle the operation
            if unary_op:
                temp_var = self.new_temporary()
                # Generate a quadruple for the unary operation
                self.generate_quadruple(unary_op, operand, None, temp_var)
                # Push the result of the unary operation onto the operand stack
                self.operand_stack.append(temp_var)
            else:
                # Push the operand onto the operand stack
                self.operand_stack.append(operand)

            print("Operand stack: ", self.operand_stack)
            print("")
            return self.operand_stack[-1] if self.operand_stack else None
    
    def generate_quadruple(self, operator, left_operand, right_operand, result):
        # Create a quadruple tuple and add it to the list of quadruples
        quadruple = (operator, left_operand, right_operand, result)
        self.quadruples.append(quadruple)



    def visitExpression(self, ctx: BabyDuckParser.ExpressionContext):
        if ctx.getChildCount() == 1:
            # If there's only one child, it's just an 'exp'
            return self.visit(ctx.exp(0))

        elif ctx.getChildCount() == 3:
            # If there are three children, it's an 'exp' followed by a relational operator and another 'exp'
            lhs_result = self.visit(ctx.exp(0))
            rhs_result = self.visit(ctx.exp(1))
            
            # The relational operator will be the second child of the expression context
            rel_op = ctx.getChild(1).getText()
            
            temp_var = self.new_temporary()

            self.generate_quadruple(rel_op, lhs_result, rhs_result, temp_var)

            self.operand_stack.append(temp_var)
            
            return temp_var
        else:
            raise Exception("Unsupported expression structure")
        
    
    def visitTerm(self, ctx: BabyDuckParser.TerminoContext):
        # Start by visiting the first factor
        result = self.visit(ctx.factor(0))

        # Go through the operators and subsequent factors
        # Since the factors are separated by operators, the number of operators will be one less than the number of factors
        num_operators = len(ctx.factor()) - 1

        for i in range(num_operators):
            # The operator is located at odd indices in the children list (1, 3, 5, ...)
            operator = ctx.getChild(2 * i + 1).getText()
            # Visit the next factor
            right = self.visit(ctx.factor(i + 1))

            if right is not None:
                result_temp = self.new_temporary()

                # Generate a quadruple for the operation
                self.generate_quadruple(operator, result, right, result_temp)

                # The result of this operation will be used as the left operand
                # for the next operation (if any)
                result = result_temp

        return result



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
        print("Sin errores de sintaxis")

    print("---------------------------------------------------------------------")
    print("Directory of Functions")
    print(listener.dir_func.df)
    print("\nVariable Table")
    print(listener.var_table.df)
    print("\nPARSING COMPLETE")
    print("---------------------------------------------------------------------")


    # Create a visitor instance
    visitor = Visitor()
    visitor.visit(tree)
    visitor.printQuadruples()

    

if __name__ == '__main__':
    main(sys.argv)

import sys
from antlr4 import *
from antlr4 import TerminalNode
from utils.BabyDuckLexer import BabyDuckLexer
from utils.BabyDuckParser import BabyDuckParser
from utils.BabyDuckListener import BabyDuckListener   
from utils.BabyDuckVisitor import BabyDuckVisitor
from antlr4.tree.Trees import Trees
from semanticTable import DirFunc, VarTable
from visitor import Visitor
import pandas as pd


class Listener(BabyDuckListener):
    """
    Listener class that inherits from the generated BabyDuckListener class.
    This class defines methods that are called when the listener enters or exits a specific rule in the parse tree.
    It also contains methods for checking variable declarations and function calls.
    """
    def __init__(self, debug=False):
        """
        Constructor for the Listener class.
        Initializes the variable tables and scope stack, and sets the debug flag.
        """
        self.dir_func = DirFunc()
        self.var_tables = {"Global": VarTable()}  # Dictionary of variable tables, one for each scope
        self.scope_stack = ["Global"]  # Initialize with global scope
        self.debug = debug

    def exitVars(self, ctx: BabyDuckParser.VarsContext):
        """
        Method called when the listener exits the Vars rule in the parse tree.
        Extracts variable declarations and adds them to the current scope's variable table.
        """
        # The current scope is the top of the scope stack
        current_scope = self.scope_stack[-1]

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

                        #check the last memory direction on global variable table so that they dont overlap (local variable table) 
                        #TODO!!!

                        if self.debug:
                            print(f"Added variable: {var_name} | type: {var_type} | scope: {current_scope}")
                        # Add the variable to the current scope's variable table
                        self.var_tables[current_scope].add_var(var_name, var_type, scope=current_scope)
                    j -= 1

    def exitStatement(self, ctx: BabyDuckParser.StatementContext):
        """
        Method called when the listener exits the Statement rule in the parse tree.
        Determines the type of statement and extracts relevant information.
        """
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
            
            if self.debug:
                print(f"Variable Name: {var_name} | Expression: {expression}")

        #CONDITION
        elif ctx.condition():
            statement_type = "Condition (if-else)"
            parenthesized_expression_ctx = ctx.condition().expression().getText()

            if self.debug:
                print(f"Condition Expression: {parenthesized_expression_ctx}")

            # Check if the true body of the condition is present
            if ctx.condition().body():
                # Get the statements within the true body
                true_body_ctx = ctx.condition().body(0).statement()
                true_body = ' '.join([statement.getText() for statement in true_body_ctx])

                if self.debug:
                    print(f"True Body: {true_body}")
            else:
                if self.debug:
                    print("No true body found for the condition.")

            # Initialize false_body as None
            false_body = None

            # Check if there's an 'else' body by counting the number of body contexts
            if len(ctx.condition().body()) > 1:
                # Get the statements within the false body
                false_body_ctx = ctx.condition().body(1).statement()
                false_body = ' '.join([statement.getText() for statement in false_body_ctx])

                if self.debug:
                    print(f"False Body: {false_body}")
            else:

                if self.debug:
                    print("No false body found for the condition.")

        #CYCLE
        elif ctx.cycle():
            statement_type = "Cycle (while-do)"
            while_body = ctx.cycle().body().getText()  # Body of the while loop
            do_expression = ctx.cycle().expression().getText()  # Expression after the 'do' keyword

            if self.debug:
                print(f"While Body: {while_body}")
                print(f"Do Expression: {do_expression}")


        elif ctx.f_call():
            statement_type = "Function Call"
            func_name = ctx.f_call().ID().getText()
            func_params = []
            if ctx.f_call().expression():
                func_params = [param.getText() for param in ctx.f_call().expression()]
                
                if self.debug:
                    print(f"Function Name: {func_name} | Parameters: {func_params}")
            else:
                if self.debug:
                    print(f"Function Name: {func_name} | No Parameters")
                
        if self.debug:
            print("")

    def enterFuncs(self, ctx: BabyDuckParser.FuncsContext):
        """
        Method called when the listener enters the Funcs rule in the parse tree.
        Pushes the function name to the scope stack and creates a new variable table for the function scope.
        """
        # Push the function name to the scope stack when entering a function
        func_name = ctx.ID()[0].getText()
        self.scope_stack.append(func_name)
        # Create a new variable table for this function scope
        self.var_tables[func_name] = VarTable()
        
        # Add the function to the directory of functions
        func_type = "void"  # Placeholder for function type, adjust as needed
        self.dir_func.add_func(func_name, func_type, scope=func_name)

    def exitFuncs(self, ctx: BabyDuckParser.FuncsContext):
        """
        Method called when the listener exits the Funcs rule in the parse tree.
        Pops the function name from the scope stack.
        """
        # Pop the function name from the scope stack when exiting a function
        self.scope_stack.pop()
    
    def exitAssign(self, ctx: BabyDuckParser.AssignContext):
        """
        Method called when the listener exits the Assign rule in the parse tree.
        Checks if the variable being assigned to is declared.
        """
        # Check if the variable being assigned to is declared
        var_name = ctx.ID().getText()
        if not self.is_var_declared(var_name):
            raise ValueError(f"Error: Undeclared variable {var_name}")

    def is_var_declared(self, var_name):
        """
        Method for checking if a variable is declared in the current scope or any outer scope.
        """
        # Check if a variable is declared in the current scope or any outer scope
        for scope in reversed(self.scope_stack):
            if var_name in self.var_tables[scope].df["id-name"].values:
                return True
        return False

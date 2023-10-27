import sys
from antlr4 import *
from BabyDuckLexer import BabyDuckLexer
from BabyDuckParser import BabyDuckParser
from BabyDuckListener import BabyDuckListener   
from antlr4.tree.Trees import Trees
from semanticAnalyzer import SemanticAnalyzer
from semanticTable import SemanticTable

#helper funcions to debug
""" class Listener(BabyDuckListener):
    def exitVars(self, ctx: BabyDuckParser.VarsContext):
        print("var " + ctx.getText())

        return super().exitVars(ctx)
    def exitStatement(self, ctx: BabyDuckParser.StatementContext):
        print("statement " + ctx.getText())
        return super().exitStatement(ctx)  """

class Listener(BabyDuckListener):
    def __init__(self):
        self.semantic_table = SemanticTable()  # Create an instance of the SemanticTable class

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
                    j -= 1


    def exitStatement(self, ctx: BabyDuckParser.StatementContext):
        # Capture the entire text of the statement
        statement_text = ctx.getText()

        # Determine the type of the statement
        if ctx.assign():
            statement_type = "Assignment"
        elif ctx.condition():
            statement_type = "Condition (if-else)"
        elif ctx.cycle():
            statement_type = "Cycle (while-do)"
        elif ctx.f_call():
            statement_type = "Function Call"
        elif ctx.print_():  # Note the underscore here
            statement_type = "Print"
        else:
            statement_type = "Unknown"

        # Print the captured statement and its type
        print(f"Statement Type: {statement_type} | Text: {statement_text}")


def main(argv):
    # Leer el archivo de entrada
    input_stream = FileStream(argv[1])
    
    # Tokenizar el archivo de entrada
    lexer = BabyDuckLexer(input_stream)
    stream = CommonTokenStream(lexer)
    
    # Parsear el archivo de entrada
    parser = BabyDuckParser(stream)

    tree = parser.program()  # 'program' es la regla inicial de la gramática


    #parser.addParseListener(Listener())
    
    # Crea una instancia del Listener y pasa la instancia a ParseTreeWalker
    listener = Listener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    
    if(tree.exception is None):
        print("Sin errores de sintaxis")
    

if __name__ == '__main__':
    main(sys.argv)

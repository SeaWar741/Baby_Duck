import sys
from antlr4 import *
from BabyDuckLexer import BabyDuckLexer
from BabyDuckParser import BabyDuckParser
from BabyDuckListener import BabyDuckListener   
from antlr4.tree.Trees import Trees

class Listener(BabyDuckListener):
    def exitVars(self, ctx: BabyDuckParser.VarsContext):
        print("var " + ctx.getText())

        return super().exitVars(ctx)
    def exitStatement(self, ctx: BabyDuckParser.StatementContext):
        print("statement " + ctx.getText())
        return super().exitStatement(ctx)
    

def main(argv):
    # Leer el archivo de entrada
    input_stream = FileStream(argv[1])
    
    # Tokenizar el archivo de entrada
    lexer = BabyDuckLexer(input_stream)
    stream = CommonTokenStream(lexer)
    
    # Parsear el archivo de entrada
    parser = BabyDuckParser(stream)
    #parser.addParseListener(Listener())
    tree = parser.program()  # 'program' es la regla inicial de la gramática
    if(tree.exception is None):
        print("Sin errores de sintaxis")

if __name__ == '__main__':
    main(sys.argv)

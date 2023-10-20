import sys
from antlr4 import *
from BabyDuckLexer import BabyDuckLexer
from BabyDuckParser import BabyDuckParser
from antlr4.tree.Trees import Trees

def main(argv):
    # Leer el archivo de entrada
    input_stream = FileStream(argv[1])
    
    # Tokenizar el archivo de entrada
    lexer = BabyDuckLexer(input_stream)
    stream = CommonTokenStream(lexer)
    
    # Parsear el archivo de entrada
    parser = BabyDuckParser(stream)
    tree = parser.program()  # 'program' es la regla inicial de la gramática

if __name__ == '__main__':
    main(sys.argv)

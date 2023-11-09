import sys
from antlr4 import *
from utils.BabyDuckLexer import BabyDuckLexer
from utils.BabyDuckParser import BabyDuckParser
from visitor import Visitor
from listener import Listener


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

    print("\n---------------------------------------------------------------------")
    print("PARSING COMPLETE")
    print("---------------------------------------------------------------------\n")

    # Print the Directory of Functions
    print("Directory of Functions:")
    print(listener.dir_func.df)

    # Print the Variable Tables for each scope
    print("\nVariable Tables by Scope:")
    for scope, var_table in listener.var_tables.items():
        print(f"\nScope: {scope}")
        print(var_table.df)

    print("\n---------------------------------------------------------------------")
    print("END OF PARSING")
    print("---------------------------------------------------------------------\n")


    # Create a visitor instance
    visitor = Visitor()
    visitor.visit(tree)
    visitor.printQuadruples()
    visitor.printStacks()
    

if __name__ == '__main__':
    main(sys.argv)

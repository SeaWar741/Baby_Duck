import sys
from antlr4 import *
from utils.BabyDuckLexer import BabyDuckLexer
from utils.BabyDuckParser import BabyDuckParser
from visitor import Visitor
from listener import Listener
from semanticTable import Directions
from vm import VirtualMachine




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
    functions_directory = listener.dir_func.df
    print("Directory of Functions:")
    print(functions_directory)

    # Print the Variable Tables for each scope
    var_tables = listener.var_tables
    print("\nVariable Tables by Scope:")
    for scope, var_table in var_tables.items():
        print(f"\nScope: {scope}")
        print(var_table.df)

    print("\n---------------------------------------------------------------------")
    print("END OF PARSING")
    print("---------------------------------------------------------------------\n")


    # Create a visitor instance
    visitor = Visitor(var_tables, functions_directory)
    visitor.visit(tree)
    visitor.printQuadruples()
    visitor.printStacks()
    
    print("\n---------------------------------------------------------------------")
    print("END OF VISITING")
    print("---------------------------------------------------------------------\n")

    # Create an instance of virtual machine
    #vm = VirtualMachine(visitor.quadruples, var_tables, functions_directory)
    #vm.run()



if __name__ == '__main__':
    main(sys.argv)

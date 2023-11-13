import sys
from antlr4 import *
from utils.BabyDuckLexer import BabyDuckLexer
from utils.BabyDuckParser import BabyDuckParser
from visitor import Visitor
from listener import Listener
from semanticTable import Directions
from vm import VirtualMachine

def dataframe_to_dict(df):
    # Initialize an empty dictionary
    global_vars = {}
    
    # Iterate over the DataFrame rows
    for index, row in df.iterrows():
        # Use 'id-name' as the key and create a nested dictionary with 'value'
        # If 'value' is None, it can be set to a default value or kept as None
        global_vars[row['id-name']] = {'value': row['value'] or 0}  # Replace 0 with the desired default value
    
    return global_vars


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
    visitor = Visitor()
    visitor.visit(tree)
    visitor.printQuadruples()
    visitor.printStacks()
    
    print("\n---------------------------------------------------------------------")
    print("END OF VISITING")
    print("---------------------------------------------------------------------\n")

    # Create a Virtual Machine instance
    virtual_machine = VirtualMachine(visitor.quadruples, var_tables, functions_directory)

    # Execute the quadruples
    virtual_machine.run()


if __name__ == '__main__':
    main(sys.argv)

import sys
import argparse
from antlr4 import *
from utils.BabyDuckLexer import BabyDuckLexer
from utils.BabyDuckParser import BabyDuckParser
from antlr4.error.ErrorListener import ErrorListener
from semanticTable import Directions
from visitor import Visitor
from listener import Listener
from vm import VirtualMachine


class CustomErrorListener(ErrorListener):
    """
    A custom error listener for handling syntax errors in the Baby Duck language.

    Args:
        ErrorListener: The base class for error listeners in ANTLR4.

    Attributes:
        None

    Methods:
        syntaxError: Called by ANTLR4 when a syntax error is encountered.
    """
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        """
        Called by ANTLR4 when a syntax error is encountered.

        Args:
            recognizer: The parser or lexer where the error occurred.
            offendingSymbol: The token that caused the error.
            line: The line number where the error occurred.
            column: The column number where the error occurred.
            msg: The error message.
            e: The exception that caused the error.

        Returns:
            None
        """
        print(f"Syntax error at line {line}, column {column}: {msg}")
        sys.exit(1)  # Salir con un código de error


def main(argv):
    """
    This function is the entry point of the Baby Duck compiler. It takes in command-line arguments and uses them to
    read, tokenize, parse, and interpret a Baby Duck program.

    Args:
        argv (list): A list of command-line arguments. The first argument should be the path to the input file. The
        optional "--debug" flag can be used to enable debugging output.

    Raises:
        Exception: If there is a syntax error in the input file.

    Returns:
        None
    """
    
    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="input file path")
    parser.add_argument("--debug", help="enable debugging", action="store_true")
    args = parser.parse_args(argv[1:])

    # Leer el archivo de entrada
    input_stream = FileStream(args.input_file)

    # Tokenizar el archivo de entrada
    lexer = BabyDuckLexer(input_stream)
    stream = CommonTokenStream(lexer)
    
    # Parsear el archivo de entrada
    parser = BabyDuckParser(stream)
    parser.removeErrorListeners()  # Elimina los listeners de error por defecto
    parser.addErrorListener(CustomErrorListener())  # Añade tu custom listener
    
    
    tree = parser.program()  # 'program' es la regla inicial de la gramática

    # Crea una instancia del Listener y pasa la instancia a ParseTreeWalker
    listener = Listener(debug=args.debug)
    walker = ParseTreeWalker()

    walker.walk(listener, tree)

    if(tree.exception is None):

        # Print the Directory of Functions
        functions_directory = listener.dir_func.df


        # Print the Variable Tables for each scope
        var_tables = listener.var_tables



        # Create a visitor instance
        visitor = Visitor(var_tables, functions_directory,debug=args.debug)
        visitor.visit(tree)

        
        
        if args.debug:
            visitor.printQuadruples()
            visitor.printStacks()
        

        # Create an instance of virtual machine
        vm = VirtualMachine(visitor.quadruples, visitor.varTables, visitor.functions_directory,visitor.type_dict,visitor.operand_stack,debug=args.debug)
        vm.run()

    else:
        raise Exception("Syntax Error")


if __name__ == '__main__':
    main(sys.argv)

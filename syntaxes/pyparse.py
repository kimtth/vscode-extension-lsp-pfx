import os
import sys  
from antlr4 import *  
from antlr4_parser.powerfx.PowerFxLexer import PowerFxLexer
from antlr4_parser.powerfx.PowerFxParser import PowerFxParser  
from antlr4.error.ErrorListener import ErrorListener  
  
  
class MyErrorListener(ErrorListener):  
    def __init__(self):  
        super(MyErrorListener, self).__init__()  
  
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):  
        print(f"Syntax error at line {line}, column {column}: {msg}")  
  
  
def main(script_path: str):  
    # Read input  
    input_stream = FileStream(script_path, encoding='utf-8')  
  
    # Initialize lexer  
    lexer = PowerFxLexer(input_stream)  
    stream = CommonTokenStream(lexer)  
  
    # Initialize parser  
    parser = PowerFxParser(stream)  
  
    # Add custom error listener  
    error_listener = MyErrorListener()  
    parser.removeErrorListeners()  
    parser.addErrorListener(error_listener)  
  
    # Parse the input (starting from the entry point 'expressionUnit')  
    tree = parser.expressionUnit()  
  
    # Print the parse tree  
    print(tree.toStringTree(recog=parser))  
  
  
if __name__ == "__main__":  
    script_dir_base = os.path.dirname(os.path.realpath(__file__))
    script_dir_path = os.path.join(script_dir_base, 'powerfx-script-sample')
    script_path = os.path.join(script_dir_path, 'test1.pfx')
    main(script_path)  

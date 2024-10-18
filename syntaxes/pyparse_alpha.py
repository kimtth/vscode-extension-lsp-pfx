import os
from antlr4 import *
from antlr4_parser.powerfx_alpha.PowerFxAlphaLexer import PowerFxAlphaLexer
from antlr4_parser.powerfx_alpha.PowerFxAlphaParser import PowerFxAlphaParser
from antlr4.error.ErrorListener import ErrorListener


class MyErrorListener(ErrorListener):
    def __init__(self):
        super(MyErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"Syntax error at line {line}, column {column}: {msg}")


def parse_by_string(script: str):
    # Initialize lexer
    input_stream = InputStream(script)
    lexer = PowerFxAlphaLexer(input_stream)
    stream = CommonTokenStream(lexer)

    # Initialize parser
    parser = PowerFxAlphaParser(stream)

    # Add custom error listener
    error_listener = MyErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    # Parse the input (starting from the entry point 'expressionUnit')
    tree = parser.expressionUnit()

    # Print the parse tree
    print(tree.toStringTree(recog=parser))

    return tree


"""
To get the function name, we need to traverse the parse tree and look for the FunctionIdentifierContext and FunctionCallContext nodes.
"""
def function_identifier(node):
    if PowerFxAlphaParser.FunctionIdentifierContext is type(node):
        print(f"func-identifier: {node.getText()}")

    if PowerFxAlphaParser.FunctionCallContext is type(node):
        print(f"func-call: {node.getText()}")


def traverse_tree(node):
    # Recursively traverse the children of the current node
    if hasattr(node, "children"):
        assert isinstance(node.children, list)
        for child in node.children:
            traverse_tree(child)
            function_identifier(child)


def parse_by_file_path(script_path: str):
    # Read input
    input_stream = FileStream(script_path, encoding="utf-8")

    # Initialize lexer
    lexer = PowerFxAlphaLexer(input_stream)
    stream = CommonTokenStream(lexer)

    # Initialize parser
    parser = PowerFxAlphaParser(stream)

    # Add custom error listener
    error_listener = MyErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    # Parse the input (starting from the entry point 'expressionUnit')
    tree = parser.expressionUnit()

    for node in tree.children:
        # print(type(node))
        traverse_tree(node)

    # Print the parse tree
    # print(tree.toStringTree(recog=parser))

    return tree


if __name__ == "__main__":
    script_dir_base = os.path.dirname(os.path.realpath(__file__))
    script_dir_path = os.path.join(script_dir_base, "powerfx-script-sample")
    script_path = os.path.join(script_dir_path, "test1-alpha.pfa")
    # parse_by_file_path(script_path)
    print("-" * 50)
    script_path = os.path.join(script_dir_path, "test2-alpha.pfa")
    # parse_by_file_path(script_path)
    script_path = os.path.join(script_dir_path, "test3-alpha.pfa")
    parse_by_file_path(script_path)

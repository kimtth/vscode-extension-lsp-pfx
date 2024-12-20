from collections.abc import Iterable
from dataclasses import dataclass
import os
from typing import List
from antlr4 import *
from antlr4_parser.powerfx_alpha.PowerFxAlphaLexer import PowerFxAlphaLexer
from antlr4_parser.powerfx_alpha.PowerFxAlphaParser import PowerFxAlphaParser
from antlr4.error.ErrorListener import ErrorListener


@dataclass
class SyntaxError:
    line: int
    column: int
    msg: str


class ExternalHandler:
    def __init__(self):
        self.error_messages = []

    def handle_syntax_error(self, line, column, msg):
        se = SyntaxError(line, column, msg)
        # keep last 5 messages
        if len(self.error_messages) >= 5:
            self.error_messages = []
        self.error_messages.append(se)

    def get_syntax_error_messages(self):
        return self.error_messages


class MyErrorListener(ErrorListener):
    def __init__(self, external_handler: ExternalHandler = None):
        super(MyErrorListener, self).__init__()
        self.external_handler = external_handler

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        if self.external_handler:
            self.external_handler.handle_syntax_error(line, column, msg)
        else:
            print(f"Syntax error at line {line}, column {column}: {msg}")


def parse_by_string(script: str):
    # Initialize lexer
    input_stream = InputStream(script)
    lexer = PowerFxAlphaLexer(input_stream)
    stream = CommonTokenStream(lexer)

    # Initialize parser
    parser = PowerFxAlphaParser(stream)

    # Add custom error listener
    external_handler = ExternalHandler()
    error_listener = MyErrorListener(external_handler)
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    # Parse the input (starting from the entry point 'expressionUnit')
    tree = parser.expressionUnit()

    # Print the parse tree
    # print(tree.toStringTree(recog=parser))

    return tree


"""
To get the function name, we need to traverse the parse tree and look for the FunctionIdentifierContext and FunctionCallContext nodes.
"""


def is_function_identifier(node):
    if PowerFxAlphaParser.FunctionIdentifierContext is type(node):

        # print(f"func-identifier: {node.getText()}")
        return True

    if PowerFxAlphaParser.FunctionCallContext is type(node):
        # print(f"func-call: {node.getText()}")
        return True

    return False


def traverse_tree(node, func_nodes: List):
    # Recursively traverse the children of the current node
    if hasattr(node, "children"):
        # check is iterable
        if isinstance(node.children, Iterable):
            for child in node.children:
                traverse_tree(child, func_nodes)
                if is_function_identifier(child):
                    func_nodes.append(child)
                else:
                    continue

    return func_nodes


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

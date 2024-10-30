from enum import Enum
import re
import time
from typing import List
from pygls.lsp.server import LanguageServer
from pygls.workspace import TextDocument
from lsprotocol import types
from common.pyparse_alpha import parse_by_string, traverse_tree
from common.const import Const


class PowerFXAlphaLanguageServer(LanguageServer):
    def __init__(self, *args):
        super().__init__(*args)
        self.index = {}

    def parse(self, doc: TextDocument):
        funcdefs = {}
        try:
            document_text = doc.source
            if Const.FUNC_DEF in document_text:
                tree = parse_by_string(document_text)
                func_nodes = []
                for node in traverse_tree(tree, func_nodes):
                    if node:
                        # print(node.getText())
                        function_name = node.getText()
                        start_char_pos = node.start.start
                        end_char_pos = node.start.stop
                        linum = node.start.line

                        funcdefs[function_name] = types.Range(
                            start=types.Position(line=linum, character=start_char_pos),
                            end=types.Position(line=linum, character=end_char_pos),
                        )

                self.index[doc.uri] = {"functions": funcdefs}

        except Exception as e:
            print(f"Error parsing document: {e}")
            return


server = PowerFXAlphaLanguageServer("powerfxalpha-server", "v0.1")


# Completion feature
@server.feature(
    types.TEXT_DOCUMENT_COMPLETION,
    types.CompletionOptions(trigger_characters=["D", "De"]),
)
def completions(ls: PowerFXAlphaLanguageServer, params: types.CompletionParams):
    document = ls.workspace.get_text_document(params.text_document.uri)
    current_line = document.lines[params.position.line].strip()

    if not current_line.startswith("D"):
        return []

    return [
        types.CompletionItem(label="Define "),
        types.CompletionItem(label="Define {{}}"),
    ]


# Hover feature
@server.feature(types.TEXT_DOCUMENT_HOVER)
def hover(ls: PowerFXAlphaLanguageServer, params: types.HoverParams):
    pos = params.position
    document_uri = params.text_document.uri
    document = ls.workspace.get_text_document(document_uri)

    try:
        line = document.lines[pos.line]
    except IndexError:
        return None

    hover_content = [
        "```",
        "PowerFXAlpha Hover Content: ",
        f" echo ... {line.strip()}",
        "```",
    ]

    return types.Hover(
        contents=types.MarkupContent(
            kind=types.MarkupKind.Markdown,
            value="\n".join(hover_content),
        ),
        range=types.Range(
            start=types.Position(line=pos.line, character=0),
            end=types.Position(line=pos.line + 1, character=0),
        ),
    )


# Custom command - Simple notification
CHAT_REQUEST = "chat/request"
CHAT_RESPONSE = "chat/response"
@server.feature(CHAT_REQUEST)
async def handle_chat_message(ls: PowerFXAlphaLanguageServer, params):
    """
    Handle incoming chat messages from the client.
    """
    if hasattr(params, "message"):
        message = params.message
        # Optionally, send a response or notification to the client
        ls.protocol.notify(CHAT_RESPONSE, {"message": f"Message received! {message}"})


# Custom command - Chat
CAT_CHAT_REQUEST = "catChat/request"
@server.feature(CAT_CHAT_REQUEST)
async def handle_cat_chat_message(ls: PowerFXAlphaLanguageServer, params):
    """
    Handle incoming chat messages from the client.
    """
    if hasattr(params, "messages"):
        messages = params.messages
        # TODO - OpenAI call
        last_message = messages[-1]
        response = {'text': [last_message, 'meow']}
        return response



@server.feature(types.TEXT_DOCUMENT_DID_OPEN)
def did_open(ls: PowerFXAlphaLanguageServer, params: types.DidOpenTextDocumentParams):
    """Parse each document when it is opened"""
    doc = ls.workspace.get_text_document(params.text_document.uri)
    ls.parse(doc)


@server.feature(types.TEXT_DOCUMENT_DID_CHANGE)
def did_change(ls: PowerFXAlphaLanguageServer, params: types.DidOpenTextDocumentParams):
    """Parse each document when it is changed"""
    doc = ls.workspace.get_text_document(params.text_document.uri)
    ls.parse(doc)
    time.sleep(
        2
    )  # Sleep for a second to prevent invoking the parse function multiple times.


@server.feature(types.TEXT_DOCUMENT_RENAME)
def rename(ls: PowerFXAlphaLanguageServer, params: types.RenameParams):
    """Rename the symbol at the given position."""
    doc = ls.workspace.get_text_document(params.text_document.uri)
    index = ls.index.get(doc.uri)
    if index is None:
        return None

    word = doc.word_at_position(params.position)
    is_object = any([word in index[name] for name in index])
    if not is_object:
        return None

    edits: List[types.TextEdit] = []
    for linum, line in enumerate(doc.lines):
        for match in re.finditer(f"\\b{word}\\b", line):
            edits.append(
                types.TextEdit(
                    new_text=params.new_name,
                    range=types.Range(
                        start=types.Position(line=linum, character=match.start()),
                        end=types.Position(line=linum, character=match.end()),
                    ),
                )
            )

    return types.WorkspaceEdit(changes={params.text_document.uri: edits})


@server.feature(types.TEXT_DOCUMENT_PREPARE_RENAME)
def prepare_rename(ls: PowerFXAlphaLanguageServer, params: types.PrepareRenameParams):
    """Called by the client to determine if renaming the symbol at the given location
    is a valid operation."""
    doc = ls.workspace.get_text_document(params.text_document.uri)
    index = ls.index.get(doc.uri)
    if index is None:
        return None

    word = doc.word_at_position(params.position)
    is_object = any([word in index[name] for name in index])
    if not is_object:
        return None

    # At this point, we can rename this symbol.
    #
    # For simplicity we can tell the client to use its default behaviour however, it's
    # relatively new to the spec (LSP v3.16+) so a production server should check the
    # client's capabilities before responding in this way
    return types.PrepareRenameDefaultBehavior(default_behavior=True)


if __name__ == "__main__":
    """
    pygls supports TCP, STDIO and WEBSOCKET connections.
      1. https://pygls.readthedocs.io/en/stable/pages/user-guide.html
      2. server.start_io() # STDIO: starting the server as a child process
        - extension.ts -> TransportKind.stdio
      3. server.start_tcp("127.0.0.1", 8080) # TCP: starting the server as a TCP server
        - extension.ts -> TransportKind.socket
    """
    # server.start_io()
    print("PowerFX Language Server is running.")
    server.start_tcp("127.0.0.1", 8080)
    # server.start_io()

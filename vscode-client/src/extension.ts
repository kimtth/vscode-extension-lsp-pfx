/* --------------------------------------------------------------------------------------------
 * Copyright (c) Microsoft Corporation. All rights reserved.
 * Licensed under the MIT License. See License.txt in the project root for license information.
 * ------------------------------------------------------------------------------------------ */

import * as path from 'path';
import { workspace, ExtensionContext } from 'vscode';
import * as vscode from 'vscode';
import * as net from 'net';
import {
    LanguageClient,
    LanguageClientOptions,
    ServerOptions,
    StreamInfo,
    TransportKind
} from 'vscode-languageclient/node';

let client: LanguageClient;

export function activate(context: ExtensionContext) {
    // Defines the search path of your language server.
    const currentPath = __dirname;
    const basePath = context.asAbsolutePath('.');
    const languageServerPaths = [`server/lsp_server.py`];

    // get current file path of extension.ts
    console.log("currentPath: " + currentPath);
    console.log("basePath: " + basePath);

    // Add the code for loading under src/env_config.json 
    const configPath = path.join(basePath, 'vscode-client/src/config.json');
    // read the config json file
    let config = null;
    try {
        config = JSON.parse(require('fs').readFileSync(configPath, 'utf8'));
    } catch (e) {
        console.log(e);
    }
    const pythonPath = config?.pythonPath;
    const debugMode = config?.debugMode;

    var fs = require('fs');
    // The server is implemented in node
    let serverModule: string = '';
    for (let p of languageServerPaths) {
        p = context.asAbsolutePath(p);
        console.log(p);
        if (fs.existsSync(p)) {
            serverModule += p;
            break;
        }
    }
    // serverModule = path.join(serverModule, currentPath, 'hello.py');
    console.log("serverModule: " + serverModule);

    let workspaceDirectory = '';
    if (serverModule !== null) {
        workspaceDirectory = path.dirname(currentPath);
        // console.log("workPath: " + workPath);
    }
    // If the extension is launched in debug mode then the debug server options are used
    // Otherwise the run options are used
    // https://github.com/lextm/vscode-ansic/blob/main/src/languageServer/extension.ts
    // https://github.com/itemis/xtext-languageserver-example/blob/master/vscode-extension/src/extension.ts
    let serverOptions: ServerOptions;
    if (debugMode) {
        let connectionInfo = {
            port: 8080,
            host: "127.0.0.1"
        };
        serverOptions = () => {
            // Connect to language server via socket
            let socket = net.connect(connectionInfo);
            let result: StreamInfo = {
                writer: socket,
                reader: socket
            };
            return Promise.resolve(result);
        };
    } else {
        serverOptions = {
            // TransportKind.socket -> server.start_tcp('127.0.0.1', 8080)
            // TransportKind.stdio -> server.start_io()
            run: { command: pythonPath, args: [serverModule], options: { cwd: workspaceDirectory }, transport: TransportKind.socket },
            debug: { command: pythonPath, args: [serverModule, "--debug"], options: { cwd: workspaceDirectory }, transport: TransportKind.socket }
        };
    };

    // Options to control the language client
    const clientOptions: LanguageClientOptions = {
        // Register the server for powerfx-alpha documents
        documentSelector: [{ scheme: 'file', language: 'powerfx-alpha' }, { scheme: 'untitled', language: 'powerfx-alpha' }],
        synchronize: {
            // Notify the server about file changes to '.pfa files contained in the workspace
            fileEvents: workspace.createFileSystemWatcher('**/.pfa')
        },
        // Set initialization timeout (in milliseconds)
        initializationOptions: {
            initializationTimeout: 30000, // Increase to 30 seconds
        },
    };

    // Create the language client and start the client.
    client = new LanguageClient(
        'powerfxalpha-server',
        'Language Server PowerFxAlpha',
        serverOptions,
        clientOptions
    );

    // Start the client. This will also launch the server
    client.start();

    // Register the command to show a message box: custom command, which sends a message from the client without the server.
    const helloCmd = vscode.commands.registerCommand('extension.helloWorld', () => {
        // The code you place here will be executed every time your command is executed

        // Display a message box to the user
        vscode.window.showInformationMessage('Hello PowerFxAlpha!');
    });

    // Register a command to send chat messages: custom command, which sends a message to the server.
    const CHAT_MESSAGE = "chat/message";
    const CHAT_RESPONSE = "chat/response";
    const sendChatCmd = vscode.commands.registerCommand('extension.sendChatMessage', async () => {
        const message = await vscode.window.showInputBox({ prompt: 'Enter your chat message' });
        if (message) {
            client.sendNotification(CHAT_MESSAGE, { message });
        }
    });

    // Handle responses from the server
    const receiveChatNotification  = client.onNotification(CHAT_RESPONSE, (params) => {
        vscode.window.showInformationMessage(params.message);
    });
    context.subscriptions.push(helloCmd, sendChatCmd, receiveChatNotification);
}

export function deactivate(): Thenable<void> | undefined {
    if (!client) {
        return undefined;
    }
    return client.stop();
}
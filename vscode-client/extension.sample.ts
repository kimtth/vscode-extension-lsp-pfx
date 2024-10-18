// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
import * as vscode from 'vscode';

// This method is called when your extension is activated
// Your extension is activated the very first time the command is executed
export function activate(context: vscode.ExtensionContext) {

	// Use the console to output diagnostic information (console.log) and errors (console.error)
	// This line of code will only be executed once when your extension is activated
	console.log('Congratulations, your extension is now active!');

	// The command has been defined in the package.json file
	// Now provide the implementation of the command with registerCommand
	// The commandId parameter must match the command field in package.json
	const helloworldcommand = vscode.commands.registerCommand('vc-extension-auto-completion-aoai.helloWorld', () => {
		// The code you place here will be executed every time your command is executed
		// Display a message box to the user
		vscode.window.showInformationMessage('Hello World');
	});

	const spellCheckerCommand = vscode.commands.registerCommand('vc-extension-auto-completion-aoai.spellingChecker', () => {
		// The code you place here will be
		// executed every time your command is executed
		// Display a message box to the user
		vscode.window.showInformationMessage('Spell Checker!');
	});

	// Register a completion item provider for the custom language
	const provider = vscode.languages.registerCompletionItemProvider('markdown', {
		provideCompletionItems(document: vscode.TextDocument, position: vscode.Position) {
			// This function provides completion items for the DSL

			// Example: predefined keywords or phrases
			const completionItems = [
				new vscode.CompletionItem('create', vscode.CompletionItemKind.Keyword),
				new vscode.CompletionItem('read', vscode.CompletionItemKind.Keyword),
				new vscode.CompletionItem('update', vscode.CompletionItemKind.Keyword),
				new vscode.CompletionItem('delete', vscode.CompletionItemKind.Keyword),
			];

			// Get the current line of text where the cursor is located
			const lineText = document.lineAt(position).text;
			const currentWord = lineText.slice(0, position.character).trim();

			// Filter the completion items based on the current word
			const filteredItems = completionItems.filter(item => {
				// Check if item.label is a string, then use startsWith
				if (typeof item.label === 'string') {
					return item.label.startsWith(currentWord);
				}
				return false;
			});

			return filteredItems;
		}
	});
	
	context.subscriptions.push(provider);
	context.subscriptions.push(helloworldcommand);
}

// This method is called when your extension is deactivated
export function deactivate() {}

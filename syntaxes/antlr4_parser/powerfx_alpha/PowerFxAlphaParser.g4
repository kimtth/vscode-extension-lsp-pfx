parser grammar PowerFxAlphaParser;

options {
    tokenVocab=PowerFxAlphaLexer;
}

// Top-level rule: allows multiple expressions, import statements, or function definitions
expressionUnit
    : (importStatement | functionDefinition | expressionElements)* ;

// Import statement
importStatement : IMPORT STRING SEMI;

// Function definition
functionDefinition
    : DEFINE functionIdentifier LPAREN functionArguments? RPAREN LBRACE functionBody RBRACE
    ;

// Function arguments: input arguments can be identifiers or literals
functionArguments
    : (argument | literal) (COMMA (argument | literal))*  // Comma-separated list of arguments
    ;

// Argument rule: handles only identifiers as input arguments
argument
    : IDENTIFIER  // Regular input argument only
    ;

// Function body: consists of one or more expressions
functionBody
    : expressionElements*  // List of expressions that make up the function body
    ;

// Expression elements: consists of expressions
expressionElements
    : expression SEMI            // End each expression with a semicolon
    ;

// Function call: handles functions being called with arguments
functionCall
    : functionIdentifier LPAREN functionArguments? RPAREN
    ;

// Function identifier: defines the function name
functionIdentifier : IDENTIFIER (DOT IDENTIFIER)* ;

// Literal values: handles different types of literals
literal
    : numberLiteral
    | textLiteral
    | logicalLiteral
    ;

// Logical literals: true and false values
logicalLiteral
    : TRUE
    | FALSE
    ;

// Number and string literals
numberLiteral : NUMBER ;
textLiteral   : STRING ;

// Expressions: handles literals, references, function calls, and assignments
expression
    : literal
    | reference
    | functionCall          // Handles function calls such as Set(), Multiply()
    | assignment            // Handles in-function assignments such as Result = Number1 * Number2
    | LPAREN expression RPAREN
    | expression binaryOperator expression  // Allows binary operations (e.g., Result = Number1 * Number2)
    ;

// Assignment: assigns a value to an identifier (e.g., Result = Number1 * Number2)
assignment
    : IDENTIFIER EQ expression  // Assignment of an identifier to an expression
    ;

// Reference: variables or identifiers
reference
    : baseReference (referenceOperator referenceList)?
    ;

baseReference
    : IDENTIFIER
    | disambiguatedIdentifier
    | contextKeyword
    ;

// Reference operator (e.g., dot notation)
referenceOperator : DOT | NOT ;
referenceList     : IDENTIFIER (referenceOperator referenceList)? ;

// Inline records and tables remain unchanged
inlineRecord
    : LBRACE inlineRecordList? RBRACE
    | IDENTIFIER AT LBRACE inlineRecordList RBRACE
    ;

inlineRecordList
    : (IDENTIFIER COLON expression | SINGLE_QUOTE_STRING COLON expression)
      (COMMA (IDENTIFIER COLON expression | SINGLE_QUOTE_STRING COLON expression))*
    ;

inlineTable : LBRACK inlineTableList? RBRACK ;
inlineTableList : expression (COMMA inlineTableList)? ;

disambiguatedIdentifier : tableColumnIdentifier | globalIdentifier ;

tableColumnIdentifier : IDENTIFIER OPEN_BRACKET_AT IDENTIFIER RBRACK ;
globalIdentifier       : OPEN_BRACKET_AT IDENTIFIER RBRACK ;

// Context keywords for accessing parent, self, etc.
contextKeyword
    : PARENT
    | SELF
    | THISITEM
    | THISRECORD
    ;

// Binary operators for expressions
binaryOperator
    : EQ
    | LT
    | LTE
    | GT
    | GTE
    | NEQ
    | PLUS
    | MINUS
    | MUL
    | DIV
    | POW
    | AND
    | OR
    | IN
    | EXACTIN
    ;

// Prefix and postfix operators
prefixOperator  : NOT ;
postfixOperator : MOD ;

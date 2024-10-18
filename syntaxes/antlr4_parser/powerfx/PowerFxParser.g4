// PowerFxParser.g4  
parser grammar PowerFxParser;  
  
options {  
    tokenVocab=PowerFxLexer;  
}
  
// Parser Rules  
expressionUnit    : expressionElements? ;  
expressionElements : expressionElement+ ;  
expressionElement  : WS | LINE_COMMENT | BLOCK_COMMENT | expression ;  
expression        : literal  
                  | reference  
                  | inlineRecord  
                  | inlineTable  
                  | functionCall  
                  | LPAREN expression RPAREN  
                  | prefixOperator expression  
                  | expression postfixOperator  
                  | expression binaryOperator expression  
                  ;  
literal           : logicalLiteral  
                  | numberLiteral  
                  | textLiteral  
                  ;  
logicalLiteral    : TRUE  
                  | FALSE  
                  ;  
numberLiteral     : NUMBER ;  
textLiteral       : STRING ;  
reference         : baseReference (referenceOperator referenceList)? ;  
  
baseReference     : IDENTIFIER  
                  | disambiguatedIdentifier  
                  | contextKeyword  
                  ;  
  
referenceOperator : DOT | NOT ; // Using NOT in place of EXCL  
referenceList     : IDENTIFIER (referenceOperator referenceList)? ;  
  
inlineRecord      : LBRACE inlineRecordList? RBRACE  
                  | IDENTIFIER AT LBRACE inlineRecordList RBRACE  
                  ;  
inlineRecordList  : (IDENTIFIER COLON expression | SINGLE_QUOTE_STRING COLON expression) (COMMA (IDENTIFIER COLON expression | SINGLE_QUOTE_STRING COLON expression))*; 
inlineTable       : LBRACK inlineTableList? RBRACK ;  
inlineTableList   : expression (COMMA inlineTableList)? ;  
  
disambiguatedIdentifier : tableColumnIdentifier  
                        | globalIdentifier  
                        ;  
  
tableColumnIdentifier : IDENTIFIER OPEN_BRACKET_AT IDENTIFIER RBRACK ; // Using RBRACK in place of CLOSE_BRACKET  
globalIdentifier  : OPEN_BRACKET_AT IDENTIFIER RBRACK ; // Using RBRACK in place of CLOSE_BRACKET  
  
functionCall      : functionIdentifier LPAREN functionArguments RPAREN ;  
functionIdentifier : IDENTIFIER (DOT IDENTIFIER)*; // Ensure the function identifier is defined
functionArguments : chainedExpression (COMMA chainedExpression)*; // Ensure comma-separated
chainedExpression : expression (SEMI expression)?; // Ensure semicolon-separated expressions
  
contextKeyword    : PARENT  
                  | SELF  
                  | THISITEM  
                  | THISRECORD  
                  ;  
  
// Operators  
binaryOperator    : EQ  
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
  
prefixOperator    : NOT ; // Using NOT in place of EXCL  
postfixOperator   : MOD ;  

// PowerFxAlphaLexer.g4  
lexer grammar PowerFxAlphaLexer;  
  
// Whitespace and Comments  
WS : [ \t\r\n\u000B\u000C\u0085]+ -> skip ; // Whitespace: skip spaces, tabs, new lines, etc.  
LINE_COMMENT : '//' ~[\r\n]* -> skip ; // Single line comment: skips until newline  
BLOCK_COMMENT : '/*' ( . | NEWLINE )*? '*/' -> skip ; // Multi-line comment: skips everything inside  
  
fragment NEWLINE : [\r\n]; // Define a fragment for newline  
  
// Operator Tokens  
PLUS  : '+' ;  
MINUS : '-' ;  
MUL   : '*' ;  
DIV   : '/' ;  
POW   : '^' ;  
MOD   : '%' ;  
AND   : '&&' ;  
OR    : '||' ;  
NOT   : '!' ;  
EQ    : '=' ;  
LT    : '<' ;  
LTE   : '<=' ;  
GT    : '>' ;  
GTE   : '>=' ;  
NEQ   : '<>' ;  
IN    : 'in' ;  
EXACTIN : 'exactin' ;  
DOT   : '.' ;  
SEMI  : ';' ;  
COMMA : ',' ;  
LPAREN: '(' ;  
RPAREN: ')' ;  
LBRACE: '{' ;  
RBRACE: '}' ;  
LBRACK: '[' ;  
RBRACK: ']' ;  
AT    : '@' ;  
COLON : ':' ;  
  
// Keywords  
PARENT : 'Parent' ;  
SELF   : 'Self' ;  
THISITEM : 'ThisItem' ;  
THISRECORD : 'ThisRecord' ;  

// Keywords for the custom syntax
IMPORT : 'Import' ;  // For importing external files
DEFINE : 'Define' ;  // For defining functions
OUT    : 'out' ;     // For output parameters in functions

  
// Literals  
TRUE  : 'true' ;  
FALSE : 'false' ;  
NUMBER : [0-9]+ ('.' [0-9]+)? ([eE] [+-]? [0-9]+)? ;  
STRING : '"' ('""' | ~'"')* '"' ;  
IDENTIFIER : [a-zA-Z_] [a-zA-Z0-9_]* ;  
SINGLE_QUOTE_STRING : '\'' ('\'\'' | ~'\'')* '\''; // Single-quoted strings
  
// Special Tokens  
OPEN_BRACKET_AT : '[@' ;  




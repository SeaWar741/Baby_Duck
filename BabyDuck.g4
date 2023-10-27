grammar BabyDuck;

// Parser Rules
program: 'program' ID SEMICOLON (vars)? (funcs)* main body end;

vars: 'var' (ID (COMMA ID)* COLON type SEMICOLON)+;

type: int | float;

funcs: void ID LPAREN (ID COLON type (COMMA ID COLON type)*)? RPAREN LBRACKET (vars)? body RBRACKET SEMICOLON;

body: LBRACE (statement)* RBRACE;

statement: assign | condition | cycle | f_call | print;

assign: ID EQUALS expression SEMICOLON;

condition: if LPAREN expression RPAREN body (else body)? SEMICOLON;

cycle: while body do LPAREN expression RPAREN SEMICOLON;

print: print_w LPAREN (expression | STRING) (COMMA (expression|STRING))* RPAREN SEMICOLON;

f_call: ID LPAREN (expression (COMMA expression)* )? RPAREN SEMICOLON;

expression: exp ((GREATERTHAN | LESSTHAN | NOTEQUALS) exp)?;

exp: termino ((PLUS | MINUS) termino)*;

termino: factor ((MULTIPLY | DIVIDE) factor)?;

factor: (LPAREN expression RPAREN) | ((MINUS | PLUS)? (ID | cte));

cte: INTEGER | FLOAT_NUM;

// Tokens
INTEGER: [0-9]+;
FLOAT_NUM: [0-9]+ '.' [0-9]+;
ID: [a-zA-Z] ([a-zA-Z] | [0-9])*;
STRING: '"' .*? '"';

// Operators and Comparators
PLUS: '+';
MINUS: '-';
MULTIPLY: '*';
DIVIDE: '/';
EQUALS: '=';
NOTEQUALS: '!=';
GREATERTHAN: '>';
LESSTHAN: '<';

// Keywords
if: 'if';
else: 'else';
while: 'while';
do: 'do';
print_w: 'print';
void: 'void';
int: 'int';
float: 'float';
main: 'main';
end: 'end';

// Whitespace 
WS: [ \t\r\n]+ -> skip;

// Punctuation
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
LBRACKET: '[';
RBRACKET: ']';
SEMICOLON: ';';
COMMA: ',';
COLON: ':';

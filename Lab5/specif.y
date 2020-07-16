%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define YYDEBUG 1
%}

%token IDENTIFIER
%token CONSTANT
%token CHAR
%token INT
%token IF
%token ELSE
%token PRINTF
%token SCANF
%token WHILE
%token MAIN
%token RETURN
%token COLON
%token SEMI_COLON
%token PLUS
%token MINUS
%token MULTIPLY
%token DIVISION
%token MOD
%token LESS_THAN
%token LESS_OR_EQUAL_THAN
%token ASSIGNMENT
%token GREATER_OR_EQUAL_THAN
%token GREATER_THAN
%token EQUAL
%token AND
%token OR
%token NOT
%token NOT_EQUAL
%token LEFT_SQUARE_PARENTHESIS
%token RIGHT_SQUARE_PARENTHESIS
%token LEFT_ROUND_PARENTHESIS
%token RIGHT_ROUND_PARENTHESIS
%token LEFT_ACCOLADE
%token RIGHT_ACCOLADE

%start program

%%

program : INT MAIN LEFT_ROUND_PARENTHESIS RIGHT_ROUND_PARENTHESIS LEFT_ACCOLADE statement_list RETURN CONSTANT SEMI_COLON RIGHT_ACCOLADE ;
statement_list : statement statement_list | statement ;
statement : declaration | simple_statement | complicated_statement ;
declaration : type IDENTIFIER SEMI_COLON | type IDENTIFIER LEFT_SQUARE_PARENTHESIS CONSTANT RIGHT_SQUARE_PARENTHESIS SEMI_COLON ; 
type : INT | CHAR ;
simple_statement : assignment | out_statement | in_statement ;
assignment : IDENTIFIER ASSIGNMENT expression SEMI_COLON | IDENTIFIER LEFT_SQUARE_PARENTHESIS CONSTANT RIGHT_SQUARE_PARENTHESIS ASSIGNMENT expression SEMI_COLON ;
expression : term | NOT term | expression operation expression | NOT expression operation expression | LEFT_ROUND_PARENTHESIS expression operation expression RIGHT_ROUND_PARENTHESIS | NOT LEFT_ROUND_PARENTHESIS expression operation expression RIGHT_ROUND_PARENTHESIS ;
operation : PLUS | MINUS | MULTIPLY | DIVISION | MOD ;
term : IDENTIFIER | CONSTANT ;
out_statement : PRINTF LEFT_ROUND_PARENTHESIS term RIGHT_ROUND_PARENTHESIS SEMI_COLON ;
in_statement : SCANF LEFT_ROUND_PARENTHESIS IDENTIFIER RIGHT_ROUND_PARENTHESIS SEMI_COLON
complicated_statement : if_statement | while_statement
if_statement : IF LEFT_ROUND_PARENTHESIS condition RIGHT_ROUND_PARENTHESIS LEFT_ACCOLADE statement_list RIGHT_ACCOLADE | IF LEFT_ROUND_PARENTHESIS condition RIGHT_ROUND_PARENTHESIS LEFT_ACCOLADE statement_list RIGHT_ACCOLADE ELSE LEFT_ACCOLADE statement_list RIGHT_ACCOLADE
condition : expression relation expression
while_statement : WHILE LEFT_ROUND_PARENTHESIS condition RIGHT_ROUND_PARENTHESIS LEFT_ACCOLADE statement_list RIGHT_ACCOLADE
relation : LESS_THAN | LESS_OR_EQUAL_THAN | EQUAL | NOT_EQUAL | GREATER_OR_EQUAL_THAN | GREATER_THAN | AND | OR

%%

yyerror(char *s)
{
  printf("%s\n", s);
}

extern FILE *yyin;

main(int argc, char **argv)
{
  if (argc > 1) 
    yyin = fopen(argv[1], "r");
  if ( (argc > 2) && ( !strcmp(argv[2], "-d") ) ) 
    yydebug = 1;
  if ( !yyparse() ) 
    fprintf(stderr,"\t U GOOOOOD !!!\n");
}

/* A Bison parser, made by GNU Bison 2.4.1.  */

/* Skeleton interface for Bison's Yacc-like parsers in C
   
      Copyright (C) 1984, 1989, 1990, 2000, 2001, 2002, 2003, 2004, 2005, 2006
   Free Software Foundation, Inc.
   
   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.
   
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
   
   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.
   
   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */


/* Tokens.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
   /* Put the tokens into the symbol table, so that GDB and other debuggers
      know about them.  */
   enum yytokentype {
     IDENTIFIER = 258,
     CONSTANT = 259,
     CHAR = 260,
     INT = 261,
     IF = 262,
     ELSE = 263,
     PRINTF = 264,
     SCANF = 265,
     WHILE = 266,
     MAIN = 267,
     RETURN = 268,
     COLON = 269,
     SEMI_COLON = 270,
     PLUS = 271,
     MINUS = 272,
     MULTIPLY = 273,
     DIVISION = 274,
     MOD = 275,
     LESS_THAN = 276,
     LESS_OR_EQUAL_THAN = 277,
     ASSIGNMENT = 278,
     GREATER_OR_EQUAL_THAN = 279,
     GREATER_THAN = 280,
     EQUAL = 281,
     AND = 282,
     OR = 283,
     NOT = 284,
     NOT_EQUAL = 285,
     LEFT_SQUARE_PARENTHESIS = 286,
     RIGHT_SQUARE_PARENTHESIS = 287,
     LEFT_ROUND_PARENTHESIS = 288,
     RIGHT_ROUND_PARENTHESIS = 289,
     LEFT_ACCOLADE = 290,
     RIGHT_ACCOLADE = 291
   };
#endif



#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
#endif

extern YYSTYPE yylval;



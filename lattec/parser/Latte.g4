grammar Latte;

program
    : topDef+
    ;

topDef
    : type_ name=ID LPAREN argVec? RPAREN block  # FnDef
    | CLS name=ID LBRACE clsElem* RBRACE         # ClsDef
    ;

argVec
    : arg ( COMMA arg )*
    ;

arg : type_ name=ID;

block
    : LBRACE stmt* RBRACE
    ;

clsElem
    : type_ ID SEM                       # Field
    | topDef                             # Method
    ;

stmt
    : SEM                                  # Empty
    | block                                # BlockStmt
    | type_ item ( COMMA item )* SEM       # Decl
    | target=expr ASS value=expr SEM        # Ass
    | name=ID INCR SEM                     # Incr
    | name=ID DECR SEM                     # Decr
    | RETURN expr SEM                      # Ret
    | RETURN SEM                           # VRet
    | IF LPAREN cond=expr RPAREN true_stmt=stmt               # Cond
    | IF LPAREN cond=expr RPAREN true_stmt=stmt ELSE false_stmt=stmt   # CondElse
    | WHILE LPAREN cond=expr RPAREN true_stmt=stmt        # While
    | FOR LPAREN type_ ID COLON expr RPAREN stmt # ForEach
    | expr SEM                             # SExp
    ;

type_
    : base_type                    #TNonArray
    | basic_type (LBRACK RBRACK)+  #TArray
    ;

base_type
    : basic_type # TBasic
    | ID         # TIdent
    ;

basic_type
    : INT  # TInt
    | STR  # TStr
    | BOOL # TBool
    | VOID # TVoid
    ;

new_expr_type
    : class_name=ID                    # NewObj
    | class_name=ID LBRACK expr RBRACK # NewObjArray
    | basic_type (LBRACK expr RBRACK)+ # NewBasicTypeArray
    ;

item
    : name=ID
    | name=ID ASS expr
    ;

expr
    : expr DOT expr                                      # EAcc
    | NEW new_expr_type                                  # ENew
    | expr LBRACK expr RBRACK                            # EAccArr
    | (SUB|NOT) expr                                     # EUnOp
    | lhs=expr mulOp rhs=expr                            # EMulOp
    | lhs=expr addOp rhs=expr                            # EAddOp
    | lhs=expr relOp rhs=expr                            # ERelOp
    | <assoc=right> lhs=expr AND rhs=expr                # EAnd
    | <assoc=right> lhs=expr OR rhs=expr                 # EOr
    | ID                                                 # EId
    | NUMBER                                             # EInt
    | TRUE                                               # ETrue
    | FALSE                                              # EFalse
    | NULL                                               # ENull
    | name=ID LPAREN ( expr ( COMMA expr )* )? RPAREN    # EFunCall
    | LPAREN ID RPAREN expr                              # ECast
    | STRING                                             # EStr
    | LPAREN expr RPAREN                                 # EParen
    ;

addOp
    : ADD
    | SUB
    ;

mulOp
    : MUL
    | DIV
    | MOD
    ;

relOp
    : LT
    | LEQ
    | GT
    | GEQ
    | EQ
    | NEQ
    ;

COMMENT : ('#' ~[\r\n]* | '//' ~[\r\n]*) -> channel(HIDDEN);
MULTICOMMENT : '/*' .*? '*/' -> channel(HIDDEN);

SEM   : ';';
COLON : ':';

LBRACE : '{';
LBRACK : '[';
LPAREN : '(';
RBRACE : '}';
RBRACK : ']';
RPAREN : ')';
COMMA  : ',';
DOT    : '.';

INT    : 'int';
BOOL   : 'boolean';
STR    : 'string';
VOID   : 'void';

AND : '&&';
OR  : '||';
ADD : '+';
SUB : '-';
MUL : '*';
DIV : '/';
MOD : '%';
LT  : '<';
LEQ : '<=';
GT  : '>';
GEQ : '>=';
EQ  : '==';
NEQ : '!=';
NOT : '!';

ASS  : '=';
INCR : '++';
DECR : '--';

RETURN  : 'return';
IF      : 'if';
ELSE    : 'else';
WHILE   : 'while';
FOR     : 'for';

TRUE    : 'true';
FALSE   : 'false';

CLS     : 'class';
NEW     : 'new';
NULL    : 'null';

fragment Letter  : Capital | Small ;
fragment Capital : [A-Z\u00C0-\u00D6\u00D8-\u00DE] ;
fragment Small   : [a-z\u00DF-\u00F6\u00F8-\u00FF] ;
fragment Digit : [0-9] ;

NUMBER : Digit+ ;
fragment ID_First : Letter | '_';
ID : ID_First (ID_First | Digit)* ;

WS : (' ' | '\r' | '\t' | '\n')+ ->  skip;

STRING
    :   '"' StringCharacters? '"'
    ;
fragment StringCharacters
    :   StringCharacter+
    ;
fragment
StringCharacter
    :   ~["\\]
    |   '\\' [tnr"\\]
    ;


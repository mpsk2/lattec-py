# Generated from lattec/parser/Latte.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\62")
        buf.write("\u0125\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\3\2\6\2(\n\2\r\2\16\2)\3\3\3\3\3\3\3\3\5\3\60\n\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\5\39\n\3\3\3\3\3\7\3=\n\3\f\3")
        buf.write("\16\3@\13\3\3\3\5\3C\n\3\3\4\3\4\3\4\7\4H\n\4\f\4\16\4")
        buf.write("K\13\4\3\5\3\5\3\5\3\6\3\6\7\6R\n\6\f\6\16\6U\13\6\3\6")
        buf.write("\3\6\3\7\3\7\3\7\3\7\3\7\5\7^\n\7\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\7\bf\n\b\f\b\16\bi\13\b\3\b\3\b\3\b\3\b\7\bo\n\b")
        buf.write("\f\b\16\br\13\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u00a4")
        buf.write("\n\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\7\n\u00ad\n\n\f\n\16")
        buf.write("\n\u00b0\13\n\3\13\3\13\3\13\3\13\6\13\u00b6\n\13\r\13")
        buf.write("\16\13\u00b7\5\13\u00ba\n\13\3\f\3\f\5\f\u00be\n\f\3\r")
        buf.write("\3\r\3\r\3\r\5\r\u00c4\n\r\3\16\3\16\3\16\3\16\3\16\5")
        buf.write("\16\u00cb\n\16\3\16\3\16\3\16\3\16\3\16\6\16\u00d2\n\16")
        buf.write("\r\16\16\16\u00d3\5\16\u00d6\n\16\3\17\3\17\3\17\3\17")
        buf.write("\5\17\u00dc\n\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\7\20\u00ed\n\20")
        buf.write("\f\20\16\20\u00f0\13\20\5\20\u00f2\n\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u00fe\n\20\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\7\20\u011a\n\20\f\20\16\20\u011d")
        buf.write("\13\20\3\21\3\21\3\22\3\22\3\23\3\23\3\23\2\3\36\24\2")
        buf.write("\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$\2\6\4\2\26\26")
        buf.write("  \3\2\25\26\3\2\27\31\3\2\32\37\2\u0146\2\'\3\2\2\2\4")
        buf.write("B\3\2\2\2\6D\3\2\2\2\bL\3\2\2\2\nO\3\2\2\2\f]\3\2\2\2")
        buf.write("\16\u00a3\3\2\2\2\20\u00a5\3\2\2\2\22\u00a9\3\2\2\2\24")
        buf.write("\u00b9\3\2\2\2\26\u00bd\3\2\2\2\30\u00c3\3\2\2\2\32\u00d5")
        buf.write("\3\2\2\2\34\u00db\3\2\2\2\36\u00fd\3\2\2\2 \u011e\3\2")
        buf.write("\2\2\"\u0120\3\2\2\2$\u0122\3\2\2\2&(\5\4\3\2\'&\3\2\2")
        buf.write("\2()\3\2\2\2)\'\3\2\2\2)*\3\2\2\2*\3\3\2\2\2+,\5\24\13")
        buf.write("\2,-\7\60\2\2-/\7\t\2\2.\60\5\6\4\2/.\3\2\2\2/\60\3\2")
        buf.write("\2\2\60\61\3\2\2\2\61\62\7\f\2\2\62\63\5\n\6\2\63C\3\2")
        buf.write("\2\2\64\65\7+\2\2\658\7\60\2\2\66\67\7,\2\2\679\7\60\2")
        buf.write("\28\66\3\2\2\289\3\2\2\29:\3\2\2\2:>\7\7\2\2;=\5\f\7\2")
        buf.write("<;\3\2\2\2=@\3\2\2\2><\3\2\2\2>?\3\2\2\2?A\3\2\2\2@>\3")
        buf.write("\2\2\2AC\7\n\2\2B+\3\2\2\2B\64\3\2\2\2C\5\3\2\2\2DI\5")
        buf.write("\b\5\2EF\7\r\2\2FH\5\b\5\2GE\3\2\2\2HK\3\2\2\2IG\3\2\2")
        buf.write("\2IJ\3\2\2\2J\7\3\2\2\2KI\3\2\2\2LM\5\24\13\2MN\7\60\2")
        buf.write("\2N\t\3\2\2\2OS\7\7\2\2PR\5\16\b\2QP\3\2\2\2RU\3\2\2\2")
        buf.write("SQ\3\2\2\2ST\3\2\2\2TV\3\2\2\2US\3\2\2\2VW\7\n\2\2W\13")
        buf.write("\3\2\2\2XY\5\24\13\2YZ\7\60\2\2Z[\7\5\2\2[^\3\2\2\2\\")
        buf.write("^\5\4\3\2]X\3\2\2\2]\\\3\2\2\2^\r\3\2\2\2_\u00a4\7\5\2")
        buf.write("\2`\u00a4\5\n\6\2ab\5\24\13\2bg\5\34\17\2cd\7\r\2\2df")
        buf.write("\5\34\17\2ec\3\2\2\2fi\3\2\2\2ge\3\2\2\2gh\3\2\2\2hj\3")
        buf.write("\2\2\2ig\3\2\2\2jk\7\5\2\2k\u00a4\3\2\2\2lp\5\22\n\2m")
        buf.write("o\5\20\t\2nm\3\2\2\2or\3\2\2\2pn\3\2\2\2pq\3\2\2\2qs\3")
        buf.write("\2\2\2rp\3\2\2\2st\7!\2\2tu\5\36\20\2uv\7\5\2\2v\u00a4")
        buf.write("\3\2\2\2wx\7\60\2\2xy\7\"\2\2y\u00a4\7\5\2\2z{\7\60\2")
        buf.write("\2{|\7#\2\2|\u00a4\7\5\2\2}~\7$\2\2~\177\5\36\20\2\177")
        buf.write("\u0080\7\5\2\2\u0080\u00a4\3\2\2\2\u0081\u0082\7$\2\2")
        buf.write("\u0082\u00a4\7\5\2\2\u0083\u0084\7%\2\2\u0084\u0085\7")
        buf.write("\t\2\2\u0085\u0086\5\36\20\2\u0086\u0087\7\f\2\2\u0087")
        buf.write("\u0088\5\16\b\2\u0088\u00a4\3\2\2\2\u0089\u008a\7%\2\2")
        buf.write("\u008a\u008b\7\t\2\2\u008b\u008c\5\36\20\2\u008c\u008d")
        buf.write("\7\f\2\2\u008d\u008e\5\16\b\2\u008e\u008f\7&\2\2\u008f")
        buf.write("\u0090\5\16\b\2\u0090\u00a4\3\2\2\2\u0091\u0092\7\'\2")
        buf.write("\2\u0092\u0093\7\t\2\2\u0093\u0094\5\36\20\2\u0094\u0095")
        buf.write("\7\f\2\2\u0095\u0096\5\16\b\2\u0096\u00a4\3\2\2\2\u0097")
        buf.write("\u0098\7(\2\2\u0098\u0099\7\t\2\2\u0099\u009a\5\24\13")
        buf.write("\2\u009a\u009b\7\60\2\2\u009b\u009c\7\6\2\2\u009c\u009d")
        buf.write("\5\36\20\2\u009d\u009e\7\f\2\2\u009e\u009f\5\16\b\2\u009f")
        buf.write("\u00a4\3\2\2\2\u00a0\u00a1\5\36\20\2\u00a1\u00a2\7\5\2")
        buf.write("\2\u00a2\u00a4\3\2\2\2\u00a3_\3\2\2\2\u00a3`\3\2\2\2\u00a3")
        buf.write("a\3\2\2\2\u00a3l\3\2\2\2\u00a3w\3\2\2\2\u00a3z\3\2\2\2")
        buf.write("\u00a3}\3\2\2\2\u00a3\u0081\3\2\2\2\u00a3\u0083\3\2\2")
        buf.write("\2\u00a3\u0089\3\2\2\2\u00a3\u0091\3\2\2\2\u00a3\u0097")
        buf.write("\3\2\2\2\u00a3\u00a0\3\2\2\2\u00a4\17\3\2\2\2\u00a5\u00a6")
        buf.write("\7\b\2\2\u00a6\u00a7\5\36\20\2\u00a7\u00a8\7\13\2\2\u00a8")
        buf.write("\21\3\2\2\2\u00a9\u00ae\7\60\2\2\u00aa\u00ab\7\16\2\2")
        buf.write("\u00ab\u00ad\7\60\2\2\u00ac\u00aa\3\2\2\2\u00ad\u00b0")
        buf.write("\3\2\2\2\u00ae\u00ac\3\2\2\2\u00ae\u00af\3\2\2\2\u00af")
        buf.write("\23\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b1\u00ba\5\26\f\2\u00b2")
        buf.write("\u00b5\5\30\r\2\u00b3\u00b4\7\b\2\2\u00b4\u00b6\7\13\2")
        buf.write("\2\u00b5\u00b3\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\u00b5")
        buf.write("\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00ba\3\2\2\2\u00b9")
        buf.write("\u00b1\3\2\2\2\u00b9\u00b2\3\2\2\2\u00ba\25\3\2\2\2\u00bb")
        buf.write("\u00be\5\30\r\2\u00bc\u00be\7\60\2\2\u00bd\u00bb\3\2\2")
        buf.write("\2\u00bd\u00bc\3\2\2\2\u00be\27\3\2\2\2\u00bf\u00c4\7")
        buf.write("\17\2\2\u00c0\u00c4\7\21\2\2\u00c1\u00c4\7\20\2\2\u00c2")
        buf.write("\u00c4\7\22\2\2\u00c3\u00bf\3\2\2\2\u00c3\u00c0\3\2\2")
        buf.write("\2\u00c3\u00c1\3\2\2\2\u00c3\u00c2\3\2\2\2\u00c4\31\3")
        buf.write("\2\2\2\u00c5\u00ca\7\60\2\2\u00c6\u00c7\7\b\2\2\u00c7")
        buf.write("\u00c8\5\36\20\2\u00c8\u00c9\7\13\2\2\u00c9\u00cb\3\2")
        buf.write("\2\2\u00ca\u00c6\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\u00d6")
        buf.write("\3\2\2\2\u00cc\u00d1\5\30\r\2\u00cd\u00ce\7\b\2\2\u00ce")
        buf.write("\u00cf\5\36\20\2\u00cf\u00d0\7\13\2\2\u00d0\u00d2\3\2")
        buf.write("\2\2\u00d1\u00cd\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d1")
        buf.write("\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\u00d6\3\2\2\2\u00d5")
        buf.write("\u00c5\3\2\2\2\u00d5\u00cc\3\2\2\2\u00d6\33\3\2\2\2\u00d7")
        buf.write("\u00dc\7\60\2\2\u00d8\u00d9\7\60\2\2\u00d9\u00da\7!\2")
        buf.write("\2\u00da\u00dc\5\36\20\2\u00db\u00d7\3\2\2\2\u00db\u00d8")
        buf.write("\3\2\2\2\u00dc\35\3\2\2\2\u00dd\u00de\b\20\1\2\u00de\u00df")
        buf.write("\t\2\2\2\u00df\u00fe\5\36\20\24\u00e0\u00fe\7\60\2\2\u00e1")
        buf.write("\u00fe\7/\2\2\u00e2\u00fe\7)\2\2\u00e3\u00fe\7*\2\2\u00e4")
        buf.write("\u00fe\7.\2\2\u00e5\u00e6\7-\2\2\u00e6\u00fe\5\32\16\2")
        buf.write("\u00e7\u00e8\7\60\2\2\u00e8\u00f1\7\t\2\2\u00e9\u00ee")
        buf.write("\5\36\20\2\u00ea\u00eb\7\r\2\2\u00eb\u00ed\5\36\20\2\u00ec")
        buf.write("\u00ea\3\2\2\2\u00ed\u00f0\3\2\2\2\u00ee\u00ec\3\2\2\2")
        buf.write("\u00ee\u00ef\3\2\2\2\u00ef\u00f2\3\2\2\2\u00f0\u00ee\3")
        buf.write("\2\2\2\u00f1\u00e9\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\u00f3")
        buf.write("\3\2\2\2\u00f3\u00fe\7\f\2\2\u00f4\u00f5\7\t\2\2\u00f5")
        buf.write("\u00f6\7\60\2\2\u00f6\u00f7\7\f\2\2\u00f7\u00fe\5\36\20")
        buf.write("\5\u00f8\u00fe\7\62\2\2\u00f9\u00fa\7\t\2\2\u00fa\u00fb")
        buf.write("\5\36\20\2\u00fb\u00fc\7\f\2\2\u00fc\u00fe\3\2\2\2\u00fd")
        buf.write("\u00dd\3\2\2\2\u00fd\u00e0\3\2\2\2\u00fd\u00e1\3\2\2\2")
        buf.write("\u00fd\u00e2\3\2\2\2\u00fd\u00e3\3\2\2\2\u00fd\u00e4\3")
        buf.write("\2\2\2\u00fd\u00e5\3\2\2\2\u00fd\u00e7\3\2\2\2\u00fd\u00f4")
        buf.write("\3\2\2\2\u00fd\u00f8\3\2\2\2\u00fd\u00f9\3\2\2\2\u00fe")
        buf.write("\u011b\3\2\2\2\u00ff\u0100\f\23\2\2\u0100\u0101\5\"\22")
        buf.write("\2\u0101\u0102\5\36\20\24\u0102\u011a\3\2\2\2\u0103\u0104")
        buf.write("\f\22\2\2\u0104\u0105\5 \21\2\u0105\u0106\5\36\20\23\u0106")
        buf.write("\u011a\3\2\2\2\u0107\u0108\f\21\2\2\u0108\u0109\5$\23")
        buf.write("\2\u0109\u010a\5\36\20\22\u010a\u011a\3\2\2\2\u010b\u010c")
        buf.write("\f\20\2\2\u010c\u010d\7\23\2\2\u010d\u011a\5\36\20\20")
        buf.write("\u010e\u010f\f\17\2\2\u010f\u0110\7\24\2\2\u0110\u011a")
        buf.write("\5\36\20\17\u0111\u0112\f\b\2\2\u0112\u0113\7\16\2\2\u0113")
        buf.write("\u011a\5\36\20\b\u0114\u0115\f\7\2\2\u0115\u0116\7\b\2")
        buf.write("\2\u0116\u0117\5\36\20\2\u0117\u0118\7\13\2\2\u0118\u011a")
        buf.write("\3\2\2\2\u0119\u00ff\3\2\2\2\u0119\u0103\3\2\2\2\u0119")
        buf.write("\u0107\3\2\2\2\u0119\u010b\3\2\2\2\u0119\u010e\3\2\2\2")
        buf.write("\u0119\u0111\3\2\2\2\u0119\u0114\3\2\2\2\u011a\u011d\3")
        buf.write("\2\2\2\u011b\u0119\3\2\2\2\u011b\u011c\3\2\2\2\u011c\37")
        buf.write("\3\2\2\2\u011d\u011b\3\2\2\2\u011e\u011f\t\3\2\2\u011f")
        buf.write("!\3\2\2\2\u0120\u0121\t\4\2\2\u0121#\3\2\2\2\u0122\u0123")
        buf.write("\t\5\2\2\u0123%\3\2\2\2\33)/8>BIS]gp\u00a3\u00ae\u00b7")
        buf.write("\u00b9\u00bd\u00c3\u00ca\u00d3\u00d5\u00db\u00ee\u00f1")
        buf.write("\u00fd\u0119\u011b")
        return buf.getvalue()


class LatteParser ( Parser ):

    grammarFileName = "Latte.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "';'", "':'", 
                     "'{'", "'['", "'('", "'}'", "']'", "')'", "','", "'.'", 
                     "'int'", "'boolean'", "'string'", "'void'", "'&&'", 
                     "'||'", "'+'", "'-'", "'*'", "'/'", "'%'", "'<'", "'<='", 
                     "'>'", "'>='", "'=='", "'!='", "'!'", "'='", "'++'", 
                     "'--'", "'return'", "'if'", "'else'", "'while'", "'for'", 
                     "'true'", "'false'", "'class'", "'extends'", "'new'", 
                     "'null'" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "MULTICOMMENT", "SEM", "COLON", 
                      "LBRACE", "LBRACK", "LPAREN", "RBRACE", "RBRACK", 
                      "RPAREN", "COMMA", "DOT", "INT", "BOOL", "STR", "VOID", 
                      "AND", "OR", "ADD", "SUB", "MUL", "DIV", "MOD", "LT", 
                      "LEQ", "GT", "GEQ", "EQ", "NEQ", "NOT", "ASS", "INCR", 
                      "DECR", "RETURN", "IF", "ELSE", "WHILE", "FOR", "TRUE", 
                      "FALSE", "CLS", "EXTENDS", "NEW", "NULL", "NUMBER", 
                      "ID", "WS", "STRING" ]

    RULE_program = 0
    RULE_topDef = 1
    RULE_argVec = 2
    RULE_arg = 3
    RULE_block = 4
    RULE_clsElem = 5
    RULE_stmt = 6
    RULE_arrAcc = 7
    RULE_identVec = 8
    RULE_type_ = 9
    RULE_base_type = 10
    RULE_basic_type = 11
    RULE_new_expr_type = 12
    RULE_item = 13
    RULE_expr = 14
    RULE_addOp = 15
    RULE_mulOp = 16
    RULE_relOp = 17

    ruleNames =  [ "program", "topDef", "argVec", "arg", "block", "clsElem", 
                   "stmt", "arrAcc", "identVec", "type_", "base_type", "basic_type", 
                   "new_expr_type", "item", "expr", "addOp", "mulOp", "relOp" ]

    EOF = Token.EOF
    COMMENT=1
    MULTICOMMENT=2
    SEM=3
    COLON=4
    LBRACE=5
    LBRACK=6
    LPAREN=7
    RBRACE=8
    RBRACK=9
    RPAREN=10
    COMMA=11
    DOT=12
    INT=13
    BOOL=14
    STR=15
    VOID=16
    AND=17
    OR=18
    ADD=19
    SUB=20
    MUL=21
    DIV=22
    MOD=23
    LT=24
    LEQ=25
    GT=26
    GEQ=27
    EQ=28
    NEQ=29
    NOT=30
    ASS=31
    INCR=32
    DECR=33
    RETURN=34
    IF=35
    ELSE=36
    WHILE=37
    FOR=38
    TRUE=39
    FALSE=40
    CLS=41
    EXTENDS=42
    NEW=43
    NULL=44
    NUMBER=45
    ID=46
    WS=47
    STRING=48

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def topDef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatteParser.TopDefContext)
            else:
                return self.getTypedRuleContext(LatteParser.TopDefContext,i)


        def getRuleIndex(self):
            return LatteParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = LatteParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 36
                self.topDef()
                self.state = 39 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LatteParser.INT) | (1 << LatteParser.BOOL) | (1 << LatteParser.STR) | (1 << LatteParser.VOID) | (1 << LatteParser.CLS) | (1 << LatteParser.ID))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TopDefContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LatteParser.RULE_topDef

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FnDefContext(TopDefContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.TopDefContext
            super().__init__(parser)
            self.name = None # Token
            self.copyFrom(ctx)

        def type_(self):
            return self.getTypedRuleContext(LatteParser.Type_Context,0)

        def LPAREN(self):
            return self.getToken(LatteParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(LatteParser.RPAREN, 0)
        def block(self):
            return self.getTypedRuleContext(LatteParser.BlockContext,0)

        def ID(self):
            return self.getToken(LatteParser.ID, 0)
        def argVec(self):
            return self.getTypedRuleContext(LatteParser.ArgVecContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFnDef" ):
                listener.enterFnDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFnDef" ):
                listener.exitFnDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFnDef" ):
                return visitor.visitFnDef(self)
            else:
                return visitor.visitChildren(self)


    class ClsDefContext(TopDefContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.TopDefContext
            super().__init__(parser)
            self.name = None # Token
            self.supercls = None # Token
            self.copyFrom(ctx)

        def CLS(self):
            return self.getToken(LatteParser.CLS, 0)
        def LBRACE(self):
            return self.getToken(LatteParser.LBRACE, 0)
        def RBRACE(self):
            return self.getToken(LatteParser.RBRACE, 0)
        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(LatteParser.ID)
            else:
                return self.getToken(LatteParser.ID, i)
        def EXTENDS(self):
            return self.getToken(LatteParser.EXTENDS, 0)
        def clsElem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatteParser.ClsElemContext)
            else:
                return self.getTypedRuleContext(LatteParser.ClsElemContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClsDef" ):
                listener.enterClsDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClsDef" ):
                listener.exitClsDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClsDef" ):
                return visitor.visitClsDef(self)
            else:
                return visitor.visitChildren(self)



    def topDef(self):

        localctx = LatteParser.TopDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_topDef)
        self._la = 0 # Token type
        try:
            self.state = 64
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LatteParser.INT, LatteParser.BOOL, LatteParser.STR, LatteParser.VOID, LatteParser.ID]:
                localctx = LatteParser.FnDefContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.type_()
                self.state = 42
                localctx.name = self.match(LatteParser.ID)
                self.state = 43
                self.match(LatteParser.LPAREN)
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LatteParser.INT) | (1 << LatteParser.BOOL) | (1 << LatteParser.STR) | (1 << LatteParser.VOID) | (1 << LatteParser.ID))) != 0):
                    self.state = 44
                    self.argVec()


                self.state = 47
                self.match(LatteParser.RPAREN)
                self.state = 48
                self.block()
                pass
            elif token in [LatteParser.CLS]:
                localctx = LatteParser.ClsDefContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.match(LatteParser.CLS)
                self.state = 51
                localctx.name = self.match(LatteParser.ID)
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==LatteParser.EXTENDS:
                    self.state = 52
                    self.match(LatteParser.EXTENDS)
                    self.state = 53
                    localctx.supercls = self.match(LatteParser.ID)


                self.state = 56
                self.match(LatteParser.LBRACE)
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LatteParser.INT) | (1 << LatteParser.BOOL) | (1 << LatteParser.STR) | (1 << LatteParser.VOID) | (1 << LatteParser.CLS) | (1 << LatteParser.ID))) != 0):
                    self.state = 57
                    self.clsElem()
                    self.state = 62
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 63
                self.match(LatteParser.RBRACE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArgVecContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatteParser.ArgContext)
            else:
                return self.getTypedRuleContext(LatteParser.ArgContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(LatteParser.COMMA)
            else:
                return self.getToken(LatteParser.COMMA, i)

        def getRuleIndex(self):
            return LatteParser.RULE_argVec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgVec" ):
                listener.enterArgVec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgVec" ):
                listener.exitArgVec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgVec" ):
                return visitor.visitArgVec(self)
            else:
                return visitor.visitChildren(self)




    def argVec(self):

        localctx = LatteParser.ArgVecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_argVec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.arg()
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LatteParser.COMMA:
                self.state = 67
                self.match(LatteParser.COMMA)
                self.state = 68
                self.arg()
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token

        def type_(self):
            return self.getTypedRuleContext(LatteParser.Type_Context,0)


        def ID(self):
            return self.getToken(LatteParser.ID, 0)

        def getRuleIndex(self):
            return LatteParser.RULE_arg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArg" ):
                listener.enterArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArg" ):
                listener.exitArg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArg" ):
                return visitor.visitArg(self)
            else:
                return visitor.visitChildren(self)




    def arg(self):

        localctx = LatteParser.ArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_arg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.type_()
            self.state = 75
            localctx.name = self.match(LatteParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(LatteParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(LatteParser.RBRACE, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatteParser.StmtContext)
            else:
                return self.getTypedRuleContext(LatteParser.StmtContext,i)


        def getRuleIndex(self):
            return LatteParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = LatteParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(LatteParser.LBRACE)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LatteParser.SEM) | (1 << LatteParser.LBRACE) | (1 << LatteParser.LPAREN) | (1 << LatteParser.INT) | (1 << LatteParser.BOOL) | (1 << LatteParser.STR) | (1 << LatteParser.VOID) | (1 << LatteParser.SUB) | (1 << LatteParser.NOT) | (1 << LatteParser.RETURN) | (1 << LatteParser.IF) | (1 << LatteParser.WHILE) | (1 << LatteParser.FOR) | (1 << LatteParser.TRUE) | (1 << LatteParser.FALSE) | (1 << LatteParser.NEW) | (1 << LatteParser.NULL) | (1 << LatteParser.NUMBER) | (1 << LatteParser.ID) | (1 << LatteParser.STRING))) != 0):
                self.state = 78
                self.stmt()
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 84
            self.match(LatteParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ClsElemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LatteParser.RULE_clsElem

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FieldContext(ClsElemContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.ClsElemContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def type_(self):
            return self.getTypedRuleContext(LatteParser.Type_Context,0)

        def ID(self):
            return self.getToken(LatteParser.ID, 0)
        def SEM(self):
            return self.getToken(LatteParser.SEM, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField" ):
                listener.enterField(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField" ):
                listener.exitField(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField" ):
                return visitor.visitField(self)
            else:
                return visitor.visitChildren(self)


    class MethodContext(ClsElemContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.ClsElemContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def topDef(self):
            return self.getTypedRuleContext(LatteParser.TopDefContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod" ):
                listener.enterMethod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod" ):
                listener.exitMethod(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod" ):
                return visitor.visitMethod(self)
            else:
                return visitor.visitChildren(self)



    def clsElem(self):

        localctx = LatteParser.ClsElemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_clsElem)
        try:
            self.state = 91
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = LatteParser.FieldContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.type_()
                self.state = 87
                self.match(LatteParser.ID)
                self.state = 88
                self.match(LatteParser.SEM)
                pass

            elif la_ == 2:
                localctx = LatteParser.MethodContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.topDef()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LatteParser.RULE_stmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AssContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def identVec(self):
            return self.getTypedRuleContext(LatteParser.IdentVecContext,0)

        def ASS(self):
            return self.getToken(LatteParser.ASS, 0)
        def expr(self):
            return self.getTypedRuleContext(LatteParser.ExprContext,0)

        def SEM(self):
            return self.getToken(LatteParser.SEM, 0)
        def arrAcc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatteParser.ArrAccContext)
            else:
                return self.getTypedRuleContext(LatteParser.ArrAccContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAss" ):
                listener.enterAss(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAss" ):
                listener.exitAss(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAss" ):
                return visitor.visitAss(self)
            else:
                return visitor.visitChildren(self)


    class RetContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(LatteParser.RETURN, 0)
        def expr(self):
            return self.getTypedRuleContext(LatteParser.ExprContext,0)

        def SEM(self):
            return self.getToken(LatteParser.SEM, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRet" ):
                listener.enterRet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRet" ):
                listener.exitRet(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRet" ):
                return visitor.visitRet(self)
            else:
                return visitor.visitChildren(self)


    class CondContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.StmtContext
            super().__init__(parser)
            self.cond = None # ExprContext
            self.true_stmt = None # StmtContext
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(LatteParser.IF, 0)
        def LPAREN(self):
            return self.getToken(LatteParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(LatteParser.RPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(LatteParser.ExprContext,0)

        def stmt(self):
            return self.getTypedRuleContext(LatteParser.StmtContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCond" ):
                listener.enterCond(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCond" ):
                listener.exitCond(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCond" ):
                return visitor.visitCond(self)
            else:
                return visitor.visitChildren(self)


    class CondElseContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.StmtContext
            super().__init__(parser)
            self.cond = None # ExprContext
            self.true_stmt = None # StmtContext
            self.false_stmt = None # StmtContext
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(LatteParser.IF, 0)
        def LPAREN(self):
            return self.getToken(LatteParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(LatteParser.RPAREN, 0)
        def ELSE(self):
            return self.getToken(LatteParser.ELSE, 0)
        def expr(self):
            return self.getTypedRuleContext(LatteParser.ExprContext,0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatteParser.StmtContext)
            else:
                return self.getTypedRuleContext(LatteParser.StmtContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondElse" ):
                listener.enterCondElse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondElse" ):
                listener.exitCondElse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondElse" ):
                return visitor.visitCondElse(self)
            else:
                return visitor.visitChildren(self)


    class VRetContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(LatteParser.RETURN, 0)
        def SEM(self):
            return self.getToken(LatteParser.SEM, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVRet" ):
                listener.enterVRet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVRet" ):
                listener.exitVRet(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVRet" ):
                return visitor.visitVRet(self)
            else:
                return visitor.visitChildren(self)


    class BlockStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def block(self):
            return self.getTypedRuleContext(LatteParser.BlockContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockStmt" ):
                listener.enterBlockStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockStmt" ):
                listener.exitBlockStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockStmt" ):
                return visitor.visitBlockStmt(self)
            else:
                return visitor.visitChildren(self)


    class DeclContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def type_(self):
            return self.getTypedRuleContext(LatteParser.Type_Context,0)

        def item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatteParser.ItemContext)
            else:
                return self.getTypedRuleContext(LatteParser.ItemContext,i)

        def SEM(self):
            return self.getToken(LatteParser.SEM, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(LatteParser.COMMA)
            else:
                return self.getToken(LatteParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecl" ):
                listener.enterDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecl" ):
                listener.exitDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)


    class WhileContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.StmtContext
            super().__init__(parser)
            self.cond = None # ExprContext
            self.true_stmt = None # StmtContext
            self.copyFrom(ctx)

        def WHILE(self):
            return self.getToken(LatteParser.WHILE, 0)
        def LPAREN(self):
            return self.getToken(LatteParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(LatteParser.RPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(LatteParser.ExprContext,0)

        def stmt(self):
            return self.getTypedRuleContext(LatteParser.StmtContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile" ):
                listener.enterWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile" ):
                listener.exitWhile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile" ):
                return visitor.visitWhile(self)
            else:
                return visitor.visitChildren(self)


    class SExpContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(LatteParser.ExprContext,0)

        def SEM(self):
            return self.getToken(LatteParser.SEM, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSExp" ):
                listener.enterSExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSExp" ):
                listener.exitSExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSExp" ):
                return visitor.visitSExp(self)
            else:
                return visitor.visitChildren(self)


    class ForEachContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FOR(self):
            return self.getToken(LatteParser.FOR, 0)
        def LPAREN(self):
            return self.getToken(LatteParser.LPAREN, 0)
        def type_(self):
            return self.getTypedRuleContext(LatteParser.Type_Context,0)

        def ID(self):
            return self.getToken(LatteParser.ID, 0)
        def COLON(self):
            return self.getToken(LatteParser.COLON, 0)
        def expr(self):
            return self.getTypedRuleContext(LatteParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(LatteParser.RPAREN, 0)
        def stmt(self):
            return self.getTypedRuleContext(LatteParser.StmtContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForEach" ):
                listener.enterForEach(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForEach" ):
                listener.exitForEach(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForEach" ):
                return visitor.visitForEach(self)
            else:
                return visitor.visitChildren(self)


    class DecrContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.StmtContext
            super().__init__(parser)
            self.name = None # Token
            self.copyFrom(ctx)

        def DECR(self):
            return self.getToken(LatteParser.DECR, 0)
        def SEM(self):
            return self.getToken(LatteParser.SEM, 0)
        def ID(self):
            return self.getToken(LatteParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecr" ):
                listener.enterDecr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecr" ):
                listener.exitDecr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecr" ):
                return visitor.visitDecr(self)
            else:
                return visitor.visitChildren(self)


    class EmptyContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SEM(self):
            return self.getToken(LatteParser.SEM, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmpty" ):
                listener.enterEmpty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmpty" ):
                listener.exitEmpty(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmpty" ):
                return visitor.visitEmpty(self)
            else:
                return visitor.visitChildren(self)


    class IncrContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.StmtContext
            super().__init__(parser)
            self.name = None # Token
            self.copyFrom(ctx)

        def INCR(self):
            return self.getToken(LatteParser.INCR, 0)
        def SEM(self):
            return self.getToken(LatteParser.SEM, 0)
        def ID(self):
            return self.getToken(LatteParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIncr" ):
                listener.enterIncr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIncr" ):
                listener.exitIncr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIncr" ):
                return visitor.visitIncr(self)
            else:
                return visitor.visitChildren(self)



    def stmt(self):

        localctx = LatteParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_stmt)
        self._la = 0 # Token type
        try:
            self.state = 161
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                localctx = LatteParser.EmptyContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.match(LatteParser.SEM)
                pass

            elif la_ == 2:
                localctx = LatteParser.BlockStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 94
                self.block()
                pass

            elif la_ == 3:
                localctx = LatteParser.DeclContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 95
                self.type_()
                self.state = 96
                self.item()
                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==LatteParser.COMMA:
                    self.state = 97
                    self.match(LatteParser.COMMA)
                    self.state = 98
                    self.item()
                    self.state = 103
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 104
                self.match(LatteParser.SEM)
                pass

            elif la_ == 4:
                localctx = LatteParser.AssContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 106
                self.identVec()
                self.state = 110
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==LatteParser.LBRACK:
                    self.state = 107
                    self.arrAcc()
                    self.state = 112
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 113
                self.match(LatteParser.ASS)
                self.state = 114
                self.expr(0)
                self.state = 115
                self.match(LatteParser.SEM)
                pass

            elif la_ == 5:
                localctx = LatteParser.IncrContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 117
                localctx.name = self.match(LatteParser.ID)
                self.state = 118
                self.match(LatteParser.INCR)
                self.state = 119
                self.match(LatteParser.SEM)
                pass

            elif la_ == 6:
                localctx = LatteParser.DecrContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 120
                localctx.name = self.match(LatteParser.ID)
                self.state = 121
                self.match(LatteParser.DECR)
                self.state = 122
                self.match(LatteParser.SEM)
                pass

            elif la_ == 7:
                localctx = LatteParser.RetContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 123
                self.match(LatteParser.RETURN)
                self.state = 124
                self.expr(0)
                self.state = 125
                self.match(LatteParser.SEM)
                pass

            elif la_ == 8:
                localctx = LatteParser.VRetContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 127
                self.match(LatteParser.RETURN)
                self.state = 128
                self.match(LatteParser.SEM)
                pass

            elif la_ == 9:
                localctx = LatteParser.CondContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 129
                self.match(LatteParser.IF)
                self.state = 130
                self.match(LatteParser.LPAREN)
                self.state = 131
                localctx.cond = self.expr(0)
                self.state = 132
                self.match(LatteParser.RPAREN)
                self.state = 133
                localctx.true_stmt = self.stmt()
                pass

            elif la_ == 10:
                localctx = LatteParser.CondElseContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 135
                self.match(LatteParser.IF)
                self.state = 136
                self.match(LatteParser.LPAREN)
                self.state = 137
                localctx.cond = self.expr(0)
                self.state = 138
                self.match(LatteParser.RPAREN)
                self.state = 139
                localctx.true_stmt = self.stmt()
                self.state = 140
                self.match(LatteParser.ELSE)
                self.state = 141
                localctx.false_stmt = self.stmt()
                pass

            elif la_ == 11:
                localctx = LatteParser.WhileContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 143
                self.match(LatteParser.WHILE)
                self.state = 144
                self.match(LatteParser.LPAREN)
                self.state = 145
                localctx.cond = self.expr(0)
                self.state = 146
                self.match(LatteParser.RPAREN)
                self.state = 147
                localctx.true_stmt = self.stmt()
                pass

            elif la_ == 12:
                localctx = LatteParser.ForEachContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 149
                self.match(LatteParser.FOR)
                self.state = 150
                self.match(LatteParser.LPAREN)
                self.state = 151
                self.type_()
                self.state = 152
                self.match(LatteParser.ID)
                self.state = 153
                self.match(LatteParser.COLON)
                self.state = 154
                self.expr(0)
                self.state = 155
                self.match(LatteParser.RPAREN)
                self.state = 156
                self.stmt()
                pass

            elif la_ == 13:
                localctx = LatteParser.SExpContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 158
                self.expr(0)
                self.state = 159
                self.match(LatteParser.SEM)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArrAccContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(LatteParser.LBRACK, 0)

        def expr(self):
            return self.getTypedRuleContext(LatteParser.ExprContext,0)


        def RBRACK(self):
            return self.getToken(LatteParser.RBRACK, 0)

        def getRuleIndex(self):
            return LatteParser.RULE_arrAcc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrAcc" ):
                listener.enterArrAcc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrAcc" ):
                listener.exitArrAcc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrAcc" ):
                return visitor.visitArrAcc(self)
            else:
                return visitor.visitChildren(self)




    def arrAcc(self):

        localctx = LatteParser.ArrAccContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_arrAcc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(LatteParser.LBRACK)
            self.state = 164
            self.expr(0)
            self.state = 165
            self.match(LatteParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IdentVecContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(LatteParser.ID)
            else:
                return self.getToken(LatteParser.ID, i)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(LatteParser.DOT)
            else:
                return self.getToken(LatteParser.DOT, i)

        def getRuleIndex(self):
            return LatteParser.RULE_identVec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentVec" ):
                listener.enterIdentVec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentVec" ):
                listener.exitIdentVec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentVec" ):
                return visitor.visitIdentVec(self)
            else:
                return visitor.visitChildren(self)




    def identVec(self):

        localctx = LatteParser.IdentVecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_identVec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(LatteParser.ID)
            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LatteParser.DOT:
                self.state = 168
                self.match(LatteParser.DOT)
                self.state = 169
                self.match(LatteParser.ID)
                self.state = 174
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Type_Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LatteParser.RULE_type_

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TNonArrayContext(Type_Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.Type_Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def base_type(self):
            return self.getTypedRuleContext(LatteParser.Base_typeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTNonArray" ):
                listener.enterTNonArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTNonArray" ):
                listener.exitTNonArray(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTNonArray" ):
                return visitor.visitTNonArray(self)
            else:
                return visitor.visitChildren(self)


    class TArrayContext(Type_Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.Type_Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def basic_type(self):
            return self.getTypedRuleContext(LatteParser.Basic_typeContext,0)

        def LBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(LatteParser.LBRACK)
            else:
                return self.getToken(LatteParser.LBRACK, i)
        def RBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(LatteParser.RBRACK)
            else:
                return self.getToken(LatteParser.RBRACK, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTArray" ):
                listener.enterTArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTArray" ):
                listener.exitTArray(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTArray" ):
                return visitor.visitTArray(self)
            else:
                return visitor.visitChildren(self)



    def type_(self):

        localctx = LatteParser.Type_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_type_)
        self._la = 0 # Token type
        try:
            self.state = 183
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                localctx = LatteParser.TNonArrayContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.base_type()
                pass

            elif la_ == 2:
                localctx = LatteParser.TArrayContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 176
                self.basic_type()
                self.state = 179 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 177
                    self.match(LatteParser.LBRACK)
                    self.state = 178
                    self.match(LatteParser.RBRACK)
                    self.state = 181 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==LatteParser.LBRACK):
                        break

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Base_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LatteParser.RULE_base_type

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TIdentContext(Base_typeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.Base_typeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(LatteParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTIdent" ):
                listener.enterTIdent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTIdent" ):
                listener.exitTIdent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTIdent" ):
                return visitor.visitTIdent(self)
            else:
                return visitor.visitChildren(self)


    class TBasicContext(Base_typeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.Base_typeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def basic_type(self):
            return self.getTypedRuleContext(LatteParser.Basic_typeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTBasic" ):
                listener.enterTBasic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTBasic" ):
                listener.exitTBasic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTBasic" ):
                return visitor.visitTBasic(self)
            else:
                return visitor.visitChildren(self)



    def base_type(self):

        localctx = LatteParser.Base_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_base_type)
        try:
            self.state = 187
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LatteParser.INT, LatteParser.BOOL, LatteParser.STR, LatteParser.VOID]:
                localctx = LatteParser.TBasicContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 185
                self.basic_type()
                pass
            elif token in [LatteParser.ID]:
                localctx = LatteParser.TIdentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 186
                self.match(LatteParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Basic_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LatteParser.RULE_basic_type

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TVoidContext(Basic_typeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.Basic_typeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VOID(self):
            return self.getToken(LatteParser.VOID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTVoid" ):
                listener.enterTVoid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTVoid" ):
                listener.exitTVoid(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTVoid" ):
                return visitor.visitTVoid(self)
            else:
                return visitor.visitChildren(self)


    class TBoolContext(Basic_typeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.Basic_typeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL(self):
            return self.getToken(LatteParser.BOOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTBool" ):
                listener.enterTBool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTBool" ):
                listener.exitTBool(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTBool" ):
                return visitor.visitTBool(self)
            else:
                return visitor.visitChildren(self)


    class TStrContext(Basic_typeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.Basic_typeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STR(self):
            return self.getToken(LatteParser.STR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTStr" ):
                listener.enterTStr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTStr" ):
                listener.exitTStr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTStr" ):
                return visitor.visitTStr(self)
            else:
                return visitor.visitChildren(self)


    class TIntContext(Basic_typeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.Basic_typeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(LatteParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTInt" ):
                listener.enterTInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTInt" ):
                listener.exitTInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTInt" ):
                return visitor.visitTInt(self)
            else:
                return visitor.visitChildren(self)



    def basic_type(self):

        localctx = LatteParser.Basic_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_basic_type)
        try:
            self.state = 193
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LatteParser.INT]:
                localctx = LatteParser.TIntContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                self.match(LatteParser.INT)
                pass
            elif token in [LatteParser.STR]:
                localctx = LatteParser.TStrContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 190
                self.match(LatteParser.STR)
                pass
            elif token in [LatteParser.BOOL]:
                localctx = LatteParser.TBoolContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 191
                self.match(LatteParser.BOOL)
                pass
            elif token in [LatteParser.VOID]:
                localctx = LatteParser.TVoidContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 192
                self.match(LatteParser.VOID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class New_expr_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LatteParser.ID, 0)

        def LBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(LatteParser.LBRACK)
            else:
                return self.getToken(LatteParser.LBRACK, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatteParser.ExprContext)
            else:
                return self.getTypedRuleContext(LatteParser.ExprContext,i)


        def RBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(LatteParser.RBRACK)
            else:
                return self.getToken(LatteParser.RBRACK, i)

        def basic_type(self):
            return self.getTypedRuleContext(LatteParser.Basic_typeContext,0)


        def getRuleIndex(self):
            return LatteParser.RULE_new_expr_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNew_expr_type" ):
                listener.enterNew_expr_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNew_expr_type" ):
                listener.exitNew_expr_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNew_expr_type" ):
                return visitor.visitNew_expr_type(self)
            else:
                return visitor.visitChildren(self)




    def new_expr_type(self):

        localctx = LatteParser.New_expr_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_new_expr_type)
        try:
            self.state = 211
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LatteParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self.match(LatteParser.ID)
                self.state = 200
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                if la_ == 1:
                    self.state = 196
                    self.match(LatteParser.LBRACK)
                    self.state = 197
                    self.expr(0)
                    self.state = 198
                    self.match(LatteParser.RBRACK)


                pass
            elif token in [LatteParser.INT, LatteParser.BOOL, LatteParser.STR, LatteParser.VOID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 202
                self.basic_type()
                self.state = 207 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 203
                        self.match(LatteParser.LBRACK)
                        self.state = 204
                        self.expr(0)
                        self.state = 205
                        self.match(LatteParser.RBRACK)

                    else:
                        raise NoViableAltException(self)
                    self.state = 209 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ItemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token

        def ID(self):
            return self.getToken(LatteParser.ID, 0)

        def ASS(self):
            return self.getToken(LatteParser.ASS, 0)

        def expr(self):
            return self.getTypedRuleContext(LatteParser.ExprContext,0)


        def getRuleIndex(self):
            return LatteParser.RULE_item

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItem" ):
                listener.enterItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItem" ):
                listener.exitItem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitItem" ):
                return visitor.visitItem(self)
            else:
                return visitor.visitChildren(self)




    def item(self):

        localctx = LatteParser.ItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_item)
        try:
            self.state = 217
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                localctx.name = self.match(LatteParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 214
                localctx.name = self.match(LatteParser.ID)
                self.state = 215
                self.match(LatteParser.ASS)
                self.state = 216
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LatteParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class EIdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(LatteParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEId" ):
                listener.enterEId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEId" ):
                listener.exitEId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEId" ):
                return visitor.visitEId(self)
            else:
                return visitor.visitChildren(self)


    class EFunCallContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.ExprContext
            super().__init__(parser)
            self.name = None # Token
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(LatteParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(LatteParser.RPAREN, 0)
        def ID(self):
            return self.getToken(LatteParser.ID, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatteParser.ExprContext)
            else:
                return self.getTypedRuleContext(LatteParser.ExprContext,i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(LatteParser.COMMA)
            else:
                return self.getToken(LatteParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEFunCall" ):
                listener.enterEFunCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEFunCall" ):
                listener.exitEFunCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEFunCall" ):
                return visitor.visitEFunCall(self)
            else:
                return visitor.visitChildren(self)


    class ERelOpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.ExprContext
            super().__init__(parser)
            self.lhs = None # ExprContext
            self.rhs = None # ExprContext
            self.copyFrom(ctx)

        def relOp(self):
            return self.getTypedRuleContext(LatteParser.RelOpContext,0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatteParser.ExprContext)
            else:
                return self.getTypedRuleContext(LatteParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterERelOp" ):
                listener.enterERelOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitERelOp" ):
                listener.exitERelOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitERelOp" ):
                return visitor.visitERelOp(self)
            else:
                return visitor.visitChildren(self)


    class ETrueContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TRUE(self):
            return self.getToken(LatteParser.TRUE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterETrue" ):
                listener.enterETrue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitETrue" ):
                listener.exitETrue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitETrue" ):
                return visitor.visitETrue(self)
            else:
                return visitor.visitChildren(self)


    class ECastContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(LatteParser.LPAREN, 0)
        def ID(self):
            return self.getToken(LatteParser.ID, 0)
        def RPAREN(self):
            return self.getToken(LatteParser.RPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(LatteParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterECast" ):
                listener.enterECast(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitECast" ):
                listener.exitECast(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitECast" ):
                return visitor.visitECast(self)
            else:
                return visitor.visitChildren(self)


    class EOrContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.ExprContext
            super().__init__(parser)
            self.lhs = None # ExprContext
            self.rhs = None # ExprContext
            self.copyFrom(ctx)

        def OR(self):
            return self.getToken(LatteParser.OR, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatteParser.ExprContext)
            else:
                return self.getTypedRuleContext(LatteParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEOr" ):
                listener.enterEOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEOr" ):
                listener.exitEOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEOr" ):
                return visitor.visitEOr(self)
            else:
                return visitor.visitChildren(self)


    class EIntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(LatteParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEInt" ):
                listener.enterEInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEInt" ):
                listener.exitEInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEInt" ):
                return visitor.visitEInt(self)
            else:
                return visitor.visitChildren(self)


    class EUnOpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(LatteParser.ExprContext,0)

        def SUB(self):
            return self.getToken(LatteParser.SUB, 0)
        def NOT(self):
            return self.getToken(LatteParser.NOT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEUnOp" ):
                listener.enterEUnOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEUnOp" ):
                listener.exitEUnOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEUnOp" ):
                return visitor.visitEUnOp(self)
            else:
                return visitor.visitChildren(self)


    class EStrContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(LatteParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEStr" ):
                listener.enterEStr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEStr" ):
                listener.exitEStr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEStr" ):
                return visitor.visitEStr(self)
            else:
                return visitor.visitChildren(self)


    class EMulOpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.ExprContext
            super().__init__(parser)
            self.lhs = None # ExprContext
            self.rhs = None # ExprContext
            self.copyFrom(ctx)

        def mulOp(self):
            return self.getTypedRuleContext(LatteParser.MulOpContext,0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatteParser.ExprContext)
            else:
                return self.getTypedRuleContext(LatteParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEMulOp" ):
                listener.enterEMulOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEMulOp" ):
                listener.exitEMulOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEMulOp" ):
                return visitor.visitEMulOp(self)
            else:
                return visitor.visitChildren(self)


    class EAndContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.ExprContext
            super().__init__(parser)
            self.lhs = None # ExprContext
            self.rhs = None # ExprContext
            self.copyFrom(ctx)

        def AND(self):
            return self.getToken(LatteParser.AND, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatteParser.ExprContext)
            else:
                return self.getTypedRuleContext(LatteParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEAnd" ):
                listener.enterEAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEAnd" ):
                listener.exitEAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEAnd" ):
                return visitor.visitEAnd(self)
            else:
                return visitor.visitChildren(self)


    class EParenContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(LatteParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(LatteParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(LatteParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEParen" ):
                listener.enterEParen(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEParen" ):
                listener.exitEParen(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEParen" ):
                return visitor.visitEParen(self)
            else:
                return visitor.visitChildren(self)


    class EFalseContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FALSE(self):
            return self.getToken(LatteParser.FALSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEFalse" ):
                listener.enterEFalse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEFalse" ):
                listener.exitEFalse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEFalse" ):
                return visitor.visitEFalse(self)
            else:
                return visitor.visitChildren(self)


    class ENewContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEW(self):
            return self.getToken(LatteParser.NEW, 0)
        def new_expr_type(self):
            return self.getTypedRuleContext(LatteParser.New_expr_typeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterENew" ):
                listener.enterENew(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitENew" ):
                listener.exitENew(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitENew" ):
                return visitor.visitENew(self)
            else:
                return visitor.visitChildren(self)


    class EAddOpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.ExprContext
            super().__init__(parser)
            self.lhs = None # ExprContext
            self.rhs = None # ExprContext
            self.copyFrom(ctx)

        def addOp(self):
            return self.getTypedRuleContext(LatteParser.AddOpContext,0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatteParser.ExprContext)
            else:
                return self.getTypedRuleContext(LatteParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEAddOp" ):
                listener.enterEAddOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEAddOp" ):
                listener.exitEAddOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEAddOp" ):
                return visitor.visitEAddOp(self)
            else:
                return visitor.visitChildren(self)


    class EAccContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatteParser.ExprContext)
            else:
                return self.getTypedRuleContext(LatteParser.ExprContext,i)

        def DOT(self):
            return self.getToken(LatteParser.DOT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEAcc" ):
                listener.enterEAcc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEAcc" ):
                listener.exitEAcc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEAcc" ):
                return visitor.visitEAcc(self)
            else:
                return visitor.visitChildren(self)


    class ENullContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NULL(self):
            return self.getToken(LatteParser.NULL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterENull" ):
                listener.enterENull(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitENull" ):
                listener.exitENull(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitENull" ):
                return visitor.visitENull(self)
            else:
                return visitor.visitChildren(self)


    class EAccArrContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LatteParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatteParser.ExprContext)
            else:
                return self.getTypedRuleContext(LatteParser.ExprContext,i)

        def LBRACK(self):
            return self.getToken(LatteParser.LBRACK, 0)
        def RBRACK(self):
            return self.getToken(LatteParser.RBRACK, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEAccArr" ):
                listener.enterEAccArr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEAccArr" ):
                listener.exitEAccArr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEAccArr" ):
                return visitor.visitEAccArr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LatteParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                localctx = LatteParser.EUnOpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 220
                _la = self._input.LA(1)
                if not(_la==LatteParser.SUB or _la==LatteParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 221
                self.expr(18)
                pass

            elif la_ == 2:
                localctx = LatteParser.EIdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 222
                self.match(LatteParser.ID)
                pass

            elif la_ == 3:
                localctx = LatteParser.EIntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 223
                self.match(LatteParser.NUMBER)
                pass

            elif la_ == 4:
                localctx = LatteParser.ETrueContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 224
                self.match(LatteParser.TRUE)
                pass

            elif la_ == 5:
                localctx = LatteParser.EFalseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 225
                self.match(LatteParser.FALSE)
                pass

            elif la_ == 6:
                localctx = LatteParser.ENullContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 226
                self.match(LatteParser.NULL)
                pass

            elif la_ == 7:
                localctx = LatteParser.ENewContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 227
                self.match(LatteParser.NEW)
                self.state = 228
                self.new_expr_type()
                pass

            elif la_ == 8:
                localctx = LatteParser.EFunCallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 229
                localctx.name = self.match(LatteParser.ID)
                self.state = 230
                self.match(LatteParser.LPAREN)
                self.state = 239
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LatteParser.LPAREN) | (1 << LatteParser.SUB) | (1 << LatteParser.NOT) | (1 << LatteParser.TRUE) | (1 << LatteParser.FALSE) | (1 << LatteParser.NEW) | (1 << LatteParser.NULL) | (1 << LatteParser.NUMBER) | (1 << LatteParser.ID) | (1 << LatteParser.STRING))) != 0):
                    self.state = 231
                    self.expr(0)
                    self.state = 236
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==LatteParser.COMMA:
                        self.state = 232
                        self.match(LatteParser.COMMA)
                        self.state = 233
                        self.expr(0)
                        self.state = 238
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 241
                self.match(LatteParser.RPAREN)
                pass

            elif la_ == 9:
                localctx = LatteParser.ECastContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 242
                self.match(LatteParser.LPAREN)
                self.state = 243
                self.match(LatteParser.ID)
                self.state = 244
                self.match(LatteParser.RPAREN)
                self.state = 245
                self.expr(3)
                pass

            elif la_ == 10:
                localctx = LatteParser.EStrContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 246
                self.match(LatteParser.STRING)
                pass

            elif la_ == 11:
                localctx = LatteParser.EParenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 247
                self.match(LatteParser.LPAREN)
                self.state = 248
                self.expr(0)
                self.state = 249
                self.match(LatteParser.RPAREN)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 281
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 279
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                    if la_ == 1:
                        localctx = LatteParser.EMulOpContext(self, LatteParser.ExprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 253
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 254
                        self.mulOp()
                        self.state = 255
                        localctx.rhs = self.expr(18)
                        pass

                    elif la_ == 2:
                        localctx = LatteParser.EAddOpContext(self, LatteParser.ExprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 257
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 258
                        self.addOp()
                        self.state = 259
                        localctx.rhs = self.expr(17)
                        pass

                    elif la_ == 3:
                        localctx = LatteParser.ERelOpContext(self, LatteParser.ExprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 261
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 262
                        self.relOp()
                        self.state = 263
                        localctx.rhs = self.expr(16)
                        pass

                    elif la_ == 4:
                        localctx = LatteParser.EAndContext(self, LatteParser.ExprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 265
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 266
                        self.match(LatteParser.AND)
                        self.state = 267
                        localctx.rhs = self.expr(14)
                        pass

                    elif la_ == 5:
                        localctx = LatteParser.EOrContext(self, LatteParser.ExprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 268
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 269
                        self.match(LatteParser.OR)
                        self.state = 270
                        localctx.rhs = self.expr(13)
                        pass

                    elif la_ == 6:
                        localctx = LatteParser.EAccContext(self, LatteParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 271
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 272
                        self.match(LatteParser.DOT)
                        self.state = 273
                        self.expr(6)
                        pass

                    elif la_ == 7:
                        localctx = LatteParser.EAccArrContext(self, LatteParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 274
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 275
                        self.match(LatteParser.LBRACK)
                        self.state = 276
                        self.expr(0)
                        self.state = 277
                        self.match(LatteParser.RBRACK)
                        pass

             
                self.state = 283
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class AddOpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(LatteParser.ADD, 0)

        def SUB(self):
            return self.getToken(LatteParser.SUB, 0)

        def getRuleIndex(self):
            return LatteParser.RULE_addOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddOp" ):
                listener.enterAddOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddOp" ):
                listener.exitAddOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddOp" ):
                return visitor.visitAddOp(self)
            else:
                return visitor.visitChildren(self)




    def addOp(self):

        localctx = LatteParser.AddOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_addOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            _la = self._input.LA(1)
            if not(_la==LatteParser.ADD or _la==LatteParser.SUB):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MulOpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MUL(self):
            return self.getToken(LatteParser.MUL, 0)

        def DIV(self):
            return self.getToken(LatteParser.DIV, 0)

        def MOD(self):
            return self.getToken(LatteParser.MOD, 0)

        def getRuleIndex(self):
            return LatteParser.RULE_mulOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulOp" ):
                listener.enterMulOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulOp" ):
                listener.exitMulOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulOp" ):
                return visitor.visitMulOp(self)
            else:
                return visitor.visitChildren(self)




    def mulOp(self):

        localctx = LatteParser.MulOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_mulOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LatteParser.MUL) | (1 << LatteParser.DIV) | (1 << LatteParser.MOD))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RelOpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(LatteParser.LT, 0)

        def LEQ(self):
            return self.getToken(LatteParser.LEQ, 0)

        def GT(self):
            return self.getToken(LatteParser.GT, 0)

        def GEQ(self):
            return self.getToken(LatteParser.GEQ, 0)

        def EQ(self):
            return self.getToken(LatteParser.EQ, 0)

        def NEQ(self):
            return self.getToken(LatteParser.NEQ, 0)

        def getRuleIndex(self):
            return LatteParser.RULE_relOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelOp" ):
                listener.enterRelOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelOp" ):
                listener.exitRelOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelOp" ):
                return visitor.visitRelOp(self)
            else:
                return visitor.visitChildren(self)




    def relOp(self):

        localctx = LatteParser.RelOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_relOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LatteParser.LT) | (1 << LatteParser.LEQ) | (1 << LatteParser.GT) | (1 << LatteParser.GEQ) | (1 << LatteParser.EQ) | (1 << LatteParser.NEQ))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[14] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 5)
         





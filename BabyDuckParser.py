# Generated from BabyDuck.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,36,257,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        1,0,1,0,1,0,1,0,3,0,59,8,0,1,0,5,0,62,8,0,10,0,12,0,65,9,0,1,0,1,
        0,1,0,1,0,1,1,4,1,72,8,1,11,1,12,1,73,1,2,1,2,1,2,1,2,5,2,80,8,2,
        10,2,12,2,83,9,2,1,2,1,2,1,2,1,2,1,3,1,3,3,3,91,8,3,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,103,8,4,10,4,12,4,106,9,4,3,4,108,
        8,4,1,4,1,4,1,4,5,4,113,8,4,10,4,12,4,116,9,4,1,4,1,4,1,4,1,4,1,
        5,1,5,5,5,124,8,5,10,5,12,5,127,9,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,
        3,6,136,8,6,1,7,1,7,1,7,1,7,3,7,142,8,7,1,7,1,7,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,3,8,154,8,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,10,1,10,1,10,1,10,1,10,5,10,171,8,10,10,10,12,10,174,9,10,
        1,10,1,10,3,10,178,8,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,
        5,11,188,8,11,10,11,12,11,191,9,11,1,11,1,11,1,11,1,11,1,12,1,12,
        5,12,199,8,12,10,12,12,12,202,9,12,1,12,1,12,1,13,1,13,5,13,208,
        8,13,10,13,12,13,211,9,13,1,13,1,13,1,14,1,14,5,14,217,8,14,10,14,
        12,14,220,9,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,3,15,
        231,8,15,3,15,233,8,15,1,16,1,16,1,17,1,17,1,18,1,18,1,19,1,19,1,
        20,1,20,1,21,1,21,1,22,1,22,1,23,1,23,1,24,1,24,1,25,1,25,1,26,1,
        26,1,26,0,0,27,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,44,46,48,50,52,0,4,1,0,22,24,1,0,17,18,1,0,19,20,1,0,
        13,14,252,0,54,1,0,0,0,2,71,1,0,0,0,4,75,1,0,0,0,6,90,1,0,0,0,8,
        92,1,0,0,0,10,121,1,0,0,0,12,135,1,0,0,0,14,137,1,0,0,0,16,145,1,
        0,0,0,18,157,1,0,0,0,20,165,1,0,0,0,22,182,1,0,0,0,24,196,1,0,0,
        0,26,205,1,0,0,0,28,214,1,0,0,0,30,232,1,0,0,0,32,234,1,0,0,0,34,
        236,1,0,0,0,36,238,1,0,0,0,38,240,1,0,0,0,40,242,1,0,0,0,42,244,
        1,0,0,0,44,246,1,0,0,0,46,248,1,0,0,0,48,250,1,0,0,0,50,252,1,0,
        0,0,52,254,1,0,0,0,54,55,5,1,0,0,55,56,5,15,0,0,56,58,5,34,0,0,57,
        59,3,2,1,0,58,57,1,0,0,0,58,59,1,0,0,0,59,63,1,0,0,0,60,62,3,8,4,
        0,61,60,1,0,0,0,62,65,1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,66,
        1,0,0,0,65,63,1,0,0,0,66,67,3,50,25,0,67,68,3,52,26,0,68,69,5,34,
        0,0,69,1,1,0,0,0,70,72,3,4,2,0,71,70,1,0,0,0,72,73,1,0,0,0,73,71,
        1,0,0,0,73,74,1,0,0,0,74,3,1,0,0,0,75,76,5,2,0,0,76,81,5,15,0,0,
        77,78,5,35,0,0,78,80,5,15,0,0,79,77,1,0,0,0,80,83,1,0,0,0,81,79,
        1,0,0,0,81,82,1,0,0,0,82,84,1,0,0,0,83,81,1,0,0,0,84,85,5,36,0,0,
        85,86,3,6,3,0,86,87,5,34,0,0,87,5,1,0,0,0,88,91,3,46,23,0,89,91,
        3,48,24,0,90,88,1,0,0,0,90,89,1,0,0,0,91,7,1,0,0,0,92,93,3,44,22,
        0,93,94,5,15,0,0,94,107,5,28,0,0,95,96,5,15,0,0,96,97,5,36,0,0,97,
        104,3,6,3,0,98,99,5,35,0,0,99,100,5,15,0,0,100,101,5,36,0,0,101,
        103,3,6,3,0,102,98,1,0,0,0,103,106,1,0,0,0,104,102,1,0,0,0,104,105,
        1,0,0,0,105,108,1,0,0,0,106,104,1,0,0,0,107,95,1,0,0,0,107,108,1,
        0,0,0,108,109,1,0,0,0,109,110,5,29,0,0,110,114,5,32,0,0,111,113,
        3,4,2,0,112,111,1,0,0,0,113,116,1,0,0,0,114,112,1,0,0,0,114,115,
        1,0,0,0,115,117,1,0,0,0,116,114,1,0,0,0,117,118,3,10,5,0,118,119,
        5,33,0,0,119,120,5,34,0,0,120,9,1,0,0,0,121,125,5,30,0,0,122,124,
        3,12,6,0,123,122,1,0,0,0,124,127,1,0,0,0,125,123,1,0,0,0,125,126,
        1,0,0,0,126,128,1,0,0,0,127,125,1,0,0,0,128,129,5,31,0,0,129,11,
        1,0,0,0,130,136,3,14,7,0,131,136,3,16,8,0,132,136,3,18,9,0,133,136,
        3,22,11,0,134,136,3,20,10,0,135,130,1,0,0,0,135,131,1,0,0,0,135,
        132,1,0,0,0,135,133,1,0,0,0,135,134,1,0,0,0,136,13,1,0,0,0,137,138,
        5,15,0,0,138,141,5,21,0,0,139,142,3,24,12,0,140,142,5,16,0,0,141,
        139,1,0,0,0,141,140,1,0,0,0,142,143,1,0,0,0,143,144,5,34,0,0,144,
        15,1,0,0,0,145,146,3,34,17,0,146,147,5,28,0,0,147,148,3,24,12,0,
        148,149,5,29,0,0,149,153,3,10,5,0,150,151,3,36,18,0,151,152,3,10,
        5,0,152,154,1,0,0,0,153,150,1,0,0,0,153,154,1,0,0,0,154,155,1,0,
        0,0,155,156,5,34,0,0,156,17,1,0,0,0,157,158,3,38,19,0,158,159,3,
        10,5,0,159,160,3,40,20,0,160,161,5,28,0,0,161,162,3,24,12,0,162,
        163,5,29,0,0,163,164,5,34,0,0,164,19,1,0,0,0,165,166,3,42,21,0,166,
        172,5,28,0,0,167,168,3,24,12,0,168,169,5,35,0,0,169,171,1,0,0,0,
        170,167,1,0,0,0,171,174,1,0,0,0,172,170,1,0,0,0,172,173,1,0,0,0,
        173,177,1,0,0,0,174,172,1,0,0,0,175,178,3,24,12,0,176,178,5,16,0,
        0,177,175,1,0,0,0,177,176,1,0,0,0,178,179,1,0,0,0,179,180,5,29,0,
        0,180,181,5,34,0,0,181,21,1,0,0,0,182,183,5,15,0,0,183,189,5,28,
        0,0,184,185,3,24,12,0,185,186,5,35,0,0,186,188,1,0,0,0,187,184,1,
        0,0,0,188,191,1,0,0,0,189,187,1,0,0,0,189,190,1,0,0,0,190,192,1,
        0,0,0,191,189,1,0,0,0,192,193,3,24,12,0,193,194,5,29,0,0,194,195,
        5,34,0,0,195,23,1,0,0,0,196,200,3,26,13,0,197,199,7,0,0,0,198,197,
        1,0,0,0,199,202,1,0,0,0,200,198,1,0,0,0,200,201,1,0,0,0,201,203,
        1,0,0,0,202,200,1,0,0,0,203,204,3,26,13,0,204,25,1,0,0,0,205,209,
        3,28,14,0,206,208,7,1,0,0,207,206,1,0,0,0,208,211,1,0,0,0,209,207,
        1,0,0,0,209,210,1,0,0,0,210,212,1,0,0,0,211,209,1,0,0,0,212,213,
        3,28,14,0,213,27,1,0,0,0,214,218,3,30,15,0,215,217,7,2,0,0,216,215,
        1,0,0,0,217,220,1,0,0,0,218,216,1,0,0,0,218,219,1,0,0,0,219,221,
        1,0,0,0,220,218,1,0,0,0,221,222,3,30,15,0,222,29,1,0,0,0,223,224,
        5,28,0,0,224,225,3,24,12,0,225,226,5,29,0,0,226,233,1,0,0,0,227,
        230,7,1,0,0,228,231,5,15,0,0,229,231,3,32,16,0,230,228,1,0,0,0,230,
        229,1,0,0,0,231,233,1,0,0,0,232,223,1,0,0,0,232,227,1,0,0,0,233,
        31,1,0,0,0,234,235,7,3,0,0,235,33,1,0,0,0,236,237,5,3,0,0,237,35,
        1,0,0,0,238,239,5,4,0,0,239,37,1,0,0,0,240,241,5,5,0,0,241,39,1,
        0,0,0,242,243,5,6,0,0,243,41,1,0,0,0,244,245,5,7,0,0,245,43,1,0,
        0,0,246,247,5,8,0,0,247,45,1,0,0,0,248,249,5,9,0,0,249,47,1,0,0,
        0,250,251,5,10,0,0,251,49,1,0,0,0,252,253,5,11,0,0,253,51,1,0,0,
        0,254,255,5,12,0,0,255,53,1,0,0,0,20,58,63,73,81,90,104,107,114,
        125,135,141,153,172,177,189,200,209,218,230,232
    ]

class BabyDuckParser ( Parser ):

    grammarFileName = "BabyDuck.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'program'", "'var'", "'if'", "'else'", 
                     "'while'", "'do'", "'print'", "'void'", "'int'", "'float'", 
                     "'main'", "'end'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'='", "'!='", 
                     "'>'", "'<'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", "','", 
                     "':'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "INTEGER", "FLOAT_NUM", "ID", "STRING", 
                      "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "EQUALS", "NOTEQUALS", 
                      "GREATERTHAN", "LESSTHAN", "WS", "COMMENT", "COMMENT2", 
                      "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACKET", 
                      "RBRACKET", "SEMICOLON", "COMMA", "COLON" ]

    RULE_program = 0
    RULE_declarations = 1
    RULE_vars = 2
    RULE_type = 3
    RULE_funcs = 4
    RULE_body = 5
    RULE_statement = 6
    RULE_assign = 7
    RULE_condition = 8
    RULE_cycle = 9
    RULE_print = 10
    RULE_f_call = 11
    RULE_expression = 12
    RULE_exp = 13
    RULE_termino = 14
    RULE_factor = 15
    RULE_cte = 16
    RULE_if = 17
    RULE_else = 18
    RULE_while = 19
    RULE_do = 20
    RULE_print_w = 21
    RULE_void = 22
    RULE_int = 23
    RULE_float = 24
    RULE_main = 25
    RULE_end = 26

    ruleNames =  [ "program", "declarations", "vars", "type", "funcs", "body", 
                   "statement", "assign", "condition", "cycle", "print", 
                   "f_call", "expression", "exp", "termino", "factor", "cte", 
                   "if", "else", "while", "do", "print_w", "void", "int", 
                   "float", "main", "end" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    INTEGER=13
    FLOAT_NUM=14
    ID=15
    STRING=16
    PLUS=17
    MINUS=18
    MULTIPLY=19
    DIVIDE=20
    EQUALS=21
    NOTEQUALS=22
    GREATERTHAN=23
    LESSTHAN=24
    WS=25
    COMMENT=26
    COMMENT2=27
    LPAREN=28
    RPAREN=29
    LBRACE=30
    RBRACE=31
    LBRACKET=32
    RBRACKET=33
    SEMICOLON=34
    COMMA=35
    COLON=36

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BabyDuckParser.ID, 0)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(BabyDuckParser.SEMICOLON)
            else:
                return self.getToken(BabyDuckParser.SEMICOLON, i)

        def main(self):
            return self.getTypedRuleContext(BabyDuckParser.MainContext,0)


        def end(self):
            return self.getTypedRuleContext(BabyDuckParser.EndContext,0)


        def declarations(self):
            return self.getTypedRuleContext(BabyDuckParser.DeclarationsContext,0)


        def funcs(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BabyDuckParser.FuncsContext)
            else:
                return self.getTypedRuleContext(BabyDuckParser.FuncsContext,i)


        def getRuleIndex(self):
            return BabyDuckParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = BabyDuckParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(BabyDuckParser.T__0)
            self.state = 55
            self.match(BabyDuckParser.ID)
            self.state = 56
            self.match(BabyDuckParser.SEMICOLON)
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 57
                self.declarations()


            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 60
                self.funcs()
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 66
            self.main()
            self.state = 67
            self.end()
            self.state = 68
            self.match(BabyDuckParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vars_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BabyDuckParser.VarsContext)
            else:
                return self.getTypedRuleContext(BabyDuckParser.VarsContext,i)


        def getRuleIndex(self):
            return BabyDuckParser.RULE_declarations

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclarations" ):
                listener.enterDeclarations(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclarations" ):
                listener.exitDeclarations(self)




    def declarations(self):

        localctx = BabyDuckParser.DeclarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declarations)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 70
                self.vars_()
                self.state = 73 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==2):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BabyDuckParser.ID)
            else:
                return self.getToken(BabyDuckParser.ID, i)

        def COLON(self):
            return self.getToken(BabyDuckParser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(BabyDuckParser.TypeContext,0)


        def SEMICOLON(self):
            return self.getToken(BabyDuckParser.SEMICOLON, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BabyDuckParser.COMMA)
            else:
                return self.getToken(BabyDuckParser.COMMA, i)

        def getRuleIndex(self):
            return BabyDuckParser.RULE_vars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVars" ):
                listener.enterVars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVars" ):
                listener.exitVars(self)




    def vars_(self):

        localctx = BabyDuckParser.VarsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_vars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(BabyDuckParser.T__1)
            self.state = 76
            self.match(BabyDuckParser.ID)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==35:
                self.state = 77
                self.match(BabyDuckParser.COMMA)
                self.state = 78
                self.match(BabyDuckParser.ID)
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 84
            self.match(BabyDuckParser.COLON)
            self.state = 85
            self.type_()
            self.state = 86
            self.match(BabyDuckParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def int_(self):
            return self.getTypedRuleContext(BabyDuckParser.IntContext,0)


        def float_(self):
            return self.getTypedRuleContext(BabyDuckParser.FloatContext,0)


        def getRuleIndex(self):
            return BabyDuckParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)




    def type_(self):

        localctx = BabyDuckParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_type)
        try:
            self.state = 90
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                self.int_()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 89
                self.float_()
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


    class FuncsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def void(self):
            return self.getTypedRuleContext(BabyDuckParser.VoidContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BabyDuckParser.ID)
            else:
                return self.getToken(BabyDuckParser.ID, i)

        def LPAREN(self):
            return self.getToken(BabyDuckParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(BabyDuckParser.RPAREN, 0)

        def LBRACKET(self):
            return self.getToken(BabyDuckParser.LBRACKET, 0)

        def body(self):
            return self.getTypedRuleContext(BabyDuckParser.BodyContext,0)


        def RBRACKET(self):
            return self.getToken(BabyDuckParser.RBRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(BabyDuckParser.SEMICOLON, 0)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(BabyDuckParser.COLON)
            else:
                return self.getToken(BabyDuckParser.COLON, i)

        def type_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BabyDuckParser.TypeContext)
            else:
                return self.getTypedRuleContext(BabyDuckParser.TypeContext,i)


        def vars_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BabyDuckParser.VarsContext)
            else:
                return self.getTypedRuleContext(BabyDuckParser.VarsContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BabyDuckParser.COMMA)
            else:
                return self.getToken(BabyDuckParser.COMMA, i)

        def getRuleIndex(self):
            return BabyDuckParser.RULE_funcs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncs" ):
                listener.enterFuncs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncs" ):
                listener.exitFuncs(self)




    def funcs(self):

        localctx = BabyDuckParser.FuncsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_funcs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.void()
            self.state = 93
            self.match(BabyDuckParser.ID)
            self.state = 94
            self.match(BabyDuckParser.LPAREN)
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 95
                self.match(BabyDuckParser.ID)
                self.state = 96
                self.match(BabyDuckParser.COLON)
                self.state = 97
                self.type_()
                self.state = 104
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==35:
                    self.state = 98
                    self.match(BabyDuckParser.COMMA)
                    self.state = 99
                    self.match(BabyDuckParser.ID)
                    self.state = 100
                    self.match(BabyDuckParser.COLON)
                    self.state = 101
                    self.type_()
                    self.state = 106
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 109
            self.match(BabyDuckParser.RPAREN)
            self.state = 110
            self.match(BabyDuckParser.LBRACKET)
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 111
                self.vars_()
                self.state = 116
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 117
            self.body()
            self.state = 118
            self.match(BabyDuckParser.RBRACKET)
            self.state = 119
            self.match(BabyDuckParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(BabyDuckParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(BabyDuckParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BabyDuckParser.StatementContext)
            else:
                return self.getTypedRuleContext(BabyDuckParser.StatementContext,i)


        def getRuleIndex(self):
            return BabyDuckParser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)




    def body(self):

        localctx = BabyDuckParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(BabyDuckParser.LBRACE)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 32936) != 0):
                self.state = 122
                self.statement()
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 128
            self.match(BabyDuckParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self):
            return self.getTypedRuleContext(BabyDuckParser.AssignContext,0)


        def condition(self):
            return self.getTypedRuleContext(BabyDuckParser.ConditionContext,0)


        def cycle(self):
            return self.getTypedRuleContext(BabyDuckParser.CycleContext,0)


        def f_call(self):
            return self.getTypedRuleContext(BabyDuckParser.F_callContext,0)


        def print_(self):
            return self.getTypedRuleContext(BabyDuckParser.PrintContext,0)


        def getRuleIndex(self):
            return BabyDuckParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = BabyDuckParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_statement)
        try:
            self.state = 135
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.assign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self.condition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 132
                self.cycle()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 133
                self.f_call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 134
                self.print_()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BabyDuckParser.ID, 0)

        def EQUALS(self):
            return self.getToken(BabyDuckParser.EQUALS, 0)

        def SEMICOLON(self):
            return self.getToken(BabyDuckParser.SEMICOLON, 0)

        def expression(self):
            return self.getTypedRuleContext(BabyDuckParser.ExpressionContext,0)


        def STRING(self):
            return self.getToken(BabyDuckParser.STRING, 0)

        def getRuleIndex(self):
            return BabyDuckParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)




    def assign(self):

        localctx = BabyDuckParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(BabyDuckParser.ID)
            self.state = 138
            self.match(BabyDuckParser.EQUALS)
            self.state = 141
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17, 18, 28]:
                self.state = 139
                self.expression()
                pass
            elif token in [16]:
                self.state = 140
                self.match(BabyDuckParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 143
            self.match(BabyDuckParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_(self):
            return self.getTypedRuleContext(BabyDuckParser.IfContext,0)


        def LPAREN(self):
            return self.getToken(BabyDuckParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(BabyDuckParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(BabyDuckParser.RPAREN, 0)

        def body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BabyDuckParser.BodyContext)
            else:
                return self.getTypedRuleContext(BabyDuckParser.BodyContext,i)


        def SEMICOLON(self):
            return self.getToken(BabyDuckParser.SEMICOLON, 0)

        def else_(self):
            return self.getTypedRuleContext(BabyDuckParser.ElseContext,0)


        def getRuleIndex(self):
            return BabyDuckParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = BabyDuckParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.if_()
            self.state = 146
            self.match(BabyDuckParser.LPAREN)
            self.state = 147
            self.expression()
            self.state = 148
            self.match(BabyDuckParser.RPAREN)
            self.state = 149
            self.body()
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 150
                self.else_()
                self.state = 151
                self.body()


            self.state = 155
            self.match(BabyDuckParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CycleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def while_(self):
            return self.getTypedRuleContext(BabyDuckParser.WhileContext,0)


        def body(self):
            return self.getTypedRuleContext(BabyDuckParser.BodyContext,0)


        def do(self):
            return self.getTypedRuleContext(BabyDuckParser.DoContext,0)


        def LPAREN(self):
            return self.getToken(BabyDuckParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(BabyDuckParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(BabyDuckParser.RPAREN, 0)

        def SEMICOLON(self):
            return self.getToken(BabyDuckParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return BabyDuckParser.RULE_cycle

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCycle" ):
                listener.enterCycle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCycle" ):
                listener.exitCycle(self)




    def cycle(self):

        localctx = BabyDuckParser.CycleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_cycle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.while_()
            self.state = 158
            self.body()
            self.state = 159
            self.do()
            self.state = 160
            self.match(BabyDuckParser.LPAREN)
            self.state = 161
            self.expression()
            self.state = 162
            self.match(BabyDuckParser.RPAREN)
            self.state = 163
            self.match(BabyDuckParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def print_w(self):
            return self.getTypedRuleContext(BabyDuckParser.Print_wContext,0)


        def LPAREN(self):
            return self.getToken(BabyDuckParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(BabyDuckParser.RPAREN, 0)

        def SEMICOLON(self):
            return self.getToken(BabyDuckParser.SEMICOLON, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BabyDuckParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BabyDuckParser.ExpressionContext,i)


        def STRING(self):
            return self.getToken(BabyDuckParser.STRING, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BabyDuckParser.COMMA)
            else:
                return self.getToken(BabyDuckParser.COMMA, i)

        def getRuleIndex(self):
            return BabyDuckParser.RULE_print

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)




    def print_(self):

        localctx = BabyDuckParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.print_w()
            self.state = 166
            self.match(BabyDuckParser.LPAREN)
            self.state = 172
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 167
                    self.expression()
                    self.state = 168
                    self.match(BabyDuckParser.COMMA) 
                self.state = 174
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

            self.state = 177
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17, 18, 28]:
                self.state = 175
                self.expression()
                pass
            elif token in [16]:
                self.state = 176
                self.match(BabyDuckParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 179
            self.match(BabyDuckParser.RPAREN)
            self.state = 180
            self.match(BabyDuckParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class F_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BabyDuckParser.ID, 0)

        def LPAREN(self):
            return self.getToken(BabyDuckParser.LPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BabyDuckParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BabyDuckParser.ExpressionContext,i)


        def RPAREN(self):
            return self.getToken(BabyDuckParser.RPAREN, 0)

        def SEMICOLON(self):
            return self.getToken(BabyDuckParser.SEMICOLON, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BabyDuckParser.COMMA)
            else:
                return self.getToken(BabyDuckParser.COMMA, i)

        def getRuleIndex(self):
            return BabyDuckParser.RULE_f_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterF_call" ):
                listener.enterF_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitF_call" ):
                listener.exitF_call(self)




    def f_call(self):

        localctx = BabyDuckParser.F_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_f_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(BabyDuckParser.ID)
            self.state = 183
            self.match(BabyDuckParser.LPAREN)
            self.state = 189
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 184
                    self.expression()
                    self.state = 185
                    self.match(BabyDuckParser.COMMA) 
                self.state = 191
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

            self.state = 192
            self.expression()
            self.state = 193
            self.match(BabyDuckParser.RPAREN)
            self.state = 194
            self.match(BabyDuckParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BabyDuckParser.ExpContext)
            else:
                return self.getTypedRuleContext(BabyDuckParser.ExpContext,i)


        def GREATERTHAN(self, i:int=None):
            if i is None:
                return self.getTokens(BabyDuckParser.GREATERTHAN)
            else:
                return self.getToken(BabyDuckParser.GREATERTHAN, i)

        def LESSTHAN(self, i:int=None):
            if i is None:
                return self.getTokens(BabyDuckParser.LESSTHAN)
            else:
                return self.getToken(BabyDuckParser.LESSTHAN, i)

        def NOTEQUALS(self, i:int=None):
            if i is None:
                return self.getTokens(BabyDuckParser.NOTEQUALS)
            else:
                return self.getToken(BabyDuckParser.NOTEQUALS, i)

        def getRuleIndex(self):
            return BabyDuckParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = BabyDuckParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.exp()
            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 29360128) != 0):
                self.state = 197
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 29360128) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 202
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 203
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termino(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BabyDuckParser.TerminoContext)
            else:
                return self.getTypedRuleContext(BabyDuckParser.TerminoContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(BabyDuckParser.PLUS)
            else:
                return self.getToken(BabyDuckParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(BabyDuckParser.MINUS)
            else:
                return self.getToken(BabyDuckParser.MINUS, i)

        def getRuleIndex(self):
            return BabyDuckParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)




    def exp(self):

        localctx = BabyDuckParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.termino()
            self.state = 209
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 206
                    _la = self._input.LA(1)
                    if not(_la==17 or _la==18):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 211
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

            self.state = 212
            self.termino()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TerminoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BabyDuckParser.FactorContext)
            else:
                return self.getTypedRuleContext(BabyDuckParser.FactorContext,i)


        def MULTIPLY(self, i:int=None):
            if i is None:
                return self.getTokens(BabyDuckParser.MULTIPLY)
            else:
                return self.getToken(BabyDuckParser.MULTIPLY, i)

        def DIVIDE(self, i:int=None):
            if i is None:
                return self.getTokens(BabyDuckParser.DIVIDE)
            else:
                return self.getToken(BabyDuckParser.DIVIDE, i)

        def getRuleIndex(self):
            return BabyDuckParser.RULE_termino

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermino" ):
                listener.enterTermino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermino" ):
                listener.exitTermino(self)




    def termino(self):

        localctx = BabyDuckParser.TerminoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_termino)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.factor()
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19 or _la==20:
                self.state = 215
                _la = self._input.LA(1)
                if not(_la==19 or _la==20):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 220
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 221
            self.factor()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(BabyDuckParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(BabyDuckParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(BabyDuckParser.RPAREN, 0)

        def MINUS(self):
            return self.getToken(BabyDuckParser.MINUS, 0)

        def PLUS(self):
            return self.getToken(BabyDuckParser.PLUS, 0)

        def ID(self):
            return self.getToken(BabyDuckParser.ID, 0)

        def cte(self):
            return self.getTypedRuleContext(BabyDuckParser.CteContext,0)


        def getRuleIndex(self):
            return BabyDuckParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = BabyDuckParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.state = 232
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self.match(BabyDuckParser.LPAREN)
                self.state = 224
                self.expression()
                self.state = 225
                self.match(BabyDuckParser.RPAREN)
                pass
            elif token in [17, 18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 227
                _la = self._input.LA(1)
                if not(_la==17 or _la==18):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 230
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [15]:
                    self.state = 228
                    self.match(BabyDuckParser.ID)
                    pass
                elif token in [13, 14]:
                    self.state = 229
                    self.cte()
                    pass
                else:
                    raise NoViableAltException(self)

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


    class CteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(BabyDuckParser.INTEGER, 0)

        def FLOAT_NUM(self):
            return self.getToken(BabyDuckParser.FLOAT_NUM, 0)

        def getRuleIndex(self):
            return BabyDuckParser.RULE_cte

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCte" ):
                listener.enterCte(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCte" ):
                listener.exitCte(self)




    def cte(self):

        localctx = BabyDuckParser.CteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_cte)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            _la = self._input.LA(1)
            if not(_la==13 or _la==14):
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


    class IfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BabyDuckParser.RULE_if

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf" ):
                listener.enterIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf" ):
                listener.exitIf(self)




    def if_(self):

        localctx = BabyDuckParser.IfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_if)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.match(BabyDuckParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BabyDuckParser.RULE_else

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse" ):
                listener.enterElse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse" ):
                listener.exitElse(self)




    def else_(self):

        localctx = BabyDuckParser.ElseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_else)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(BabyDuckParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BabyDuckParser.RULE_while

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile" ):
                listener.enterWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile" ):
                listener.exitWhile(self)




    def while_(self):

        localctx = BabyDuckParser.WhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_while)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.match(BabyDuckParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BabyDuckParser.RULE_do

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDo" ):
                listener.enterDo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDo" ):
                listener.exitDo(self)




    def do(self):

        localctx = BabyDuckParser.DoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_do)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(BabyDuckParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_wContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BabyDuckParser.RULE_print_w

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint_w" ):
                listener.enterPrint_w(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint_w" ):
                listener.exitPrint_w(self)




    def print_w(self):

        localctx = BabyDuckParser.Print_wContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_print_w)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(BabyDuckParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VoidContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BabyDuckParser.RULE_void

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVoid" ):
                listener.enterVoid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVoid" ):
                listener.exitVoid(self)




    def void(self):

        localctx = BabyDuckParser.VoidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_void)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.match(BabyDuckParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BabyDuckParser.RULE_int

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)




    def int_(self):

        localctx = BabyDuckParser.IntContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_int)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(BabyDuckParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FloatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BabyDuckParser.RULE_float

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)




    def float_(self):

        localctx = BabyDuckParser.FloatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_float)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.match(BabyDuckParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BabyDuckParser.RULE_main

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMain" ):
                listener.enterMain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMain" ):
                listener.exitMain(self)




    def main(self):

        localctx = BabyDuckParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_main)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.match(BabyDuckParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EndContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BabyDuckParser.RULE_end

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnd" ):
                listener.enterEnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnd" ):
                listener.exitEnd(self)




    def end(self):

        localctx = BabyDuckParser.EndContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_end)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(BabyDuckParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






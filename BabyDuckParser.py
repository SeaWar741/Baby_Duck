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
        4,1,36,259,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        1,0,1,0,1,0,1,0,4,0,59,8,0,11,0,12,0,60,3,0,63,8,0,1,0,5,0,66,8,
        0,10,0,12,0,69,9,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,5,1,79,8,1,10,
        1,12,1,82,9,1,1,1,1,1,1,2,1,2,1,2,5,2,89,8,2,10,2,12,2,92,9,2,1,
        2,1,2,1,2,1,3,1,3,3,3,99,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,5,4,111,8,4,10,4,12,4,114,9,4,3,4,116,8,4,1,4,1,4,1,4,4,4,121,
        8,4,11,4,12,4,122,3,4,125,8,4,1,4,1,4,1,4,1,4,1,5,1,5,5,5,133,8,
        5,10,5,12,5,136,9,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,3,6,145,8,6,1,7,
        1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,160,8,8,1,8,
        1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,5,10,
        177,8,10,10,10,12,10,180,9,10,1,10,1,10,3,10,184,8,10,1,10,1,10,
        1,10,1,11,1,11,1,11,1,11,1,11,5,11,194,8,11,10,11,12,11,197,9,11,
        1,11,1,11,1,11,1,11,1,12,1,12,1,12,3,12,206,8,12,1,13,1,13,5,13,
        210,8,13,10,13,12,13,213,9,13,1,13,1,13,1,14,1,14,5,14,219,8,14,
        10,14,12,14,222,9,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        3,15,233,8,15,3,15,235,8,15,1,16,1,16,1,17,1,17,1,18,1,18,1,19,1,
        19,1,20,1,20,1,21,1,21,1,22,1,22,1,23,1,23,1,24,1,24,1,25,1,25,1,
        26,1,26,1,26,0,0,27,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,
        34,36,38,40,42,44,46,48,50,52,0,4,1,0,22,24,1,0,17,18,1,0,19,20,
        1,0,13,14,255,0,54,1,0,0,0,2,74,1,0,0,0,4,85,1,0,0,0,6,98,1,0,0,
        0,8,100,1,0,0,0,10,130,1,0,0,0,12,144,1,0,0,0,14,146,1,0,0,0,16,
        151,1,0,0,0,18,163,1,0,0,0,20,171,1,0,0,0,22,188,1,0,0,0,24,202,
        1,0,0,0,26,207,1,0,0,0,28,216,1,0,0,0,30,234,1,0,0,0,32,236,1,0,
        0,0,34,238,1,0,0,0,36,240,1,0,0,0,38,242,1,0,0,0,40,244,1,0,0,0,
        42,246,1,0,0,0,44,248,1,0,0,0,46,250,1,0,0,0,48,252,1,0,0,0,50,254,
        1,0,0,0,52,256,1,0,0,0,54,55,5,1,0,0,55,56,5,15,0,0,56,62,5,34,0,
        0,57,59,3,2,1,0,58,57,1,0,0,0,59,60,1,0,0,0,60,58,1,0,0,0,60,61,
        1,0,0,0,61,63,1,0,0,0,62,58,1,0,0,0,62,63,1,0,0,0,63,67,1,0,0,0,
        64,66,3,8,4,0,65,64,1,0,0,0,66,69,1,0,0,0,67,65,1,0,0,0,67,68,1,
        0,0,0,68,70,1,0,0,0,69,67,1,0,0,0,70,71,3,50,25,0,71,72,3,10,5,0,
        72,73,3,52,26,0,73,1,1,0,0,0,74,75,5,2,0,0,75,80,3,4,2,0,76,77,5,
        34,0,0,77,79,3,4,2,0,78,76,1,0,0,0,79,82,1,0,0,0,80,78,1,0,0,0,80,
        81,1,0,0,0,81,83,1,0,0,0,82,80,1,0,0,0,83,84,5,34,0,0,84,3,1,0,0,
        0,85,90,5,15,0,0,86,87,5,35,0,0,87,89,5,15,0,0,88,86,1,0,0,0,89,
        92,1,0,0,0,90,88,1,0,0,0,90,91,1,0,0,0,91,93,1,0,0,0,92,90,1,0,0,
        0,93,94,5,36,0,0,94,95,3,6,3,0,95,5,1,0,0,0,96,99,3,46,23,0,97,99,
        3,48,24,0,98,96,1,0,0,0,98,97,1,0,0,0,99,7,1,0,0,0,100,101,3,44,
        22,0,101,102,5,15,0,0,102,115,5,28,0,0,103,104,5,15,0,0,104,105,
        5,36,0,0,105,112,3,6,3,0,106,107,5,35,0,0,107,108,5,15,0,0,108,109,
        5,36,0,0,109,111,3,6,3,0,110,106,1,0,0,0,111,114,1,0,0,0,112,110,
        1,0,0,0,112,113,1,0,0,0,113,116,1,0,0,0,114,112,1,0,0,0,115,103,
        1,0,0,0,115,116,1,0,0,0,116,117,1,0,0,0,117,118,5,29,0,0,118,124,
        5,32,0,0,119,121,3,2,1,0,120,119,1,0,0,0,121,122,1,0,0,0,122,120,
        1,0,0,0,122,123,1,0,0,0,123,125,1,0,0,0,124,120,1,0,0,0,124,125,
        1,0,0,0,125,126,1,0,0,0,126,127,3,10,5,0,127,128,5,33,0,0,128,129,
        5,34,0,0,129,9,1,0,0,0,130,134,5,30,0,0,131,133,3,12,6,0,132,131,
        1,0,0,0,133,136,1,0,0,0,134,132,1,0,0,0,134,135,1,0,0,0,135,137,
        1,0,0,0,136,134,1,0,0,0,137,138,5,31,0,0,138,11,1,0,0,0,139,145,
        3,14,7,0,140,145,3,16,8,0,141,145,3,18,9,0,142,145,3,22,11,0,143,
        145,3,20,10,0,144,139,1,0,0,0,144,140,1,0,0,0,144,141,1,0,0,0,144,
        142,1,0,0,0,144,143,1,0,0,0,145,13,1,0,0,0,146,147,5,15,0,0,147,
        148,5,21,0,0,148,149,3,24,12,0,149,150,5,34,0,0,150,15,1,0,0,0,151,
        152,3,34,17,0,152,153,5,28,0,0,153,154,3,24,12,0,154,155,5,29,0,
        0,155,159,3,10,5,0,156,157,3,36,18,0,157,158,3,10,5,0,158,160,1,
        0,0,0,159,156,1,0,0,0,159,160,1,0,0,0,160,161,1,0,0,0,161,162,5,
        34,0,0,162,17,1,0,0,0,163,164,3,38,19,0,164,165,3,10,5,0,165,166,
        3,40,20,0,166,167,5,28,0,0,167,168,3,24,12,0,168,169,5,29,0,0,169,
        170,5,34,0,0,170,19,1,0,0,0,171,172,3,42,21,0,172,178,5,28,0,0,173,
        174,3,24,12,0,174,175,5,35,0,0,175,177,1,0,0,0,176,173,1,0,0,0,177,
        180,1,0,0,0,178,176,1,0,0,0,178,179,1,0,0,0,179,183,1,0,0,0,180,
        178,1,0,0,0,181,184,3,24,12,0,182,184,5,16,0,0,183,181,1,0,0,0,183,
        182,1,0,0,0,184,185,1,0,0,0,185,186,5,29,0,0,186,187,5,34,0,0,187,
        21,1,0,0,0,188,189,5,15,0,0,189,195,5,28,0,0,190,191,3,24,12,0,191,
        192,5,35,0,0,192,194,1,0,0,0,193,190,1,0,0,0,194,197,1,0,0,0,195,
        193,1,0,0,0,195,196,1,0,0,0,196,198,1,0,0,0,197,195,1,0,0,0,198,
        199,3,24,12,0,199,200,5,29,0,0,200,201,5,34,0,0,201,23,1,0,0,0,202,
        205,3,26,13,0,203,204,7,0,0,0,204,206,3,26,13,0,205,203,1,0,0,0,
        205,206,1,0,0,0,206,25,1,0,0,0,207,211,3,28,14,0,208,210,7,1,0,0,
        209,208,1,0,0,0,210,213,1,0,0,0,211,209,1,0,0,0,211,212,1,0,0,0,
        212,214,1,0,0,0,213,211,1,0,0,0,214,215,3,28,14,0,215,27,1,0,0,0,
        216,220,3,30,15,0,217,219,7,2,0,0,218,217,1,0,0,0,219,222,1,0,0,
        0,220,218,1,0,0,0,220,221,1,0,0,0,221,223,1,0,0,0,222,220,1,0,0,
        0,223,224,3,30,15,0,224,29,1,0,0,0,225,226,5,28,0,0,226,227,3,24,
        12,0,227,228,5,29,0,0,228,235,1,0,0,0,229,232,7,1,0,0,230,233,5,
        15,0,0,231,233,3,32,16,0,232,230,1,0,0,0,232,231,1,0,0,0,233,235,
        1,0,0,0,234,225,1,0,0,0,234,229,1,0,0,0,235,31,1,0,0,0,236,237,7,
        3,0,0,237,33,1,0,0,0,238,239,5,3,0,0,239,35,1,0,0,0,240,241,5,4,
        0,0,241,37,1,0,0,0,242,243,5,5,0,0,243,39,1,0,0,0,244,245,5,6,0,
        0,245,41,1,0,0,0,246,247,5,7,0,0,247,43,1,0,0,0,248,249,5,8,0,0,
        249,45,1,0,0,0,250,251,5,9,0,0,251,47,1,0,0,0,252,253,5,10,0,0,253,
        49,1,0,0,0,254,255,5,11,0,0,255,51,1,0,0,0,256,257,5,12,0,0,257,
        53,1,0,0,0,21,60,62,67,80,90,98,112,115,122,124,134,144,159,178,
        183,195,205,211,220,232,234
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
    RULE_vars = 1
    RULE_varGroup = 2
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

    ruleNames =  [ "program", "vars", "varGroup", "type", "funcs", "body", 
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

        def SEMICOLON(self):
            return self.getToken(BabyDuckParser.SEMICOLON, 0)

        def main(self):
            return self.getTypedRuleContext(BabyDuckParser.MainContext,0)


        def body(self):
            return self.getTypedRuleContext(BabyDuckParser.BodyContext,0)


        def end(self):
            return self.getTypedRuleContext(BabyDuckParser.EndContext,0)


        def funcs(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BabyDuckParser.FuncsContext)
            else:
                return self.getTypedRuleContext(BabyDuckParser.FuncsContext,i)


        def vars_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BabyDuckParser.VarsContext)
            else:
                return self.getTypedRuleContext(BabyDuckParser.VarsContext,i)


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
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 58 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 57
                    self.vars_()
                    self.state = 60 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==2):
                        break



            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 64
                self.funcs()
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 70
            self.main()
            self.state = 71
            self.body()
            self.state = 72
            self.end()
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

        def varGroup(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BabyDuckParser.VarGroupContext)
            else:
                return self.getTypedRuleContext(BabyDuckParser.VarGroupContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(BabyDuckParser.SEMICOLON)
            else:
                return self.getToken(BabyDuckParser.SEMICOLON, i)

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
        self.enterRule(localctx, 2, self.RULE_vars)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(BabyDuckParser.T__1)
            self.state = 75
            self.varGroup()
            self.state = 80
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 76
                    self.match(BabyDuckParser.SEMICOLON)
                    self.state = 77
                    self.varGroup() 
                self.state = 82
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 83
            self.match(BabyDuckParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarGroupContext(ParserRuleContext):
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


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BabyDuckParser.COMMA)
            else:
                return self.getToken(BabyDuckParser.COMMA, i)

        def getRuleIndex(self):
            return BabyDuckParser.RULE_varGroup

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarGroup" ):
                listener.enterVarGroup(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarGroup" ):
                listener.exitVarGroup(self)




    def varGroup(self):

        localctx = BabyDuckParser.VarGroupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_varGroup)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(BabyDuckParser.ID)
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==35:
                self.state = 86
                self.match(BabyDuckParser.COMMA)
                self.state = 87
                self.match(BabyDuckParser.ID)
                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 93
            self.match(BabyDuckParser.COLON)
            self.state = 94
            self.type_()
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
            self.state = 98
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 96
                self.int_()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 97
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


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BabyDuckParser.COMMA)
            else:
                return self.getToken(BabyDuckParser.COMMA, i)

        def vars_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BabyDuckParser.VarsContext)
            else:
                return self.getTypedRuleContext(BabyDuckParser.VarsContext,i)


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
            self.state = 100
            self.void()
            self.state = 101
            self.match(BabyDuckParser.ID)
            self.state = 102
            self.match(BabyDuckParser.LPAREN)
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 103
                self.match(BabyDuckParser.ID)
                self.state = 104
                self.match(BabyDuckParser.COLON)
                self.state = 105
                self.type_()
                self.state = 112
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==35:
                    self.state = 106
                    self.match(BabyDuckParser.COMMA)
                    self.state = 107
                    self.match(BabyDuckParser.ID)
                    self.state = 108
                    self.match(BabyDuckParser.COLON)
                    self.state = 109
                    self.type_()
                    self.state = 114
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 117
            self.match(BabyDuckParser.RPAREN)
            self.state = 118
            self.match(BabyDuckParser.LBRACKET)
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 120 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 119
                    self.vars_()
                    self.state = 122 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==2):
                        break



            self.state = 126
            self.body()
            self.state = 127
            self.match(BabyDuckParser.RBRACKET)
            self.state = 128
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
            self.state = 130
            self.match(BabyDuckParser.LBRACE)
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 32936) != 0):
                self.state = 131
                self.statement()
                self.state = 136
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 137
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
            self.state = 144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.assign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.condition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 141
                self.cycle()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 142
                self.f_call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 143
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
            self.state = 146
            self.match(BabyDuckParser.ID)
            self.state = 147
            self.match(BabyDuckParser.EQUALS)

            self.state = 148
            self.expression()
            self.state = 149
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
            self.state = 151
            self.if_()
            self.state = 152
            self.match(BabyDuckParser.LPAREN)
            self.state = 153
            self.expression()
            self.state = 154
            self.match(BabyDuckParser.RPAREN)
            self.state = 155
            self.body()
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 156
                self.else_()
                self.state = 157
                self.body()


            self.state = 161
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
            self.state = 163
            self.while_()
            self.state = 164
            self.body()
            self.state = 165
            self.do()
            self.state = 166
            self.match(BabyDuckParser.LPAREN)
            self.state = 167
            self.expression()
            self.state = 168
            self.match(BabyDuckParser.RPAREN)
            self.state = 169
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
            self.state = 171
            self.print_w()
            self.state = 172
            self.match(BabyDuckParser.LPAREN)
            self.state = 178
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 173
                    self.expression()
                    self.state = 174
                    self.match(BabyDuckParser.COMMA) 
                self.state = 180
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

            self.state = 183
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17, 18, 28]:
                self.state = 181
                self.expression()
                pass
            elif token in [16]:
                self.state = 182
                self.match(BabyDuckParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 185
            self.match(BabyDuckParser.RPAREN)
            self.state = 186
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
            self.state = 188
            self.match(BabyDuckParser.ID)
            self.state = 189
            self.match(BabyDuckParser.LPAREN)
            self.state = 195
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 190
                    self.expression()
                    self.state = 191
                    self.match(BabyDuckParser.COMMA) 
                self.state = 197
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

            self.state = 198
            self.expression()
            self.state = 199
            self.match(BabyDuckParser.RPAREN)
            self.state = 200
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


        def GREATERTHAN(self):
            return self.getToken(BabyDuckParser.GREATERTHAN, 0)

        def LESSTHAN(self):
            return self.getToken(BabyDuckParser.LESSTHAN, 0)

        def NOTEQUALS(self):
            return self.getToken(BabyDuckParser.NOTEQUALS, 0)

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
            self.state = 202
            self.exp()
            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 29360128) != 0):
                self.state = 203
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 29360128) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 204
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
            self.state = 207
            self.termino()
            self.state = 211
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 208
                    _la = self._input.LA(1)
                    if not(_la==17 or _la==18):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 213
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

            self.state = 214
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
            self.state = 216
            self.factor()
            self.state = 220
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19 or _la==20:
                self.state = 217
                _la = self._input.LA(1)
                if not(_la==19 or _la==20):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 222
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 223
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
            self.state = 234
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.match(BabyDuckParser.LPAREN)
                self.state = 226
                self.expression()
                self.state = 227
                self.match(BabyDuckParser.RPAREN)
                pass
            elif token in [17, 18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 229
                _la = self._input.LA(1)
                if not(_la==17 or _la==18):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 232
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [15]:
                    self.state = 230
                    self.match(BabyDuckParser.ID)
                    pass
                elif token in [13, 14]:
                    self.state = 231
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
            self.state = 236
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
            self.state = 238
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
            self.state = 240
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
            self.state = 242
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
            self.state = 244
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
            self.state = 246
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
            self.state = 248
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
            self.state = 250
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
            self.state = 252
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
            self.state = 254
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
            self.state = 256
            self.match(BabyDuckParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






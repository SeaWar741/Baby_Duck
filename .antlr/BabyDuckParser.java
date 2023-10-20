// Generated from c:/Users/juanc/Desktop/Baby_Duck/BabyDuck.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class BabyDuckParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, INTEGER=13, FLOAT_NUM=14, ID=15, STRING=16, 
		PLUS=17, MINUS=18, MULTIPLY=19, DIVIDE=20, EQUALS=21, NOTEQUALS=22, GREATERTHAN=23, 
		LESSTHAN=24, WS=25, COMMENT=26, COMMENT2=27, LPAREN=28, RPAREN=29, LBRACE=30, 
		RBRACE=31, LBRACKET=32, RBRACKET=33, SEMICOLON=34, COMMA=35, COLON=36;
	public static final int
		RULE_program = 0, RULE_declarations = 1, RULE_vars = 2, RULE_type = 3, 
		RULE_funcs = 4, RULE_body = 5, RULE_statement = 6, RULE_assign = 7, RULE_condition = 8, 
		RULE_cycle = 9, RULE_print = 10, RULE_f_call = 11, RULE_expression = 12, 
		RULE_exp = 13, RULE_termino = 14, RULE_factor = 15, RULE_cte = 16, RULE_if = 17, 
		RULE_else = 18, RULE_while = 19, RULE_do = 20, RULE_print_w = 21, RULE_void = 22, 
		RULE_int = 23, RULE_float = 24, RULE_main = 25, RULE_end = 26;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "declarations", "vars", "type", "funcs", "body", "statement", 
			"assign", "condition", "cycle", "print", "f_call", "expression", "exp", 
			"termino", "factor", "cte", "if", "else", "while", "do", "print_w", "void", 
			"int", "float", "main", "end"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'program'", "'var'", "'if'", "'else'", "'while'", "'do'", "'print'", 
			"'void'", "'int'", "'float'", "'main'", "'end'", null, null, null, null, 
			"'+'", "'-'", "'*'", "'/'", "'='", "'!='", "'>'", "'<'", null, null, 
			null, "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", "','", "':'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, "INTEGER", "FLOAT_NUM", "ID", "STRING", "PLUS", "MINUS", "MULTIPLY", 
			"DIVIDE", "EQUALS", "NOTEQUALS", "GREATERTHAN", "LESSTHAN", "WS", "COMMENT", 
			"COMMENT2", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACKET", "RBRACKET", 
			"SEMICOLON", "COMMA", "COLON"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "BabyDuck.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public BabyDuckParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(BabyDuckParser.ID, 0); }
		public List<TerminalNode> SEMICOLON() { return getTokens(BabyDuckParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(BabyDuckParser.SEMICOLON, i);
		}
		public MainContext main() {
			return getRuleContext(MainContext.class,0);
		}
		public EndContext end() {
			return getRuleContext(EndContext.class,0);
		}
		public DeclarationsContext declarations() {
			return getRuleContext(DeclarationsContext.class,0);
		}
		public List<FuncsContext> funcs() {
			return getRuleContexts(FuncsContext.class);
		}
		public FuncsContext funcs(int i) {
			return getRuleContext(FuncsContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(54);
			match(T__0);
			setState(55);
			match(ID);
			setState(56);
			match(SEMICOLON);
			setState(58);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__1) {
				{
				setState(57);
				declarations();
				}
			}

			setState(63);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__7) {
				{
				{
				setState(60);
				funcs();
				}
				}
				setState(65);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(66);
			main();
			setState(67);
			end();
			setState(68);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclarationsContext extends ParserRuleContext {
		public List<VarsContext> vars() {
			return getRuleContexts(VarsContext.class);
		}
		public VarsContext vars(int i) {
			return getRuleContext(VarsContext.class,i);
		}
		public DeclarationsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declarations; }
	}

	public final DeclarationsContext declarations() throws RecognitionException {
		DeclarationsContext _localctx = new DeclarationsContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_declarations);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(71); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(70);
				vars();
				}
				}
				setState(73); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==T__1 );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VarsContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(BabyDuckParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(BabyDuckParser.ID, i);
		}
		public TerminalNode COLON() { return getToken(BabyDuckParser.COLON, 0); }
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(BabyDuckParser.SEMICOLON, 0); }
		public List<TerminalNode> COMMA() { return getTokens(BabyDuckParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(BabyDuckParser.COMMA, i);
		}
		public VarsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vars; }
	}

	public final VarsContext vars() throws RecognitionException {
		VarsContext _localctx = new VarsContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_vars);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(75);
			match(T__1);
			setState(76);
			match(ID);
			setState(81);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(77);
				match(COMMA);
				setState(78);
				match(ID);
				}
				}
				setState(83);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(84);
			match(COLON);
			setState(85);
			type();
			setState(86);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypeContext extends ParserRuleContext {
		public IntContext int_() {
			return getRuleContext(IntContext.class,0);
		}
		public FloatContext float_() {
			return getRuleContext(FloatContext.class,0);
		}
		public TypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type; }
	}

	public final TypeContext type() throws RecognitionException {
		TypeContext _localctx = new TypeContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_type);
		try {
			setState(90);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__8:
				enterOuterAlt(_localctx, 1);
				{
				setState(88);
				int_();
				}
				break;
			case T__9:
				enterOuterAlt(_localctx, 2);
				{
				setState(89);
				float_();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FuncsContext extends ParserRuleContext {
		public VoidContext void_() {
			return getRuleContext(VoidContext.class,0);
		}
		public List<TerminalNode> ID() { return getTokens(BabyDuckParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(BabyDuckParser.ID, i);
		}
		public TerminalNode LPAREN() { return getToken(BabyDuckParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(BabyDuckParser.RPAREN, 0); }
		public TerminalNode LBRACKET() { return getToken(BabyDuckParser.LBRACKET, 0); }
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public TerminalNode RBRACKET() { return getToken(BabyDuckParser.RBRACKET, 0); }
		public TerminalNode SEMICOLON() { return getToken(BabyDuckParser.SEMICOLON, 0); }
		public List<TerminalNode> COLON() { return getTokens(BabyDuckParser.COLON); }
		public TerminalNode COLON(int i) {
			return getToken(BabyDuckParser.COLON, i);
		}
		public List<TypeContext> type() {
			return getRuleContexts(TypeContext.class);
		}
		public TypeContext type(int i) {
			return getRuleContext(TypeContext.class,i);
		}
		public List<VarsContext> vars() {
			return getRuleContexts(VarsContext.class);
		}
		public VarsContext vars(int i) {
			return getRuleContext(VarsContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(BabyDuckParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(BabyDuckParser.COMMA, i);
		}
		public FuncsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcs; }
	}

	public final FuncsContext funcs() throws RecognitionException {
		FuncsContext _localctx = new FuncsContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_funcs);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(92);
			void_();
			setState(93);
			match(ID);
			setState(94);
			match(LPAREN);
			setState(107);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(95);
				match(ID);
				setState(96);
				match(COLON);
				setState(97);
				type();
				setState(104);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(98);
					match(COMMA);
					setState(99);
					match(ID);
					setState(100);
					match(COLON);
					setState(101);
					type();
					}
					}
					setState(106);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(109);
			match(RPAREN);
			setState(110);
			match(LBRACKET);
			setState(114);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__1) {
				{
				{
				setState(111);
				vars();
				}
				}
				setState(116);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(117);
			body();
			setState(118);
			match(RBRACKET);
			setState(119);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BodyContext extends ParserRuleContext {
		public TerminalNode LBRACE() { return getToken(BabyDuckParser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(BabyDuckParser.RBRACE, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public BodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_body; }
	}

	public final BodyContext body() throws RecognitionException {
		BodyContext _localctx = new BodyContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_body);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(121);
			match(LBRACE);
			setState(125);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 32936L) != 0)) {
				{
				{
				setState(122);
				statement();
				}
				}
				setState(127);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(128);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public AssignContext assign() {
			return getRuleContext(AssignContext.class,0);
		}
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public CycleContext cycle() {
			return getRuleContext(CycleContext.class,0);
		}
		public F_callContext f_call() {
			return getRuleContext(F_callContext.class,0);
		}
		public PrintContext print() {
			return getRuleContext(PrintContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_statement);
		try {
			setState(135);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(130);
				assign();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(131);
				condition();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(132);
				cycle();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(133);
				f_call();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(134);
				print();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(BabyDuckParser.ID, 0); }
		public TerminalNode EQUALS() { return getToken(BabyDuckParser.EQUALS, 0); }
		public TerminalNode SEMICOLON() { return getToken(BabyDuckParser.SEMICOLON, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode STRING() { return getToken(BabyDuckParser.STRING, 0); }
		public AssignContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign; }
	}

	public final AssignContext assign() throws RecognitionException {
		AssignContext _localctx = new AssignContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_assign);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(137);
			match(ID);
			setState(138);
			match(EQUALS);
			setState(141);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PLUS:
			case MINUS:
			case LPAREN:
				{
				setState(139);
				expression();
				}
				break;
			case STRING:
				{
				setState(140);
				match(STRING);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(143);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConditionContext extends ParserRuleContext {
		public IfContext if_() {
			return getRuleContext(IfContext.class,0);
		}
		public TerminalNode LPAREN() { return getToken(BabyDuckParser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(BabyDuckParser.RPAREN, 0); }
		public List<BodyContext> body() {
			return getRuleContexts(BodyContext.class);
		}
		public BodyContext body(int i) {
			return getRuleContext(BodyContext.class,i);
		}
		public TerminalNode SEMICOLON() { return getToken(BabyDuckParser.SEMICOLON, 0); }
		public ElseContext else_() {
			return getRuleContext(ElseContext.class,0);
		}
		public ConditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condition; }
	}

	public final ConditionContext condition() throws RecognitionException {
		ConditionContext _localctx = new ConditionContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_condition);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(145);
			if_();
			setState(146);
			match(LPAREN);
			setState(147);
			expression();
			setState(148);
			match(RPAREN);
			setState(149);
			body();
			setState(153);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__3) {
				{
				setState(150);
				else_();
				setState(151);
				body();
				}
			}

			setState(155);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CycleContext extends ParserRuleContext {
		public WhileContext while_() {
			return getRuleContext(WhileContext.class,0);
		}
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public DoContext do_() {
			return getRuleContext(DoContext.class,0);
		}
		public TerminalNode LPAREN() { return getToken(BabyDuckParser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(BabyDuckParser.RPAREN, 0); }
		public TerminalNode SEMICOLON() { return getToken(BabyDuckParser.SEMICOLON, 0); }
		public CycleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cycle; }
	}

	public final CycleContext cycle() throws RecognitionException {
		CycleContext _localctx = new CycleContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_cycle);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(157);
			while_();
			setState(158);
			body();
			setState(159);
			do_();
			setState(160);
			match(LPAREN);
			setState(161);
			expression();
			setState(162);
			match(RPAREN);
			setState(163);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrintContext extends ParserRuleContext {
		public Print_wContext print_w() {
			return getRuleContext(Print_wContext.class,0);
		}
		public TerminalNode LPAREN() { return getToken(BabyDuckParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(BabyDuckParser.RPAREN, 0); }
		public TerminalNode SEMICOLON() { return getToken(BabyDuckParser.SEMICOLON, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode STRING() { return getToken(BabyDuckParser.STRING, 0); }
		public List<TerminalNode> COMMA() { return getTokens(BabyDuckParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(BabyDuckParser.COMMA, i);
		}
		public PrintContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_print; }
	}

	public final PrintContext print() throws RecognitionException {
		PrintContext _localctx = new PrintContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_print);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(165);
			print_w();
			setState(166);
			match(LPAREN);
			setState(172);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(167);
					expression();
					setState(168);
					match(COMMA);
					}
					} 
				}
				setState(174);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			}
			setState(177);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PLUS:
			case MINUS:
			case LPAREN:
				{
				setState(175);
				expression();
				}
				break;
			case STRING:
				{
				setState(176);
				match(STRING);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(179);
			match(RPAREN);
			setState(180);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class F_callContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(BabyDuckParser.ID, 0); }
		public TerminalNode LPAREN() { return getToken(BabyDuckParser.LPAREN, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode RPAREN() { return getToken(BabyDuckParser.RPAREN, 0); }
		public TerminalNode SEMICOLON() { return getToken(BabyDuckParser.SEMICOLON, 0); }
		public List<TerminalNode> COMMA() { return getTokens(BabyDuckParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(BabyDuckParser.COMMA, i);
		}
		public F_callContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_f_call; }
	}

	public final F_callContext f_call() throws RecognitionException {
		F_callContext _localctx = new F_callContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_f_call);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(182);
			match(ID);
			setState(183);
			match(LPAREN);
			setState(189);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,14,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(184);
					expression();
					setState(185);
					match(COMMA);
					}
					} 
				}
				setState(191);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,14,_ctx);
			}
			setState(192);
			expression();
			setState(193);
			match(RPAREN);
			setState(194);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpressionContext extends ParserRuleContext {
		public List<ExpContext> exp() {
			return getRuleContexts(ExpContext.class);
		}
		public ExpContext exp(int i) {
			return getRuleContext(ExpContext.class,i);
		}
		public List<TerminalNode> GREATERTHAN() { return getTokens(BabyDuckParser.GREATERTHAN); }
		public TerminalNode GREATERTHAN(int i) {
			return getToken(BabyDuckParser.GREATERTHAN, i);
		}
		public List<TerminalNode> LESSTHAN() { return getTokens(BabyDuckParser.LESSTHAN); }
		public TerminalNode LESSTHAN(int i) {
			return getToken(BabyDuckParser.LESSTHAN, i);
		}
		public List<TerminalNode> NOTEQUALS() { return getTokens(BabyDuckParser.NOTEQUALS); }
		public TerminalNode NOTEQUALS(int i) {
			return getToken(BabyDuckParser.NOTEQUALS, i);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_expression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(196);
			exp();
			setState(200);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 29360128L) != 0)) {
				{
				{
				setState(197);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 29360128L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				}
				setState(202);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(203);
			exp();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpContext extends ParserRuleContext {
		public List<TerminoContext> termino() {
			return getRuleContexts(TerminoContext.class);
		}
		public TerminoContext termino(int i) {
			return getRuleContext(TerminoContext.class,i);
		}
		public List<TerminalNode> PLUS() { return getTokens(BabyDuckParser.PLUS); }
		public TerminalNode PLUS(int i) {
			return getToken(BabyDuckParser.PLUS, i);
		}
		public List<TerminalNode> MINUS() { return getTokens(BabyDuckParser.MINUS); }
		public TerminalNode MINUS(int i) {
			return getToken(BabyDuckParser.MINUS, i);
		}
		public ExpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp; }
	}

	public final ExpContext exp() throws RecognitionException {
		ExpContext _localctx = new ExpContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_exp);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(205);
			termino();
			setState(209);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,16,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(206);
					_la = _input.LA(1);
					if ( !(_la==PLUS || _la==MINUS) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					}
					} 
				}
				setState(211);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,16,_ctx);
			}
			setState(212);
			termino();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TerminoContext extends ParserRuleContext {
		public List<FactorContext> factor() {
			return getRuleContexts(FactorContext.class);
		}
		public FactorContext factor(int i) {
			return getRuleContext(FactorContext.class,i);
		}
		public List<TerminalNode> MULTIPLY() { return getTokens(BabyDuckParser.MULTIPLY); }
		public TerminalNode MULTIPLY(int i) {
			return getToken(BabyDuckParser.MULTIPLY, i);
		}
		public List<TerminalNode> DIVIDE() { return getTokens(BabyDuckParser.DIVIDE); }
		public TerminalNode DIVIDE(int i) {
			return getToken(BabyDuckParser.DIVIDE, i);
		}
		public TerminoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_termino; }
	}

	public final TerminoContext termino() throws RecognitionException {
		TerminoContext _localctx = new TerminoContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_termino);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(214);
			factor();
			setState(218);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==MULTIPLY || _la==DIVIDE) {
				{
				{
				setState(215);
				_la = _input.LA(1);
				if ( !(_la==MULTIPLY || _la==DIVIDE) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				}
				setState(220);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(221);
			factor();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FactorContext extends ParserRuleContext {
		public TerminalNode LPAREN() { return getToken(BabyDuckParser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(BabyDuckParser.RPAREN, 0); }
		public TerminalNode MINUS() { return getToken(BabyDuckParser.MINUS, 0); }
		public TerminalNode PLUS() { return getToken(BabyDuckParser.PLUS, 0); }
		public TerminalNode ID() { return getToken(BabyDuckParser.ID, 0); }
		public CteContext cte() {
			return getRuleContext(CteContext.class,0);
		}
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_factor);
		int _la;
		try {
			setState(232);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LPAREN:
				enterOuterAlt(_localctx, 1);
				{
				{
				setState(223);
				match(LPAREN);
				setState(224);
				expression();
				setState(225);
				match(RPAREN);
				}
				}
				break;
			case PLUS:
			case MINUS:
				enterOuterAlt(_localctx, 2);
				{
				setState(227);
				_la = _input.LA(1);
				if ( !(_la==PLUS || _la==MINUS) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(230);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case ID:
					{
					setState(228);
					match(ID);
					}
					break;
				case INTEGER:
				case FLOAT_NUM:
					{
					setState(229);
					cte();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CteContext extends ParserRuleContext {
		public TerminalNode INTEGER() { return getToken(BabyDuckParser.INTEGER, 0); }
		public TerminalNode FLOAT_NUM() { return getToken(BabyDuckParser.FLOAT_NUM, 0); }
		public CteContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cte; }
	}

	public final CteContext cte() throws RecognitionException {
		CteContext _localctx = new CteContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_cte);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(234);
			_la = _input.LA(1);
			if ( !(_la==INTEGER || _la==FLOAT_NUM) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IfContext extends ParserRuleContext {
		public IfContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if; }
	}

	public final IfContext if_() throws RecognitionException {
		IfContext _localctx = new IfContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_if);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(236);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ElseContext extends ParserRuleContext {
		public ElseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_else; }
	}

	public final ElseContext else_() throws RecognitionException {
		ElseContext _localctx = new ElseContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_else);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(238);
			match(T__3);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WhileContext extends ParserRuleContext {
		public WhileContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_while; }
	}

	public final WhileContext while_() throws RecognitionException {
		WhileContext _localctx = new WhileContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_while);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(240);
			match(T__4);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DoContext extends ParserRuleContext {
		public DoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_do; }
	}

	public final DoContext do_() throws RecognitionException {
		DoContext _localctx = new DoContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_do);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(242);
			match(T__5);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Print_wContext extends ParserRuleContext {
		public Print_wContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_print_w; }
	}

	public final Print_wContext print_w() throws RecognitionException {
		Print_wContext _localctx = new Print_wContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_print_w);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(244);
			match(T__6);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VoidContext extends ParserRuleContext {
		public VoidContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_void; }
	}

	public final VoidContext void_() throws RecognitionException {
		VoidContext _localctx = new VoidContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_void);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(246);
			match(T__7);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IntContext extends ParserRuleContext {
		public IntContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_int; }
	}

	public final IntContext int_() throws RecognitionException {
		IntContext _localctx = new IntContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_int);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(248);
			match(T__8);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FloatContext extends ParserRuleContext {
		public FloatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_float; }
	}

	public final FloatContext float_() throws RecognitionException {
		FloatContext _localctx = new FloatContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_float);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(250);
			match(T__9);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MainContext extends ParserRuleContext {
		public MainContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_main; }
	}

	public final MainContext main() throws RecognitionException {
		MainContext _localctx = new MainContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_main);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(252);
			match(T__10);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EndContext extends ParserRuleContext {
		public EndContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_end; }
	}

	public final EndContext end() throws RecognitionException {
		EndContext _localctx = new EndContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_end);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(254);
			match(T__11);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001$\u0101\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0003\u0000;\b\u0000\u0001\u0000\u0005\u0000"+
		">\b\u0000\n\u0000\f\u0000A\t\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0001\u0004\u0001H\b\u0001\u000b\u0001\f\u0001I\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0005\u0002P\b\u0002\n\u0002"+
		"\f\u0002S\t\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0003\u0001\u0003\u0003\u0003[\b\u0003\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0005\u0004g\b\u0004\n\u0004\f\u0004j\t\u0004\u0003"+
		"\u0004l\b\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0005\u0004q\b\u0004"+
		"\n\u0004\f\u0004t\t\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0005\u0001\u0005\u0005\u0005|\b\u0005\n\u0005\f\u0005\u007f\t"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0003\u0006\u0088\b\u0006\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0003\u0007\u008e\b\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0003\b\u009a"+
		"\b\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001"+
		"\t\u0001\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0005\n\u00ab\b\n\n"+
		"\n\f\n\u00ae\t\n\u0001\n\u0001\n\u0003\n\u00b2\b\n\u0001\n\u0001\n\u0001"+
		"\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0005\u000b"+
		"\u00bc\b\u000b\n\u000b\f\u000b\u00bf\t\u000b\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\f\u0001\f\u0005\f\u00c7\b\f\n\f\f\f\u00ca\t\f"+
		"\u0001\f\u0001\f\u0001\r\u0001\r\u0005\r\u00d0\b\r\n\r\f\r\u00d3\t\r\u0001"+
		"\r\u0001\r\u0001\u000e\u0001\u000e\u0005\u000e\u00d9\b\u000e\n\u000e\f"+
		"\u000e\u00dc\t\u000e\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0003\u000f\u00e7"+
		"\b\u000f\u0003\u000f\u00e9\b\u000f\u0001\u0010\u0001\u0010\u0001\u0011"+
		"\u0001\u0011\u0001\u0012\u0001\u0012\u0001\u0013\u0001\u0013\u0001\u0014"+
		"\u0001\u0014\u0001\u0015\u0001\u0015\u0001\u0016\u0001\u0016\u0001\u0017"+
		"\u0001\u0017\u0001\u0018\u0001\u0018\u0001\u0019\u0001\u0019\u0001\u001a"+
		"\u0001\u001a\u0001\u001a\u0000\u0000\u001b\u0000\u0002\u0004\u0006\b\n"+
		"\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e \"$&(*,.024\u0000"+
		"\u0004\u0001\u0000\u0016\u0018\u0001\u0000\u0011\u0012\u0001\u0000\u0013"+
		"\u0014\u0001\u0000\r\u000e\u00fc\u00006\u0001\u0000\u0000\u0000\u0002"+
		"G\u0001\u0000\u0000\u0000\u0004K\u0001\u0000\u0000\u0000\u0006Z\u0001"+
		"\u0000\u0000\u0000\b\\\u0001\u0000\u0000\u0000\ny\u0001\u0000\u0000\u0000"+
		"\f\u0087\u0001\u0000\u0000\u0000\u000e\u0089\u0001\u0000\u0000\u0000\u0010"+
		"\u0091\u0001\u0000\u0000\u0000\u0012\u009d\u0001\u0000\u0000\u0000\u0014"+
		"\u00a5\u0001\u0000\u0000\u0000\u0016\u00b6\u0001\u0000\u0000\u0000\u0018"+
		"\u00c4\u0001\u0000\u0000\u0000\u001a\u00cd\u0001\u0000\u0000\u0000\u001c"+
		"\u00d6\u0001\u0000\u0000\u0000\u001e\u00e8\u0001\u0000\u0000\u0000 \u00ea"+
		"\u0001\u0000\u0000\u0000\"\u00ec\u0001\u0000\u0000\u0000$\u00ee\u0001"+
		"\u0000\u0000\u0000&\u00f0\u0001\u0000\u0000\u0000(\u00f2\u0001\u0000\u0000"+
		"\u0000*\u00f4\u0001\u0000\u0000\u0000,\u00f6\u0001\u0000\u0000\u0000."+
		"\u00f8\u0001\u0000\u0000\u00000\u00fa\u0001\u0000\u0000\u00002\u00fc\u0001"+
		"\u0000\u0000\u00004\u00fe\u0001\u0000\u0000\u000067\u0005\u0001\u0000"+
		"\u000078\u0005\u000f\u0000\u00008:\u0005\"\u0000\u00009;\u0003\u0002\u0001"+
		"\u0000:9\u0001\u0000\u0000\u0000:;\u0001\u0000\u0000\u0000;?\u0001\u0000"+
		"\u0000\u0000<>\u0003\b\u0004\u0000=<\u0001\u0000\u0000\u0000>A\u0001\u0000"+
		"\u0000\u0000?=\u0001\u0000\u0000\u0000?@\u0001\u0000\u0000\u0000@B\u0001"+
		"\u0000\u0000\u0000A?\u0001\u0000\u0000\u0000BC\u00032\u0019\u0000CD\u0003"+
		"4\u001a\u0000DE\u0005\"\u0000\u0000E\u0001\u0001\u0000\u0000\u0000FH\u0003"+
		"\u0004\u0002\u0000GF\u0001\u0000\u0000\u0000HI\u0001\u0000\u0000\u0000"+
		"IG\u0001\u0000\u0000\u0000IJ\u0001\u0000\u0000\u0000J\u0003\u0001\u0000"+
		"\u0000\u0000KL\u0005\u0002\u0000\u0000LQ\u0005\u000f\u0000\u0000MN\u0005"+
		"#\u0000\u0000NP\u0005\u000f\u0000\u0000OM\u0001\u0000\u0000\u0000PS\u0001"+
		"\u0000\u0000\u0000QO\u0001\u0000\u0000\u0000QR\u0001\u0000\u0000\u0000"+
		"RT\u0001\u0000\u0000\u0000SQ\u0001\u0000\u0000\u0000TU\u0005$\u0000\u0000"+
		"UV\u0003\u0006\u0003\u0000VW\u0005\"\u0000\u0000W\u0005\u0001\u0000\u0000"+
		"\u0000X[\u0003.\u0017\u0000Y[\u00030\u0018\u0000ZX\u0001\u0000\u0000\u0000"+
		"ZY\u0001\u0000\u0000\u0000[\u0007\u0001\u0000\u0000\u0000\\]\u0003,\u0016"+
		"\u0000]^\u0005\u000f\u0000\u0000^k\u0005\u001c\u0000\u0000_`\u0005\u000f"+
		"\u0000\u0000`a\u0005$\u0000\u0000ah\u0003\u0006\u0003\u0000bc\u0005#\u0000"+
		"\u0000cd\u0005\u000f\u0000\u0000de\u0005$\u0000\u0000eg\u0003\u0006\u0003"+
		"\u0000fb\u0001\u0000\u0000\u0000gj\u0001\u0000\u0000\u0000hf\u0001\u0000"+
		"\u0000\u0000hi\u0001\u0000\u0000\u0000il\u0001\u0000\u0000\u0000jh\u0001"+
		"\u0000\u0000\u0000k_\u0001\u0000\u0000\u0000kl\u0001\u0000\u0000\u0000"+
		"lm\u0001\u0000\u0000\u0000mn\u0005\u001d\u0000\u0000nr\u0005 \u0000\u0000"+
		"oq\u0003\u0004\u0002\u0000po\u0001\u0000\u0000\u0000qt\u0001\u0000\u0000"+
		"\u0000rp\u0001\u0000\u0000\u0000rs\u0001\u0000\u0000\u0000su\u0001\u0000"+
		"\u0000\u0000tr\u0001\u0000\u0000\u0000uv\u0003\n\u0005\u0000vw\u0005!"+
		"\u0000\u0000wx\u0005\"\u0000\u0000x\t\u0001\u0000\u0000\u0000y}\u0005"+
		"\u001e\u0000\u0000z|\u0003\f\u0006\u0000{z\u0001\u0000\u0000\u0000|\u007f"+
		"\u0001\u0000\u0000\u0000}{\u0001\u0000\u0000\u0000}~\u0001\u0000\u0000"+
		"\u0000~\u0080\u0001\u0000\u0000\u0000\u007f}\u0001\u0000\u0000\u0000\u0080"+
		"\u0081\u0005\u001f\u0000\u0000\u0081\u000b\u0001\u0000\u0000\u0000\u0082"+
		"\u0088\u0003\u000e\u0007\u0000\u0083\u0088\u0003\u0010\b\u0000\u0084\u0088"+
		"\u0003\u0012\t\u0000\u0085\u0088\u0003\u0016\u000b\u0000\u0086\u0088\u0003"+
		"\u0014\n\u0000\u0087\u0082\u0001\u0000\u0000\u0000\u0087\u0083\u0001\u0000"+
		"\u0000\u0000\u0087\u0084\u0001\u0000\u0000\u0000\u0087\u0085\u0001\u0000"+
		"\u0000\u0000\u0087\u0086\u0001\u0000\u0000\u0000\u0088\r\u0001\u0000\u0000"+
		"\u0000\u0089\u008a\u0005\u000f\u0000\u0000\u008a\u008d\u0005\u0015\u0000"+
		"\u0000\u008b\u008e\u0003\u0018\f\u0000\u008c\u008e\u0005\u0010\u0000\u0000"+
		"\u008d\u008b\u0001\u0000\u0000\u0000\u008d\u008c\u0001\u0000\u0000\u0000"+
		"\u008e\u008f\u0001\u0000\u0000\u0000\u008f\u0090\u0005\"\u0000\u0000\u0090"+
		"\u000f\u0001\u0000\u0000\u0000\u0091\u0092\u0003\"\u0011\u0000\u0092\u0093"+
		"\u0005\u001c\u0000\u0000\u0093\u0094\u0003\u0018\f\u0000\u0094\u0095\u0005"+
		"\u001d\u0000\u0000\u0095\u0099\u0003\n\u0005\u0000\u0096\u0097\u0003$"+
		"\u0012\u0000\u0097\u0098\u0003\n\u0005\u0000\u0098\u009a\u0001\u0000\u0000"+
		"\u0000\u0099\u0096\u0001\u0000\u0000\u0000\u0099\u009a\u0001\u0000\u0000"+
		"\u0000\u009a\u009b\u0001\u0000\u0000\u0000\u009b\u009c\u0005\"\u0000\u0000"+
		"\u009c\u0011\u0001\u0000\u0000\u0000\u009d\u009e\u0003&\u0013\u0000\u009e"+
		"\u009f\u0003\n\u0005\u0000\u009f\u00a0\u0003(\u0014\u0000\u00a0\u00a1"+
		"\u0005\u001c\u0000\u0000\u00a1\u00a2\u0003\u0018\f\u0000\u00a2\u00a3\u0005"+
		"\u001d\u0000\u0000\u00a3\u00a4\u0005\"\u0000\u0000\u00a4\u0013\u0001\u0000"+
		"\u0000\u0000\u00a5\u00a6\u0003*\u0015\u0000\u00a6\u00ac\u0005\u001c\u0000"+
		"\u0000\u00a7\u00a8\u0003\u0018\f\u0000\u00a8\u00a9\u0005#\u0000\u0000"+
		"\u00a9\u00ab\u0001\u0000\u0000\u0000\u00aa\u00a7\u0001\u0000\u0000\u0000"+
		"\u00ab\u00ae\u0001\u0000\u0000\u0000\u00ac\u00aa\u0001\u0000\u0000\u0000"+
		"\u00ac\u00ad\u0001\u0000\u0000\u0000\u00ad\u00b1\u0001\u0000\u0000\u0000"+
		"\u00ae\u00ac\u0001\u0000\u0000\u0000\u00af\u00b2\u0003\u0018\f\u0000\u00b0"+
		"\u00b2\u0005\u0010\u0000\u0000\u00b1\u00af\u0001\u0000\u0000\u0000\u00b1"+
		"\u00b0\u0001\u0000\u0000\u0000\u00b2\u00b3\u0001\u0000\u0000\u0000\u00b3"+
		"\u00b4\u0005\u001d\u0000\u0000\u00b4\u00b5\u0005\"\u0000\u0000\u00b5\u0015"+
		"\u0001\u0000\u0000\u0000\u00b6\u00b7\u0005\u000f\u0000\u0000\u00b7\u00bd"+
		"\u0005\u001c\u0000\u0000\u00b8\u00b9\u0003\u0018\f\u0000\u00b9\u00ba\u0005"+
		"#\u0000\u0000\u00ba\u00bc\u0001\u0000\u0000\u0000\u00bb\u00b8\u0001\u0000"+
		"\u0000\u0000\u00bc\u00bf\u0001\u0000\u0000\u0000\u00bd\u00bb\u0001\u0000"+
		"\u0000\u0000\u00bd\u00be\u0001\u0000\u0000\u0000\u00be\u00c0\u0001\u0000"+
		"\u0000\u0000\u00bf\u00bd\u0001\u0000\u0000\u0000\u00c0\u00c1\u0003\u0018"+
		"\f\u0000\u00c1\u00c2\u0005\u001d\u0000\u0000\u00c2\u00c3\u0005\"\u0000"+
		"\u0000\u00c3\u0017\u0001\u0000\u0000\u0000\u00c4\u00c8\u0003\u001a\r\u0000"+
		"\u00c5\u00c7\u0007\u0000\u0000\u0000\u00c6\u00c5\u0001\u0000\u0000\u0000"+
		"\u00c7\u00ca\u0001\u0000\u0000\u0000\u00c8\u00c6\u0001\u0000\u0000\u0000"+
		"\u00c8\u00c9\u0001\u0000\u0000\u0000\u00c9\u00cb\u0001\u0000\u0000\u0000"+
		"\u00ca\u00c8\u0001\u0000\u0000\u0000\u00cb\u00cc\u0003\u001a\r\u0000\u00cc"+
		"\u0019\u0001\u0000\u0000\u0000\u00cd\u00d1\u0003\u001c\u000e\u0000\u00ce"+
		"\u00d0\u0007\u0001\u0000\u0000\u00cf\u00ce\u0001\u0000\u0000\u0000\u00d0"+
		"\u00d3\u0001\u0000\u0000\u0000\u00d1\u00cf\u0001\u0000\u0000\u0000\u00d1"+
		"\u00d2\u0001\u0000\u0000\u0000\u00d2\u00d4\u0001\u0000\u0000\u0000\u00d3"+
		"\u00d1\u0001\u0000\u0000\u0000\u00d4\u00d5\u0003\u001c\u000e\u0000\u00d5"+
		"\u001b\u0001\u0000\u0000\u0000\u00d6\u00da\u0003\u001e\u000f\u0000\u00d7"+
		"\u00d9\u0007\u0002\u0000\u0000\u00d8\u00d7\u0001\u0000\u0000\u0000\u00d9"+
		"\u00dc\u0001\u0000\u0000\u0000\u00da\u00d8\u0001\u0000\u0000\u0000\u00da"+
		"\u00db\u0001\u0000\u0000\u0000\u00db\u00dd\u0001\u0000\u0000\u0000\u00dc"+
		"\u00da\u0001\u0000\u0000\u0000\u00dd\u00de\u0003\u001e\u000f\u0000\u00de"+
		"\u001d\u0001\u0000\u0000\u0000\u00df\u00e0\u0005\u001c\u0000\u0000\u00e0"+
		"\u00e1\u0003\u0018\f\u0000\u00e1\u00e2\u0005\u001d\u0000\u0000\u00e2\u00e9"+
		"\u0001\u0000\u0000\u0000\u00e3\u00e6\u0007\u0001\u0000\u0000\u00e4\u00e7"+
		"\u0005\u000f\u0000\u0000\u00e5\u00e7\u0003 \u0010\u0000\u00e6\u00e4\u0001"+
		"\u0000\u0000\u0000\u00e6\u00e5\u0001\u0000\u0000\u0000\u00e7\u00e9\u0001"+
		"\u0000\u0000\u0000\u00e8\u00df\u0001\u0000\u0000\u0000\u00e8\u00e3\u0001"+
		"\u0000\u0000\u0000\u00e9\u001f\u0001\u0000\u0000\u0000\u00ea\u00eb\u0007"+
		"\u0003\u0000\u0000\u00eb!\u0001\u0000\u0000\u0000\u00ec\u00ed\u0005\u0003"+
		"\u0000\u0000\u00ed#\u0001\u0000\u0000\u0000\u00ee\u00ef\u0005\u0004\u0000"+
		"\u0000\u00ef%\u0001\u0000\u0000\u0000\u00f0\u00f1\u0005\u0005\u0000\u0000"+
		"\u00f1\'\u0001\u0000\u0000\u0000\u00f2\u00f3\u0005\u0006\u0000\u0000\u00f3"+
		")\u0001\u0000\u0000\u0000\u00f4\u00f5\u0005\u0007\u0000\u0000\u00f5+\u0001"+
		"\u0000\u0000\u0000\u00f6\u00f7\u0005\b\u0000\u0000\u00f7-\u0001\u0000"+
		"\u0000\u0000\u00f8\u00f9\u0005\t\u0000\u0000\u00f9/\u0001\u0000\u0000"+
		"\u0000\u00fa\u00fb\u0005\n\u0000\u0000\u00fb1\u0001\u0000\u0000\u0000"+
		"\u00fc\u00fd\u0005\u000b\u0000\u0000\u00fd3\u0001\u0000\u0000\u0000\u00fe"+
		"\u00ff\u0005\f\u0000\u0000\u00ff5\u0001\u0000\u0000\u0000\u0014:?IQZh"+
		"kr}\u0087\u008d\u0099\u00ac\u00b1\u00bd\u00c8\u00d1\u00da\u00e6\u00e8";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
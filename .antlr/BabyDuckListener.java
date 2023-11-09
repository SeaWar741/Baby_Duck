// Generated from c:/Users/juanc/Desktop/Baby_Duck/BabyDuck.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link BabyDuckParser}.
 */
public interface BabyDuckListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(BabyDuckParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(BabyDuckParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#vars}.
	 * @param ctx the parse tree
	 */
	void enterVars(BabyDuckParser.VarsContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#vars}.
	 * @param ctx the parse tree
	 */
	void exitVars(BabyDuckParser.VarsContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#type}.
	 * @param ctx the parse tree
	 */
	void enterType(BabyDuckParser.TypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#type}.
	 * @param ctx the parse tree
	 */
	void exitType(BabyDuckParser.TypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#funcs}.
	 * @param ctx the parse tree
	 */
	void enterFuncs(BabyDuckParser.FuncsContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#funcs}.
	 * @param ctx the parse tree
	 */
	void exitFuncs(BabyDuckParser.FuncsContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#body}.
	 * @param ctx the parse tree
	 */
	void enterBody(BabyDuckParser.BodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#body}.
	 * @param ctx the parse tree
	 */
	void exitBody(BabyDuckParser.BodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(BabyDuckParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(BabyDuckParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#assign}.
	 * @param ctx the parse tree
	 */
	void enterAssign(BabyDuckParser.AssignContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#assign}.
	 * @param ctx the parse tree
	 */
	void exitAssign(BabyDuckParser.AssignContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#condition}.
	 * @param ctx the parse tree
	 */
	void enterCondition(BabyDuckParser.ConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#condition}.
	 * @param ctx the parse tree
	 */
	void exitCondition(BabyDuckParser.ConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#cycle}.
	 * @param ctx the parse tree
	 */
	void enterCycle(BabyDuckParser.CycleContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#cycle}.
	 * @param ctx the parse tree
	 */
	void exitCycle(BabyDuckParser.CycleContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#print}.
	 * @param ctx the parse tree
	 */
	void enterPrint(BabyDuckParser.PrintContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#print}.
	 * @param ctx the parse tree
	 */
	void exitPrint(BabyDuckParser.PrintContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#f_call}.
	 * @param ctx the parse tree
	 */
	void enterF_call(BabyDuckParser.F_callContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#f_call}.
	 * @param ctx the parse tree
	 */
	void exitF_call(BabyDuckParser.F_callContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(BabyDuckParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(BabyDuckParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#relop}.
	 * @param ctx the parse tree
	 */
	void enterRelop(BabyDuckParser.RelopContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#relop}.
	 * @param ctx the parse tree
	 */
	void exitRelop(BabyDuckParser.RelopContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#exp}.
	 * @param ctx the parse tree
	 */
	void enterExp(BabyDuckParser.ExpContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#exp}.
	 * @param ctx the parse tree
	 */
	void exitExp(BabyDuckParser.ExpContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#termino}.
	 * @param ctx the parse tree
	 */
	void enterTermino(BabyDuckParser.TerminoContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#termino}.
	 * @param ctx the parse tree
	 */
	void exitTermino(BabyDuckParser.TerminoContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#factor}.
	 * @param ctx the parse tree
	 */
	void enterFactor(BabyDuckParser.FactorContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#factor}.
	 * @param ctx the parse tree
	 */
	void exitFactor(BabyDuckParser.FactorContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#parenthesized_expression}.
	 * @param ctx the parse tree
	 */
	void enterParenthesized_expression(BabyDuckParser.Parenthesized_expressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#parenthesized_expression}.
	 * @param ctx the parse tree
	 */
	void exitParenthesized_expression(BabyDuckParser.Parenthesized_expressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#unary_expression}.
	 * @param ctx the parse tree
	 */
	void enterUnary_expression(BabyDuckParser.Unary_expressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#unary_expression}.
	 * @param ctx the parse tree
	 */
	void exitUnary_expression(BabyDuckParser.Unary_expressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#cte}.
	 * @param ctx the parse tree
	 */
	void enterCte(BabyDuckParser.CteContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#cte}.
	 * @param ctx the parse tree
	 */
	void exitCte(BabyDuckParser.CteContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#if}.
	 * @param ctx the parse tree
	 */
	void enterIf(BabyDuckParser.IfContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#if}.
	 * @param ctx the parse tree
	 */
	void exitIf(BabyDuckParser.IfContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#else}.
	 * @param ctx the parse tree
	 */
	void enterElse(BabyDuckParser.ElseContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#else}.
	 * @param ctx the parse tree
	 */
	void exitElse(BabyDuckParser.ElseContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#while}.
	 * @param ctx the parse tree
	 */
	void enterWhile(BabyDuckParser.WhileContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#while}.
	 * @param ctx the parse tree
	 */
	void exitWhile(BabyDuckParser.WhileContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#do}.
	 * @param ctx the parse tree
	 */
	void enterDo(BabyDuckParser.DoContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#do}.
	 * @param ctx the parse tree
	 */
	void exitDo(BabyDuckParser.DoContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#print_w}.
	 * @param ctx the parse tree
	 */
	void enterPrint_w(BabyDuckParser.Print_wContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#print_w}.
	 * @param ctx the parse tree
	 */
	void exitPrint_w(BabyDuckParser.Print_wContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#void}.
	 * @param ctx the parse tree
	 */
	void enterVoid(BabyDuckParser.VoidContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#void}.
	 * @param ctx the parse tree
	 */
	void exitVoid(BabyDuckParser.VoidContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#int}.
	 * @param ctx the parse tree
	 */
	void enterInt(BabyDuckParser.IntContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#int}.
	 * @param ctx the parse tree
	 */
	void exitInt(BabyDuckParser.IntContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#float}.
	 * @param ctx the parse tree
	 */
	void enterFloat(BabyDuckParser.FloatContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#float}.
	 * @param ctx the parse tree
	 */
	void exitFloat(BabyDuckParser.FloatContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#main}.
	 * @param ctx the parse tree
	 */
	void enterMain(BabyDuckParser.MainContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#main}.
	 * @param ctx the parse tree
	 */
	void exitMain(BabyDuckParser.MainContext ctx);
	/**
	 * Enter a parse tree produced by {@link BabyDuckParser#end}.
	 * @param ctx the parse tree
	 */
	void enterEnd(BabyDuckParser.EndContext ctx);
	/**
	 * Exit a parse tree produced by {@link BabyDuckParser#end}.
	 * @param ctx the parse tree
	 */
	void exitEnd(BabyDuckParser.EndContext ctx);
}
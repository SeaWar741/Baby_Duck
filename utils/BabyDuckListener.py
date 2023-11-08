# Generated from BabyDuck.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .BabyDuckParser import BabyDuckParser
else:
    from BabyDuckParser import BabyDuckParser

# This class defines a complete listener for a parse tree produced by BabyDuckParser.
class BabyDuckListener(ParseTreeListener):

    # Enter a parse tree produced by BabyDuckParser#program.
    def enterProgram(self, ctx:BabyDuckParser.ProgramContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#program.
    def exitProgram(self, ctx:BabyDuckParser.ProgramContext):
        pass


    # Enter a parse tree produced by BabyDuckParser#vars.
    def enterVars(self, ctx:BabyDuckParser.VarsContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#vars.
    def exitVars(self, ctx:BabyDuckParser.VarsContext):
        pass


    # Enter a parse tree produced by BabyDuckParser#type.
    def enterType(self, ctx:BabyDuckParser.TypeContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#type.
    def exitType(self, ctx:BabyDuckParser.TypeContext):
        pass


    # Enter a parse tree produced by BabyDuckParser#funcs.
    def enterFuncs(self, ctx:BabyDuckParser.FuncsContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#funcs.
    def exitFuncs(self, ctx:BabyDuckParser.FuncsContext):
        pass


    # Enter a parse tree produced by BabyDuckParser#body.
    def enterBody(self, ctx:BabyDuckParser.BodyContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#body.
    def exitBody(self, ctx:BabyDuckParser.BodyContext):
        pass


    # Enter a parse tree produced by BabyDuckParser#statement.
    def enterStatement(self, ctx:BabyDuckParser.StatementContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#statement.
    def exitStatement(self, ctx:BabyDuckParser.StatementContext):
        pass


    # Enter a parse tree produced by BabyDuckParser#assign.
    def enterAssign(self, ctx:BabyDuckParser.AssignContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#assign.
    def exitAssign(self, ctx:BabyDuckParser.AssignContext):
        pass


    # Enter a parse tree produced by BabyDuckParser#condition.
    def enterCondition(self, ctx:BabyDuckParser.ConditionContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#condition.
    def exitCondition(self, ctx:BabyDuckParser.ConditionContext):
        pass


    # Enter a parse tree produced by BabyDuckParser#cycle.
    def enterCycle(self, ctx:BabyDuckParser.CycleContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#cycle.
    def exitCycle(self, ctx:BabyDuckParser.CycleContext):
        pass


    # Enter a parse tree produced by BabyDuckParser#print.
    def enterPrint(self, ctx:BabyDuckParser.PrintContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#print.
    def exitPrint(self, ctx:BabyDuckParser.PrintContext):
        pass


    # Enter a parse tree produced by BabyDuckParser#f_call.
    def enterF_call(self, ctx:BabyDuckParser.F_callContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#f_call.
    def exitF_call(self, ctx:BabyDuckParser.F_callContext):
        pass


    # Enter a parse tree produced by BabyDuckParser#expression.
    def enterExpression(self, ctx:BabyDuckParser.ExpressionContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#expression.
    def exitExpression(self, ctx:BabyDuckParser.ExpressionContext):
        pass


    # Enter a parse tree produced by BabyDuckParser#relop.
    def enterRelop(self, ctx:BabyDuckParser.RelopContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#relop.
    def exitRelop(self, ctx:BabyDuckParser.RelopContext):
        pass


    # Enter a parse tree produced by BabyDuckParser#exp.
    def enterExp(self, ctx:BabyDuckParser.ExpContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#exp.
    def exitExp(self, ctx:BabyDuckParser.ExpContext):
        pass


    # Enter a parse tree produced by BabyDuckParser#termino.
    def enterTermino(self, ctx:BabyDuckParser.TerminoContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#termino.
    def exitTermino(self, ctx:BabyDuckParser.TerminoContext):
        pass


    # Enter a parse tree produced by BabyDuckParser#factor.
    def enterFactor(self, ctx:BabyDuckParser.FactorContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#factor.
    def exitFactor(self, ctx:BabyDuckParser.FactorContext):
        pass


    # Enter a parse tree produced by BabyDuckParser#parenthesized_expression.
    def enterParenthesized_expression(self, ctx:BabyDuckParser.Parenthesized_expressionContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#parenthesized_expression.
    def exitParenthesized_expression(self, ctx:BabyDuckParser.Parenthesized_expressionContext):
        pass


    # Enter a parse tree produced by BabyDuckParser#unary_expression.
    def enterUnary_expression(self, ctx:BabyDuckParser.Unary_expressionContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#unary_expression.
    def exitUnary_expression(self, ctx:BabyDuckParser.Unary_expressionContext):
        pass


    # Enter a parse tree produced by BabyDuckParser#cte.
    def enterCte(self, ctx:BabyDuckParser.CteContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#cte.
    def exitCte(self, ctx:BabyDuckParser.CteContext):
        pass


    # Enter a parse tree produced by BabyDuckParser#if.
    def enterIf(self, ctx:BabyDuckParser.IfContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#if.
    def exitIf(self, ctx:BabyDuckParser.IfContext):
        pass


    # Enter a parse tree produced by BabyDuckParser#else.
    def enterElse(self, ctx:BabyDuckParser.ElseContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#else.
    def exitElse(self, ctx:BabyDuckParser.ElseContext):
        pass


    # Enter a parse tree produced by BabyDuckParser#while.
    def enterWhile(self, ctx:BabyDuckParser.WhileContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#while.
    def exitWhile(self, ctx:BabyDuckParser.WhileContext):
        pass


    # Enter a parse tree produced by BabyDuckParser#do.
    def enterDo(self, ctx:BabyDuckParser.DoContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#do.
    def exitDo(self, ctx:BabyDuckParser.DoContext):
        pass


    # Enter a parse tree produced by BabyDuckParser#print_w.
    def enterPrint_w(self, ctx:BabyDuckParser.Print_wContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#print_w.
    def exitPrint_w(self, ctx:BabyDuckParser.Print_wContext):
        pass


    # Enter a parse tree produced by BabyDuckParser#void.
    def enterVoid(self, ctx:BabyDuckParser.VoidContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#void.
    def exitVoid(self, ctx:BabyDuckParser.VoidContext):
        pass


    # Enter a parse tree produced by BabyDuckParser#int.
    def enterInt(self, ctx:BabyDuckParser.IntContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#int.
    def exitInt(self, ctx:BabyDuckParser.IntContext):
        pass


    # Enter a parse tree produced by BabyDuckParser#float.
    def enterFloat(self, ctx:BabyDuckParser.FloatContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#float.
    def exitFloat(self, ctx:BabyDuckParser.FloatContext):
        pass


    # Enter a parse tree produced by BabyDuckParser#main.
    def enterMain(self, ctx:BabyDuckParser.MainContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#main.
    def exitMain(self, ctx:BabyDuckParser.MainContext):
        pass


    # Enter a parse tree produced by BabyDuckParser#end.
    def enterEnd(self, ctx:BabyDuckParser.EndContext):
        pass

    # Exit a parse tree produced by BabyDuckParser#end.
    def exitEnd(self, ctx:BabyDuckParser.EndContext):
        pass



del BabyDuckParser
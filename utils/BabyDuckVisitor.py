# Generated from BabyDuck.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .BabyDuckParser import BabyDuckParser
else:
    from BabyDuckParser import BabyDuckParser

# This class defines a complete generic visitor for a parse tree produced by BabyDuckParser.

class BabyDuckVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BabyDuckParser#program.
    def visitProgram(self, ctx:BabyDuckParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#mainSection.
    def visitMainSection(self, ctx:BabyDuckParser.MainSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#vars.
    def visitVars(self, ctx:BabyDuckParser.VarsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#type.
    def visitType(self, ctx:BabyDuckParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#funcs.
    def visitFuncs(self, ctx:BabyDuckParser.FuncsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#body.
    def visitBody(self, ctx:BabyDuckParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#statement.
    def visitStatement(self, ctx:BabyDuckParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#assign.
    def visitAssign(self, ctx:BabyDuckParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#condition.
    def visitCondition(self, ctx:BabyDuckParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#cycle.
    def visitCycle(self, ctx:BabyDuckParser.CycleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#print.
    def visitPrint(self, ctx:BabyDuckParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#f_call.
    def visitF_call(self, ctx:BabyDuckParser.F_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#expression.
    def visitExpression(self, ctx:BabyDuckParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#relop.
    def visitRelop(self, ctx:BabyDuckParser.RelopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#exp.
    def visitExp(self, ctx:BabyDuckParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#termino.
    def visitTermino(self, ctx:BabyDuckParser.TerminoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#factor.
    def visitFactor(self, ctx:BabyDuckParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#parenthesized_expression.
    def visitParenthesized_expression(self, ctx:BabyDuckParser.Parenthesized_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#unary_expression.
    def visitUnary_expression(self, ctx:BabyDuckParser.Unary_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#cte.
    def visitCte(self, ctx:BabyDuckParser.CteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#if.
    def visitIf(self, ctx:BabyDuckParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#else.
    def visitElse(self, ctx:BabyDuckParser.ElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#while.
    def visitWhile(self, ctx:BabyDuckParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#do.
    def visitDo(self, ctx:BabyDuckParser.DoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#print_w.
    def visitPrint_w(self, ctx:BabyDuckParser.Print_wContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#void.
    def visitVoid(self, ctx:BabyDuckParser.VoidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#int.
    def visitInt(self, ctx:BabyDuckParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#float.
    def visitFloat(self, ctx:BabyDuckParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#main.
    def visitMain(self, ctx:BabyDuckParser.MainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BabyDuckParser#end.
    def visitEnd(self, ctx:BabyDuckParser.EndContext):
        return self.visitChildren(ctx)



del BabyDuckParser
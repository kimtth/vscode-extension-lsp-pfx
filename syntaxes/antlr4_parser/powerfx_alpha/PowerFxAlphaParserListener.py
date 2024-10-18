# Generated from PowerFxAlphaParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PowerFxAlphaParser import PowerFxAlphaParser
else:
    from PowerFxAlphaParser import PowerFxAlphaParser

# This class defines a complete listener for a parse tree produced by PowerFxAlphaParser.
class PowerFxAlphaParserListener(ParseTreeListener):

    # Enter a parse tree produced by PowerFxAlphaParser#expressionUnit.
    def enterExpressionUnit(self, ctx:PowerFxAlphaParser.ExpressionUnitContext):
        pass

    # Exit a parse tree produced by PowerFxAlphaParser#expressionUnit.
    def exitExpressionUnit(self, ctx:PowerFxAlphaParser.ExpressionUnitContext):
        pass


    # Enter a parse tree produced by PowerFxAlphaParser#importStatement.
    def enterImportStatement(self, ctx:PowerFxAlphaParser.ImportStatementContext):
        pass

    # Exit a parse tree produced by PowerFxAlphaParser#importStatement.
    def exitImportStatement(self, ctx:PowerFxAlphaParser.ImportStatementContext):
        pass


    # Enter a parse tree produced by PowerFxAlphaParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:PowerFxAlphaParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by PowerFxAlphaParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:PowerFxAlphaParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by PowerFxAlphaParser#functionArguments.
    def enterFunctionArguments(self, ctx:PowerFxAlphaParser.FunctionArgumentsContext):
        pass

    # Exit a parse tree produced by PowerFxAlphaParser#functionArguments.
    def exitFunctionArguments(self, ctx:PowerFxAlphaParser.FunctionArgumentsContext):
        pass


    # Enter a parse tree produced by PowerFxAlphaParser#argument.
    def enterArgument(self, ctx:PowerFxAlphaParser.ArgumentContext):
        pass

    # Exit a parse tree produced by PowerFxAlphaParser#argument.
    def exitArgument(self, ctx:PowerFxAlphaParser.ArgumentContext):
        pass


    # Enter a parse tree produced by PowerFxAlphaParser#functionBody.
    def enterFunctionBody(self, ctx:PowerFxAlphaParser.FunctionBodyContext):
        pass

    # Exit a parse tree produced by PowerFxAlphaParser#functionBody.
    def exitFunctionBody(self, ctx:PowerFxAlphaParser.FunctionBodyContext):
        pass


    # Enter a parse tree produced by PowerFxAlphaParser#expressionElements.
    def enterExpressionElements(self, ctx:PowerFxAlphaParser.ExpressionElementsContext):
        pass

    # Exit a parse tree produced by PowerFxAlphaParser#expressionElements.
    def exitExpressionElements(self, ctx:PowerFxAlphaParser.ExpressionElementsContext):
        pass


    # Enter a parse tree produced by PowerFxAlphaParser#functionCall.
    def enterFunctionCall(self, ctx:PowerFxAlphaParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by PowerFxAlphaParser#functionCall.
    def exitFunctionCall(self, ctx:PowerFxAlphaParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by PowerFxAlphaParser#functionIdentifier.
    def enterFunctionIdentifier(self, ctx:PowerFxAlphaParser.FunctionIdentifierContext):
        pass

    # Exit a parse tree produced by PowerFxAlphaParser#functionIdentifier.
    def exitFunctionIdentifier(self, ctx:PowerFxAlphaParser.FunctionIdentifierContext):
        pass


    # Enter a parse tree produced by PowerFxAlphaParser#literal.
    def enterLiteral(self, ctx:PowerFxAlphaParser.LiteralContext):
        pass

    # Exit a parse tree produced by PowerFxAlphaParser#literal.
    def exitLiteral(self, ctx:PowerFxAlphaParser.LiteralContext):
        pass


    # Enter a parse tree produced by PowerFxAlphaParser#logicalLiteral.
    def enterLogicalLiteral(self, ctx:PowerFxAlphaParser.LogicalLiteralContext):
        pass

    # Exit a parse tree produced by PowerFxAlphaParser#logicalLiteral.
    def exitLogicalLiteral(self, ctx:PowerFxAlphaParser.LogicalLiteralContext):
        pass


    # Enter a parse tree produced by PowerFxAlphaParser#numberLiteral.
    def enterNumberLiteral(self, ctx:PowerFxAlphaParser.NumberLiteralContext):
        pass

    # Exit a parse tree produced by PowerFxAlphaParser#numberLiteral.
    def exitNumberLiteral(self, ctx:PowerFxAlphaParser.NumberLiteralContext):
        pass


    # Enter a parse tree produced by PowerFxAlphaParser#textLiteral.
    def enterTextLiteral(self, ctx:PowerFxAlphaParser.TextLiteralContext):
        pass

    # Exit a parse tree produced by PowerFxAlphaParser#textLiteral.
    def exitTextLiteral(self, ctx:PowerFxAlphaParser.TextLiteralContext):
        pass


    # Enter a parse tree produced by PowerFxAlphaParser#expression.
    def enterExpression(self, ctx:PowerFxAlphaParser.ExpressionContext):
        pass

    # Exit a parse tree produced by PowerFxAlphaParser#expression.
    def exitExpression(self, ctx:PowerFxAlphaParser.ExpressionContext):
        pass


    # Enter a parse tree produced by PowerFxAlphaParser#assignment.
    def enterAssignment(self, ctx:PowerFxAlphaParser.AssignmentContext):
        pass

    # Exit a parse tree produced by PowerFxAlphaParser#assignment.
    def exitAssignment(self, ctx:PowerFxAlphaParser.AssignmentContext):
        pass


    # Enter a parse tree produced by PowerFxAlphaParser#reference.
    def enterReference(self, ctx:PowerFxAlphaParser.ReferenceContext):
        pass

    # Exit a parse tree produced by PowerFxAlphaParser#reference.
    def exitReference(self, ctx:PowerFxAlphaParser.ReferenceContext):
        pass


    # Enter a parse tree produced by PowerFxAlphaParser#baseReference.
    def enterBaseReference(self, ctx:PowerFxAlphaParser.BaseReferenceContext):
        pass

    # Exit a parse tree produced by PowerFxAlphaParser#baseReference.
    def exitBaseReference(self, ctx:PowerFxAlphaParser.BaseReferenceContext):
        pass


    # Enter a parse tree produced by PowerFxAlphaParser#referenceOperator.
    def enterReferenceOperator(self, ctx:PowerFxAlphaParser.ReferenceOperatorContext):
        pass

    # Exit a parse tree produced by PowerFxAlphaParser#referenceOperator.
    def exitReferenceOperator(self, ctx:PowerFxAlphaParser.ReferenceOperatorContext):
        pass


    # Enter a parse tree produced by PowerFxAlphaParser#referenceList.
    def enterReferenceList(self, ctx:PowerFxAlphaParser.ReferenceListContext):
        pass

    # Exit a parse tree produced by PowerFxAlphaParser#referenceList.
    def exitReferenceList(self, ctx:PowerFxAlphaParser.ReferenceListContext):
        pass


    # Enter a parse tree produced by PowerFxAlphaParser#inlineRecord.
    def enterInlineRecord(self, ctx:PowerFxAlphaParser.InlineRecordContext):
        pass

    # Exit a parse tree produced by PowerFxAlphaParser#inlineRecord.
    def exitInlineRecord(self, ctx:PowerFxAlphaParser.InlineRecordContext):
        pass


    # Enter a parse tree produced by PowerFxAlphaParser#inlineRecordList.
    def enterInlineRecordList(self, ctx:PowerFxAlphaParser.InlineRecordListContext):
        pass

    # Exit a parse tree produced by PowerFxAlphaParser#inlineRecordList.
    def exitInlineRecordList(self, ctx:PowerFxAlphaParser.InlineRecordListContext):
        pass


    # Enter a parse tree produced by PowerFxAlphaParser#inlineTable.
    def enterInlineTable(self, ctx:PowerFxAlphaParser.InlineTableContext):
        pass

    # Exit a parse tree produced by PowerFxAlphaParser#inlineTable.
    def exitInlineTable(self, ctx:PowerFxAlphaParser.InlineTableContext):
        pass


    # Enter a parse tree produced by PowerFxAlphaParser#inlineTableList.
    def enterInlineTableList(self, ctx:PowerFxAlphaParser.InlineTableListContext):
        pass

    # Exit a parse tree produced by PowerFxAlphaParser#inlineTableList.
    def exitInlineTableList(self, ctx:PowerFxAlphaParser.InlineTableListContext):
        pass


    # Enter a parse tree produced by PowerFxAlphaParser#disambiguatedIdentifier.
    def enterDisambiguatedIdentifier(self, ctx:PowerFxAlphaParser.DisambiguatedIdentifierContext):
        pass

    # Exit a parse tree produced by PowerFxAlphaParser#disambiguatedIdentifier.
    def exitDisambiguatedIdentifier(self, ctx:PowerFxAlphaParser.DisambiguatedIdentifierContext):
        pass


    # Enter a parse tree produced by PowerFxAlphaParser#tableColumnIdentifier.
    def enterTableColumnIdentifier(self, ctx:PowerFxAlphaParser.TableColumnIdentifierContext):
        pass

    # Exit a parse tree produced by PowerFxAlphaParser#tableColumnIdentifier.
    def exitTableColumnIdentifier(self, ctx:PowerFxAlphaParser.TableColumnIdentifierContext):
        pass


    # Enter a parse tree produced by PowerFxAlphaParser#globalIdentifier.
    def enterGlobalIdentifier(self, ctx:PowerFxAlphaParser.GlobalIdentifierContext):
        pass

    # Exit a parse tree produced by PowerFxAlphaParser#globalIdentifier.
    def exitGlobalIdentifier(self, ctx:PowerFxAlphaParser.GlobalIdentifierContext):
        pass


    # Enter a parse tree produced by PowerFxAlphaParser#contextKeyword.
    def enterContextKeyword(self, ctx:PowerFxAlphaParser.ContextKeywordContext):
        pass

    # Exit a parse tree produced by PowerFxAlphaParser#contextKeyword.
    def exitContextKeyword(self, ctx:PowerFxAlphaParser.ContextKeywordContext):
        pass


    # Enter a parse tree produced by PowerFxAlphaParser#binaryOperator.
    def enterBinaryOperator(self, ctx:PowerFxAlphaParser.BinaryOperatorContext):
        pass

    # Exit a parse tree produced by PowerFxAlphaParser#binaryOperator.
    def exitBinaryOperator(self, ctx:PowerFxAlphaParser.BinaryOperatorContext):
        pass


    # Enter a parse tree produced by PowerFxAlphaParser#prefixOperator.
    def enterPrefixOperator(self, ctx:PowerFxAlphaParser.PrefixOperatorContext):
        pass

    # Exit a parse tree produced by PowerFxAlphaParser#prefixOperator.
    def exitPrefixOperator(self, ctx:PowerFxAlphaParser.PrefixOperatorContext):
        pass


    # Enter a parse tree produced by PowerFxAlphaParser#postfixOperator.
    def enterPostfixOperator(self, ctx:PowerFxAlphaParser.PostfixOperatorContext):
        pass

    # Exit a parse tree produced by PowerFxAlphaParser#postfixOperator.
    def exitPostfixOperator(self, ctx:PowerFxAlphaParser.PostfixOperatorContext):
        pass



del PowerFxAlphaParser
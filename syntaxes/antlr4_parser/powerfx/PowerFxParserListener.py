# Generated from PowerFxParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PowerFxParser import PowerFxParser
else:
    from PowerFxParser import PowerFxParser

# This class defines a complete listener for a parse tree produced by PowerFxParser.
class PowerFxParserListener(ParseTreeListener):

    # Enter a parse tree produced by PowerFxParser#expressionUnit.
    def enterExpressionUnit(self, ctx:PowerFxParser.ExpressionUnitContext):
        pass

    # Exit a parse tree produced by PowerFxParser#expressionUnit.
    def exitExpressionUnit(self, ctx:PowerFxParser.ExpressionUnitContext):
        pass


    # Enter a parse tree produced by PowerFxParser#expressionElements.
    def enterExpressionElements(self, ctx:PowerFxParser.ExpressionElementsContext):
        pass

    # Exit a parse tree produced by PowerFxParser#expressionElements.
    def exitExpressionElements(self, ctx:PowerFxParser.ExpressionElementsContext):
        pass


    # Enter a parse tree produced by PowerFxParser#expressionElement.
    def enterExpressionElement(self, ctx:PowerFxParser.ExpressionElementContext):
        pass

    # Exit a parse tree produced by PowerFxParser#expressionElement.
    def exitExpressionElement(self, ctx:PowerFxParser.ExpressionElementContext):
        pass


    # Enter a parse tree produced by PowerFxParser#expression.
    def enterExpression(self, ctx:PowerFxParser.ExpressionContext):
        pass

    # Exit a parse tree produced by PowerFxParser#expression.
    def exitExpression(self, ctx:PowerFxParser.ExpressionContext):
        pass


    # Enter a parse tree produced by PowerFxParser#literal.
    def enterLiteral(self, ctx:PowerFxParser.LiteralContext):
        pass

    # Exit a parse tree produced by PowerFxParser#literal.
    def exitLiteral(self, ctx:PowerFxParser.LiteralContext):
        pass


    # Enter a parse tree produced by PowerFxParser#logicalLiteral.
    def enterLogicalLiteral(self, ctx:PowerFxParser.LogicalLiteralContext):
        pass

    # Exit a parse tree produced by PowerFxParser#logicalLiteral.
    def exitLogicalLiteral(self, ctx:PowerFxParser.LogicalLiteralContext):
        pass


    # Enter a parse tree produced by PowerFxParser#numberLiteral.
    def enterNumberLiteral(self, ctx:PowerFxParser.NumberLiteralContext):
        pass

    # Exit a parse tree produced by PowerFxParser#numberLiteral.
    def exitNumberLiteral(self, ctx:PowerFxParser.NumberLiteralContext):
        pass


    # Enter a parse tree produced by PowerFxParser#textLiteral.
    def enterTextLiteral(self, ctx:PowerFxParser.TextLiteralContext):
        pass

    # Exit a parse tree produced by PowerFxParser#textLiteral.
    def exitTextLiteral(self, ctx:PowerFxParser.TextLiteralContext):
        pass


    # Enter a parse tree produced by PowerFxParser#reference.
    def enterReference(self, ctx:PowerFxParser.ReferenceContext):
        pass

    # Exit a parse tree produced by PowerFxParser#reference.
    def exitReference(self, ctx:PowerFxParser.ReferenceContext):
        pass


    # Enter a parse tree produced by PowerFxParser#baseReference.
    def enterBaseReference(self, ctx:PowerFxParser.BaseReferenceContext):
        pass

    # Exit a parse tree produced by PowerFxParser#baseReference.
    def exitBaseReference(self, ctx:PowerFxParser.BaseReferenceContext):
        pass


    # Enter a parse tree produced by PowerFxParser#referenceOperator.
    def enterReferenceOperator(self, ctx:PowerFxParser.ReferenceOperatorContext):
        pass

    # Exit a parse tree produced by PowerFxParser#referenceOperator.
    def exitReferenceOperator(self, ctx:PowerFxParser.ReferenceOperatorContext):
        pass


    # Enter a parse tree produced by PowerFxParser#referenceList.
    def enterReferenceList(self, ctx:PowerFxParser.ReferenceListContext):
        pass

    # Exit a parse tree produced by PowerFxParser#referenceList.
    def exitReferenceList(self, ctx:PowerFxParser.ReferenceListContext):
        pass


    # Enter a parse tree produced by PowerFxParser#inlineRecord.
    def enterInlineRecord(self, ctx:PowerFxParser.InlineRecordContext):
        pass

    # Exit a parse tree produced by PowerFxParser#inlineRecord.
    def exitInlineRecord(self, ctx:PowerFxParser.InlineRecordContext):
        pass


    # Enter a parse tree produced by PowerFxParser#inlineRecordList.
    def enterInlineRecordList(self, ctx:PowerFxParser.InlineRecordListContext):
        pass

    # Exit a parse tree produced by PowerFxParser#inlineRecordList.
    def exitInlineRecordList(self, ctx:PowerFxParser.InlineRecordListContext):
        pass


    # Enter a parse tree produced by PowerFxParser#inlineTable.
    def enterInlineTable(self, ctx:PowerFxParser.InlineTableContext):
        pass

    # Exit a parse tree produced by PowerFxParser#inlineTable.
    def exitInlineTable(self, ctx:PowerFxParser.InlineTableContext):
        pass


    # Enter a parse tree produced by PowerFxParser#inlineTableList.
    def enterInlineTableList(self, ctx:PowerFxParser.InlineTableListContext):
        pass

    # Exit a parse tree produced by PowerFxParser#inlineTableList.
    def exitInlineTableList(self, ctx:PowerFxParser.InlineTableListContext):
        pass


    # Enter a parse tree produced by PowerFxParser#disambiguatedIdentifier.
    def enterDisambiguatedIdentifier(self, ctx:PowerFxParser.DisambiguatedIdentifierContext):
        pass

    # Exit a parse tree produced by PowerFxParser#disambiguatedIdentifier.
    def exitDisambiguatedIdentifier(self, ctx:PowerFxParser.DisambiguatedIdentifierContext):
        pass


    # Enter a parse tree produced by PowerFxParser#tableColumnIdentifier.
    def enterTableColumnIdentifier(self, ctx:PowerFxParser.TableColumnIdentifierContext):
        pass

    # Exit a parse tree produced by PowerFxParser#tableColumnIdentifier.
    def exitTableColumnIdentifier(self, ctx:PowerFxParser.TableColumnIdentifierContext):
        pass


    # Enter a parse tree produced by PowerFxParser#globalIdentifier.
    def enterGlobalIdentifier(self, ctx:PowerFxParser.GlobalIdentifierContext):
        pass

    # Exit a parse tree produced by PowerFxParser#globalIdentifier.
    def exitGlobalIdentifier(self, ctx:PowerFxParser.GlobalIdentifierContext):
        pass


    # Enter a parse tree produced by PowerFxParser#functionCall.
    def enterFunctionCall(self, ctx:PowerFxParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by PowerFxParser#functionCall.
    def exitFunctionCall(self, ctx:PowerFxParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by PowerFxParser#functionIdentifier.
    def enterFunctionIdentifier(self, ctx:PowerFxParser.FunctionIdentifierContext):
        pass

    # Exit a parse tree produced by PowerFxParser#functionIdentifier.
    def exitFunctionIdentifier(self, ctx:PowerFxParser.FunctionIdentifierContext):
        pass


    # Enter a parse tree produced by PowerFxParser#functionArguments.
    def enterFunctionArguments(self, ctx:PowerFxParser.FunctionArgumentsContext):
        pass

    # Exit a parse tree produced by PowerFxParser#functionArguments.
    def exitFunctionArguments(self, ctx:PowerFxParser.FunctionArgumentsContext):
        pass


    # Enter a parse tree produced by PowerFxParser#chainedExpression.
    def enterChainedExpression(self, ctx:PowerFxParser.ChainedExpressionContext):
        pass

    # Exit a parse tree produced by PowerFxParser#chainedExpression.
    def exitChainedExpression(self, ctx:PowerFxParser.ChainedExpressionContext):
        pass


    # Enter a parse tree produced by PowerFxParser#contextKeyword.
    def enterContextKeyword(self, ctx:PowerFxParser.ContextKeywordContext):
        pass

    # Exit a parse tree produced by PowerFxParser#contextKeyword.
    def exitContextKeyword(self, ctx:PowerFxParser.ContextKeywordContext):
        pass


    # Enter a parse tree produced by PowerFxParser#binaryOperator.
    def enterBinaryOperator(self, ctx:PowerFxParser.BinaryOperatorContext):
        pass

    # Exit a parse tree produced by PowerFxParser#binaryOperator.
    def exitBinaryOperator(self, ctx:PowerFxParser.BinaryOperatorContext):
        pass


    # Enter a parse tree produced by PowerFxParser#prefixOperator.
    def enterPrefixOperator(self, ctx:PowerFxParser.PrefixOperatorContext):
        pass

    # Exit a parse tree produced by PowerFxParser#prefixOperator.
    def exitPrefixOperator(self, ctx:PowerFxParser.PrefixOperatorContext):
        pass


    # Enter a parse tree produced by PowerFxParser#postfixOperator.
    def enterPostfixOperator(self, ctx:PowerFxParser.PostfixOperatorContext):
        pass

    # Exit a parse tree produced by PowerFxParser#postfixOperator.
    def exitPostfixOperator(self, ctx:PowerFxParser.PostfixOperatorContext):
        pass



del PowerFxParser
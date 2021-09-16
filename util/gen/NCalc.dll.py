


class <Module>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class <PrivateImplementationDetails>{EADAF598-9AF7-465D-B217-EF510BDC61D3}:
	$$method0x6000113-1: System.Collections.Generic.Dictionary<System.String,System.Int32>
    offsets = {'$$method0x6000113-1': 0}    
    def __init__(self, $$method0x6000113-1: System.Collections.Generic.Dictionary<System.String,System.Int32>, **kwargs):
        super().__init__(self, **kwargs)
		self.$$method0x6000113-1 = $$method0x6000113-1


class HashListEnumerator:

    offsets = {'_hashList': 16, '_orderList': 24, '_mode': 32, '_index': 36, '_version': 40, '_key': 48, '_value': 56}    
    def __init__(self, _hashList: Antlr.Runtime.Collections.HashList, _orderList: System.Collections.Generic.List<System.Object>, _mode: Antlr.Runtime.Collections.HashList.HashListEnumerator.EnumerationMode, _index: System.Int32, _version: System.Int32, _key: System.Object, _value: System.Object, **kwargs):
        super().__init__(self, **kwargs)
		self._hashList = _hashList
		self._orderList = _orderList
		self._mode = _mode
		self._index = _index
		self._version = _version
		self._key = _key
		self._value = _value


class EnumerationMode:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class KeyCollection:

    offsets = {'_hashList': 16}    
    def __init__(self, _hashList: Antlr.Runtime.Collections.HashList, **kwargs):
        super().__init__(self, **kwargs)
		self._hashList = _hashList


class ValueCollection:

    offsets = {'_hashList': 16}    
    def __init__(self, _hashList: Antlr.Runtime.Collections.HashList, **kwargs):
        super().__init__(self, **kwargs)
		self._hashList = _hashList


class SpecialStateTransitionHandler:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class <>c__DisplayClass2:

    offsets = {'leftValue': 16, 'rightValue': 24, '<>4__this': 32, 'expression': 40}    
    def __init__(self, leftValue: System.Object, rightValue: System.Object, <>4__this: NCalc.Domain.EvaluationVisitor, expression: NCalc.Domain.BinaryExpression, **kwargs):
        super().__init__(self, **kwargs)
		self.leftValue = leftValue
		self.rightValue = rightValue
		self.<>4__this = <>4__this
		self.expression = expression


class Func<T>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class NCalcLexer:

    offsets = {'dfa7': 32, 'dfa14': 40}    
    def __init__(self, dfa7: NCalcLexer.DFA7, dfa14: NCalcLexer.DFA14, **kwargs):
        super().__init__(self, **kwargs)
		self.dfa7 = dfa7
		self.dfa14 = dfa14


class DFA14:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class DFA7:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class NCalcParser:

    offsets = {'numberFormatInfo': 8, 'FOLLOW_logicalExpression_in_ncalcExpression56': 16, 'FOLLOW_EOF_in_ncalcExpression58': 24, 'FOLLOW_conditionalExpression_in_logicalExpression78': 32, 'FOLLOW_19_in_logicalExpression84': 40, 'FOLLOW_conditionalExpression_in_logicalExpression88': 48, 'FOLLOW_20_in_logicalExpression90': 56, 'FOLLOW_conditionalExpression_in_logicalExpression94': 64, 'FOLLOW_booleanAndExpression_in_conditionalExpression121': 72, 'FOLLOW_set_in_conditionalExpression130': 80, 'FOLLOW_conditionalExpression_in_conditionalExpression146': 88, 'FOLLOW_bitwiseOrExpression_in_booleanAndExpression180': 96, 'FOLLOW_set_in_booleanAndExpression189': 104, 'FOLLOW_bitwiseOrExpression_in_booleanAndExpression205': 112, 'FOLLOW_bitwiseXOrExpression_in_bitwiseOrExpression237': 120, 'FOLLOW_25_in_bitwiseOrExpression246': 128, 'FOLLOW_bitwiseOrExpression_in_bitwiseOrExpression256': 136, 'FOLLOW_bitwiseAndExpression_in_bitwiseXOrExpression290': 144, 'FOLLOW_26_in_bitwiseXOrExpression299': 152, 'FOLLOW_bitwiseAndExpression_in_bitwiseXOrExpression309': 160, 'FOLLOW_equalityExpression_in_bitwiseAndExpression341': 168, 'FOLLOW_27_in_bitwiseAndExpression350': 176, 'FOLLOW_equalityExpression_in_bitwiseAndExpression360': 184, 'FOLLOW_relationalExpression_in_equalityExpression394': 192, 'FOLLOW_set_in_equalityExpression405': 200, 'FOLLOW_set_in_equalityExpression422': 208, 'FOLLOW_relationalExpression_in_equalityExpression441': 216, 'FOLLOW_shiftExpression_in_relationalExpression474': 224, 'FOLLOW_32_in_relationalExpression485': 232, 'FOLLOW_33_in_relationalExpression495': 240, 'FOLLOW_34_in_relationalExpression506': 248, 'FOLLOW_35_in_relationalExpression516': 256, 'FOLLOW_shiftExpression_in_relationalExpression528': 264, 'FOLLOW_additiveExpression_in_shiftExpression560': 272, 'FOLLOW_36_in_shiftExpression571': 280, 'FOLLOW_37_in_shiftExpression581': 288, 'FOLLOW_additiveExpression_in_shiftExpression593': 296, 'FOLLOW_multiplicativeExpression_in_additiveExpression625': 304, 'FOLLOW_38_in_additiveExpression636': 312, 'FOLLOW_39_in_additiveExpression646': 320, 'FOLLOW_multiplicativeExpression_in_additiveExpression658': 328, 'FOLLOW_unaryExpression_in_multiplicativeExpression690': 336, 'FOLLOW_40_in_multiplicativeExpression701': 344, 'FOLLOW_41_in_multiplicativeExpression711': 352, 'FOLLOW_42_in_multiplicativeExpression721': 360, 'FOLLOW_unaryExpression_in_multiplicativeExpression733': 368, 'FOLLOW_primaryExpression_in_unaryExpression760': 376, 'FOLLOW_set_in_unaryExpression771': 384, 'FOLLOW_primaryExpression_in_unaryExpression779': 392, 'FOLLOW_45_in_unaryExpression791': 400, 'FOLLOW_primaryExpression_in_unaryExpression794': 408, 'FOLLOW_39_in_unaryExpression805': 416, 'FOLLOW_primaryExpression_in_unaryExpression807': 424, 'FOLLOW_46_in_primaryExpression829': 432, 'FOLLOW_logicalExpression_in_primaryExpression831': 440, 'FOLLOW_47_in_primaryExpression833': 448, 'FOLLOW_value_in_primaryExpression843': 456, 'FOLLOW_identifier_in_primaryExpression851': 464, 'FOLLOW_arguments_in_primaryExpression856': 472, 'FOLLOW_INTEGER_in_value876': 480, 'FOLLOW_FLOAT_in_value884': 488, 'FOLLOW_STRING_in_value892': 496, 'FOLLOW_DATETIME_in_value901': 504, 'FOLLOW_TRUE_in_value908': 512, 'FOLLOW_FALSE_in_value916': 520, 'FOLLOW_ID_in_identifier934': 528, 'FOLLOW_NAME_in_identifier942': 536, 'FOLLOW_logicalExpression_in_expressionList966': 544, 'FOLLOW_48_in_expressionList973': 552, 'FOLLOW_logicalExpression_in_expressionList977': 560, 'FOLLOW_46_in_arguments1006': 568, 'FOLLOW_expressionList_in_arguments1010': 576, 'FOLLOW_47_in_arguments1017': 584, 'adaptor': 32, '<Errors>k__BackingField': 40}    
    def __init__(self, numberFormatInfo: System.Globalization.NumberFormatInfo, FOLLOW_logicalExpression_in_ncalcExpression56: Antlr.Runtime.BitSet, FOLLOW_EOF_in_ncalcExpression58: Antlr.Runtime.BitSet, FOLLOW_conditionalExpression_in_logicalExpression78: Antlr.Runtime.BitSet, FOLLOW_19_in_logicalExpression84: Antlr.Runtime.BitSet, FOLLOW_conditionalExpression_in_logicalExpression88: Antlr.Runtime.BitSet, FOLLOW_20_in_logicalExpression90: Antlr.Runtime.BitSet, FOLLOW_conditionalExpression_in_logicalExpression94: Antlr.Runtime.BitSet, FOLLOW_booleanAndExpression_in_conditionalExpression121: Antlr.Runtime.BitSet, FOLLOW_set_in_conditionalExpression130: Antlr.Runtime.BitSet, FOLLOW_conditionalExpression_in_conditionalExpression146: Antlr.Runtime.BitSet, FOLLOW_bitwiseOrExpression_in_booleanAndExpression180: Antlr.Runtime.BitSet, FOLLOW_set_in_booleanAndExpression189: Antlr.Runtime.BitSet, FOLLOW_bitwiseOrExpression_in_booleanAndExpression205: Antlr.Runtime.BitSet, FOLLOW_bitwiseXOrExpression_in_bitwiseOrExpression237: Antlr.Runtime.BitSet, FOLLOW_25_in_bitwiseOrExpression246: Antlr.Runtime.BitSet, FOLLOW_bitwiseOrExpression_in_bitwiseOrExpression256: Antlr.Runtime.BitSet, FOLLOW_bitwiseAndExpression_in_bitwiseXOrExpression290: Antlr.Runtime.BitSet, FOLLOW_26_in_bitwiseXOrExpression299: Antlr.Runtime.BitSet, FOLLOW_bitwiseAndExpression_in_bitwiseXOrExpression309: Antlr.Runtime.BitSet, FOLLOW_equalityExpression_in_bitwiseAndExpression341: Antlr.Runtime.BitSet, FOLLOW_27_in_bitwiseAndExpression350: Antlr.Runtime.BitSet, FOLLOW_equalityExpression_in_bitwiseAndExpression360: Antlr.Runtime.BitSet, FOLLOW_relationalExpression_in_equalityExpression394: Antlr.Runtime.BitSet, FOLLOW_set_in_equalityExpression405: Antlr.Runtime.BitSet, FOLLOW_set_in_equalityExpression422: Antlr.Runtime.BitSet, FOLLOW_relationalExpression_in_equalityExpression441: Antlr.Runtime.BitSet, FOLLOW_shiftExpression_in_relationalExpression474: Antlr.Runtime.BitSet, FOLLOW_32_in_relationalExpression485: Antlr.Runtime.BitSet, FOLLOW_33_in_relationalExpression495: Antlr.Runtime.BitSet, FOLLOW_34_in_relationalExpression506: Antlr.Runtime.BitSet, FOLLOW_35_in_relationalExpression516: Antlr.Runtime.BitSet, FOLLOW_shiftExpression_in_relationalExpression528: Antlr.Runtime.BitSet, FOLLOW_additiveExpression_in_shiftExpression560: Antlr.Runtime.BitSet, FOLLOW_36_in_shiftExpression571: Antlr.Runtime.BitSet, FOLLOW_37_in_shiftExpression581: Antlr.Runtime.BitSet, FOLLOW_additiveExpression_in_shiftExpression593: Antlr.Runtime.BitSet, FOLLOW_multiplicativeExpression_in_additiveExpression625: Antlr.Runtime.BitSet, FOLLOW_38_in_additiveExpression636: Antlr.Runtime.BitSet, FOLLOW_39_in_additiveExpression646: Antlr.Runtime.BitSet, FOLLOW_multiplicativeExpression_in_additiveExpression658: Antlr.Runtime.BitSet, FOLLOW_unaryExpression_in_multiplicativeExpression690: Antlr.Runtime.BitSet, FOLLOW_40_in_multiplicativeExpression701: Antlr.Runtime.BitSet, FOLLOW_41_in_multiplicativeExpression711: Antlr.Runtime.BitSet, FOLLOW_42_in_multiplicativeExpression721: Antlr.Runtime.BitSet, FOLLOW_unaryExpression_in_multiplicativeExpression733: Antlr.Runtime.BitSet, FOLLOW_primaryExpression_in_unaryExpression760: Antlr.Runtime.BitSet, FOLLOW_set_in_unaryExpression771: Antlr.Runtime.BitSet, FOLLOW_primaryExpression_in_unaryExpression779: Antlr.Runtime.BitSet, FOLLOW_45_in_unaryExpression791: Antlr.Runtime.BitSet, FOLLOW_primaryExpression_in_unaryExpression794: Antlr.Runtime.BitSet, FOLLOW_39_in_unaryExpression805: Antlr.Runtime.BitSet, FOLLOW_primaryExpression_in_unaryExpression807: Antlr.Runtime.BitSet, FOLLOW_46_in_primaryExpression829: Antlr.Runtime.BitSet, FOLLOW_logicalExpression_in_primaryExpression831: Antlr.Runtime.BitSet, FOLLOW_47_in_primaryExpression833: Antlr.Runtime.BitSet, FOLLOW_value_in_primaryExpression843: Antlr.Runtime.BitSet, FOLLOW_identifier_in_primaryExpression851: Antlr.Runtime.BitSet, FOLLOW_arguments_in_primaryExpression856: Antlr.Runtime.BitSet, FOLLOW_INTEGER_in_value876: Antlr.Runtime.BitSet, FOLLOW_FLOAT_in_value884: Antlr.Runtime.BitSet, FOLLOW_STRING_in_value892: Antlr.Runtime.BitSet, FOLLOW_DATETIME_in_value901: Antlr.Runtime.BitSet, FOLLOW_TRUE_in_value908: Antlr.Runtime.BitSet, FOLLOW_FALSE_in_value916: Antlr.Runtime.BitSet, FOLLOW_ID_in_identifier934: Antlr.Runtime.BitSet, FOLLOW_NAME_in_identifier942: Antlr.Runtime.BitSet, FOLLOW_logicalExpression_in_expressionList966: Antlr.Runtime.BitSet, FOLLOW_48_in_expressionList973: Antlr.Runtime.BitSet, FOLLOW_logicalExpression_in_expressionList977: Antlr.Runtime.BitSet, FOLLOW_46_in_arguments1006: Antlr.Runtime.BitSet, FOLLOW_expressionList_in_arguments1010: Antlr.Runtime.BitSet, FOLLOW_47_in_arguments1017: Antlr.Runtime.BitSet, adaptor: Antlr.Runtime.Tree.ITreeAdaptor, <Errors>k__BackingField: System.Collections.Generic.List<System.String>, **kwargs):
        super().__init__(self, **kwargs)
		self.numberFormatInfo = numberFormatInfo
		self.FOLLOW_logicalExpression_in_ncalcExpression56 = FOLLOW_logicalExpression_in_ncalcExpression56
		self.FOLLOW_EOF_in_ncalcExpression58 = FOLLOW_EOF_in_ncalcExpression58
		self.FOLLOW_conditionalExpression_in_logicalExpression78 = FOLLOW_conditionalExpression_in_logicalExpression78
		self.FOLLOW_19_in_logicalExpression84 = FOLLOW_19_in_logicalExpression84
		self.FOLLOW_conditionalExpression_in_logicalExpression88 = FOLLOW_conditionalExpression_in_logicalExpression88
		self.FOLLOW_20_in_logicalExpression90 = FOLLOW_20_in_logicalExpression90
		self.FOLLOW_conditionalExpression_in_logicalExpression94 = FOLLOW_conditionalExpression_in_logicalExpression94
		self.FOLLOW_booleanAndExpression_in_conditionalExpression121 = FOLLOW_booleanAndExpression_in_conditionalExpression121
		self.FOLLOW_set_in_conditionalExpression130 = FOLLOW_set_in_conditionalExpression130
		self.FOLLOW_conditionalExpression_in_conditionalExpression146 = FOLLOW_conditionalExpression_in_conditionalExpression146
		self.FOLLOW_bitwiseOrExpression_in_booleanAndExpression180 = FOLLOW_bitwiseOrExpression_in_booleanAndExpression180
		self.FOLLOW_set_in_booleanAndExpression189 = FOLLOW_set_in_booleanAndExpression189
		self.FOLLOW_bitwiseOrExpression_in_booleanAndExpression205 = FOLLOW_bitwiseOrExpression_in_booleanAndExpression205
		self.FOLLOW_bitwiseXOrExpression_in_bitwiseOrExpression237 = FOLLOW_bitwiseXOrExpression_in_bitwiseOrExpression237
		self.FOLLOW_25_in_bitwiseOrExpression246 = FOLLOW_25_in_bitwiseOrExpression246
		self.FOLLOW_bitwiseOrExpression_in_bitwiseOrExpression256 = FOLLOW_bitwiseOrExpression_in_bitwiseOrExpression256
		self.FOLLOW_bitwiseAndExpression_in_bitwiseXOrExpression290 = FOLLOW_bitwiseAndExpression_in_bitwiseXOrExpression290
		self.FOLLOW_26_in_bitwiseXOrExpression299 = FOLLOW_26_in_bitwiseXOrExpression299
		self.FOLLOW_bitwiseAndExpression_in_bitwiseXOrExpression309 = FOLLOW_bitwiseAndExpression_in_bitwiseXOrExpression309
		self.FOLLOW_equalityExpression_in_bitwiseAndExpression341 = FOLLOW_equalityExpression_in_bitwiseAndExpression341
		self.FOLLOW_27_in_bitwiseAndExpression350 = FOLLOW_27_in_bitwiseAndExpression350
		self.FOLLOW_equalityExpression_in_bitwiseAndExpression360 = FOLLOW_equalityExpression_in_bitwiseAndExpression360
		self.FOLLOW_relationalExpression_in_equalityExpression394 = FOLLOW_relationalExpression_in_equalityExpression394
		self.FOLLOW_set_in_equalityExpression405 = FOLLOW_set_in_equalityExpression405
		self.FOLLOW_set_in_equalityExpression422 = FOLLOW_set_in_equalityExpression422
		self.FOLLOW_relationalExpression_in_equalityExpression441 = FOLLOW_relationalExpression_in_equalityExpression441
		self.FOLLOW_shiftExpression_in_relationalExpression474 = FOLLOW_shiftExpression_in_relationalExpression474
		self.FOLLOW_32_in_relationalExpression485 = FOLLOW_32_in_relationalExpression485
		self.FOLLOW_33_in_relationalExpression495 = FOLLOW_33_in_relationalExpression495
		self.FOLLOW_34_in_relationalExpression506 = FOLLOW_34_in_relationalExpression506
		self.FOLLOW_35_in_relationalExpression516 = FOLLOW_35_in_relationalExpression516
		self.FOLLOW_shiftExpression_in_relationalExpression528 = FOLLOW_shiftExpression_in_relationalExpression528
		self.FOLLOW_additiveExpression_in_shiftExpression560 = FOLLOW_additiveExpression_in_shiftExpression560
		self.FOLLOW_36_in_shiftExpression571 = FOLLOW_36_in_shiftExpression571
		self.FOLLOW_37_in_shiftExpression581 = FOLLOW_37_in_shiftExpression581
		self.FOLLOW_additiveExpression_in_shiftExpression593 = FOLLOW_additiveExpression_in_shiftExpression593
		self.FOLLOW_multiplicativeExpression_in_additiveExpression625 = FOLLOW_multiplicativeExpression_in_additiveExpression625
		self.FOLLOW_38_in_additiveExpression636 = FOLLOW_38_in_additiveExpression636
		self.FOLLOW_39_in_additiveExpression646 = FOLLOW_39_in_additiveExpression646
		self.FOLLOW_multiplicativeExpression_in_additiveExpression658 = FOLLOW_multiplicativeExpression_in_additiveExpression658
		self.FOLLOW_unaryExpression_in_multiplicativeExpression690 = FOLLOW_unaryExpression_in_multiplicativeExpression690
		self.FOLLOW_40_in_multiplicativeExpression701 = FOLLOW_40_in_multiplicativeExpression701
		self.FOLLOW_41_in_multiplicativeExpression711 = FOLLOW_41_in_multiplicativeExpression711
		self.FOLLOW_42_in_multiplicativeExpression721 = FOLLOW_42_in_multiplicativeExpression721
		self.FOLLOW_unaryExpression_in_multiplicativeExpression733 = FOLLOW_unaryExpression_in_multiplicativeExpression733
		self.FOLLOW_primaryExpression_in_unaryExpression760 = FOLLOW_primaryExpression_in_unaryExpression760
		self.FOLLOW_set_in_unaryExpression771 = FOLLOW_set_in_unaryExpression771
		self.FOLLOW_primaryExpression_in_unaryExpression779 = FOLLOW_primaryExpression_in_unaryExpression779
		self.FOLLOW_45_in_unaryExpression791 = FOLLOW_45_in_unaryExpression791
		self.FOLLOW_primaryExpression_in_unaryExpression794 = FOLLOW_primaryExpression_in_unaryExpression794
		self.FOLLOW_39_in_unaryExpression805 = FOLLOW_39_in_unaryExpression805
		self.FOLLOW_primaryExpression_in_unaryExpression807 = FOLLOW_primaryExpression_in_unaryExpression807
		self.FOLLOW_46_in_primaryExpression829 = FOLLOW_46_in_primaryExpression829
		self.FOLLOW_logicalExpression_in_primaryExpression831 = FOLLOW_logicalExpression_in_primaryExpression831
		self.FOLLOW_47_in_primaryExpression833 = FOLLOW_47_in_primaryExpression833
		self.FOLLOW_value_in_primaryExpression843 = FOLLOW_value_in_primaryExpression843
		self.FOLLOW_identifier_in_primaryExpression851 = FOLLOW_identifier_in_primaryExpression851
		self.FOLLOW_arguments_in_primaryExpression856 = FOLLOW_arguments_in_primaryExpression856
		self.FOLLOW_INTEGER_in_value876 = FOLLOW_INTEGER_in_value876
		self.FOLLOW_FLOAT_in_value884 = FOLLOW_FLOAT_in_value884
		self.FOLLOW_STRING_in_value892 = FOLLOW_STRING_in_value892
		self.FOLLOW_DATETIME_in_value901 = FOLLOW_DATETIME_in_value901
		self.FOLLOW_TRUE_in_value908 = FOLLOW_TRUE_in_value908
		self.FOLLOW_FALSE_in_value916 = FOLLOW_FALSE_in_value916
		self.FOLLOW_ID_in_identifier934 = FOLLOW_ID_in_identifier934
		self.FOLLOW_NAME_in_identifier942 = FOLLOW_NAME_in_identifier942
		self.FOLLOW_logicalExpression_in_expressionList966 = FOLLOW_logicalExpression_in_expressionList966
		self.FOLLOW_48_in_expressionList973 = FOLLOW_48_in_expressionList973
		self.FOLLOW_logicalExpression_in_expressionList977 = FOLLOW_logicalExpression_in_expressionList977
		self.FOLLOW_46_in_arguments1006 = FOLLOW_46_in_arguments1006
		self.FOLLOW_expressionList_in_arguments1010 = FOLLOW_expressionList_in_arguments1010
		self.FOLLOW_47_in_arguments1017 = FOLLOW_47_in_arguments1017
		self.adaptor = adaptor
		self.<Errors>k__BackingField = <Errors>k__BackingField


class additiveExpression_return:

    offsets = {'value': 32, 'tree': 40}    
    def __init__(self, value: NCalc.Domain.LogicalExpression, tree: Antlr.Runtime.Tree.CommonTree, **kwargs):
        super().__init__(self, **kwargs)
		self.value = value
		self.tree = tree


class arguments_return:

    offsets = {'value': 32, 'tree': 40}    
    def __init__(self, value: System.Collections.Generic.List<NCalc.Domain.LogicalExpression>, tree: Antlr.Runtime.Tree.CommonTree, **kwargs):
        super().__init__(self, **kwargs)
		self.value = value
		self.tree = tree


class bitwiseAndExpression_return:

    offsets = {'value': 32, 'tree': 40}    
    def __init__(self, value: NCalc.Domain.LogicalExpression, tree: Antlr.Runtime.Tree.CommonTree, **kwargs):
        super().__init__(self, **kwargs)
		self.value = value
		self.tree = tree


class bitwiseOrExpression_return:

    offsets = {'value': 32, 'tree': 40}    
    def __init__(self, value: NCalc.Domain.LogicalExpression, tree: Antlr.Runtime.Tree.CommonTree, **kwargs):
        super().__init__(self, **kwargs)
		self.value = value
		self.tree = tree


class bitwiseXOrExpression_return:

    offsets = {'value': 32, 'tree': 40}    
    def __init__(self, value: NCalc.Domain.LogicalExpression, tree: Antlr.Runtime.Tree.CommonTree, **kwargs):
        super().__init__(self, **kwargs)
		self.value = value
		self.tree = tree


class booleanAndExpression_return:

    offsets = {'value': 32, 'tree': 40}    
    def __init__(self, value: NCalc.Domain.LogicalExpression, tree: Antlr.Runtime.Tree.CommonTree, **kwargs):
        super().__init__(self, **kwargs)
		self.value = value
		self.tree = tree


class conditionalExpression_return:

    offsets = {'value': 32, 'tree': 40}    
    def __init__(self, value: NCalc.Domain.LogicalExpression, tree: Antlr.Runtime.Tree.CommonTree, **kwargs):
        super().__init__(self, **kwargs)
		self.value = value
		self.tree = tree


class equalityExpression_return:

    offsets = {'value': 32, 'tree': 40}    
    def __init__(self, value: NCalc.Domain.LogicalExpression, tree: Antlr.Runtime.Tree.CommonTree, **kwargs):
        super().__init__(self, **kwargs)
		self.value = value
		self.tree = tree


class expressionList_return:

    offsets = {'value': 32, 'tree': 40}    
    def __init__(self, value: System.Collections.Generic.List<NCalc.Domain.LogicalExpression>, tree: Antlr.Runtime.Tree.CommonTree, **kwargs):
        super().__init__(self, **kwargs)
		self.value = value
		self.tree = tree


class identifier_return:

    offsets = {'value': 32, 'tree': 40}    
    def __init__(self, value: NCalc.Domain.Identifier, tree: Antlr.Runtime.Tree.CommonTree, **kwargs):
        super().__init__(self, **kwargs)
		self.value = value
		self.tree = tree


class logicalExpression_return:

    offsets = {'value': 32, 'tree': 40}    
    def __init__(self, value: NCalc.Domain.LogicalExpression, tree: Antlr.Runtime.Tree.CommonTree, **kwargs):
        super().__init__(self, **kwargs)
		self.value = value
		self.tree = tree


class multiplicativeExpression_return:

    offsets = {'value': 32, 'tree': 40}    
    def __init__(self, value: NCalc.Domain.LogicalExpression, tree: Antlr.Runtime.Tree.CommonTree, **kwargs):
        super().__init__(self, **kwargs)
		self.value = value
		self.tree = tree


class ncalcExpression_return:

    offsets = {'value': 32, 'tree': 40}    
    def __init__(self, value: NCalc.Domain.LogicalExpression, tree: Antlr.Runtime.Tree.CommonTree, **kwargs):
        super().__init__(self, **kwargs)
		self.value = value
		self.tree = tree


class primaryExpression_return:

    offsets = {'value': 32, 'tree': 40}    
    def __init__(self, value: NCalc.Domain.LogicalExpression, tree: Antlr.Runtime.Tree.CommonTree, **kwargs):
        super().__init__(self, **kwargs)
		self.value = value
		self.tree = tree


class relationalExpression_return:

    offsets = {'value': 32, 'tree': 40}    
    def __init__(self, value: NCalc.Domain.LogicalExpression, tree: Antlr.Runtime.Tree.CommonTree, **kwargs):
        super().__init__(self, **kwargs)
		self.value = value
		self.tree = tree


class shiftExpression_return:

    offsets = {'value': 32, 'tree': 40}    
    def __init__(self, value: NCalc.Domain.LogicalExpression, tree: Antlr.Runtime.Tree.CommonTree, **kwargs):
        super().__init__(self, **kwargs)
		self.value = value
		self.tree = tree


class unaryExpression_return:

    offsets = {'value': 32, 'tree': 40}    
    def __init__(self, value: NCalc.Domain.LogicalExpression, tree: Antlr.Runtime.Tree.CommonTree, **kwargs):
        super().__init__(self, **kwargs)
		self.value = value
		self.tree = tree


class value_return:

    offsets = {'value': 32, 'tree': 40}    
    def __init__(self, value: NCalc.Domain.ValueExpression, tree: Antlr.Runtime.Tree.CommonTree, **kwargs):
        super().__init__(self, **kwargs)
		self.value = value
		self.tree = tree


class ANTLRStringStream:

    offsets = {'n': 24, 'p': 28, 'line': 32, 'charPositionInLine': 36, 'markDepth': 40, 'markers': 48, 'lastMarker': 56}    
    def __init__(self, n: System.Int32, p: System.Int32, line: System.Int32, charPositionInLine: System.Int32, markDepth: System.Int32, markers: System.Collections.IList, lastMarker: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.n = n
		self.p = p
		self.line = line
		self.charPositionInLine = charPositionInLine
		self.markDepth = markDepth
		self.markers = markers
		self.lastMarker = lastMarker


class BaseRecognizer:
	NEXT_TOKEN_RULE_NAME: System.String
    offsets = {'NEXT_TOKEN_RULE_NAME': 0, 'state': 16}    
    def __init__(self, NEXT_TOKEN_RULE_NAME: System.String, state: Antlr.Runtime.RecognizerSharedState, **kwargs):
        super().__init__(self, **kwargs)
		self.NEXT_TOKEN_RULE_NAME = NEXT_TOKEN_RULE_NAME
		self.state = state


class BitSet:
	MOD_MASK: System.Int32
    offsets = {'MOD_MASK': 0}    
    def __init__(self, MOD_MASK: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.MOD_MASK = MOD_MASK


class CharStreamState:

    offsets = {'p': 16, 'line': 20, 'charPositionInLine': 24}    
    def __init__(self, p: System.Int32, line: System.Int32, charPositionInLine: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.p = p
		self.line = line
		self.charPositionInLine = charPositionInLine


class CommonErrorNode:

    offsets = {'input': 56, 'start': 64, 'stop': 72, 'trappedException': 80}    
    def __init__(self, input: Antlr.Runtime.IIntStream, start: Antlr.Runtime.IToken, stop: Antlr.Runtime.IToken, trappedException: Antlr.Runtime.RecognitionException, **kwargs):
        super().__init__(self, **kwargs)
		self.input = input
		self.start = start
		self.stop = stop
		self.trappedException = trappedException


class CommonToken:

    offsets = {'type': 16, 'line': 20, 'charPositionInLine': 24, 'channel': 28, 'input': 32, 'text': 40, 'index': 48, 'start': 52, 'stop': 56}    
    def __init__(self, type: System.Int32, line: System.Int32, charPositionInLine: System.Int32, channel: System.Int32, input: Antlr.Runtime.ICharStream, text: System.String, index: System.Int32, start: System.Int32, stop: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.type = type
		self.line = line
		self.charPositionInLine = charPositionInLine
		self.channel = channel
		self.input = input
		self.text = text
		self.index = index
		self.start = start
		self.stop = stop


class CommonTokenStream:

    offsets = {'tokenSource': 16, 'tokens': 24, 'channelOverrideMap': 32, 'discardSet': 40, 'channel': 48, 'discardOffChannelTokens': 52, 'lastMarker': 56, 'p': 60}    
    def __init__(self, tokenSource: Antlr.Runtime.ITokenSource, tokens: System.Collections.IList, channelOverrideMap: System.Collections.IDictionary, discardSet: Antlr.Runtime.Collections.HashList, channel: System.Int32, discardOffChannelTokens: System.Boolean, lastMarker: System.Int32, p: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.tokenSource = tokenSource
		self.tokens = tokens
		self.channelOverrideMap = channelOverrideMap
		self.discardSet = discardSet
		self.channel = channel
		self.discardOffChannelTokens = discardOffChannelTokens
		self.lastMarker = lastMarker
		self.p = p


class DFA:

    offsets = {'decisionNumber': 72, 'specialStateTransitionHandler': 80, 'recognizer': 88}    
    def __init__(self, decisionNumber: System.Int32, specialStateTransitionHandler: Antlr.Runtime.DFA.SpecialStateTransitionHandler, recognizer: Antlr.Runtime.BaseRecognizer, **kwargs):
        super().__init__(self, **kwargs)
		self.decisionNumber = decisionNumber
		self.specialStateTransitionHandler = specialStateTransitionHandler
		self.recognizer = recognizer


class EarlyExitException:

    offsets = {'decisionNumber': 184}    
    def __init__(self, decisionNumber: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.decisionNumber = decisionNumber


class FailedPredicateException:

    offsets = {'ruleName': 184, 'predicateText': 192}    
    def __init__(self, ruleName: System.String, predicateText: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.ruleName = ruleName
		self.predicateText = predicateText


class ICharStream:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IIntStream:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IToken:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ITokenSource:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ITokenStream:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Lexer:

    offsets = {'input': 24}    
    def __init__(self, input: Antlr.Runtime.ICharStream, **kwargs):
        super().__init__(self, **kwargs)
		self.input = input


class MismatchedNotSetException:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class MismatchedRangeException:

    offsets = {'a': 184, 'b': 188}    
    def __init__(self, a: System.Int32, b: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.a = a
		self.b = b


class MismatchedSetException:

    offsets = {'expecting': 184}    
    def __init__(self, expecting: Antlr.Runtime.BitSet, **kwargs):
        super().__init__(self, **kwargs)
		self.expecting = expecting


class MismatchedTokenException:

    offsets = {'expecting': 184}    
    def __init__(self, expecting: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.expecting = expecting


class MismatchedTreeNodeException:

    offsets = {'expecting': 184}    
    def __init__(self, expecting: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.expecting = expecting


class MissingTokenException:

    offsets = {'inserted': 192}    
    def __init__(self, inserted: System.Object, **kwargs):
        super().__init__(self, **kwargs)
		self.inserted = inserted


class NoViableAltException:

    offsets = {'grammarDecisionDescription': 184, 'decisionNumber': 192, 'stateNumber': 196}    
    def __init__(self, grammarDecisionDescription: System.String, decisionNumber: System.Int32, stateNumber: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.grammarDecisionDescription = grammarDecisionDescription
		self.decisionNumber = decisionNumber
		self.stateNumber = stateNumber


class Parser:

    offsets = {'input': 24}    
    def __init__(self, input: Antlr.Runtime.ITokenStream, **kwargs):
        super().__init__(self, **kwargs)
		self.input = input


class ParserRuleReturnScope:

    offsets = {'start': 16, 'stop': 24}    
    def __init__(self, start: Antlr.Runtime.IToken, stop: Antlr.Runtime.IToken, **kwargs):
        super().__init__(self, **kwargs)
		self.start = start
		self.stop = stop


class RecognitionException:

    offsets = {'input': 136, 'index': 144, 'token': 152, 'node': 160, 'c': 168, 'line': 172, 'charPositionInLine': 176, 'approximateLineInfo': 180}    
    def __init__(self, input: Antlr.Runtime.IIntStream, index: System.Int32, token: Antlr.Runtime.IToken, node: System.Object, c: System.Int32, line: System.Int32, charPositionInLine: System.Int32, approximateLineInfo: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.input = input
		self.index = index
		self.token = token
		self.node = node
		self.c = c
		self.line = line
		self.charPositionInLine = charPositionInLine
		self.approximateLineInfo = approximateLineInfo


class RecognizerSharedState:

    offsets = {'followingStackPointer': 24, 'errorRecovery': 28, 'lastErrorIndex': 32, 'failed': 36, 'syntaxErrors': 40, 'backtracking': 44, 'token': 56, 'tokenStartCharIndex': 64, 'tokenStartLine': 68, 'tokenStartCharPositionInLine': 72, 'channel': 76, 'type': 80, 'text': 88}    
    def __init__(self, followingStackPointer: System.Int32, errorRecovery: System.Boolean, lastErrorIndex: System.Int32, failed: System.Boolean, syntaxErrors: System.Int32, backtracking: System.Int32, token: Antlr.Runtime.IToken, tokenStartCharIndex: System.Int32, tokenStartLine: System.Int32, tokenStartCharPositionInLine: System.Int32, channel: System.Int32, type: System.Int32, text: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.followingStackPointer = followingStackPointer
		self.errorRecovery = errorRecovery
		self.lastErrorIndex = lastErrorIndex
		self.failed = failed
		self.syntaxErrors = syntaxErrors
		self.backtracking = backtracking
		self.token = token
		self.tokenStartCharIndex = tokenStartCharIndex
		self.tokenStartLine = tokenStartLine
		self.tokenStartCharPositionInLine = tokenStartCharPositionInLine
		self.channel = channel
		self.type = type
		self.text = text


class RuleReturnScope:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Token:
	MIN_TOKEN_TYPE: System.Int32
    offsets = {'MIN_TOKEN_TYPE': 0, 'EOF': 4, 'EOF_TOKEN': 8, 'INVALID_TOKEN': 16, 'SKIP_TOKEN': 24}    
    def __init__(self, MIN_TOKEN_TYPE: System.Int32, EOF: System.Int32, EOF_TOKEN: Antlr.Runtime.IToken, INVALID_TOKEN: Antlr.Runtime.IToken, SKIP_TOKEN: Antlr.Runtime.IToken, **kwargs):
        super().__init__(self, **kwargs)
		self.MIN_TOKEN_TYPE = MIN_TOKEN_TYPE
		self.EOF = EOF
		self.EOF_TOKEN = EOF_TOKEN
		self.INVALID_TOKEN = INVALID_TOKEN
		self.SKIP_TOKEN = SKIP_TOKEN


class UnwantedTokenException:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class HashList:

    offsets = {'_dictionary': 16, '_insertionOrderList': 24, '_version': 32}    
    def __init__(self, _dictionary: System.Collections.Hashtable, _insertionOrderList: System.Collections.Generic.List<System.Object>, _version: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self._dictionary = _dictionary
		self._insertionOrderList = _insertionOrderList
		self._version = _version


class BaseTree:

    offsets = {'children': 16}    
    def __init__(self, children: System.Collections.IList, **kwargs):
        super().__init__(self, **kwargs)
		self.children = children


class BaseTreeAdaptor:

    offsets = {'uniqueNodeID': 16}    
    def __init__(self, uniqueNodeID: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.uniqueNodeID = uniqueNodeID


class CommonTree:

    offsets = {'startIndex': 24, 'stopIndex': 28, 'token': 32, 'parent': 40, 'childIndex': 48}    
    def __init__(self, startIndex: System.Int32, stopIndex: System.Int32, token: Antlr.Runtime.IToken, parent: Antlr.Runtime.Tree.CommonTree, childIndex: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.startIndex = startIndex
		self.stopIndex = stopIndex
		self.token = token
		self.parent = parent
		self.childIndex = childIndex


class CommonTreeAdaptor:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ITree:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ITreeAdaptor:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ITreeNodeStream:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class EvaluateFunctionHandler:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class EvaluateOptions:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class EvaluateParameterHandler:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class EvaluationException:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Expression:
	_cacheEnabled: System.Boolean
    offsets = {'_cacheEnabled': 0, '_compiledExpressions': 8, 'Rwl': 16, 'OriginalExpression': 16, 'ParameterEnumerators': 24, 'ParametersBackup': 32, 'EvaluateFunction': 40, 'EvaluateParameter': 48, '_parameters': 56, '<Options>k__BackingField': 64, '<Error>k__BackingField': 72, '<ParsedExpression>k__BackingField': 80}    
    def __init__(self, _cacheEnabled: System.Boolean, _compiledExpressions: System.Collections.Generic.Dictionary<System.String,System.WeakReference>, Rwl: System.Threading.ReaderWriterLock, OriginalExpression: System.String, ParameterEnumerators: System.Collections.Generic.Dictionary<System.String,System.Collections.IEnumerator>, ParametersBackup: System.Collections.Generic.Dictionary<System.String,System.Object>, EvaluateFunction: NCalc.EvaluateFunctionHandler, EvaluateParameter: NCalc.EvaluateParameterHandler, _parameters: System.Collections.Generic.Dictionary<System.String,System.Object>, <Options>k__BackingField: NCalc.EvaluateOptions, <Error>k__BackingField: System.String, <ParsedExpression>k__BackingField: NCalc.Domain.LogicalExpression, **kwargs):
        super().__init__(self, **kwargs)
		self._cacheEnabled = _cacheEnabled
		self._compiledExpressions = _compiledExpressions
		self.Rwl = Rwl
		self.OriginalExpression = OriginalExpression
		self.ParameterEnumerators = ParameterEnumerators
		self.ParametersBackup = ParametersBackup
		self.EvaluateFunction = EvaluateFunction
		self.EvaluateParameter = EvaluateParameter
		self._parameters = _parameters
		self.<Options>k__BackingField = <Options>k__BackingField
		self.<Error>k__BackingField = <Error>k__BackingField
		self.<ParsedExpression>k__BackingField = <ParsedExpression>k__BackingField


class FunctionArgs:

    offsets = {'_result': 16, '<HasResult>k__BackingField': 32}    
    def __init__(self, _result: System.Object, <HasResult>k__BackingField: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self._result = _result
		self.<HasResult>k__BackingField = <HasResult>k__BackingField


class Numbers:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class ParameterArgs:

    offsets = {'_result': 16, '<HasResult>k__BackingField': 24}    
    def __init__(self, _result: System.Object, <HasResult>k__BackingField: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self._result = _result
		self.<HasResult>k__BackingField = <HasResult>k__BackingField


class BinaryExpression:

    offsets = {'<LeftExpression>k__BackingField': 16, '<RightExpression>k__BackingField': 24, '<Type>k__BackingField': 32}    
    def __init__(self, <LeftExpression>k__BackingField: NCalc.Domain.LogicalExpression, <RightExpression>k__BackingField: NCalc.Domain.LogicalExpression, <Type>k__BackingField: NCalc.Domain.BinaryExpressionType, **kwargs):
        super().__init__(self, **kwargs)
		self.<LeftExpression>k__BackingField = <LeftExpression>k__BackingField
		self.<RightExpression>k__BackingField = <RightExpression>k__BackingField
		self.<Type>k__BackingField = <Type>k__BackingField


class BinaryExpressionType:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class EvaluationVisitor:

    offsets = {'_options': 16, 'EvaluateFunction': 24, 'EvaluateParameter': 32, '<Result>k__BackingField': 40, '<Parameters>k__BackingField': 48}    
    def __init__(self, _options: NCalc.EvaluateOptions, EvaluateFunction: NCalc.EvaluateFunctionHandler, EvaluateParameter: NCalc.EvaluateParameterHandler, <Result>k__BackingField: System.Object, <Parameters>k__BackingField: System.Collections.Generic.Dictionary<System.String,System.Object>, **kwargs):
        super().__init__(self, **kwargs)
		self._options = _options
		self.EvaluateFunction = EvaluateFunction
		self.EvaluateParameter = EvaluateParameter
		self.<Result>k__BackingField = <Result>k__BackingField
		self.<Parameters>k__BackingField = <Parameters>k__BackingField


class Function:

    offsets = {'<Identifier>k__BackingField': 16}    
    def __init__(self, <Identifier>k__BackingField: NCalc.Domain.Identifier, **kwargs):
        super().__init__(self, **kwargs)
		self.<Identifier>k__BackingField = <Identifier>k__BackingField


class Identifier:

    offsets = {'<Name>k__BackingField': 16}    
    def __init__(self, <Name>k__BackingField: System.String, **kwargs):
        super().__init__(self, **kwargs)
		self.<Name>k__BackingField = <Name>k__BackingField


class LogicalExpression:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class LogicalExpressionVisitor:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class SerializationVisitor:

    offsets = {'_numberFormatInfo': 16, '<Result>k__BackingField': 24}    
    def __init__(self, _numberFormatInfo: System.Globalization.NumberFormatInfo, <Result>k__BackingField: System.Text.StringBuilder, **kwargs):
        super().__init__(self, **kwargs)
		self._numberFormatInfo = _numberFormatInfo
		self.<Result>k__BackingField = <Result>k__BackingField


class TernaryExpression:

    offsets = {'<LeftExpression>k__BackingField': 16, '<MiddleExpression>k__BackingField': 24, '<RightExpression>k__BackingField': 32}    
    def __init__(self, <LeftExpression>k__BackingField: NCalc.Domain.LogicalExpression, <MiddleExpression>k__BackingField: NCalc.Domain.LogicalExpression, <RightExpression>k__BackingField: NCalc.Domain.LogicalExpression, **kwargs):
        super().__init__(self, **kwargs)
		self.<LeftExpression>k__BackingField = <LeftExpression>k__BackingField
		self.<MiddleExpression>k__BackingField = <MiddleExpression>k__BackingField
		self.<RightExpression>k__BackingField = <RightExpression>k__BackingField


class UnaryExpression:

    offsets = {'<Expression>k__BackingField': 16, '<Type>k__BackingField': 24}    
    def __init__(self, <Expression>k__BackingField: NCalc.Domain.LogicalExpression, <Type>k__BackingField: NCalc.Domain.UnaryExpressionType, **kwargs):
        super().__init__(self, **kwargs)
		self.<Expression>k__BackingField = <Expression>k__BackingField
		self.<Type>k__BackingField = <Type>k__BackingField


class UnaryExpressionType:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__


class ValueExpression:

    offsets = {'<Value>k__BackingField': 16, '<Type>k__BackingField': 24}    
    def __init__(self, <Value>k__BackingField: System.Object, <Type>k__BackingField: NCalc.Domain.ValueType, **kwargs):
        super().__init__(self, **kwargs)
		self.<Value>k__BackingField = <Value>k__BackingField
		self.<Type>k__BackingField = <Type>k__BackingField


class ValueType:

    offsets = {'value__': 16}    
    def __init__(self, value__: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.value__ = value__
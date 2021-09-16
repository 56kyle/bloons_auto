


class <Module>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class <PrivateImplementationDetails>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class __StaticArrayInitTypeSize=1024:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class __StaticArrayInitTypeSize=120:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class __StaticArrayInitTypeSize=256:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class SR:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Enumerator<T>:

    offsets = {'_set': 0, '_index': 0, '_version': 0, '_current': 0}    
    def __init__(self, _set: System.Collections.Generic.HashSet<T>, _index: System.Int32, _version: System.Int32, _current: T, **kwargs):
        super().__init__(self, **kwargs)
		self._set = _set
		self._index = _index
		self._version = _version
		self._current = _current


class Slot<T>:

    offsets = {'hashCode': 0, 'next': 0, 'value': 0}    
    def __init__(self, hashCode: System.Int32, next: System.Int32, value: T, **kwargs):
        super().__init__(self, **kwargs)
		self.hashCode = hashCode
		self.next = next
		self.value = value


class <>c__DisplayClass6_0<TSource>:

    offsets = {'predicate1': 0, 'predicate2': 0}    
    def __init__(self, predicate1: System.Func<TSource,System.Boolean>, predicate2: System.Func<TSource,System.Boolean>, **kwargs):
        super().__init__(self, **kwargs)
		self.predicate1 = predicate1
		self.predicate2 = predicate2


class <>c__DisplayClass7_0<TSource,TMiddle,TResult>:

    offsets = {'selector2': 0, 'selector1': 0}    
    def __init__(self, selector2: System.Func<TMiddle,TResult>, selector1: System.Func<TSource,TMiddle>, **kwargs):
        super().__init__(self, **kwargs)
		self.selector2 = selector2
		self.selector1 = selector1


class <CastIterator>d__99<TResult>:

    offsets = {'<>1__state': 0, '<>2__current': 0, '<>l__initialThreadId': 0, 'source': 0, '<>3__source': 0, '<>7__wrap1': 0}    
    def __init__(self, <>1__state: System.Int32, <>2__current: TResult, <>l__initialThreadId: System.Int32, source: System.Collections.IEnumerable, <>3__source: System.Collections.IEnumerable, <>7__wrap1: System.Collections.IEnumerator, **kwargs):
        super().__init__(self, **kwargs)
		self.<>1__state = <>1__state
		self.<>2__current = <>2__current
		self.<>l__initialThreadId = <>l__initialThreadId
		self.source = source
		self.<>3__source = <>3__source
		self.<>7__wrap1 = <>7__wrap1


class <ConcatIterator>d__59<TSource>:

    offsets = {'<>1__state': 0, '<>2__current': 0, '<>l__initialThreadId': 0, 'first': 0, '<>3__first': 0, 'second': 0, '<>3__second': 0, '<>7__wrap1': 0}    
    def __init__(self, <>1__state: System.Int32, <>2__current: TSource, <>l__initialThreadId: System.Int32, first: System.Collections.Generic.IEnumerable<TSource>, <>3__first: System.Collections.Generic.IEnumerable<TSource>, second: System.Collections.Generic.IEnumerable<TSource>, <>3__second: System.Collections.Generic.IEnumerable<TSource>, <>7__wrap1: System.Collections.Generic.IEnumerator<TSource>, **kwargs):
        super().__init__(self, **kwargs)
		self.<>1__state = <>1__state
		self.<>2__current = <>2__current
		self.<>l__initialThreadId = <>l__initialThreadId
		self.first = first
		self.<>3__first = <>3__first
		self.second = second
		self.<>3__second = <>3__second
		self.<>7__wrap1 = <>7__wrap1


class <DefaultIfEmptyIterator>d__95<TSource>:

    offsets = {'<>1__state': 0, '<>2__current': 0, '<>l__initialThreadId': 0, 'source': 0, '<>3__source': 0, '<e>5__1': 0, 'defaultValue': 0, '<>3__defaultValue': 0}    
    def __init__(self, <>1__state: System.Int32, <>2__current: TSource, <>l__initialThreadId: System.Int32, source: System.Collections.Generic.IEnumerable<TSource>, <>3__source: System.Collections.Generic.IEnumerable<TSource>, <e>5__1: System.Collections.Generic.IEnumerator<TSource>, defaultValue: TSource, <>3__defaultValue: TSource, **kwargs):
        super().__init__(self, **kwargs)
		self.<>1__state = <>1__state
		self.<>2__current = <>2__current
		self.<>l__initialThreadId = <>l__initialThreadId
		self.source = source
		self.<>3__source = <>3__source
		self.<e>5__1 = <e>5__1
		self.defaultValue = defaultValue
		self.<>3__defaultValue = <>3__defaultValue


class <DistinctIterator>d__68<TSource>:

    offsets = {'<>1__state': 0, '<>2__current': 0, '<>l__initialThreadId': 0, 'comparer': 0, '<>3__comparer': 0, 'source': 0, '<>3__source': 0, '<set>5__1': 0, '<>7__wrap1': 0}    
    def __init__(self, <>1__state: System.Int32, <>2__current: TSource, <>l__initialThreadId: System.Int32, comparer: System.Collections.Generic.IEqualityComparer<TSource>, <>3__comparer: System.Collections.Generic.IEqualityComparer<TSource>, source: System.Collections.Generic.IEnumerable<TSource>, <>3__source: System.Collections.Generic.IEnumerable<TSource>, <set>5__1: System.Linq.Set<TSource>, <>7__wrap1: System.Collections.Generic.IEnumerator<TSource>, **kwargs):
        super().__init__(self, **kwargs)
		self.<>1__state = <>1__state
		self.<>2__current = <>2__current
		self.<>l__initialThreadId = <>l__initialThreadId
		self.comparer = comparer
		self.<>3__comparer = <>3__comparer
		self.source = source
		self.<>3__source = <>3__source
		self.<set>5__1 = <set>5__1
		self.<>7__wrap1 = <>7__wrap1


class <ExceptIterator>d__77<TSource>:

    offsets = {'<>1__state': 0, '<>2__current': 0, '<>l__initialThreadId': 0, 'comparer': 0, '<>3__comparer': 0, 'second': 0, '<>3__second': 0, 'first': 0, '<>3__first': 0, '<set>5__1': 0, '<>7__wrap1': 0}    
    def __init__(self, <>1__state: System.Int32, <>2__current: TSource, <>l__initialThreadId: System.Int32, comparer: System.Collections.Generic.IEqualityComparer<TSource>, <>3__comparer: System.Collections.Generic.IEqualityComparer<TSource>, second: System.Collections.Generic.IEnumerable<TSource>, <>3__second: System.Collections.Generic.IEnumerable<TSource>, first: System.Collections.Generic.IEnumerable<TSource>, <>3__first: System.Collections.Generic.IEnumerable<TSource>, <set>5__1: System.Linq.Set<TSource>, <>7__wrap1: System.Collections.Generic.IEnumerator<TSource>, **kwargs):
        super().__init__(self, **kwargs)
		self.<>1__state = <>1__state
		self.<>2__current = <>2__current
		self.<>l__initialThreadId = <>l__initialThreadId
		self.comparer = comparer
		self.<>3__comparer = <>3__comparer
		self.second = second
		self.<>3__second = <>3__second
		self.first = first
		self.<>3__first = <>3__first
		self.<set>5__1 = <set>5__1
		self.<>7__wrap1 = <>7__wrap1


class <IntersectIterator>d__74<TSource>:

    offsets = {'<>1__state': 0, '<>2__current': 0, '<>l__initialThreadId': 0, 'comparer': 0, '<>3__comparer': 0, 'second': 0, '<>3__second': 0, 'first': 0, '<>3__first': 0, '<set>5__1': 0, '<>7__wrap1': 0}    
    def __init__(self, <>1__state: System.Int32, <>2__current: TSource, <>l__initialThreadId: System.Int32, comparer: System.Collections.Generic.IEqualityComparer<TSource>, <>3__comparer: System.Collections.Generic.IEqualityComparer<TSource>, second: System.Collections.Generic.IEnumerable<TSource>, <>3__second: System.Collections.Generic.IEnumerable<TSource>, first: System.Collections.Generic.IEnumerable<TSource>, <>3__first: System.Collections.Generic.IEnumerable<TSource>, <set>5__1: System.Linq.Set<TSource>, <>7__wrap1: System.Collections.Generic.IEnumerator<TSource>, **kwargs):
        super().__init__(self, **kwargs)
		self.<>1__state = <>1__state
		self.<>2__current = <>2__current
		self.<>l__initialThreadId = <>l__initialThreadId
		self.comparer = comparer
		self.<>3__comparer = <>3__comparer
		self.second = second
		self.<>3__second = <>3__second
		self.first = first
		self.<>3__first = <>3__first
		self.<set>5__1 = <set>5__1
		self.<>7__wrap1 = <>7__wrap1


class <JoinIterator>d__38<TOuter,TInner,TKey,TResult>:

    offsets = {'<>1__state': 0, '<>2__current': 0, '<>l__initialThreadId': 0, 'inner': 0, '<>3__inner': 0, 'innerKeySelector': 0, '<>3__innerKeySelector': 0, 'comparer': 0, '<>3__comparer': 0, 'outer': 0, '<>3__outer': 0, '<lookup>5__1': 0, 'outerKeySelector': 0, '<>3__outerKeySelector': 0, 'resultSelector': 0, '<>3__resultSelector': 0, '<item>5__2': 0, '<g>5__3': 0, '<i>5__4': 0, '<>7__wrap1': 0}    
    def __init__(self, <>1__state: System.Int32, <>2__current: TResult, <>l__initialThreadId: System.Int32, inner: System.Collections.Generic.IEnumerable<TInner>, <>3__inner: System.Collections.Generic.IEnumerable<TInner>, innerKeySelector: System.Func<TInner,TKey>, <>3__innerKeySelector: System.Func<TInner,TKey>, comparer: System.Collections.Generic.IEqualityComparer<TKey>, <>3__comparer: System.Collections.Generic.IEqualityComparer<TKey>, outer: System.Collections.Generic.IEnumerable<TOuter>, <>3__outer: System.Collections.Generic.IEnumerable<TOuter>, <lookup>5__1: System.Linq.Lookup<TKey,TInner>, outerKeySelector: System.Func<TOuter,TKey>, <>3__outerKeySelector: System.Func<TOuter,TKey>, resultSelector: System.Func<TOuter,TInner,TResult>, <>3__resultSelector: System.Func<TOuter,TInner,TResult>, <item>5__2: TOuter, <g>5__3: System.Linq.Lookup.Grouping<TKey,TInner>, <i>5__4: System.Int32, <>7__wrap1: System.Collections.Generic.IEnumerator<TOuter>, **kwargs):
        super().__init__(self, **kwargs)
		self.<>1__state = <>1__state
		self.<>2__current = <>2__current
		self.<>l__initialThreadId = <>l__initialThreadId
		self.inner = inner
		self.<>3__inner = <>3__inner
		self.innerKeySelector = innerKeySelector
		self.<>3__innerKeySelector = <>3__innerKeySelector
		self.comparer = comparer
		self.<>3__comparer = <>3__comparer
		self.outer = outer
		self.<>3__outer = <>3__outer
		self.<lookup>5__1 = <lookup>5__1
		self.outerKeySelector = outerKeySelector
		self.<>3__outerKeySelector = <>3__outerKeySelector
		self.resultSelector = resultSelector
		self.<>3__resultSelector = <>3__resultSelector
		self.<item>5__2 = <item>5__2
		self.<g>5__3 = <g>5__3
		self.<i>5__4 = <i>5__4
		self.<>7__wrap1 = <>7__wrap1


class <OfTypeIterator>d__97<TResult>:

    offsets = {'<>1__state': 0, '<>2__current': 0, '<>l__initialThreadId': 0, 'source': 0, '<>3__source': 0, '<>7__wrap1': 0}    
    def __init__(self, <>1__state: System.Int32, <>2__current: TResult, <>l__initialThreadId: System.Int32, source: System.Collections.IEnumerable, <>3__source: System.Collections.IEnumerable, <>7__wrap1: System.Collections.IEnumerator, **kwargs):
        super().__init__(self, **kwargs)
		self.<>1__state = <>1__state
		self.<>2__current = <>2__current
		self.<>l__initialThreadId = <>l__initialThreadId
		self.source = source
		self.<>3__source = <>3__source
		self.<>7__wrap1 = <>7__wrap1


class <RangeIterator>d__115:

    offsets = {'<>1__state': 16, '<>2__current': 20, '<>l__initialThreadId': 24, 'start': 28, '<>3__start': 32, '<i>5__1': 36, 'count': 40, '<>3__count': 44}    
    def __init__(self, <>1__state: System.Int32, <>2__current: System.Int32, <>l__initialThreadId: System.Int32, start: System.Int32, <>3__start: System.Int32, <i>5__1: System.Int32, count: System.Int32, <>3__count: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.<>1__state = <>1__state
		self.<>2__current = <>2__current
		self.<>l__initialThreadId = <>l__initialThreadId
		self.start = start
		self.<>3__start = <>3__start
		self.<i>5__1 = <i>5__1
		self.count = count
		self.<>3__count = <>3__count


class <RepeatIterator>d__117<TResult>:

    offsets = {'<>1__state': 0, '<>2__current': 0, '<>l__initialThreadId': 0, 'element': 0, '<>3__element': 0, '<i>5__1': 0, 'count': 0, '<>3__count': 0}    
    def __init__(self, <>1__state: System.Int32, <>2__current: TResult, <>l__initialThreadId: System.Int32, element: TResult, <>3__element: TResult, <i>5__1: System.Int32, count: System.Int32, <>3__count: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.<>1__state = <>1__state
		self.<>2__current = <>2__current
		self.<>l__initialThreadId = <>l__initialThreadId
		self.element = element
		self.<>3__element = <>3__element
		self.<i>5__1 = <i>5__1
		self.count = count
		self.<>3__count = <>3__count


class <ReverseIterator>d__79<TSource>:

    offsets = {'<>1__state': 0, '<>2__current': 0, '<>l__initialThreadId': 0, 'source': 0, '<>3__source': 0, '<buffer>5__1': 0, '<i>5__2': 0}    
    def __init__(self, <>1__state: System.Int32, <>2__current: TSource, <>l__initialThreadId: System.Int32, source: System.Collections.Generic.IEnumerable<TSource>, <>3__source: System.Collections.Generic.IEnumerable<TSource>, <buffer>5__1: System.Linq.Buffer<TSource>, <i>5__2: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.<>1__state = <>1__state
		self.<>2__current = <>2__current
		self.<>l__initialThreadId = <>l__initialThreadId
		self.source = source
		self.<>3__source = <>3__source
		self.<buffer>5__1 = <buffer>5__1
		self.<i>5__2 = <i>5__2


class <SelectManyIterator>d__17<TSource,TResult>:

    offsets = {'<>1__state': 0, '<>2__current': 0, '<>l__initialThreadId': 0, 'source': 0, '<>3__source': 0, 'selector': 0, '<>3__selector': 0, '<>7__wrap1': 0, '<>7__wrap2': 0}    
    def __init__(self, <>1__state: System.Int32, <>2__current: TResult, <>l__initialThreadId: System.Int32, source: System.Collections.Generic.IEnumerable<TSource>, <>3__source: System.Collections.Generic.IEnumerable<TSource>, selector: System.Func<TSource,System.Collections.Generic.IEnumerable<TResult>>, <>3__selector: System.Func<TSource,System.Collections.Generic.IEnumerable<TResult>>, <>7__wrap1: System.Collections.Generic.IEnumerator<TSource>, <>7__wrap2: System.Collections.Generic.IEnumerator<TResult>, **kwargs):
        super().__init__(self, **kwargs)
		self.<>1__state = <>1__state
		self.<>2__current = <>2__current
		self.<>l__initialThreadId = <>l__initialThreadId
		self.source = source
		self.<>3__source = <>3__source
		self.selector = selector
		self.<>3__selector = <>3__selector
		self.<>7__wrap1 = <>7__wrap1
		self.<>7__wrap2 = <>7__wrap2


class <SelectManyIterator>d__23<TSource,TCollection,TResult>:

    offsets = {'<>1__state': 0, '<>2__current': 0, '<>l__initialThreadId': 0, 'source': 0, '<>3__source': 0, 'collectionSelector': 0, '<>3__collectionSelector': 0, 'resultSelector': 0, '<>3__resultSelector': 0, '<element>5__1': 0, '<>7__wrap1': 0, '<>7__wrap2': 0}    
    def __init__(self, <>1__state: System.Int32, <>2__current: TResult, <>l__initialThreadId: System.Int32, source: System.Collections.Generic.IEnumerable<TSource>, <>3__source: System.Collections.Generic.IEnumerable<TSource>, collectionSelector: System.Func<TSource,System.Collections.Generic.IEnumerable<TCollection>>, <>3__collectionSelector: System.Func<TSource,System.Collections.Generic.IEnumerable<TCollection>>, resultSelector: System.Func<TSource,TCollection,TResult>, <>3__resultSelector: System.Func<TSource,TCollection,TResult>, <element>5__1: TSource, <>7__wrap1: System.Collections.Generic.IEnumerator<TSource>, <>7__wrap2: System.Collections.Generic.IEnumerator<TCollection>, **kwargs):
        super().__init__(self, **kwargs)
		self.<>1__state = <>1__state
		self.<>2__current = <>2__current
		self.<>l__initialThreadId = <>l__initialThreadId
		self.source = source
		self.<>3__source = <>3__source
		self.collectionSelector = collectionSelector
		self.<>3__collectionSelector = <>3__collectionSelector
		self.resultSelector = resultSelector
		self.<>3__resultSelector = <>3__resultSelector
		self.<element>5__1 = <element>5__1
		self.<>7__wrap1 = <>7__wrap1
		self.<>7__wrap2 = <>7__wrap2


class <TakeIterator>d__25<TSource>:

    offsets = {'<>1__state': 0, '<>2__current': 0, '<>l__initialThreadId': 0, 'count': 0, '<>3__count': 0, 'source': 0, '<>3__source': 0, '<>7__wrap1': 0}    
    def __init__(self, <>1__state: System.Int32, <>2__current: TSource, <>l__initialThreadId: System.Int32, count: System.Int32, <>3__count: System.Int32, source: System.Collections.Generic.IEnumerable<TSource>, <>3__source: System.Collections.Generic.IEnumerable<TSource>, <>7__wrap1: System.Collections.Generic.IEnumerator<TSource>, **kwargs):
        super().__init__(self, **kwargs)
		self.<>1__state = <>1__state
		self.<>2__current = <>2__current
		self.<>l__initialThreadId = <>l__initialThreadId
		self.count = count
		self.<>3__count = <>3__count
		self.source = source
		self.<>3__source = <>3__source
		self.<>7__wrap1 = <>7__wrap1


class <UnionIterator>d__71<TSource>:

    offsets = {'<>1__state': 0, '<>2__current': 0, '<>l__initialThreadId': 0, 'comparer': 0, '<>3__comparer': 0, 'first': 0, '<>3__first': 0, '<set>5__1': 0, 'second': 0, '<>3__second': 0, '<>7__wrap1': 0}    
    def __init__(self, <>1__state: System.Int32, <>2__current: TSource, <>l__initialThreadId: System.Int32, comparer: System.Collections.Generic.IEqualityComparer<TSource>, <>3__comparer: System.Collections.Generic.IEqualityComparer<TSource>, first: System.Collections.Generic.IEnumerable<TSource>, <>3__first: System.Collections.Generic.IEnumerable<TSource>, <set>5__1: System.Linq.Set<TSource>, second: System.Collections.Generic.IEnumerable<TSource>, <>3__second: System.Collections.Generic.IEnumerable<TSource>, <>7__wrap1: System.Collections.Generic.IEnumerator<TSource>, **kwargs):
        super().__init__(self, **kwargs)
		self.<>1__state = <>1__state
		self.<>2__current = <>2__current
		self.<>l__initialThreadId = <>l__initialThreadId
		self.comparer = comparer
		self.<>3__comparer = <>3__comparer
		self.first = first
		self.<>3__first = <>3__first
		self.<set>5__1 = <set>5__1
		self.second = second
		self.<>3__second = <>3__second
		self.<>7__wrap1 = <>7__wrap1


class Iterator<TSource>:

    offsets = {'threadId': 0, 'state': 0, 'current': 0}    
    def __init__(self, threadId: System.Int32, state: System.Int32, current: TSource, **kwargs):
        super().__init__(self, **kwargs)
		self.threadId = threadId
		self.state = state
		self.current = current


class WhereArrayIterator<TSource>:

    offsets = {'predicate': 0, 'index': 0}    
    def __init__(self, predicate: System.Func<TSource,System.Boolean>, index: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.predicate = predicate
		self.index = index


class WhereEnumerableIterator<TSource>:

    offsets = {'source': 0, 'predicate': 0, 'enumerator': 0}    
    def __init__(self, source: System.Collections.Generic.IEnumerable<TSource>, predicate: System.Func<TSource,System.Boolean>, enumerator: System.Collections.Generic.IEnumerator<TSource>, **kwargs):
        super().__init__(self, **kwargs)
		self.source = source
		self.predicate = predicate
		self.enumerator = enumerator


class WhereListIterator<TSource>:

    offsets = {'source': 0, 'predicate': 0, 'enumerator': 0}    
    def __init__(self, source: System.Collections.Generic.List<TSource>, predicate: System.Func<TSource,System.Boolean>, enumerator: System.Collections.Generic.List.Enumerator<TSource>, **kwargs):
        super().__init__(self, **kwargs)
		self.source = source
		self.predicate = predicate
		self.enumerator = enumerator


class WhereSelectArrayIterator<TSource,TResult>:

    offsets = {'predicate': 0, 'selector': 0, 'index': 0}    
    def __init__(self, predicate: System.Func<TSource,System.Boolean>, selector: System.Func<TSource,TResult>, index: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.predicate = predicate
		self.selector = selector
		self.index = index


class WhereSelectEnumerableIterator<TSource,TResult>:

    offsets = {'source': 0, 'predicate': 0, 'selector': 0, 'enumerator': 0}    
    def __init__(self, source: System.Collections.Generic.IEnumerable<TSource>, predicate: System.Func<TSource,System.Boolean>, selector: System.Func<TSource,TResult>, enumerator: System.Collections.Generic.IEnumerator<TSource>, **kwargs):
        super().__init__(self, **kwargs)
		self.source = source
		self.predicate = predicate
		self.selector = selector
		self.enumerator = enumerator


class WhereSelectListIterator<TSource,TResult>:

    offsets = {'source': 0, 'predicate': 0, 'selector': 0, 'enumerator': 0}    
    def __init__(self, source: System.Collections.Generic.List<TSource>, predicate: System.Func<TSource,System.Boolean>, selector: System.Func<TSource,TResult>, enumerator: System.Collections.Generic.List.Enumerator<TSource>, **kwargs):
        super().__init__(self, **kwargs)
		self.source = source
		self.predicate = predicate
		self.selector = selector
		self.enumerator = enumerator


class <>c<TElement>:
	<>9: System.Linq.IdentityFunction.<>c<TElement>
    offsets = {'<>9': 0, '<>9__1_0': 0}    
    def __init__(self, <>9: System.Linq.IdentityFunction.<>c<TElement>, <>9__1_0: System.Func<TElement,TElement>, **kwargs):
        super().__init__(self, **kwargs)
		self.<>9 = <>9
		self.<>9__1_0 = <>9__1_0


class <GetEnumerator>d__12<TKey,TElement>:

    offsets = {'<>1__state': 0, '<>2__current': 0, '<>4__this': 0, '<g>5__1': 0}    
    def __init__(self, <>1__state: System.Int32, <>2__current: System.Linq.IGrouping<TKey,TElement>, <>4__this: System.Linq.Lookup<TKey,TElement>, <g>5__1: System.Linq.Lookup.Grouping<TKey,TElement>, **kwargs):
        super().__init__(self, **kwargs)
		self.<>1__state = <>1__state
		self.<>2__current = <>2__current
		self.<>4__this = <>4__this
		self.<g>5__1 = <g>5__1


class <GetEnumerator>d__7<TKey,TElement>:

    offsets = {'<>1__state': 0, '<>2__current': 0, '<>4__this': 0, '<i>5__1': 0}    
    def __init__(self, <>1__state: System.Int32, <>2__current: TElement, <>4__this: System.Linq.Lookup.Grouping<TKey,TElement>, <i>5__1: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.<>1__state = <>1__state
		self.<>2__current = <>2__current
		self.<>4__this = <>4__this
		self.<i>5__1 = <i>5__1


class Grouping<TKey,TElement>:

    offsets = {'key': 0, 'hashCode': 0, 'count': 0, 'hashNext': 0, 'next': 0}    
    def __init__(self, key: TKey, hashCode: System.Int32, count: System.Int32, hashNext: System.Linq.Lookup.Grouping<TKey,TElement>, next: System.Linq.Lookup.Grouping<TKey,TElement>, **kwargs):
        super().__init__(self, **kwargs)
		self.key = key
		self.hashCode = hashCode
		self.count = count
		self.hashNext = hashNext
		self.next = next


class <GetEnumerator>d__1<TElement>:

    offsets = {'<>1__state': 0, '<>2__current': 0, '<>4__this': 0, '<buffer>5__1': 0, '<i>5__3': 0}    
    def __init__(self, <>1__state: System.Int32, <>2__current: TElement, <>4__this: System.Linq.OrderedEnumerable<TElement>, <buffer>5__1: System.Linq.Buffer<TElement>, <i>5__3: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.<>1__state = <>1__state
		self.<>2__current = <>2__current
		self.<>4__this = <>4__this
		self.<buffer>5__1 = <buffer>5__1
		self.<i>5__3 = <i>5__3


class Slot<TElement>:

    offsets = {'hashCode': 0, 'value': 0, 'next': 0}    
    def __init__(self, hashCode: System.Int32, value: TElement, next: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.hashCode = hashCode
		self.value = value
		self.next = next


class BitHelper:

    offsets = {'_length': 16, '_useStackAlloc': 40}    
    def __init__(self, _length: System.Int32, _useStackAlloc: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self._length = _length
		self._useStackAlloc = _useStackAlloc


class HashSet<T>:

    offsets = {'_count': 0, '_lastIndex': 0, '_freeList': 0, '_comparer': 0, '_version': 0, '_siInfo': 0}    
    def __init__(self, _count: System.Int32, _lastIndex: System.Int32, _freeList: System.Int32, _comparer: System.Collections.Generic.IEqualityComparer<T>, _version: System.Int32, _siInfo: System.Runtime.Serialization.SerializationInfo, **kwargs):
        super().__init__(self, **kwargs)
		self._count = _count
		self._lastIndex = _lastIndex
		self._freeList = _freeList
		self._comparer = _comparer
		self._version = _version
		self._siInfo = _siInfo


class ICollectionDebugView<T>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Buffer<TElement>:

    offsets = {'count': 0}    
    def __init__(self, count: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.count = count


class EmptyEnumerable<TElement>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Enumerable:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class EnumerableSorter<TElement,TKey>:

    offsets = {'keySelector': 0, 'comparer': 0, 'descending': 0, 'next': 0}    
    def __init__(self, keySelector: System.Func<TElement,TKey>, comparer: System.Collections.Generic.IComparer<TKey>, descending: System.Boolean, next: System.Linq.EnumerableSorter<TElement>, **kwargs):
        super().__init__(self, **kwargs)
		self.keySelector = keySelector
		self.comparer = comparer
		self.descending = descending
		self.next = next


class EnumerableSorter<TElement>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Error:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class GroupedEnumerable<TSource,TKey,TElement>:

    offsets = {'source': 0, 'keySelector': 0, 'elementSelector': 0, 'comparer': 0}    
    def __init__(self, source: System.Collections.Generic.IEnumerable<TSource>, keySelector: System.Func<TSource,TKey>, elementSelector: System.Func<TSource,TElement>, comparer: System.Collections.Generic.IEqualityComparer<TKey>, **kwargs):
        super().__init__(self, **kwargs)
		self.source = source
		self.keySelector = keySelector
		self.elementSelector = elementSelector
		self.comparer = comparer


class IGrouping<TKey,TElement>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IOrderedEnumerable<TElement>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class IdentityFunction<TElement>:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class Lookup<TKey,TElement>:

    offsets = {'comparer': 0, 'lastGrouping': 0, 'count': 0}    
    def __init__(self, comparer: System.Collections.Generic.IEqualityComparer<TKey>, lastGrouping: System.Linq.Lookup.Grouping<TKey,TElement>, count: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.comparer = comparer
		self.lastGrouping = lastGrouping
		self.count = count


class OrderedEnumerable<TElement,TKey>:

    offsets = {'parent': 0, 'keySelector': 0, 'comparer': 0, 'descending': 0}    
    def __init__(self, parent: System.Linq.OrderedEnumerable<TElement>, keySelector: System.Func<TElement,TKey>, comparer: System.Collections.Generic.IComparer<TKey>, descending: System.Boolean, **kwargs):
        super().__init__(self, **kwargs)
		self.parent = parent
		self.keySelector = keySelector
		self.comparer = comparer
		self.descending = descending


class OrderedEnumerable<TElement>:

    offsets = {'source': 0}    
    def __init__(self, source: System.Collections.Generic.IEnumerable<TElement>, **kwargs):
        super().__init__(self, **kwargs)
		self.source = source


class Set<TElement>:

    offsets = {'count': 0, 'freeList': 0, 'comparer': 0}    
    def __init__(self, count: System.Int32, freeList: System.Int32, comparer: System.Collections.Generic.IEqualityComparer<TElement>, **kwargs):
        super().__init__(self, **kwargs)
		self.count = count
		self.freeList = freeList
		self.comparer = comparer


class AesCryptoServiceProvider:

    offsets = {}    
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)



class AesManaged:

    offsets = {'m_rijndael': 72}    
    def __init__(self, m_rijndael: System.Security.Cryptography.RijndaelManaged, **kwargs):
        super().__init__(self, **kwargs)
		self.m_rijndael = m_rijndael


class AesTransform:

    offsets = {'Nk': 96, 'Nr': 100}    
    def __init__(self, Nk: System.Int32, Nr: System.Int32, **kwargs):
        super().__init__(self, **kwargs)
		self.Nk = Nk
		self.Nr = Nr
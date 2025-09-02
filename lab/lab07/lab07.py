def naturals():
    """A generator function that yields the infinite sequence of natural
    numbers, starting at 1.

    >>> m = naturals()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    i = 1
    while True:
        yield i
        i += 1


def scale(it, multiplier):
    """Yield elements of the iterable it scaled by a number multiplier.

    >>> m = scale([1, 5, 2], 5)
    >>> type(m)
    <class 'generator'>
    >>> list(m)
    [5, 25, 10]

    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    "*** YOUR CODE HERE ***"
    # wrong answer: yield from [i*multiplier for i in it] (Timeout)
    yield from map(lambda i: i * multiplier, it)
    # 'yield from' + list comprehension: 
    # Eager Evaluation -> the generator will evaluate all elements in the list first then iterate over the list.
    # 'yield from' + iterator:
    # Lazy Evaluation -> the generator will yield a result right after the iterator yields a value, suitable for infinite iterables.

def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
    yield n
    if n != 1:
        if n % 2 == 0:
            yield from hailstone(n // 2)
        else:
            yield from hailstone(3 * n + 1)
    # a more concise version:
    # yield n
    # if n != 1:
    #     yield from hailstone(3*n + 1) if n%2 else hailstone(n//2)
    """
    There are also some questions and my solutions in *classes.py*.
    """
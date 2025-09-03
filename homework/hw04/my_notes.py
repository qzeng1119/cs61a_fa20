##########
# note 1 #
##########
def permutations(seq):
    """Generates all permutations of the given sequence. Each permutation is a
    list of the elements in SEQ in a different order. The permutations may be
    yielded in any order.

    >>> sorted(permutations([1, 2, 3])) # Returns a sorted list containing elements of the generator
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    >>> sorted(permutations("ab"))
    [['a', 'b'], ['b', 'a']]
    """
    # Make sure your base case works!
    # e.x. Try to figure out whether 'permutations([1])' works successfully 
    length, seq = len(seq), list(seq)
    if length == 1:
        yield seq
    else:  # This 'else' is very important! Because 'yield' is different from
           # 'return', 'yield' wouldn't make the procedure exit the function.
        for s in permutations(seq[1:]):
            for k in range(length):
                yield s[0:k] + seq[0:1] + s[k:]
    # In this generator function, if the procedure goes through the
    # 'if' clause, then it shouldn't go through the 'else' clause.
    # So do not forget the 'else:'.
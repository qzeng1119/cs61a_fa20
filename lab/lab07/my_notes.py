##########
# note 1 #
##########
"""Comparison between Instances of A Custom Class by Python:

By default, when comparing two instances of a custom class, for example, 'A' and 'B',
Python only judges whether 'A is B', namely comparing their address, instead of 
comparing their attributes one by one. So, if 'A' and 'B' are different objects, 
although the attributes of 'A' are equal to the corresponding ones of 'B', the 
value of the expression 'A == B' is still 'False', which makes the built-in function 
'remove' can not find the matched element.
"""


##########
# note 2 #
##########
"""List Slicing -> A Kind of Shallow Copy:

*list slicing* is a kind of shallow copy, each element from the new list has the
same address as the corresponding element from the old list.

example:
>>> a = [1, [0]]
>>> b = a[:]
>>> a[1] is b[1]
True
"""
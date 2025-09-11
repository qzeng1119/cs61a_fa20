##########
# note 1 #
##########
def insert(link, value, index):
    """Insert a value into a Link at the given index. Just mutate the Link passed in
    without returning anything.

    >>> link = Link(1, Link(2, Link(3)))
    >>> insert(link, 9001, 0)
    >>> print(link)
    <9001 1 2 3>
    >>> insert(link, 100, 2)
    >>> print(link)
    <9001 1 100 2 3>
    >>> insert(link, 4, 5)
    IndexError
    """
    # This is worth thinking twice.
    if index == 0 and link is not Link.empty:
        # We can't replace the line below with 'link = Link(value, link)', why? Figure out the reason by yourself.
        link.first, link.rest = value, Link(link.first, link.rest)
    elif link is Link.empty:
        raise IndexError
    else:
        insert(link.rest, value, index-1)
##########
# note 1 #
##########
"""
If the original function template only takes in one argument while you want to
keep track of more than one values during the recursion process, then write a
helper function in the body of the original function.
"""

def pingpong(n):
    """Return the nth element of the ping-pong sequence by using recursion.

    >>> pingpong(8)
    8
    >>> pingpong(22)
    -2
    >>> pingpong(82)
    0
    """
    def pingpong_helper(pingpong_value, index, direction):  # tail recursion
        """ A recursive helper function to calculate ping-pong value.
            direction is either 1 or -1
        """
        if index == n:
            return pingpong_value
        if index % 8 == 0 or num_eights(index) > 0:
            return pingpong_helper(pingpong_value - direction, index + 1, -direction)
        return pingpong_helper(pingpong_value + direction, index + 1, direction)
    return pingpong_helper(1, 1, 1)

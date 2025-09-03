##########
# note 1 #
##########
"""Difference between if-statement and if-function:
For if-function: before entering a function's body, it's operands all get evaluated.
"""

def with_if_statement():
    """
    >>> with_if_statement()
    Else-suite gets executed!
    """
    if cond():
        return true_func()
    else:
        return false_func()

def with_if_function():
    """
    >>> with_if_function()
    If-suite gets executed!
    Else-suite gets executed!
    """
    return if_function(cond(), true_func(), false_func())

def if_function(condition, true_result, false_result):
    if condition:
        return true_result
    else:
        return false_result

def cond():
    return False

def true_func():
    print('If-suite gets executed!')

def false_func():
    print('Else-suite gets executed!')
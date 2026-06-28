from link import *

def count_if(f, s):
    if s is Link.empty:
        return 0
    else:
        if f(s.first):
            return 1 + count_if(f, s.rest)
        else:
            return count_if(f, s.rest)

def contained_in(s):
    def f(s, x):
        if s is Link.empty:
            return False
        else:
            return s.first == x or f(s.rest, x)
    return lambda x: f(s, x)

def overlap(s, t):
    """For s and t with no repeats, count the numbers that appear in both.

    >>> a = Link(3, Link(4, Link(6, Link(7, Link(9, Link(10))))))
    >>> b = Link(1, Link(3, Link(5, Link(7, Link(8, Link(12))))))
    >>> overlap(a, b)  # 3 and 7
    2
    """
    return count_if(contained_in(t), s)


def of(us):
    def last(k):
        "The last k items of us"
        while k > 0:
            result.append(us.pop())
            k = k - 1
        return result
    return last
def surround(n, f):
    "n is the first and last item of f(2)"
    result = [n]
    result = f(2)
    result[0] = [n]
    return result.append(n) 

result = [1] 

from tree import *

def decorate(t):
    """Add a * child to each leaf of Tree t.
    """
    if t.is_leaf():
        t.branches.append(Tree('*'))
    else:
        for b in t.branches:
            decorate(b)

def chop_head(hydra, n):
    assert n > 0 and n <= hydra.label
    if hydra.is_leaf():
        hydra.label = 2
        hydra.branches = [Tree(1), Tree(1)]
    else:
        hydra.label += 1
    left, right = hydra.branches
    if n > left.label:
        chop_head(right, n-left.label)
    else:
        chop_head(left, n)

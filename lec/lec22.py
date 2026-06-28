class Link:
    """A linked list.

    >>> Link(1, Link(4, Link(1)))
    Link(1, Link(4, Link(1)))
    >>> Link(1, Link(4, Link(1, Link.empty)))
    Link(1, Link(4, Link(1)))
    >>> Link(1, Link(4, Link(1, 5)))
    Traceback (most recent call last):
        ...
    AssertionError
    >>> Link(1, Link(4, Link(1, Link(5))))
    Link(1, Link(4, Link(1, Link(5))))
    >>> s = Link(1, Link(4, Link(1, Link(5))))
    >>> t = s
    >>> Link(3, s)
    Link(3, Link(1, Link(4, Link(1, Link(5)))))
    >>> s
    Link(1, Link(4, Link(1, Link(5))))
    >>> s = Link(3, s)
    >>> s
    Link(3, Link(1, Link(4, Link(1, Link(5)))))
    >>> t
    Link(1, Link(4, Link(1, Link(5))))
    >>> s.rest is t
    True
    >>> s.append(2)
    Traceback (most recent call last):
        ...
    AttributeError: 'Link' object has no attribute 'append'
    >>> s
    Link(3, Link(1, Link(4, Link(1, Link(5)))))
    >>> s.rest
    Link(1, Link(4, Link(1, Link(5))))
    >>> s.rest.rest
    Link(4, Link(1, Link(5)))
    >>> s.rest.rest.rest
    Link(1, Link(5))
    >>> s.rest.rest.rest.rest
    Link(5)
    >>> s.rest.rest.rest.rest.rest
    ()
    >>> s.rest.rest.rest.rest.rest = Link(2)
    >>> s
    Link(3, Link(1, Link(4, Link(1, Link(5, Link(2))))))
    >>> t
    Link(1, Link(4, Link(1, Link(5, Link(2)))))
    >>> print(s)
    (3 1 4 1 5 2)
    >>> (3, (1, (4, (1, (5, 2)))))
    (3, (1, (4, (1, (5, 2)))))
    >>> type(s) == Link
    True
    >>> type(s) == tuple
    False
    >>> print(t)
    (1 4 1 5 2)
    >>> print(s.rest)
    (1 4 1 5 2)

    >>> from fractions import Fraction
    >>> u = Link(1, Link('hello', Link(None, Link(Fraction(1, 3)))))
    >>> print(u)
    (1 hello None 1/3)
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '('
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + ')'

def map_link(f, s):
    """Return a linked list of f(x) for each x in s.

    >>> evens = Link(4, Link(2, Link(6)))
    >>> map_link(lambda x: x + 1, evens)
    Link(5, Link(3, Link(7)))
    >>> evens
    Link(4, Link(2, Link(6)))
    """
    if s is Link.empty:
        return s
    return Link(f(s.first), map_link(f, s.rest))

def cycle(k, n):
    """Build an n-element list that cycles among range(k).

    >>> cycle(3, 10)
    [0, 1, 2, 0, 1, 2, 0, 1, 2, 0]
    """
    s = []
    for i in range(n):
        s.append(i % k)
    return s

def cycle_link(k, n):
    """Build an n-element linked list that cycles among range(k).

    >>> print(cycle_link(3, 10))
    (0 1 2 0 1 2 0 1 2 0)
    """
    first = Link.empty
    for i in range(n):
        new_link = Link(i % k)
        if first is Link.empty:
            first, last = new_link, new_link
        else:
            last.rest = new_link
            last = new_link
    return first

def double(s, v):
    """Insert another v after each v in s.

    >>> s = [2, 7, 1, 8, 2, 8]
    >>> double(s, 8)
    >>> s
    [2, 7, 1, 8, 8, 2, 8, 8]
    """
    i = 0
    while i < len(s):
        if s[i] == v:
            s.insert(i+1, v)
            i += 2
        else:
            i += 1

def double_link(s, v):
    """Insert another v after each v in s.

    >>> s = Link(2, Link(7, Link(1, Link(8, Link(2, Link(8))))))
    >>> double_link(s, 8)
    >>> print(s)
    (2 7 1 8 8 2 8 8)
    """
    while s is not Link.empty:
        if s.first == v:
            s.rest = Link(v, s.rest)
            s = s.rest.rest
        else:
            s = s.rest


def slice_link(s, i, j):
    """Return a linked list containing elements from i:j.
    >>> evens = Link(4, Link(2, Link(6)))
    >>> slice_link(evens, 1, 100)
    Link(2, Link(6))
    >>> slice_link(evens, 1, 2)
    Link(2)
    >>> slice_link(evens, 0, 2)
    Link(4, Link(2))
    >>> slice_link(evens, 1, 1) is Link.empty
    True
    """
    assert i >= 0 and j >= 0
    if j == 0 or s is Link.empty:
        return Link.empty
    elif i == 0:
        return Link(s.first, slice_link(s.rest, i , j-1))
    else:
        return slice_link(s.rest, i-1 , j-1 )
    


def insert_link(s, x, i):
    """Insert x into linked list s at index i.
    >>> evens = Link(4, Link(2, Link(6)))
    >>> insert_link(evens, 8, 1)
    >>> insert_link(evens, 10, 4)
    >>> insert_link(evens, 12, 0)
    >>> insert_link(evens, 14, 10)
    Index out of range
    >>> print(evens)
    (12 4 8 2 6 10)
    """
    if s is Link.empty:
        print('Index out of range')
    elif i == 0:
        second = Link(s.first, s.rest)
        s.first = x
        s.rest = second
    elif i == 1 and s.rest is Link.empty:
        s.rest = Link(x)
    else:
        insert_link(s.rest, x, i-1)


def tens(s):
    """Print all prefix sums of Link s that are multiples of ten.
    >>> tens(Link(3, Link(9, Link(8, Link(10, Link(0, Link(14, Link(6))))))))
    20
    30
    30
    50
    """
    def f(suffix, total):
        if total % 10 == 0:
            print(total)
        if suffix is not Link.empty:
            f(suffix.rest, total+suffix.first)
    f(s.rest, s.first)
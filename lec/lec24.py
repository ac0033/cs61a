def search_sorted(s, v):
    """Return whether v is in the sorted list s.

    >>> evens = [2*x for x in range(50)]
    >>> search_sorted(evens, 22)
    True
    >>> search_sorted(evens, 23)
    False
    """
    if len(s) == 0:
        return False
    center = len(s) // 2
    if s[center] == v:
        return True
    if s[center] > v:
        rest = s[:center]
    else:
        rest = s[center + 1:]
    return search_sorted(rest, v)

def near_pairs(s):
    """Return the length of the longest contiguous 
    sequence of repeated elements in s.

    >>> near_pairs([3, 5, 2, 2, 4, 4, 4, 2, 2]) # 3 fours!
    3
    """
    count, max_count, last = 0, 0, None
    for i in range(len(s)):
        if count == 0 or s[i] == last:
            count += 1
            max_count = max(count, max_count)
        else:
            count = 1
        last = s[i]
    return max_count
                            
def prefix(s):
    """Return a list of all prefix
    sums of list s.
    """
    t = 0
    result = []
    for x in s:
        t = t + x
        result.append(t)
    return result

def max_sum(s):
    """Return the largest sum of a contiguous subsequence of s. 

    >>> max_sum([3, 5, -12, 2, -4, 4, -1, 4, 2, 2])
    11
    """
    largest = 0
    for i in range(len(s)):
        total = 0
        for j in range(i, len(s)):
            total += s[j]
            largest = max(largest, total)
    return largest


from tree import *

def count_tree(n):
    """Return a count tree with n leaves.
    >>> print(count_tree(10))
    10
        5
            2
                1
                1
            3
                2
                    1
                    1
                1
        5
            2
                1
                1
            3
                2
                    1
                    1
                1
    """
    if n == 1:
        return Tree(1)
    left = count_tree(n//2)
    if n % 2 == 0:
        right = left
    else:
        right = Tree(left.label + 1, [left, Tree(1)])
    return Tree(left.label+right.label, [left,right])


def duplicate(s):
    """Return a list containing the list s twice.
    >>> duplicate([2, 5, 8, 11, 14, 17])
    [[2, 5, 8, 11, 14, 17], [2, 5, 8, 11, 14, 17]]
    """
    return [s, s]


from link import *


def length(s):
    """Return the number of elements in linked list s.

    >>> length(Link(3, Link(4, Link(5))))
    3
    """
    if s is Link.empty:
        return 0
    else:
        return 1 + length(s.rest)

def length_iter(s):
    """Return the number of elements in linked list s.

    >>> length_iter(Link(3, Link(4, Link(5))))
    3
    """
    k = 0
    while s is not Link.empty:
        s, k = s.rest, k + 1
    return k

def append(s, x):
    """Append x to the end of non-empty s and return None.

    >>> s = Link(3, Link(4, Link(5)))
    >>> append(s, 6)
    >>> print(s)
    <3 4 5 6>
    """
    if s.rest: 
        append(s.rest, x)
    else:
        s.rest = Link(x)

def append_iter(s, x):
    """Append x to the end of non-empty s and return None.

    >>> s = Link(3, Link(4, Link(5)))
    >>> append_iter(s, 6)
    >>> print(s)
    <3 4 5 6>
    """
    while s.rest:
        s = s.rest
    s.rest = Link(x)


def pop(s, i):
    """Remove and return element i from linked list s for positive i.

    >>> t = Link(3, Link(4, Link(5, Link(6))))
    >>> pop(t, 2)
    5
    >>> pop(t, 2)
    6
    >>> pop(t, 1)
    4
    >>> t
    Link(3)
    """
    assert i > 0 and i < length(s)
    for x in range(i-1):
        s = s.rest
    result = s.rest.first
    s.rest = s.rest.rest
    return result


def range_link(start, end):
    """Return a Link containing consecutive integers from start to end.

    >>> range_link(3, 6)
    Link(3, Link(4, Link(5)))
    """
    if start >= end:
        return Link.empty
    else:
        return Link(start, range_link(start + 1, end))

def range_link_iter(start, end):
    """Return a Link containing consecutive integers from start to end.

    >>> range_link_iter(3, 6)
    Link(3, Link(4, Link(5)))
    """
    s = Link.empty
    k = end - 1
    while k >= start:
        s = Link(k, s)
        k -= 1
    return s


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

def double_link(s, v):
    """Insert another v after each v.
    >>> end = Link(1, Link(8, Link(2, Link(8))))
    >>> t = Link(2, Link(7,end))
    >>> double_link(t, 8)
    >>> print(t)
    (2 7 1 8 8 2 8 8)
    """
    while s is not Link.empty:
        if s.first == v:
            s.rest = Link(v, s.rest)
            s.rest = s.rest.rest
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
        return Link(s.first, slice_link(s.rest, i, j-1))
    else:
        return slice_link(s.rest, i-1 , j-1)

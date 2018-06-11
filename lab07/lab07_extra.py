""" Optional Questions for Lab 07 """

from lab07 import *

# Q6
def remove_all(link , value):
    """Remove all the nodes containing value. Assume there exists some
    nodes to be removed and the first element is never removed.

    >>> l1 = Link(0, Link(2, Link(2, Link(3, Link(1, Link(2, Link(3)))))))
    >>> print(l1)
    <0 2 2 3 1 2 3>
    >>> remove_all(l1, 2)
    >>> print(l1)
    <0 3 1 3>
    >>> remove_all(l1, 3)
    >>> print(l1)
    <0 1>
    """
    "*** YOUR CODE HERE ***"
    p = link

    while True:
        q = p.rest
        if q == Link.empty:
            break

        if q.first == value:
            p.rest = q.rest
            continue
        p = q


# Q7
def deep_map_mut(fn, link):
    """Mutates a deep link by replacing each item found with the
    result of calling fn on the item.  Does NOT create new Links (so
    no use of Link's constructor)

    Does not return the modified Link object.

    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> deep_map_mut(lambda x: x * x, link1)
    >>> print(link1)
    <9 <16> 25 36>
    """
    "*** YOUR CODE HERE ***"
    # 想了半天，竟然把用栈模拟递归的老套思路忘了。。。
    q = link
    stack = [link]
    while stack:
        e = stack.pop()
        if type(e) == tuple: # empty
            continue
        elif type(e.first) == int:
            e.first = fn(e.first)
        else: # e.first -- Link
            stack.append(e.first)
        stack.append(e.rest)

# Q8
def has_cycle(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    >>> u = Link(2, Link(2, Link(2)))
    >>> has_cycle(u)
    False
    """
    "*** YOUR CODE HERE ***"
    # 使用快慢指针
    if link == Link.empty: return False
    def func(slow, fast):
        if fast == Link.empty:
            return False
        elif fast.rest == Link.empty:
            return False
        elif fast == slow or slow == fast.rest:
            return True
        else:
            return func(slow.rest, fast.rest.rest)
    return func(link, link.rest)
    # q = link
    # stack = [q]
    # while stack and q.rest != Link.empty:
    #     if q.rest is stack[0]:
    #         stack.pop(0)
    #     else:
    #         stack.append(q.rest)
    #     q = q.rest
    # return False if stack else True

def has_cycle_constant(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle_constant(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle_constant(t)
    False
    """
    "*** YOUR CODE HERE ***"
    # 代码有冗余
    if link == Link.empty: return False
    def func(slow, fast):
        if fast == Link.empty:
            return False
        elif fast.rest == Link.empty:
            return False
        elif fast == slow or slow == fast.rest:
            return True
        else:
            return func(slow.rest, fast.rest.rest)
    return func(link, link.rest)


# Q9
def reverse_other(t):
    """Mutates the tree such that nodes on every other (even_indexed) level
    have the labels of their branches all reversed.

    >>> t = Tree(1, [Tree(2), Tree(3), Tree(4)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(4), Tree(3), Tree(2)])
    >>> t = Tree(1, [Tree(2, [Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])]), Tree(8)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(8, [Tree(3, [Tree(5), Tree(4)]), Tree(6, [Tree(7)])]), Tree(2)])
    """
    "*** YOUR CODE HERE ***"

    def func(t, level):
        if (level + 1) % 2 == 0:
            labels = list( map( lambda x: x.label, t.branches ) )
            for sub_t, label in zip(t.branches, labels[::-1]):
                sub_t.label = label
        for sub_t in t.branches:
            func(sub_t, level+1)
    return func(t, 1)

    # stack_t = [t]
    # level = 1
    # level_nodes_nums = [1]
    # while stack_t:
    #     queue_num = []
    #     this_level_nodes = []
    #     this_level_nodes_num = 0
    #     for nodes in [stack_t.pop() for _ in range(level_nodes_nums[level-1])]:
    #         each_sub_nodes = []
    #         each_sub_nodes_num = []
    #         for sub_nodes in nodes.branches:
    #             this_level_nodes_num += 1
    #             this_level_nodes.append(sub_nodes)
    #             each_sub_nodes_num.append(sub_nodes.label)
    #         this_level_nodes.append(each_sub_nodes)
    #
    #     level_nodes_nums.append(this_level_nodes_num)
    #     if (level + 1) % 2 == 0:
    #         for n in this_level_nodes:
    #             for i, sub_n in enumerate(n[::-1]):
    #                 sub_n.label = queue_num[0][i]
    #             queue_num.pop(0)
    #     stack_t += this_level_nodes
    #     level += 1


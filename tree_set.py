import math
from sys import stdin



class Node():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def checker_Count(lo, hi, n):
        if n == None:
            return 0
        if n.val <= hi and n.val >= lo:
            return (checker_Count(lo, hi, n.left) +
                    checker_Count(lo, hi, n.right)+1)

        elif n.val < lo:
            return checker_Count(lo, hi, n.right)

        else:
            return checker_Count(lo, hi, n.left)

class TreeSet():

    def __init__(self):
        self.root = None
        self.size_ = 0
        self.min_ = None
        self.max_ = None

    def add(self, x):
        n = self.root
        if n == None:
            self.root = Node(x)
            self.min_ = x
            self.max_ = x
            self.size_+=1
            return

        while True:
            if x == n.val:
                return 
            elif x < n.val:
                if n.left == None:
                    n.left = Node(x)
                    self.min_ = min(self.min_, x)
                    self.max_ = max(self.max_, x)
                    self.size_ += 1
                    return
                else:
                    n = n.left
            else: 
                if n.right == None:
                    n.right = Node(x)
                    self.min_ = min(self.min_, x)
                    self.max_ = max(self.max_, x)
                    self.size_ += 1
                    return
                else:
                    n = n.right

    def contains(self, x):
        n = self.root
        while n != None:
            if x == n.val:
                return True
            elif x < n.val:
                n = n.left
            else:
                n = n.right
        return False

    def replace(self, parent, n, p):
        if parent == None:  # n is the root
            self.root = p
        elif parent.left == n:  # n is the left child
            parent.left = p
        elif parent.right == n:  # n is the right child
            parent.right = p
        else:
            assert False, 'not a child'


    def remove(self, x):
        if(self.contains(x)):
            n = self.root
            parent = None
            while n != None:
                if x < n.val:
                    parent = n
                    n = n.left  # go left
                elif x > n.val:
                    parent = n
                    n = n.right # go right
                else:  # x == n.val
                    if n.left == None and n.right == None:
                        self.replace(parent, n, None)# replace n with None
                        self.size_ -= 1
                        return
                    elif n.left == None and n.right != None:
                        self.replace(parent, n, n.right)
                        self.size_ -= 1
                        return
                    elif n.right == None and n.left != None:
                        self.replace(parent, n, n.left)
                        self.size_ -= 1
                        return
                    else:
                        temp = n.right
                        value=0
                        while True:
                            if(temp.left == None):
                                value = temp.val
                                self.remove(value)
                                if(parent == None):
                                    self.root.val = value
                                elif(parent.left == n):
                                    parent.left.val = value
                                elif(parent.right == n):
                                    parent.right.val = value
                                break
                            temp = temp.left
                        return


    def size(self):
        return self.size_

    def max(self):
        return self.max_

    def min(self):
        return self.min_

    def count(self, lo, hi):
        n = self.root
        return checker_Count(lo, hi, n)

# t = TreeSet()
# for x in [4, 2, 8, 6, 10]:
#     t.add(x)
# print(t.count(3, 6))
# def sample1():
#     t = TreeSet()
#     print(t.min())
#     print(t.max())
#     for x in [4, 2, 8, 6, 10]:
#         t.add(x)
#     t.add(4)
#     print('size =', t.size())
#     print('min =', t.min())
#     print('max =', t.max())
#     print('t.contains(8) =', t.contains(8))
#     t.remove(8)
#     print('t.contains(8) =', t.contains(8))
#     print('size =', t.size())
# def sample2():
#     t = TreeSet()
#     a = [5, 2, 3, 4, 1]
#     for x in a:
#         t.add(x)
#     for x in a:
#         print(t.contains(x))
#         t.remove(x)
#         print(t.contains(x))
#     t.remove(5)
#     print(t.size())

# def sample3():
#     t = TreeSet()
#     a = [10, 5, 3, 8]
#     for x in a:
#         t.add(x)
#     for x in [5, 8, 3, 10]:
#         print(t.contains(x))
#         t.remove(x)
#         print(t.contains(x))
#     print(t.size())
# def sample4():
#     t = TreeSet()
#     a = [10, 5, 20, 2]
#     for x in a:
#         t.add(x)
#     for x in a:
#         print(t.contains(x))
#         t.remove(x)
#         print(t.contains(x))
#     print(t.size())
#
# def sample5():
#     t = TreeSet()
#     a = [3, 9, 5, 4, 8, 2, 10]
#     for x in a:
#         t.add(x)
#     for x in a:
#         print(t.contains(x))
#         t.remove(x)
#         print(t.contains(x))
#

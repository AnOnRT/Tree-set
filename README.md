# Tree-set
A Python class TreeSet that stores a set of values in a binary search tree.

The class should support the following operations:

ts = TreeSet() - creates a TreeSet
ts.contains(x) - True if x is in the set
ts.add(x) - adds x to the set if not already present
ts.remove(x) - removes x from the set if present
ts.min() - returns the smallest value in the set, or None if the set is empty
ts.max() - returns the largest value in the set, or None if the set if empty
ts.size() - returns the total number of values in the set
ts.count(lo, hi) - returns the number of values x in the set such that lo <= x <= hi

count() only explores parts of the tree that might contain values between lo and hi.

size() runs in O(1). All other operations runs in O(h), where h is the height of the binary tree.

If a node has two children, remove() replaces its value with the smallest value in the node's right subtree.

---
title: Trees
icon: fa-star
---

A Tree is a Graph but a Graph is not Tree.

for $N =$ No of Nodes, $E =$ No of Edges, \
Always $N = E - 1$

### Application of Tree

1. File Parsing / HTML / JSON / Abstract Syntax Tree
2. Many Sub Data Structures:
    a. AVL Tree
    b. B-Tree
    c. Red Black Tree
    d. Segment Tree
    e. Fenwick Tree
    f. Treaps
    g. Suffix Tree
    h. Tree Map.
3. Game Theory
4. Probality Tree

### Binary Search Tree

Binary Seach Tree(BST) which are trees which statis the BST invariant which stats that every node x

$$
\forall x \in \text{Nodes}, \;\;\;\;\; x.left.value <= x.value <= x.right.value
$$


### Storing Binary Tree

If given tree is binary tree, then binary tree can store in flattered array.

<div style="display:flex;justify-content:center;width:100%;">
<img src="https://i.ibb.co/hRvZdQqg/ba713d246df1.png" style="height: 300px"/>
</div>

**Flattered Array** :-

$$
\boxed{
\begin{array}{c | c | c | c | c | c | c}
0 & 1 & 2 & 3 & 4 & 5 & 6 \\
\hline
A & X & C & D & E & Y & K
\end{array}
}
$$


**Accesing the value of Node & Children** :-

The root node is always at index 0
and children of the current node are accessed to relative to position $i$

$$
\begin{aligned}
\text{left node} & : M[2*i+1] \\
\text{right node} & : M[2*i+2]
\end{aligned}
$$


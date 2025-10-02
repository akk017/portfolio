---
title: A - Introduction
icon: fa-star
---

<iframe style="aspect-ratio: 16 / 9;" width="100%"  src="https://www.youtube.com/embed/videoseries?si=TrBXRu74Yb6TX1w2&amp;list=PLDV1Zeh2NRsDGO4--qE8yH72HFL1Km93P" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

**[Website To Visualize Graphs](https://csacademy.com/app/graph_editor)**

<u>Graph Theory</u> is the mathematical theory of properties and application of graph networks

### Types of Graph

1. Undirectied Graph: A Graph in which edges have no direction. the edge $(u, v) \equiv (v, u)$
2. Directed Graph: A Graph in which edges have direction.
3. Weighted Graph: A Graph in which edge have weight, ie edge is represented by $(u, v, w)$.

### Special Graph

<u>Tree</u>: A Tree is unidirecteced graph with no cycles. \
equivaltenly, If $N = \text{Number of Nodes}$ and $E = \text{Number of Edges}$, then $E = N - 1$

<u>Rooted Tree</u>: A Rooted Tree is tree with a designated root. \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; edges point away $\rightarrow$ arboresence or out-tree \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; edges point inward $\rightarrow$ anti-arboresence or in-tree

<u>Directed Acylic Graph</u>: or Simply DAG, <u>Directed Graph with No Cycles</u>

<u>Bipartite Graph</u>: A Bipartite graph is one whose edge $(u, v)$ can be split so that, the can form two independent graphs such that eery edge connect every node in graph $U$ and $V$

<u>Complete Graph</u>: A Completed graph is one where there is unqiue edge between every pair of nodes. or Every node can be accessed from every other node in the graph.

### Representing Graph

<u>Adjacency Matrix</u>: for example

\[
M =
\begin{bmatrix}
0 & 3 & 1 & 10 \\
6 & 0 & 5 & 5 \\
1 & 4 & 0 & 3 \\
4 & 6 & 4 & 0
\end{bmatrix}
\]

where $M[u][v] = w$ and $w$ is weight of the edge $u \rightarrow v$. \
and $M[u][u] = 0$, as there is no weight for the edge $u \rightarrow u$.

| Pros       | Cons |
|:---------- |:---|
| Space efficient for represent graph      | Requires $O(n^2)$ |
| Edge Weight Lookup is $O(1)$        | Iterating over all edges takes $O(v^2)$ |
| Simplest Graph Representation    ||

<u>Adjanceny List</u>:

$$
M(A) = [(B, 1), (C, 2)] \\
M(B) = [(C, 3)] \\
M(C) = [(A, 3), (D, 2), (B, 4)] \\
$$

| Pros       | Cons |
|:---------- |:---|
| Great for sparse graph      | Not Effiecient for denser graph |
| Iterating over all edges of a node is effiecient       | Edge weight lookup is $O(E)$ <br> where $E = \text{No of Edges}$ |


<u>Edge List</u>: <br> Unordeded List of edges represent in triplets.

$$
M = [(A, B, 1), (A, C, 2), (A, B, 2), (B, C, 3), (C, C, 8)]
$$

| Pros       | Cons |
|:---------- |:---|
| Space eff for representing sparse graph     | Not effiecient for denser graph |
| Iterating over all edges of a node is effiecient       | Edge weight lookup is $O(E)$ <br> where $E = \text{No of Edges}$ |
|Very simple structure| |

<br>
<br>
<br>
<br>
<br>
<br>

---

PS: These are notes taken from above Video Series Playlist.
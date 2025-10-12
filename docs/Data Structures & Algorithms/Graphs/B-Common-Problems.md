---
title: Common Graph Theory Problems
icon: fa-diagram-project
---

1. Shortest Path Problem
2. Connectivity Problem
3. Negative Cycles
4. Strongly Connected Components
5. Travelling Salesmen Problem
6. Bridge Problem
7. Articulation Point
8. Minimum Spanning Tree
9. Network Flow & Max Flow


### Shortest Path Problem

Given a weighted graph, find th e shortest path from node `A` to node `B`.

Algorithms:

1. BFS (Unweighted Graphs)
2. Dijkstra's
3. Bellman Ford
4. Floyd-Warshall

### Connectivity Problem

Can one node `A` can connect to another node `B`

**Typical Solution**: Use union find data structure or any search algorithms

### Negative Cycles

Does any weighted directed graph have any negative cycles, if so where ?

Algorithms:

1. Bellman Ford
2. Floyd Warshall

### Strongly Connected Components

Strongly connected components (SCCs) are subgraphs within a directed graph where every vertex is reachable from every other vertex.

Algorithms:

1. Tarjan's
2. Kosaraju

### Travelling Salesman Problem

Given a list of citites and distance between each pair of cities, what is the shortest path possible that visites each city exactly once and returns to the same origin city.

Algorithms:

1. Held-Karp
2. Branch & Bound
3. And Many Approx Algorithms

_** Its a NP problem **_
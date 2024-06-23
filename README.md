# Longest Path Problem in Graph Theory

## Project Overview
This project aims to solve the Longest Path problem in Graph Theory, a classic computational problem denoted as [ND29]. The goal is to find the longest simple path in an undirected graph that passes through at least k edges without repeating any vertices.

## Problem Description
The Longest Path problem involves finding a simple path between two vertices, s and t, in an undirected graph G(V, E) that contains at least k edges. This problem is NP-complete, which means its solution can be verified in polynomial time.

Applications of this problem can be found in logistics, network design, and scheduling, where the aim is to find the longest possible path between two points without revisiting any point.

## Algorithms Implemented
### 1. Brute Force Algorithm
The brute force approach generates all possible paths between vertices s and t and checks each path to see if it is a simple path with at least k edges. While this method guarantees a solution, its exponential time complexity makes it inefficient for large graphs.

### 2. Heuristic Algorithm
A heuristic approach using Depth-First Search (DFS) is also implemented. This algorithm explores paths starting from the root node and stops when a path with at least k edges is found. Although it does not guarantee an optimal solution, it has polynomial time complexity.

## Performance Analysis
To compare the performance of both algorithms, we generated 20 random test cases with increasing input sizes. We measured the running time of each test case for both algorithms.

### Results
- **Brute Force Algorithm:** Exponential time complexity (𝚹(n!)) with high running times for larger graphs.
- **Heuristic Algorithm:** Polynomial time complexity (O(V+E)) with reasonable running times for small to medium-sized graphs.

## Experimental Analysis of Correctness
We used unit tests to validate the correctness of both algorithms. The tests confirmed that both approaches correctly identify paths that meet the criteria in various graph scenarios.

### Testing Framework
- **Brute Force Algorithm:** Verified paths for simplicity and length.
- **Heuristic Algorithm:** Confirmed that DFS finds paths with at least k edges.

## Conclusion
The heuristic algorithm using DFS provides a feasible solution for small to medium-sized graphs, despite its limitations in not guaranteeing an optimal solution. The brute force method, while correct, is impractical for larger graphs due to its high time complexity.

## Authors
- Serkan Kütük
- Özge Karasu

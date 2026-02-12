# DAT600-Assignment2: Algorithm Theory

A collection of assignments for the DAT600 Algorithm Theory course, featuring implementations of fundamental data structures and algorithms.

## Contents

### Task 1: AVL Set
Implementation of a self-balancing binary search tree (AVL tree) with operations including:
- `insert()` - O(log n) insertion with automatic balancing
- `find()` - O(log n) search
- `find_min()` / `find_max()` - O(log n) finding extremes
- `find_next()` / `find_prev()` - O(log n) successor/predecessor queries

**Files:**
- `avlset.py` - AVL tree implementation
- `node.py` - Node class definition
- `main.py` - Complexity analysis with visualization

### Task 2: Disjoint Set (Union-Find)
Efficient implementation of the disjoint set data structure with union by rank and path compression:
- `make_set()` - O(1) creating singleton sets
- `find_set()` - O(α(n)) finding representative with path compression
- `union()` - O(α(n)) merging sets with union by rank

Where α(n) is the inverse Ackermann function (practically constant).

**Files:**
- `disjointset.py` - Disjoint set implementation
- `main.py` - Performance testing and visualization

### Task 3: Rod Cutting Problem
Dynamic programming solutions to the rod cutting optimization problem:
- `naive.go` - Naive recursive approach
- `topdown.go` - Top-down DP with memoization
- `bottomup.go` - Bottom-up iterative DP

**Files:**
- `main.go` - Entry point
- `naive.go`, `topdown.go`, `bottomup.go` - Different solution approaches
- `go.mod` - Go module definition

## Running the Code

### Task 1 - AVL Set
```bash
cd Task1
python3 main.py
```
Generates `avlset_complexity_graph.png` showing operation complexity.

### Task 2 - Disjoint Set
```bash
cd Task2
python3 main.py
```
Generates `disjoint_set_graph.png` showing operation scaling.

### Task 3 - Rod Cutting
```bash
cd Task3
go run main.go
```

## Complexity Analysis

All implementations include comprehensive complexity analysis and runtime visualization through graphs showing how each operation scales with input size.

## Author
Yahya

## License
MIT

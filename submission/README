# README

## Advanced Algorithms Challenge at CentraleSupélec

This project is a solution to an advanced algorithms challenge at CentraleSupélec. The task is to compute two dominating sets, **D1** and **D2**, of an undirected graph in a way that minimizes the score defined as:

\[
\text{Score} = \frac{|D1| + |D2| + |D1 \cap D2|}{|V|}
\]

where \(|V|\) is the number of vertices in the graph.

---

## Table of Contents

- [Problem Description](#problem-description)
- [Solution Overview](#solution-overview)
- [How to Run the Program](#how-to-run-the-program)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Example Usage](#example-usage)
- [Code Explanation](#code-explanation)
  - [Functions](#functions)
  - [Algorithm Steps](#algorithm-steps)
- [Contact](#contact)

---

## Problem Description

- **Objective**: Find two dominating sets \( D1 \) and \( D2 \) in a given undirected graph \( G = (V, E) \) that minimize the specified score.
- **Dominating Set**: A subset \( D \subseteq V \) such that every node not in \( D \) is adjacent to at least one node in \( D \).

---

## Solution Overview

The solution employs greedy algorithms and optimization techniques to construct the dominating sets:

- **Greedy Selection**: Iteratively select nodes with the highest degree to build the dominating sets.
- **Multiple Trials**: Start the algorithm from multiple high-degree nodes to find the best possible sets.
- **Special Case Handling**: Apply a different strategy when the graph has a specific structure (e.g., the number of nodes equals the number of edges).

---

## How to Run the Program

### Prerequisites

- **Python 3.x**
- **NetworkX Library**

### Installation

Install the required library using pip:

```bash
pip install networkx
```

### Example Usage

```bash
python dominant.py path/to/input_data path/to/output_results
```

**Note**: Replace `your_module_name` with the actual name of the Python file where the `dominant` function is defined.

---

## Code Explanation

The `dominant` function computes two dominating sets for a given undirected graph. Below is an explanation of its key components.

### Functions

#### 1. `compute_score(set1, set2, graph)`

- **Purpose**: Calculates the score based on the sizes of the two sets and their intersection.
- **Parameters**:
  - `set1`, `set2`: The two dominating sets.
  - `graph`: The original graph.
- **Returns**: The computed score.

#### 2. `is_dominating_set(graph, dom_set)`

- **Purpose**: Checks if a given set is a dominating set of the graph.
- **Parameters**:
  - `graph`: The graph.
  - `dom_set`: The set to check.
- **Returns**: `True` if `dom_set` is a dominating set; `False` otherwise.

#### 3. `generate_dom_set1(start_node, graph)`

- **Purpose**: Generates the first dominating set using a greedy algorithm starting from `start_node`.
- **Parameters**:
  - `start_node`: The node to start the algorithm.
  - `graph`: The graph.
- **Returns**: The first dominating set `D1`.

#### 4. `generate_dom_set2(start_node, graph, dom_set1)`

- **Purpose**: Generates the second dominating set, minimizing overlap with `dom_set1`.
- **Parameters**:
  - `start_node`: The node to start the algorithm.
  - `graph`: The graph.
  - `dom_set1`: The first dominating set.
- **Returns**: The second dominating set `D2`.

#### 5. `get_longest_path(graph)`

- **Purpose**: Finds the longest path in the graph using Depth-First Search (DFS).
- **Parameters**:
  - `graph`: The graph.
- **Returns**: A list of nodes representing the longest path.

### Algorithm Steps

1. **Special Case Handling**:
   - If the number of nodes equals the number of edges, the algorithm constructs dominating sets based on the longest path in the graph.
   - Nodes are selected alternately to form `D1` and `D2`.

2. **Generating Dominating Set D1**:
   - **Selection**: Choose the top 25 nodes with the highest degrees.
   - **Trials**: For each selected node, generate a dominating set using `generate_dom_set1`.
   - **Optimization**: Select the smallest dominating set among the trials.

3. **Generating Dominating Set D2**:
   - **Graph Reduction**: Remove nodes from `D1` to avoid overlap.
   - **Selection**: Choose the top 25 nodes with the highest degrees in the reduced graph.
   - **Trials**: For each selected node, generate a dominating set using `generate_dom_set2`.
   - **Optimization**: Select the dominating set with the minimal score.

4. **Result**:
   - Return the two dominating sets `D1` and `D2` that minimize the score.
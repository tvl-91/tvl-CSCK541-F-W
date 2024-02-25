# tvl-CSCK541 F-W 
 This repository was created for practical Mid Module Assignment for University of Liverpool Module - CSCK541 Software Development in Practice. This project implements the Floyd-Warshall Algorithm for finding the shortest paths between all pairs of vertices in a weighted graph recurively.
 The goal of this project is rewriting the algorithm to use recursion.
 
## Features
- Implements both iterative and recursive  for diverse problem-solving strategies.
- Includes unit tests (`iterative_test.py` & `recursive_test.py`) to ensure the correctness of both implementations using various sample graphs.
- The code is well-structured, documented, and tested.

# Implementation
There are two steps to install and run the program:
1. Download the repository or clone it using `gitclone`
   ```bash
   https://github.com/tvl-91/tvl-CSCK541-F-W.git
2. Running the program:
   1. Use any Python IDE such as PyCharm, VSCode or Jupyter.
   2. Install requirements.txt
      ```bash
      pip install -r requirements.txt
   3. Navigate the directory and run `recursive_test.py` to run recursive algorithm

 # Usage
 To run tests, follow these steps:
 - Navigate the directory to `tests` folder and in `test_cases.py` file alter sample input to own liking.
 - Run `iterative_test.py` and `recursive_test.py` to produce outputs.
 - Change the outputs to ensure accuracy, especially after running `iterative_test.py`.

 To run recursive algorithm:
 1. import `floyd_warshall` from `floyd_warshall_recursive.py`.
    ```bash
    from floyd_warshall_recursive imprt floyd_warshall
 2. Use the function within your code with the appropriate input.

 Note that the inputs are adjacency matrices as 2D lists where each element graph[i][j] represents the weight of the edge between vertex i and vertex j.
 `Eample graph: [[0, 4, inf, 6], [inf, 0, 1, 5], [inf, inf, 0, 2,], [5, inf, inf, 0]]`

 # License
 This project is licensed under the MIT License
 

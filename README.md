## Dynamic Programming

This repository was created for teaching or learning dynamic programming using problem statements. Along with the raw implementation, for using dynamic programming easily in real-life, an alternate solution using functools library is also provided.

### Identifying and Approaching a Dynamic Programming Problem
- Notice any overlapping solutions
- decide what is the trivially smallest input
- Think recursively to use Memoization
- Think iteratively to use Tabulation
- Draw a strategy first!

#### Memoization (Top - Down) Recipe

1. Develop a functional code.
-  Visualize the problem as a tree.
-  Implement the tree using recursion
-  Test it out.

2. Work on Optimality
- Add a memo object - array, dictionary, etc.
- Add a base case to return memo values, leaf nodes of the tree.
- Store return values into the memo.

#### Tabulation (Bottom - Up) Recipe

1. Visualize the problem as a table
2. Size the table based on the inputs
3. Initialize the table with default values (For python, if necessary)
4. Seed the trivial answer into the table (Initiate value(s) in
the table which will act as activation for others)
5. Iterate through the table
6. Fill further positions based on the current position
(this can also be modified to fill current position based on past values)



Some Problem Statements taken from [Learn to Solve Algorithmic Problems & Coding Challenges by Alvin Zablan](https://youtu.be/oBt53YbR9Kk)

Solutions in Python 3.9

Follow this sequence for proper order of problems:

1. [fibonacci.py](https://github.com/shreyansh96/dynamic-programming/blob/main/problems/fibonacci.py)
2. [grid_traveller.py](https://github.com/shreyansh96/dynamic-programming/blob/main/problems/grid_traveller.py)
3. [can_sum.py](https://github.com/shreyansh96/dynamic-programming/blob/main/problems/can_sum.py)
4. [how_sum.py](https://github.com/shreyansh96/dynamic-programming/blob/main/problems/how_sum.py)
5. [best_sum.py](https://github.com/shreyansh96/dynamic-programming/blob/main/problems/best_sum.py)
6. [can_construct.py](https://github.com/shreyansh96/dynamic-programming/blob/main/problems/can_construct.py)
7. [count_construct.py](https://github.com/shreyansh96/dynamic-programming/blob/main/problems/count_construct.py)
8. [all_construct.py](https://github.com/shreyansh96/dynamic-programming/blob/main/problems/all_construct.py)
9. [longest_common_subsequence.py](https://github.com/shreyansh96/dynamic-programming/blob/main/problems/longest_common_subsequence.py)

Each file has problem statement mentionend in the docstring, and complexities mentioned in the solution.

There are multiple solutions presented to the same problem, all solutions are encapsulated  in a class.

By default it will run all the solutions and compare execution times.

For simplicity, The execution should be done from home directory, simply run  
`python main.py`

This will run all the solutions, modify it accordingly.

For advanced users, you can set your path in IDE, and run the files directly.

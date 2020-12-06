"""
Problem Statement:
Say that you are a traveler on a 2D grid.
You begin in the top-left corner and your goal is to travel to the bottom-right corner. You may only move down or right.
You may only move down or right.

In how many ways can you travel to the goal on a grid with dimensions m*n?
"""
from functools import lru_cache, partial
from utils.decorators import time_this
import numpy as np


class GridTraveller:
    def __init__(self, m, n):
        self.solutions = {
            "recursive": partial(self.recursive, m, n),
            "dp_traverse_child": partial(self.dp_traverse_child, m, n),
            "dp_reduce_grid": partial(self.dp_reduce_grid, m, n),
            "dp_lru_cache": partial(self.dp_lru_cache, m, n),
            "dp_tabulation": partial(self.dp_tabulation, m, n),
        }

    @staticmethod
    def recursive(m, n):
        """
        Time complexity: O(2^(n+m))
        Space Complexity: O(n+m)

        :param m:
        :param n:
        :return:
        """
        if m == 1 and n == 1:
            return 1
        if m == 0 or n == 0:
            return 0
        return GridTraveller.recursive(m - 1, n) + GridTraveller.recursive(m, n - 1)

    @staticmethod
    def dp_traverse_child(m, n, current=None, grid_value=None):
        start = [0, 0]
        goal = [m - 1, n - 1]
        actions = ('d', 'r')
        if current is None:
            current = start
            grid_value = {}
        if tuple(current) in grid_value.keys():
            return grid_value[tuple(current)]
        value = 0
        if current == goal:
            return 1
        for action in actions:
            if action == "d":
                child = [current[0] + 1, current[1]]
            else:
                child = [current[0], current[1] + 1]

            if child == goal:
                return 1
            if child[0] >= m or child[1] >= n:
                continue
            else:
                value += GridTraveller.dp_traverse_child(m, n, child, grid_value)

        grid_value[tuple(current)] = value
        return grid_value[tuple(current)]

    @staticmethod
    def dp_reduce_grid(m, n, grid_value=None):
        """
        grid_traveller(m,n) == grid_traveller(n,m) (Symmetric)
        Time Complexity: O(nm)
        Space Complexity: O(nm)
        """
        if grid_value is None:
            grid_value = {}
        value = grid_value.get((m, n))
        if value:
            return value
        value = grid_value.get((n, m))
        if value:
            return value
        if m == 1 and n == 1:
            grid_value[(m, n)] = 1
            return 1
        if m == 0 or n == 0:
            grid_value[(m, n)] = 0
            return 0
        grid_value[(m, n)] = GridTraveller.dp_reduce_grid(m - 1, n, grid_value) + GridTraveller.dp_reduce_grid(m, n - 1, grid_value)
        return grid_value[(m, n)]

    @staticmethod
    @lru_cache
    def dp_lru_cache(m, n):
        if m == 1 and n == 1:
            return 1
        if m == 0 or n == 0:
            return 0
        return GridTraveller.dp_lru_cache(min(m - 1, n), max(m - 1, n)) + \
               GridTraveller.dp_lru_cache(min(m, n - 1), max(m, n - 1))

    @staticmethod
    def dp_tabulation(m, n, grid_value=None):
        """
        grid_traveller(m,n) == grid_traveller(n,m) (Symmetric)
        Time Complexity: O(nm)
        Space Complexity: O(nm)
        """
        grid_value_table = np.zeros((m + 1, n + 1), int)
        grid_value_table[1][1] = 1

        for i in range(m + 1):
            for j in range(n + 1):
                if i + 1 <= m:
                    grid_value_table[i + 1][j] += grid_value_table[i][j]
                if j + 1 <= n:
                    grid_value_table[i][j + 1] += grid_value_table[i][j]
        # print(grid_value_table)
        return grid_value_table[m][n]

    @staticmethod
    @time_this()
    def run(func):
        print(f"Solution: {func()}")

    def execute_all(self):

        print("\nSolutions to Grid Traveller\n")

        for name, solution in self.solutions.items():
            print(f'Algo-Name: {name} {" -" * 90}')
            self.run(solution)
            print('-' * 100)


GridTraveller(10, 10).execute_all()

"""
Problem Statement:
Write a function bestSum(targetSum, numbers) that takes in a target sum and an array
of numbers as arguments.
The function should return an array containing the minimum combination of elements that add up to exactly the targetSum.
If there is no combination return []

If there are multiple shortest combinations possible, you may return any single one.

You may use an element of the array as many times as needed.

You may assume that all input numbers are positive.

Hints for time complexity:
Considering targetSum = M and number of elements = N
the worst case will be when one of the number in array is 1
so the height of the tree will be M
for every node there will be N branches.
"""

from functools import lru_cache, partial
from utils.decorators import time_this
from copy import deepcopy


class BestSum:
    def __init__(self, target_sum, numbers):
        self.solutions = {
            # "recursive": partial(self.recursive, target_sum, numbers),
            "dynamic_programming": partial(self.dp, target_sum, numbers),
            "dp_lru_cache": partial(self.dp_lru_cache, target_sum, tuple(numbers)),
        }

    @staticmethod
    def recursive(target_sum, array):
        """
        Time complexity: O(N^M*M)
        Space Complexity: O(M^2)
        """
        if target_sum <= 0:
            return []
        shortest_tree = []
        for element in array:
            new_sum = target_sum - element
            if new_sum == 0:
                return [element]
            combination = BestSum.recursive(new_sum, array)
            if combination:
                combination += [element]
                if not shortest_tree or len(shortest_tree) > len(combination):
                    shortest_tree = combination

        return shortest_tree

    @staticmethod
    def dp(target_sum, array, memo=None):
        """
        Time complexity: O(N*M*M)
        Space Complexity: O(M^2)
        """
        if memo is None:
            memo = {}
        if target_sum <= 0:
            return []
        value = memo.get(target_sum)
        if value:
            return deepcopy(value)
        shortest_tree = []
        for element in array:
            new_sum = target_sum - element
            if new_sum == 0:
                return [element]
            combination = BestSum.dp(new_sum, array, memo)
            if combination:
                combination += [element]
                if not shortest_tree or len(shortest_tree) > len(combination):
                    shortest_tree = combination
        memo[target_sum] = deepcopy(shortest_tree)
        return shortest_tree

    @staticmethod
    @lru_cache
    def dp_lru_cache(target_sum, array):
        """
        Time complexity: O(N*M*M)
        Space Complexity: O(M^2)
        """
        if target_sum <= 0:
            return ()
        shortest_tree = ()
        for element in array:
            new_sum = target_sum - element
            if new_sum == 0:
                return (element,)
            combination = BestSum.dp_lru_cache(new_sum, array)
            if combination:
                combination += (element,)
                if not shortest_tree or len(shortest_tree) > len(combination):
                    shortest_tree = combination

        return shortest_tree

    @staticmethod
    @time_this()
    def run(func):
        print(f"Solution: {func()}")

    def execute_all(self):

        print("\nSolutions to BestSum\n")

        for name, solution in self.solutions.items():
            print(f'Algo-Name: {name} {" -" * 90}')
            self.run(solution)
            print('-' * 100)


# BestSum(7, [2, 4]).execute_all()
BestSum(7, [1, 4, 5]).execute_all()

BestSum(100, [5, 2, 4, 25]).execute_all()
# BestSum(300, [7, 14]).execute_all()

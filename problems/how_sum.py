
"""
Problem Statement:
Write a function howSum(targetSum, numbers) that takes in a target sum and an array
of numbers as arguments.
The function should return
 1. a boolean indicating whether or not it is possible to
generate the targetSum using numbers from the array
 2. an array containing any combinatio of elements that add up to exactly the targetSum.
 If there is no combination return []

If there are multiple combinations possible, you may return any single one.

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


class HowSum:
    def __init__(self, target_sum, numbers):
        self.solutions = {
            "recursive": partial(self.recursive, target_sum, numbers),
            "dynamic_programming": partial(self.dp, target_sum, numbers),
            "dp_lru_cache": partial(self.dp_lru_cache, target_sum, tuple(numbers)),
        }

    @staticmethod
    def recursive(target_sum, array, element_tree=None):
        """
        Time complexity: O(N^M*M)
        Space Complexity: O(M)
        """
        if element_tree is None:
            element_tree = []
        for element in array:
            new_sum = target_sum - element
            if new_sum < 0:
                continue
            elif new_sum == 0:
                element_tree.append(element)
                return element_tree
            if HowSum.recursive(new_sum, array, element_tree):
                element_tree.append(element)
                return element_tree
        element_tree = []
        return element_tree

    @staticmethod
    def dp(target_sum, array, memo=None, element_tree=None):
        """
        Time complexity: O(N*M*M)
        Space Complexity: O(M^2)
        """
        if memo is None:
            memo = {}
            element_tree = []
        val = memo.get(target_sum)
        if val is not None:
            return element_tree
        for element in array:
            new_sum = target_sum - element
            if new_sum < 0:
                continue
            elif new_sum == 0:
                memo[target_sum] = 1
                element_tree.append(element)
                return element_tree
            if HowSum.dp(new_sum, array, memo, element_tree):
                memo[target_sum] = 1
                element_tree.append(element)
                return element_tree
        memo[target_sum] = 0
        element_tree = []
        return element_tree


    @staticmethod
    @lru_cache
    def dp_lru_cache(target_sum, array, element_tree=None):
        """
        Time complexity: O(N*M*M)
        Space Complexity: O(M^2)
        """
        if element_tree is None:
            element_tree = []
        for element in array:
            new_sum = target_sum - element
            if new_sum < 0:
                continue
            elif new_sum == 0:
                element_tree.append(element)
                return element_tree
            if HowSum.recursive(new_sum, array, element_tree):
                element_tree.append(element)
                return element_tree
        element_tree = []
        return element_tree

    @staticmethod
    @time_this()
    def run(func):
        print(f"Solution: {func()}")

    def execute_all(self):

        print("\nSolutions to HowSum\n")

        for name, solution in self.solutions.items():
            print(f'Algo-Name: {name} {" -" * 90}')
            self.run(solution)
            print('-' * 100)


HowSum(7, [2, 4]).execute_all()
HowSum(101, [5, 2, 4, 8]).execute_all()
# HowSum(300, [7, 14]).execute_all()

"""
Problem Statement:
Write a function canSum(targetSum, numbers) that takes in a target sum and an array
of numbers as arguments.
The function should return a boolean indicating whether or not it is possible to
generate the targetSum using numbers from the array.

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


class CanSum:
    def __init__(self, target_sum, numbers):
        self.solutions = {
            # "recursive": partial(self.recursive, target_sum, numbers),
            "dynamic_programming": partial(self.dp, target_sum, numbers),
            "dp_lru_cache": partial(self.dp_lru_cache, target_sum, tuple(numbers)),
            "dp_tabulation": partial(self.dp_tabulation, target_sum, numbers),

        }

    @staticmethod
    def recursive(target_sum, array):
        """
        Time complexity: O(N^M)
        Space Complexity: O(M)
        """
        for element in array:
            new_sum = target_sum - element
            if new_sum < 0:
                continue
            elif new_sum == 0:
                return 1
            if CanSum.recursive(new_sum, array):
                return 1
        return 0

    @staticmethod
    def dp(target_sum, array, memo=None):
        """
        Time complexity: O(N*M)
        Space Complexity: O(M)
        """
        if memo is None:
            memo = {}
        val = memo.get(target_sum)
        if val is not None:
            return val
        for element in array:
            new_sum = target_sum - element
            if new_sum < 0:
                continue
            elif new_sum == 0:
                memo[target_sum] = 1
                return 1
            if CanSum.dp(new_sum, array, memo):
                memo[target_sum] = 1
                return 1
        memo[target_sum] = 0
        return 0

    @staticmethod
    @lru_cache
    def dp_lru_cache(target_sum, array):
        """
        Time complexity: O(N)
        Space Complexity: O(N)
        """
        for element in array:
            new_sum = target_sum - element
            if new_sum < 0:
                continue
            elif new_sum == 0:
                return 1
            if CanSum.dp_lru_cache(new_sum, array):
                return 1
        return 0

    @staticmethod
    def dp_tabulation(target_sum, array):
        """
        Time complexity: O(N*M)
        Space Complexity: O(M)
        """
        table = [0] * (target_sum + 1)
        table[0] = 1
        for i in range(target_sum + 1):
            if table[i]:
                for element in array:
                    if i + element <= target_sum:
                        table[i + element] = 1
        # print(table)
        return table[target_sum]

    @staticmethod
    @time_this()
    def run(func):
        print(f"Solution: {func()}")

    def execute_all(self):

        print("\nSolutions to CanSum\n")

        for name, solution in self.solutions.items():
            print(f'Algo-Name: {name} {" -" * 90}')
            self.run(solution)
            print('-' * 100)


CanSum(7, [2, 4, 1]).execute_all()
CanSum(101, [5, 2, 4, 8]).execute_all()
CanSum(300, [7, 14]).execute_all()

"""
Problem Statement:
Write a function canConstruct(target, wordBank) that accepts a target string and an array of strings.
The function should return a boolean indicating whether or not the target can be constructed by
concatenating elements of the wordbank array.

You may reuse elements of 'wordbank' as many times as needed.

canConstruct("", ["any"]) -> 1
canConstruct("abcde", ["ab", "c", "cde"]) -> 1


Hints for time complexity:
Considering targetSum = M and number of elements = N
the worst case will be when one of the number in array is 1
so the height of the tree will be M
for every node there will be N branches.
"""

from functools import lru_cache, partial
from utils.decorators import time_this


class CanConstruct:
    def __init__(self, target, wordbank):
        self.solutions = {
            "recursive": partial(self.recursive, target, wordbank),
            "dynamic_programming": partial(self.dp, target, wordbank),
            "dp_lru_cache": partial(self.dp_lru_cache, target, tuple(wordbank)),
        }

    @staticmethod
    def recursive(target, wordbank):
        """
        Time complexity: O(N^M*M)  M for finding string
        Space Complexity: O(M)
        """
        if target == "":
            return True
        for word in wordbank:
            if target.find(word) == 0:
                updated_target = target[len(word):]
                if CanConstruct.recursive(updated_target, wordbank):
                    return True
        return False

    @staticmethod
    def dp(target, wordbank, memo=None):
        """
        Time complexity: O(N*M)
        Space Complexity: O(M)
        """
        if memo is None:
            memo = {}
        val = memo.get(target)
        if val is not None:
            return val
        if target == "":
            return True
        for word in wordbank:
            if target.find(word) == 0:
                updated_target = target[len(word):]
                if CanConstruct.dp(updated_target, wordbank):
                    memo[target] = False
                    return True

        memo[target] = False
        return False

    @staticmethod
    @lru_cache
    def dp_lru_cache(target, wordbank):
        """
        Time complexity: O(N)
        Space Complexity: O(N)
        """
        if target == "":
            return True
        for word in wordbank:
            if target.find(word) == 0:
                updated_target = target[len(word):]
                if CanConstruct.dp_lru_cache(updated_target, wordbank):
                    return True
        return False

    @staticmethod
    @time_this()
    def run(func):
        print(f"Solution: {func()}")

    def execute_all(self):

        print("\nSolutions to CanConstruct\n")

        for name, solution in self.solutions.items():
            print(f'Algo-Name: {name} {" -" * 90}')
            self.run(solution)
            print('-' * 100)


CanConstruct("", ["any"]).execute_all()
CanConstruct("abcde", ["ab", "c", "cde"]).execute_all()
CanConstruct("kuchbhi", ["ha", "he", "hu", "bhi"]).execute_all()

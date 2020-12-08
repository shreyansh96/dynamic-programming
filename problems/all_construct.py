"""
Problem Statement:
Write a function allConstruct(target, wordBank) that accepts a target string and an array of strings.
The function should return a 2D array containing all of the ways that the target can be constructed
by concatenating elements of the wordbank array.

You may reuse elements of 'wordbank' as many times as needed.

canConstruct("", ["any"]) -> 0
canConstruct("abcde", ["ab", "c", "cde"]) -> [["ab", "cde"]]
canConstruct("purple", ["purp", "purpl", "le", "p", "ur"]) -> [["purp", "le"],["p", "ur", "p", "le"]]


Hints for time complexity:
Considering target is of length M and number of elements is N in wordBank
the worst case will be when words in wordBank is of length 1
so the height of the tree will be M
for every node there will be N branches.
"""

from functools import lru_cache, partial
from utils.decorators import time_this
from copy import deepcopy


class CountConstruct:
    def __init__(self, target, wordbank):
        self.solutions = {
            "recursive": partial(self.recursive, target, wordbank),
            "dynamic_programming": partial(self.dp, target, wordbank),
            "dp_lru_cache": partial(self.dp_lru_cache, target, tuple(wordbank)),
            "dp_tabulation": partial(self.dp_tabulation, target, wordbank)
        }

    @staticmethod
    def recursive(target, wordbank):
        """
        Time complexity: O(N^M*M)  M for finding string
        Space Complexity: O(M) considered only the call stack one, due to output it will be exponent.
         M due to storing a string of len M (worstcase) for every call
        """
        if target == "":
            return [[]]
        all_ways = []
        for word in wordbank:
            if target.find(word) == 0:
                updated_target = target[len(word):]
                ways = CountConstruct.recursive(updated_target, wordbank)
                if ways is not None:
                    for way in ways:
                        way.append(word)
                        all_ways.append(way)
        return all_ways

    @staticmethod
    def dp(target, wordbank, memo=None):
        """
        Time complexity: O(N^M*M)
        Space Complexity: O(M)
        """
        if memo is None:
            memo = {}
        val = memo.get(target)
        if val is not None:
            return val
        if target == "":
            return [[]]
        all_ways = []
        for word in wordbank:
            if target.find(word) == 0:
                updated_target = target[len(word):]
                ways = deepcopy(CountConstruct.dp(updated_target, wordbank, memo))
                if ways is not None:
                    for way in ways:
                        way.append(word)
                        all_ways.append(way)

        memo[target] = all_ways
        return all_ways

    @staticmethod
    @lru_cache
    def dp_lru_cache(target, wordbank):
        """
        Time complexity: O(N^M*M)
        Space Complexity: O(M)
        """
        if target == "":
            return [[]]
        all_ways = []
        for word in wordbank:
            if target.find(word) == 0:
                updated_target = target[len(word):]
                ways = deepcopy(CountConstruct.dp_lru_cache(updated_target, wordbank))
                if ways is not None:
                    for way in ways:
                        way.append(word)
                        all_ways.append(way)
        return all_ways

    @staticmethod
    def dp_tabulation(target, wordbank):
        """
        Time complexity: O(N^M*M)
        Space Complexity: O(M)
        """
        table = [None for _ in range(len(target) + 1)]
        table[0] = [[]]
        for i in range(len(target)+1):
            if table[i] is not None:
                for word in wordbank:
                    if target[i:i+len(word)] == word:
                        next_place = i + len(word)
                        if next_place <= len(target):
                            for way in table[i]:
                                if table[next_place] is None:
                                    table[next_place] = []
                                table[next_place].append(way + [word])

        # print(table)
        return table[len(target)]

    @staticmethod
    @time_this()
    def run(func):
        print(f"Solution: {func()}")

    def execute_all(self):

        print("\nSolutions to CountConstruct\n")

        for name, solution in self.solutions.items():
            print(f'Algo-Name: {name} {" -" * 90}')
            self.run(solution)
            print('-' * 100)


CountConstruct("", ["any"]).execute_all()
CountConstruct("abcde", ["ab", "c", "cde", "de"]).execute_all()
CountConstruct("abcdef", ["ab", "abc", "cd", "abcd", "def", "ef", "c"]).execute_all()
CountConstruct("purple", ["purp", "purpl", "le", "p", "ur"]).execute_all()
CountConstruct("kuchbhi", ["ha", "he", "hu", "bhi"]).execute_all()
# CountConstruct("qqqqqqqqqqqqqqqqqqqqqqqqqqq",
#                ["q", "qq", "qqq", "qqqq", "qqqqq", "qqqqqq"]).execute_all()

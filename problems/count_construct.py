"""
Problem Statement:
Write a function countConstruct(target, wordBank) that accepts a target string and an array of strings.
The function should return the number of ways that the target can be constructed
 by concatenating elements of the wordbank array.

You may reuse elements of 'wordbank' as many times as needed.

canConstruct("", ["any"]) -> 0
canConstruct("abcde", ["ab", "c", "cde"]) -> 1


Hints for time complexity:
Considering target is of length M and number of elements is N in wordBank
the worst case will be when words in wordBank is of length 1
so the height of the tree will be M
for every node there will be N branches.
"""

from functools import lru_cache, partial
from utils.decorators import time_this


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
        Space Complexity: O(M^2) M Due to call stack and
         M due to storing a string of len M (worstcase) for every call
        """
        if target == "":
            return 1
        count = 0
        for word in wordbank:
            if target.find(word) == 0:
                updated_target = target[len(word):]
                count += CountConstruct.recursive(updated_target, wordbank)
                # print(count, updated_target)
        return count

    @staticmethod
    def dp(target, wordbank, memo=None):
        """
        Time complexity: O(N*M^2)
        Space Complexity: O(M*2)
        """
        if memo is None:
            memo = {}
        val = memo.get(target)
        if val is not None:
            return val
        if target == "":
            return 1
        count = 0
        for word in wordbank:
            if target.find(word) == 0:
                updated_target = target[len(word):]
                count += CountConstruct.dp(updated_target, wordbank, memo)

        memo[target] = count
        return count

    @staticmethod
    @lru_cache
    def dp_lru_cache(target, wordbank):
        """
        Time complexity: O(N*M^2)
        Space Complexity: O(M^2)
        """
        if target == "":
            return 1
        count = 0
        for word in wordbank:
            if target.find(word) == 0:
                updated_target = target[len(word):]
                count += CountConstruct.dp_lru_cache(updated_target, wordbank)
        return count

    @staticmethod
    def dp_tabulation(target, wordbank):
        """
        Time complexity: O(N*M^2)
        Space Complexity: O(M)
        """
        table = [0]*(len(target)+1)
        table[0] = 1
        for i in range(len(target)+1):
            if table[i]:
                for word in wordbank:
                    if target[i:i+len(word)] == word:
                        next_place = i + len(word)
                        if next_place <= len(target):
                            table[next_place] += table[i]
                            # print(target[:i], word, table[next_place])

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

CountConstruct("purple", ["purp", "purpl", "le", "p", "ur"]).execute_all()
# CountConstruct("kuchbhi", ["ha", "he", "hu", "bhi"]).execute_all()
# CountConstruct("qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqe",
#                ["q", "qq", "qqq", "qqqq", "qqqqq", "qqqqqq"]).execute_all()

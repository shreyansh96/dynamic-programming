"""
Given two sequences, find the length of longest subsequence present in both of them.
A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.
 For example, "abc", "abg", "bdf", "aeg", ‘"acefg", .. etc are subsequences of "abcdefg".

LCS for input Sequences "ABCDGHI" and "AEDFHRK" is "ADH" of length 3.
LCS for input Sequences "SAGGTAB" and "PGXTXAYB" is "GTAB" of length 4.
"""
from functools import lru_cache, partial
from utils.decorators import time_this


class LCS:
    def __init__(self, primary_sequence, secondary_sequence):
        ps_index = len(primary_sequence) - 1
        ss_index = len(secondary_sequence) - 1
        self.solutions = {
            # "recursive": partial(self.recursive, primary_sequence, secondary_sequence, ps_index, ss_index),
            # "dynamic_programming": partial(self.dp, primary_sequence, secondary_sequence, ps_index, ss_index),
            "dp_tabulation": partial(self.dp_tabulation, primary_sequence, secondary_sequence, ps_index, ss_index),
            "dp_lru_cache": partial(self.dp_lru_cache, primary_sequence, secondary_sequence, ps_index, ss_index),
        }

    @staticmethod
    def recursive(primary_sequence, secondary_sequence, ps_index, ss_index):
        """
        Time complexity: O(2^max(M,N))
        Space Complexity: O(max(M,N))
        """
        if ps_index == -1 or ss_index == -1:
            return 0
        elif primary_sequence[ps_index] == secondary_sequence[ss_index]:
            return 1 + LCS.recursive(primary_sequence, secondary_sequence, ps_index - 1, ss_index - 1)
        else:
            return max(LCS.recursive(primary_sequence, secondary_sequence, ps_index - 1, ss_index), LCS.recursive(primary_sequence, secondary_sequence, ps_index, ss_index - 1))

    @staticmethod
    def dp(primary_sequence, secondary_sequence, ps_index, ss_index, memo=None):
        """
        Time complexity: O(N*M)
        Space Complexity: O(max(M,N))
        """
        if memo is None:
            memo = {}
        val = memo.get((primary_sequence, secondary_sequence, ps_index, ss_index))
        if val:
            return val
        if ps_index == -1 or ss_index == -1:
            memo[(primary_sequence, secondary_sequence, ps_index, ss_index)] = 0
            return memo[(primary_sequence, secondary_sequence, ps_index, ss_index)]
        elif primary_sequence[ps_index] == secondary_sequence[ss_index]:
            memo[(primary_sequence, secondary_sequence, ps_index, ss_index)] = 1 + LCS.dp(primary_sequence, secondary_sequence, ps_index - 1, ss_index - 1, memo)
            return memo[(primary_sequence, secondary_sequence, ps_index, ss_index)]
        else:
            memo[(primary_sequence, secondary_sequence, ps_index, ss_index)] = max(LCS.dp(primary_sequence, secondary_sequence, ps_index - 1, ss_index, memo),
                                                                                   LCS.dp(primary_sequence, secondary_sequence, ps_index, ss_index - 1, memo))
            # print(memo)
            return memo[(primary_sequence, secondary_sequence, ps_index, ss_index)]

    @staticmethod
    @lru_cache
    def dp_lru_cache(primary_sequence, secondary_sequence, ps_index, ss_index):
        """
        Time complexity: O(N*M)
        Space Complexity: O(max(M,N))
        """
        if ps_index == -1 or ss_index == -1:
            return 0
        elif primary_sequence[ps_index] == secondary_sequence[ss_index]:
            return 1 + LCS.dp_lru_cache(primary_sequence, secondary_sequence, ps_index - 1, ss_index - 1)
        else:
            return max(LCS.dp_lru_cache(primary_sequence, secondary_sequence, ps_index - 1, ss_index),
                       LCS.dp_lru_cache(primary_sequence, secondary_sequence, ps_index, ss_index - 1))

    @staticmethod
    def dp_tabulation(primary_sequence, secondary_sequence, ps_index, ss_index):
        """
        Time complexity: O(N*M)
        Space Complexity: O(max(M,N))
        """
        table = [[0] * (ps_index + 2) for _ in range(ss_index + 2)]

        for i in range(ss_index + 2):
            for j in range(ps_index + 2):
                if i == 0 or j == 0:
                    continue
                elif primary_sequence[j - 1] == secondary_sequence[i - 1]:
                    table[i][j] = 1 + table[i - 1][j - 1]
                else:
                    table[i][j] = max(table[i - 1][j], table[i][j - 1])
        # print(table)
        return table[ss_index + 1][ps_index + 1]

    @staticmethod
    @time_this()
    def run(func):
        print(f"Solution: {func()}")

    def execute_all(self):

        print("\nSolutions to LCS\n")

        for name, solution in self.solutions.items():
            print(f'Algo-Name: {name} {" -" * 90}')
            self.run(solution)
            print('-' * 100)


LCS("ABCDGHI", "AEDFHRK").execute_all()
LCS("abcdeabcdeabcde", "qwrtyqwrtyqwrty").execute_all()
LCS("SAGGTAB", "PGXTXAYB").execute_all()

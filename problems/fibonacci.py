"""
Problem Statement:

To calculate the Nth number of Fibonacci sequence.
"""

import typing as t
from functools import lru_cache, partial
from utils.decorators import time_this


class Fibonacci:
    def __init__(self, n):
        self.solutions = {
            "recursive": partial(self.recursive, n),
            "dynamic_programming": partial(self.dp, n),
            "dp_lru_cache": partial(self.dp_lru_cache, n),
            "dp_tabulation": partial(self.dp_tabulation, n),
        }

    @staticmethod
    def recursive(n):
        """
        Time complexity: O(2^N)
        Space Complexity: O(N)

        :param m:
        :param n:
        :return:
        """
        if n <= 2:
            return 1
        else:
            return Fibonacci.recursive(n - 1) + Fibonacci.recursive(n - 2)

    @staticmethod
    def dp(n: int, memo: dict = None) -> int:
        """
        Time complexity: O(N)
        Space Complexity: O(N)
        :param n:
        :param memo:
        :return:
        """
        if memo is None:
            memo = {}
        val = memo.get(n)
        if val:
            return val
        if n <= 2:
            return 1
        else:
            memo[n] = Fibonacci.dp(n - 1, memo) + Fibonacci.dp(n - 2, memo)
            return memo[n]

    @staticmethod
    @lru_cache
    def dp_lru_cache(n):
        """
        Time complexity: O(N)
        Space Complexity: O(N)

        :param m:
        :param n:
        :return:
        """
        if n <= 2:
            return 1
        else:
            return Fibonacci.dp_lru_cache(n - 1) + Fibonacci.dp_lru_cache(n - 2)

    @staticmethod
    def dp_tabulation(n):
        """
        Time complexity: O(N)
        Space Complexity: O(N)

        :param n:
        :return:
        """
        fib_seq = [0, 1]
        for i in range(2, n + 1):
            fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])
        return fib_seq[n]

    @staticmethod
    @time_this()
    def run(func):
        print(f"Solution: {func()}")

    def execute_all(self):

        print("\nSolutions to Fibonacci\n")

        for name, solution in self.solutions.items():
            print(f'Algo-Name: {name} {" -" * 90}')
            self.run(solution)
            print('-' * 100)


Fibonacci(20).execute_all()

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
    def dp(n: int, fibo_sequence: t.List[int] = None) -> int:
        """
        Time complexity: O(N)
        Space Complexity: O(N)
        :param n:
        :param fibo_sequence:
        :return:
        """
        if fibo_sequence is None:
            fibo_sequence = [1, 1]
        if n > len(fibo_sequence):
            fibo_sequence.append(Fibonacci.dp(n - 1, fibo_sequence) + Fibonacci.dp(n - 2, fibo_sequence))
            return fibo_sequence[-1]
        else:
            return fibo_sequence[n - 1]

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
            return Fibonacci.recursive(n - 1) + Fibonacci.recursive(n - 2)

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

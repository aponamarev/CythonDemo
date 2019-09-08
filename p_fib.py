# Cython Fibonacci Demo
# Project: p_fib.py
# Description: raw python implementation of the fibonacci sequence
# Author: Alexander Ponamarev


def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

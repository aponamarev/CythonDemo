# Cython Fibonacci Demo
# Project: c_fib.pyx
# Description: Cython implementation of the fibonacci sequence
# Author: Alexander Ponamarev
# Created Date: 4/19/18
# IQVIA. All Rights Reserved.

cpdef int fib(int n):
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)
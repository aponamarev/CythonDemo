# Cython Fibonacci Demo
# Project: run_test.py
# Description: measure execution times of raw python and cython implementations of Fibonacci sequence
# Author: Alexander Ponamarev
# Created Date: 4/19/18
# IQVIA. All Rights Reserved.

import pyximport
pyximport.install(reload_support=True)
from time import time
import c_fib, p_fib


def main():

    n = 36

    p_start, _f, p_end = time(), p_fib.fib(n), time()
    c_start, _f, c_end = time(), c_fib.fib(n), time()
    print "Implementation of Fibonacci sequence: fib(" + str(n) + ") = " + str(_f)
    print "Python execution time: " + str(p_end - p_start) + " seconds"
    print "Cython execution time: " + str(c_end - c_start) + " seconds"

    return 0


if __name__ == '__main__':
    main()

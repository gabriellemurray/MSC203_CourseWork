#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 09:17:17 2024

@author: gabriellemurray
"""
import math

def RollingStatUpdate(x, n, mean, variance):
    n_update = n + 1
    if n == 0:
       variance_update = 0
    else:
       variance_update = (n_update - 2) * variance /(n_update - 1) + ((x - mean) ** 2) / n_update
    mean_update = mean + (x - mean) / n_update 
    return n_update, mean_update, variance_update

def main(): 
    n = 0
    mean = 0.0
    variance = 0.0
    x = float(input("Enter a temperature measuremnt:"))
    while x > -999: 
        n, mean, variance = RollingStatUpdate(x, n, mean, variance)
        stddev = math.sqrt(variance)
        x = float(input("Enter a temperature measuremnt (less than -999 to stop:)"))
    print("For", n, "measurements, the mean is:", mean, "and the standard deviation is:", stddev)
main()
        
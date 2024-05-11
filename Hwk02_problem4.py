#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 15:50:03 2024

@author: gabriellemurray
"""
import math 

def BLUEEstimator(T1, T2, stddev1, stddev2):
    a = stddev1 ** 2 / (stddev1 ** 2 + stddev2 **2)
    meana = a * T1 + (1 - a) * T2
    stddeva = math.sqrt(stddev1 ** 2 * stddev2 **2 / (stddev1 ** 2 + stddev2 **2))
    return meana, stddeva

def main(): 
    T1 = float(input("Enter the temperature from the first instrument:"))
    stddev1 = float(input("Enter the standard deviation from the first instrument:"))
    T2 = float(input("Enter the temperature from the second instrument:"))
    stddev2 = float(input("Enter the standard deviation from the second instrument:"))
    Ta, stddeva = BLUEEstimator(T1, T2, stddev1, stddev2)
    
    print("The blue estimate is:", round(Ta, 2), "and its estimated standard deviation is:", round(stddeva, 2))
main()
    

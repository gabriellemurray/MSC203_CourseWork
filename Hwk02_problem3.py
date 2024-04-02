#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 15:29:29 2024

@author: gabriellemurray
"""

import math 
import matplotlib.pyplot as plt
import numpy as np

def LogisticFunction(po, pmax, T, t):       # initial pop, max pop, reproduction time rate, time
    p = pmax / (1+ (pmax - po) / po * math.exp(-t / T))
    return p 

def main():
    t = np.linspace(0, 100, 201)            # this function generates an array of evenly spaced numbers over the specified interva;
    po = 1
    pmax = 100
    T= 10
    p = []
    for time in t:    
        population = LogisticFunction(po, pmax, T, time)
        p.append(population)
    plt.plot(t, p)
    plt.xlabel("Time")
    plt.ylabel("Population")
    plt.title("Population Growth with Time")
    plt.show()
main()
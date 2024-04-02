#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 09:03:56 2024

@author: gabriellemurray
"""

import matplotlib.pyplot as plt
import math 

def probability(x, xmean, xstd):
    probabilityx = 1 / (xstd * math.sqrt(2 * math.pi)) * math.exp(-0.5 * ((x - xmean)/xstd)**2)
    return probabilityx

def plot(xmin, xmax, N, xmean, xstd, xsymbol):
    dx = (xmax-xmin)/N     
    x = []
    p = []
    for i in range(0, N+1):
        xi = i * dx + xmin
        pi = probability(xi, xmean, xstd)
        x.append(xi)
        p.append(pi)
    plot = plt.plot(x , p, xsymbol)
    return plot

def main():
    men_avheight = 70
    men_stddev = 4
    women_avheight = 65
    women_stddev = 3.5
    hmin = 36
    hmax = 96
    N = 200
    plot(hmin, hmax, N, men_avheight, men_stddev, 'bx')
    plot(hmin, hmax, N, women_avheight, women_stddev, 'ro')
    plt.xlabel('height in inches')
    plt.ylabel('probability')
    plt.title("Normal Distribution of Men and Women Heights In USA")
    plt.show()
    plt.savefig('heightdlist.png')
main()
    

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 09:17:10 2024

@author: gabriellemurray
"""
import math
import random
import matplotlib.pyplot as plt

def PredatorDetection(xf, yf, u, v, xp, yp):
    maxdist = 100
    maxang = 120
    r = math.sqrt((xp - xf) ** 2 + (yp - yf) ** 2)
    num = u * (xp - xf) + v * (yp - yf)
    den = r * math.sqrt(u ** 2 + v ** 2)
    alpha = 180 / math.pi * (math.acos(num / den))
    if r < maxdist and abs(alpha) < maxang: 
        return True
    else:
        return False

def main(): 
    xf, yf = 0, 0
    u, v = 1, 0
   
    detectedpoints = []
    undetectedpoints = []
   
    for i in range(100):
        xp, yp = random.uniform(-150.0, 150.0), random.uniform(-150.0, 150.0)
        found = PredatorDetection(xf, yf, u, v, xp, yp)
        if found == True: 
            detectedpoints.append((xp, yp))
        else:
            undetectedpoints.append((xp,yp))
    
    for point in detectedpoints:
        plt.plot(point[0], point[1], "ro")
    for point in undetectedpoints:
        plt.plot(point[0], point[1], "ko")
    
    plt.show()
main()
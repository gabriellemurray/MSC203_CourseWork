#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 15:34:49 2024

@author: gabriellemurray
"""
import math

def idealgaslaw(V, n, R, T):
    P = n * R * T / V                                 # compute the pressure using the ideal gas law
    return P                                          

#r = float(input("Enter vessel radius in meters: "))   # get the radius from the user 
radiilist = [0.2, 0.4, 0.8, 1.6]
T = float(input("Enter temperature in Kelvins: "))    # get the temperature from the user
n = float(input("Enter number of moles: "))           # get the number of moles from the user
R = 8.314                                             # the gas constant is 8.314 J/K*mol
                        
for r in radiilist: 
    V = 4 * math.pi * r**3 / 3                        # compute the volume of a sphere
    pressure = idealgaslaw(V, n, R, T)                                  
    print("Expected pressure for radius", r, "m in Pa is:", pressure)

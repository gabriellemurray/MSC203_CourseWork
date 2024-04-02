#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 10:37:05 2024

@author: gabriellemurray
"""
import math 

def masscylinder(r, density, l, alpha):
    M = density * r**2 * l * (alpha - 0.5 * math.sin(2 * alpha))
    return M

angles = [10, 20, 30, 40, 50, 60, 70]

R = 1.2
L = 1.5
densitywater = 1025

for alpha in angles: 
    alphar = alpha * (math.pi / 180)
    mass = masscylinder (R, densitywater, L, alphar)
    print ("The mass of the cylinder at", alpha, "degrees is", mass, "kg.")
    
    


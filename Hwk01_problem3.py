#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 12:03:21 2024

@author: gabriellemurray
"""
import math

def deg2rad(alphad):
    r = math.pi / 180 * alphad
    return r

def rad2deg(alphar):
    d = 180 / math.pi * alphar
    return d

#alphad = float(input("Enter an angle in degrees:"))
anglesdeg = [15.0, 30.0, 45.0, 60.0, 90.0]
anglesrad = [0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0]

for angle in anglesdeg:
    alphar = deg2rad(angle)
    print(angle, "degrees corresponds to", round(alphar, 2), "radians.")
    
for angle in anglesrad:
    alphad = rad2deg(angle)
    print(angle, "radians corresponds to", round(alphad, 2), "degrees.")

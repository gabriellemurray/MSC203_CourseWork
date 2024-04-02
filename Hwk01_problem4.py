#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 10:17:10 2024

@author: gabriellemurray
"""

def forcegravity(mass1, mass2, distance):
    G = 6.674e-11
    F = G * mass1 * mass2 / distance**2
    return F

massearth = 5.972e24
massmoon = 7.348e22
perigeedistance = 356400
apogeedistance = 406700

P = forcegravity(massearth, massmoon, perigeedistance)
Q = forcegravity(massearth, massmoon, apogeedistance)

print("The force at the perigee is", P, "Newton")
print("The force at the apogee is", Q, "Newton")
print("The change in force is", P-Q, "Newton")


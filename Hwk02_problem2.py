#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 13:25:54 2024

@author: gabriellemurray
"""

import math 

def DistanceonSphere (radius, lon1, lat1, lon2, lat2):
    rlon1 = math.pi / 180 * lon1 # convert degrees to radians
    rlat1 = math.pi / 180 * lat1 # convert degrees to radians
    rlon2 = math.pi / 180 * lon2 # convert degrees to radians
    rlat2 = math.pi / 180 * lat2 # convert degrees to radians
    distance = radius * math.acos(math.sin(rlat1) * math.sin(rlat2) + math.cos(rlat1) * math.cos(rlat2) * math.cos(rlon1 - rlon2))
    return distance

def main():
    re = 6371    # radius of the earth in kilometers
    
    lon1 = float(input("Enter the longitude of the first city in degrees:"))
    lat1 = float(input("Enter the latitude of the first city in degrees:"))
    lon2 = float(input("Enter the longitude of the second city in degrees:"))
    lat2 = float(input("Enter the latitude of the second city in degrees:"))
    
    distancecities = DistanceonSphere(re, lon1, lat1, lon2, lat2)
    
    print("The distance between the two cities is", distancecities, "km.")
main()
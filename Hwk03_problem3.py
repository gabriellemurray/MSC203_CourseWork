#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 21:55:58 2024

@author: gabriellemurray
"""

def isleapyear(year):
    if year % 4 == 0 and year % 100 != 0: 
        print("True")
    elif year % 400 == 0:
        print("True")
    else:
        print("False")
    
def main():
    year = int(input("Enter a year to see if it is a leap year:"))
    isleapyear(year)
main()
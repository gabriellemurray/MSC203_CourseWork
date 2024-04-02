#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 18:35:03 2024

@author: gabriellemurray
"""
import datetime

def GenerateFCfilename(year):
    filename = "FC_cable_transport_{year}.txt".format(year=year)
    return filename

def CountHeaderLines(stringList, specialc):
    nheaders = 0     #initialize the counter
    for line in stringList:
        if line[0] == specialc:
            nheaders += 1
    return nheaders

def Processing(string):
    parts = string.split()
    year = int(parts[0])
    month = int(parts[1])
    day = int(parts[2])
    transport = float(parts[3])
    date = datetime.date(year, month, day)
    return date, transport 

def main():
    
    #invocation of 7.1
    
    for year in range (1990, 1996):
        filename = GenerateFCfilename(year)
        print(filename)
    
    #invocation of 7.2
    
    carthelist = ['% ', '% ', '% ', '% ', '% ', 'CARTHE_001', 'CARTHE_001']
    FCList = ['% Christopher.Meinen@noaa.gov',
          '% (305) 361-4355',
          '% Table updated: 11-Jan-2005',
          '%',
          '%',
          '% Year Month Day Transport',
          '% [Sv]',
          '1990 1 1 31.1',
          '1990 1 2 33.4',
          '1990 1 3 33.0']

    nheadersc = CountHeaderLines(carthelist, '%')
    nheadersFC = CountHeaderLines(FCList, '%')
    print('The number of headers in carthelist is:',nheadersc,'and the number of headers in FCList is:', nheadersFC)
    
    #invocation of 7.3
    
    FCData = ['1990 1 1 31.1',
              '1990 1 2 33.4',
              '1990 1 3 33.0',
              '1990 1 4 33.0',
              '1990 1 5 33.4',
              '1990 1 6 30.4',
              '1990 1 7 30.4',
              '1990 1 8 29.8',
              '1990 1 9 29.2',
              '1990 1 10 29.4',
              '1990 1 11 29.9',
              '1990 1 12 29.5',
              '1990 1 13 31.1',
              '1990 1 14 29.8',
              '1990 1 15 28.3',
              '1990 1 16 28.8']
    
    for line in FCData:
        date, transport = Processing(line)
        print('Date:', date, 'Transport:', transport)
    
main()
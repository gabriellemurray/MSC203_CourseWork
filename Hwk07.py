#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 13:54:36 2024

@author: gabriellemurray
"""
import numpy as np
import matplotlib.pyplot as plt

def YearMonth2YearFraction(year,month):   # Converts the data as a year and month to a year fraction
    yfrac = year+ month/12.
    return yfrac

def ReadTidalData(filename, numberofHeaderLines):   # Reads tidal data skipping over headerlines and returns the yearfractions and tides
    fileObj = open(filename,'r')    # open file
    lineList = fileObj.readlines()  # read it as list of lines
    fileObj.close()                 # close the file
    
    ndata = len(lineList)-1                     # number of data items, 1 header row
    yearfrac, tides = ndata*[0.0], ndata*[0.0]  # initialize empty lists
    for i,line in enumerate(lineList[numberofHeaderLines:]):          # loop over data lines
        wordlist = line.split()             # split line into words
        year = float(wordlist[0])             # extract year
        month = float(wordlist[1])            # extract month
        yearfrac[i] = YearMonth2YearFraction(year,month)   # compute the year fraction 
        tides[i] = float( wordlist[2])      # extract tides
    return yearfrac, tides

def main():    # invokes the ReadTidalData function and plots the data from different US coastal locations
    filenames = ['/Users/gabriellemurray/VirginiaKey8723214_meantrend.txt', '/Users/gabriellemurray/Philadelphia8545240_meantrend.txt', '/Users/gabriellemurray/LaJolla9410230_meantrend.txt', 
                 '/Users/gabriellemurray/SanFrancisco9414290_meantrend.txt', '/Users/gabriellemurray/Seattle9447130_meantrend.txt', '/Users/gabriellemurray/Honolulu1612340_meantrend.txt']
    cities = ['Virginia Key', 'Philadelphia', 'La Jolla', 'San Francisco', 'Seattle', 'Honolulu']
    for file, city in zip(filenames, cities):
        ts, fs = ReadTidalData(file, 1)
        n = 1 # degree 1 for linear regression 
        a = np.polyfit(ts,fs,n)
        qs = [0.0] * len(fs)
        for i, t in enumerate(ts): 
            qs[i] = a[1] + a[0]*t
        levelmm = a[0] * 1000 
        fig,ax = plt.subplots()
        ax.plot(ts,fs,'k-+',label='samples')
        ax.plot(ts,qs,'r-',label='regression')
        ax.set_xlabel('Year')
        ax.set_ylabel('Monthly Mean Sea Level (mm)')
        ax.set_title(f"{city}: {levelmm:.4f} mm/year")
        fig.savefig(f"{city}_plot.png")
        print('City:', city, ', sea level rise: {:.4f} mm/year'.format(levelmm))
main()
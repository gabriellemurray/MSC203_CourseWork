#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 15:05:49 2024

@author: gabriellemurray
"""

import datetime
import matplotlib.pyplot as plt
import numpy as np 

def CountHeaderLines(stringList, specialc):
    nheaders = 0     #initialize the counter
    for line in stringList:
        if line[0] == specialc:
            nheaders += 1
    return nheaders

def ReadFCFile(filename, spchar):
    fileObj = open(filename,'r')    # open file
    lineList = fileObj.readlines()  # read it as list of lines
    fileObj.close()                 # close the file
    
    nheaders = CountHeaderLines(lineList,spchar)
    
    ndata = len(lineList) - nheaders         # number of data items
    year, month, day, dates, Q = ndata*[0.0], ndata*[0.0], ndata*[0.0], ndata*[0.0], ndata*[0.0]  # initialize empty lists
    for i,line in enumerate(lineList[nheaders:]): # loop over data lines, skipping headers
        wordlist = line.split()      # split line into words
        year[i] = int(wordlist[0])   # extract year
        month[i] = int( wordlist[1]) # extract month
        day[i] = int(wordlist[2])    # extract day
        dates[i] = datetime.date(year[i], month[i], day[i])
        Q[i] = float(wordlist[3])       # extract transport
    return dates, Q


def ReadFCFiles(startyear,endyear):
    allQs = []
    alldates = []
    for year in range (startyear, endyear+1):
        if year == 1999:
            continue
        else: 
            filename = "/Users/gabriellemurray/FloridaCurrent/FC_cable_transport_{year}.txt".format(year=year)
            dates, Q = ReadFCFile(filename, '%')
            allQs.extend(Q)
            alldates.extend(dates)
    return alldates, allQs


def main():
    dates, Q = ReadFCFiles(1982, 2023)
    plt.plot(dates,Q,'#f8ccdb')       # plot
    ax = plt.gca()                       # get axis object
    ax.set_xlabel('date')                # label x-axis
    ax.set_ylabel('Florida Current Transport in Sv')          # label y-axis
    
    #Stats
    Qar = np.array(Q)
    Qmean = np.nanmean(Qar)
    ax.axhline(Qmean, c='r', linestyle='-')
    Qmedian = np.nanmedian(Qar)
    ax.axhline(Qmedian, c='m', linestyle='-')
    Qstd = np.nanstd(Qar)
    ax.axhline(Qmean+Qstd, c='r', linestyle='--')
    ax.axhline(Qmean-Qstd, c='r', linestyle='--')
    Qmin = np.nanmin(Qar)
    ax.axhline(Qmin, c='k', linestyle='--')
    Qmax = np.nanmax(Qar)
    ax.axhline(Qmax, c='k', linestyle='--')
    title = 'FC mean:{:4.1f}, std:{:4.1f}, median:{}, min:{}, max:{} Sv'.format(Qmean, Qstd, Qmedian, Qmin, Qmax)
    ax.set_title(title)
    plt.show()
        
main()
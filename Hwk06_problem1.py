#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 11:19:49 2024

@author: gabriellemurray
"""
import matplotlib.pyplot as plt

def CountHeaderLines(stringList, specialc):
    nheaders = 0     #initialize the counter
    for line in stringList:
        if line[0] == specialc:
            nheaders += 1
    return nheaders

def ReadCO2Icecores(filename, spchar):
    fileObj = open(filename,'r')    # open file
    lineList = fileObj.readlines()  # read it as list of lines
    fileObj.close()                 # close the file
    
    nheaders = CountHeaderLines(lineList,spchar)
    
    ndata = len(lineList) - nheaders               # number of data items
    year, concentration = ndata*[0.0], ndata*[0.0] # initialize empty lists
    for i,line in enumerate(lineList[nheaders:]): # loop over data lines, skipping headers
        wordlist = line.split()      # split line into words
        year[i] = -float(wordlist[0])   # extract year
        concentration[i] = float( wordlist[1]) # extract concentration
    return year, concentration

def main():
    filename = '/Users/gabriellemurray/co2icecoresantarctica2015co2.txt'
    year, concentration = ReadCO2Icecores(filename, '#')
    plt.plot(year,concentration,'b')     # plot
    ax = plt.gca()                       # get axis object
    ax.set_xlabel('Years before present')                # label x-axis
    ax.set_ylabel('CO2 Concentration [ppmv]')   # label y-axis
    ax.set_title('CO2 Concentrations')
    plt.savefig('IceCore_CO2_Concentrations')
    plt.show()
main()
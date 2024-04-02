#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 09:44:12 2024

@author: gabriellemurray
"""
import random 
import matplotlib.pyplot as plt

def RunExperiment(Ncouples, avmenheight, stddevmen, avwomenheight, stddevwomen): 
    ntallerWomen = 0
    tallerwoman = []
    shorterman = []
    shorterwoman = []
    tallerman = []
    for n in range(Ncouples):
        hman = random.gauss(avmenheight, stddevmen)
        hwoman = random.gauss(avwomenheight, stddevwomen)
        if hwoman > hman: 
            ntallerWomen += 1
            tallerwoman.append(hwoman)
            shorterman.append(hman)
        else: 
            shorterwoman.append(hwoman)
            tallerman.append(hman)
            
    plt.plot(shorterman, tallerwoman, 'ro')
    plt.plot(tallerman, shorterwoman, 'ko')
    p = ntallerWomen/Ncouples
    return p

def main():

    avmenheight = 70 
    stddevmen = 4
    avwomenheight = 65
    stddevwomen = 3.5 
    Ncouples = 1                           #initialize to start loop 
    while Ncouples > 0: 
        Ncouples = int(input("Enter the number of couples to form (less than 0 to stop):"))
        if Ncouples <=0: 
            break
        p = RunExperiment(Ncouples, avmenheight, stddevmen, avwomenheight, stddevwomen)
        print("For", Ncouples, "couples, the probability that the woman is taller than the man is:", p)
    plt.xlabel('man height in inches')
    plt.ylabel('woman height in inches')
    plt.title("Couples Height In USA")
    plt.show()

main()
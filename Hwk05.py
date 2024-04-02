#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 6 13:58:24 2024

@author: gabriellemurray
"""

import matplotlib.pyplot as plt
import matplotlib.patches as pat
import random
import statistics
import math


def MoveParticlesUniform(xlist, ylist, dstd):
    numparticles = len(xlist)
    for i in range(numparticles):
        dmax = math.sqrt(3)*dstd
        dx = random.uniform(-dmax,dmax)
        dy = random.uniform(-dmax,dmax)
        xlist[i] += dx
        ylist[i] += dy

def MoveParticlesGaussian(xlist, ylist, dstd):
    numparticles = len(xlist)
    for i in range(numparticles):
        dx = random.gauss(0, dstd)
        dy = random.gauss(0,dstd)
        xlist[i] += dx
        ylist[i] += dy
  
def meanstddev(xlist, ylist):    
    xav = statistics.mean(xlist)
    yav = statistics.mean(ylist)
    xstddev = statistics.stdev(xlist)
    ystddev = statistics.stdev(ylist)
    return xav, yav, xstddev, ystddev

def ReleaseLarvae(disttype, dstd, P, N):
    xlist = P * [0.0]
    ylist = P * [0.0]
    
    plt.ion()                           # turn on interactive plotting
    fig,ax = plt.subplots()             # create figure and axis
    halfwidth = 1.0
    ax.set_xlim([-halfwidth,halfwidth]) # define x-limits
    ax.set_ylim([-halfwidth,halfwidth]) # define y-limits
    ax.set_aspect('equal')              # make aspect ratio equal
    ax.set_xlabel('x')                  # label x-axis
    ax.set_ylabel('y')                  # label y-axis
    ax.set_title('PDF is {} Standard-dev={}'.format(disttype, dstd))    # set title
    
    spreadhistory = []

    marker = ax.scatter(xlist, ylist, color='green', s=0.5)
    xav, yav, sx, sy = meanstddev(xlist, ylist)
    ellipse1 = pat.Ellipse(xy=[xav, yav], width=4*sx, height=4*sy, edgecolor='r', linewidth=2, fill=False, zorder=5)
    ax.add_patch(ellipse1)
    plt.show()

    for n in range(N):
        if disttype == 'Uniform' : 
           MoveParticlesUniform(xlist, ylist, dstd)  
           marker.set_offsets(list(zip(xlist, ylist)))             # update marker 
           spreadhistory.append((sx+sy)/2)                         # append spread history
           xav, yav, sx, sy = meanstddev(xlist, ylist)             # update center of mass and spread
           ellipse1.center = [xav,yav]
           ellipse1.width = 4 * sx
           ellipse1.height = 4 * sy
           fig.canvas.draw()  
        elif disttype == 'Gaussian':
           MoveParticlesGaussian(xlist, ylist, dstd)               # move particles
           marker.set_offsets(list(zip(xlist, ylist)))             # update marker
           spreadhistory.append((sx+sy)/2)                         # append spread history
           xav, yav, sx, sy = meanstddev(xlist, ylist)             # update center of mass and spread
           ellipse1.center = [xav,yav]
           ellipse1.width = 4 * sx
           ellipse1.height = 4 * sy
           fig.canvas.draw()                              # refresh canvas
    fig.savefig('LarvalDispersal_{}_{}.png'.format(disttype, dstd)) # save the particle plot
    
    return spreadhistory

def main():
  
    P = 2000
    N = 100
    spreadhistory1 = ReleaseLarvae('Uniform', 0.01, P, N)
    spreadhistory2 = ReleaseLarvae('Uniform', 0.02, P, N)
    spreadhistory3 = ReleaseLarvae('Gaussian', 0.01, P, N)
    spreadhistory4 = ReleaseLarvae('Gaussian', 0.02, P, N)
    
    plt.figure()
    plt.xlabel('N')
    plt.ylabel('Spread')
    plt.title("Spread history")
    plt.plot(range(N), spreadhistory1, 'b--', label='Uniform, d:0.01')
    plt.plot(range(N), spreadhistory2, 'r--', label='Uniform, d:0.02')
    plt.plot(range(N), spreadhistory3, 'b-', label='Gaussian, d:0.01')
    plt.plot(range(N), spreadhistory4, 'r-', label='Gaussian, d:0.02')
    plt.legend()
    plt.savefig('LarvalDispersal_SpreadHistory.png')
    plt.show()
main()    

    
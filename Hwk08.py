#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 11:24:29 2024

@author: gabriellemurray
"""
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import numpy as np

def MapInitPlot(lonlim,latlim):
   
    fig = plt.figure()                     # create a figure
    projObj = ccrs.PlateCarree()           # define PlateCarree projection
    ax = plt.axes(projection=projObj)      # generate an axis given the projObj
    ax.set_extent(lonlim+latlim)           # define extent of the map
    ax.coastlines(resolution='50m')        # draw the coastlines overriding the default 110m resolution
    ax.add_feature(cfeature.LAND)          # add land feature using the default land color
    ax.add_feature(cfeature.OCEAN)         # add ocean feature using the default ocean color
    ax.gridlines(draw_labels=True)         # add grid lines with labels (either gridlines or x,y ticks
    
    return fig,ax,projObj
   
def ReadCartheFile(filename):
    fileObj = open(filename,'r')          # open file
    lineList = fileObj.readlines()        # read it as list of lines
    fileObj.close()                       # close the file
    
    ndata = len(lineList)                 # number of data items
    lona, lata = ndata*[0.0], ndata*[0.0] # initialize empty lists
    for i,line in enumerate(lineList):    # loop over data lines, skipping headers
        wordlist = line.split()           # split line into words
        lata[i] = float(wordlist[2])      # extract latitude
        lona[i] = float(wordlist[3])      # extract longitude  
    return lona, lata

def FDAcd2(f,dt):
    M = len(f)
    df = np.zeros(M)
    df[1:M-1] = (f[2:M] - f[0:M-2]) / (2 * dt)
    df[0] = (-3 * f[0] + 4 * f[1] - f[2]) / (2 * dt)
    df[M-1] = (3 * f[M-1] - 4 * f[M-2] + f[M-3]) / (2 * dt)
    return df

def VisualizeDriftTraject(lona,lata,color,projObj,ax,fig):
    ax.plot(lona,lata,color=color,transform=projObj)        # plots trajectory
    ax.plot(lona[0], lata[0], marker= '+', color=color)
    ax.plot(lona[-1], lata[-1], marker='o', color=color)
    fig.canvas.draw()
    plt.pause(0.1)

def DrifterVelocity(lona,lata,dt):
    R = 6371e3 
    lonr, latr = np.radians(lona), np.radians(lata)
    N = len(lonr)
    ua = np.zeros(N) 
    va = np.zeros(N)
    dlon = FDAcd2(lonr, dt)
    dlat = FDAcd2(latr, dt)
    ua[0:N] = R * np.cos(latr[0:N])* dlon[0:N]
    va[0:N] = R * dlat[0:N]
    return ua, va

def main(): 
    dt = 900
    latlim = [21,30]
    lonlim = [-90,-81]
    skip = 8
    fig, ax, projObj = MapInitPlot(lonlim, latlim)
    drifterTagList = [1,2,3,4,5,6,7,8,10,11]
    colors = ['#FF5733', '#3366FF', '#33FF57', '#FFA833', '#9933FF',
              '#FFFF33', '#33FFFF', '#FF33FF', '#33FFCC', '#FF33CC']
    for tag, color in zip(drifterTagList, colors):
        if tag < 10:
            filename = "/Users/gabriellemurray/CARTHE_00{}.dat".format(tag)
        else: 
            filename = "/Users/gabriellemurray/CARTHE_0{}.dat".format(tag)
        lond, latd = ReadCartheFile(filename)
        u, v = DrifterVelocity(lond,latd,dt)
        s = np.sqrt(u**2 + v**2)
        smean = np.mean(s)
        sstdev = np.std(s)
        smax = np.max(s)
        print(f"For drifter {tag}, the number of positions reported is {len(lond)}, the launch longitude is {lond[0]} and the launch latitude is {latd[0]}.")
        print(f"The last longitude reported is {lond[-1]} and the last latitude reported is {latd[-1]}.The mean speed was {smean} m/s, the standard deviation was {sstdev}, and the maximum speed was {smax} m/s.")
        VisualizeDriftTraject(lond, latd, color,projObj, ax, fig)
        ax.quiver(lond[::skip], latd[::skip], u[::skip], v[::skip],transform=projObj)
    plt.show()
    
main()
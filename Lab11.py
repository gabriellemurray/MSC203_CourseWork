#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 15:30:26 2024

@author: gabriellemurray
"""

import matplotlib.pyplot as plt

def ReadXBTFile(xbtFile, nHeaderLines=0):   
    fileObj = open(xbtFile,'r')    # open file
    lineList = fileObj.readlines()  # read it as list of lines
    fileObj.close()                 # close the file
    
    ndata = len(lineList) - nHeaderLines                     # number of data items, 1 header row
    p, t, th, salt, dynh, d = ndata*[0.0], ndata*[0.0], ndata*[0.0], ndata*[0.0], ndata*[0.0], ndata*[0.0]
    for i,line in enumerate(lineList[nHeaderLines:]):          # loop over data lines
        wordlist = line.split()            
        p[i] = float(wordlist[0])
        t[i] = float(wordlist[1])            
        th[i] = float(wordlist[2]) 
        salt[i] = float(wordlist[3]) 
        dynh[i] = float(wordlist[4]) 
        d[i] = float(wordlist[5])  
    line12 = lineList[11].split()
    pu, tu, thu, saltu, dynhu, du = str(line12[0]), str(line12[1]), str(line12[2]), str(line12[3]), str(line12[4]), str(line12[5])
    line2 = lineList[1].split()
    cast, lat, lon, date, time = str(line2[0]), str(line2[1]), str(line2[2]), str(line2[4]), str(line2[5])
    xbtdict = {'pressure':p, 'temp':t, 'th':th, 'salt':salt, 'dynh':dynh, 'depth':d, 'presunits':pu, 'tempunits':tu, 'thunits':thu, 
               'saltunits':saltu, 'dynhunits':dynhu, 'depthunits':du, 'lat':lat, 'lon':lon, 'time':time,
               'date':date, 'cast':cast}  
    return xbtdict

def CreateFigure(xlabel,ylabel,titleString):
    fig,ax = plt.subplots() # create figure and axis
    ax.set_xlabel(xlabel)  # set x-label (with units)
    ax.set_ylabel(ylabel)  # set y-label (with units)
    ax.set_title(titleString)
    return fig,ax

def PlotXBTData(ax,xdata, ydata, linelabel):
    """ Plots data contains in the arrays xdata,ydata, label the axes, add the title
        and save the plot to given file"""
    ax.plot(xdata,ydata,label=linelabel)


def main():
    xbtPath = '/Users/gabriellemurray/'
    Files = ['ax70319.242','ax70319.243', 'ax70319.244']
    for file in Files:
        xbtFile = xbtPath+file
        xbt = ReadXBTFile(xbtFile,nHeaderLines=12) # read the data
        negated_depth = []
        for depth in xbt['depth']:
            negated_depth.append(-depth)
        xbt['depth'] = negated_depth
    
        time = xbt['time']
        hours = time[:2]
        minutes = time[2:]
        timenew = hours + ':' + minutes
            
        # plotting temperature profiles
        xlabel,ylabel, titleString = 'Temperate in deg', 'depth in m', f'Temperature Depth Profile for ({xbt["lat"]},{xbt["lon"]}) at {timenew}'
        figT,axT = CreateFigure(xlabel,ylabel,titleString) # create figure for temperature

        print('The location of the cast was: (', xbt['lat'], ',', xbt['lon'], '), the date was:', xbt['date'], 'and the time was:', timenew)
        PlotXBTData(axT,xbt['temp'],xbt['depth'], 'Cast '+xbt['cast']) # plt T v depth
        axT.legend()
        figT.savefig('temperature.png') # save figure as png file

        # repeate for salinity profiles

main()
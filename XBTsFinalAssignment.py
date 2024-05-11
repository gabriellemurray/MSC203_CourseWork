#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 19:51:51 2024

@authors: gabriellemurray, karinajacobsen, mackenziehoffman
"""

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import glob 
import matplotlib.pyplot as plt
import numpy as np 

def ReadXBTFiles(filename, nHeaderLines=0):  
    fileObj = open(filename,'r')     # open file
    lineList = fileObj.readlines()   # read it as list of lines
    fileObj.close()                  # close the file
    
    ndata = len(lineList) - nHeaderLines   # compute the number of data points
    te, th, salt, depth, pressure = np.zeros(ndata), np.zeros(ndata), np.zeros(ndata), np.zeros(ndata), np.zeros(ndata) # initialize empty arrays 
    for i,line in enumerate(lineList[nHeaderLines:]):
        wordlist = line.split() 
        pressure[i] = float(wordlist[0])   # extract pressure        
        te[i] = float(wordlist[1])         # extract in-situ temp
        th[i] = float(wordlist[2])         # extract potential temp
        salt[i] = float(wordlist[3])       # extract salinity
        depth[i] = float(wordlist[5])      # extract depth
    line2 = lineList[1].split()
    lat, lon = float(line2[1]), float(line2[2]) # extract lat and lon of XBT cast
    return pressure, te, th, salt, depth, lat, lon
           
def eospolyPT(th,salt,p):
    '''
    The EoS is approximated with polynomial fits for the range
    0 <= p <= 1.e+8 Pa, 
    -2 <= T <= 40 deg C, and 
    0 <= S <= 40 psu (practical salinity units)
   
    reference:
    Daniel G. Wright (1997),
    An Equation of State for Use in Ocean Models: Eckartâs Formula Revisited
    DOI: https://doi.org/10.1175/1520-0426(1997)014<0735:AEOSFU>2.0.CO;2
    
    th: potential temperature in deg C
    salt: salt in psu units
    p: pressure in Pa
    rho: density in kg/m^3
    '''
    a = np.array([7.133718e-4, 2.724670e-7,-1.646582e-7])
    b = np.array([5.613770e+8, 3.600337e+6,-3.727194e+4, 1.660557e+2, 6.844158e+5,-8.389457e+3])
    c = np.array([1.609893e+5, 8.427815e+2,-6.931554   , 3.869318e-2,-1.664201e+2,-2.765195])

    alpha = a[0] + a[1]*th + a[2]*salt
    po = ((b[3]*th + b[2])*th+b[1])*th + b[0] + (b[4]+b[5]*th) * salt
    la = ((c[3]*th + c[2])*th+c[1])*th + c[0] + (c[4]+c[5]*th) * salt
    
    ppo = p+po
    rho = ppo/(la+alpha*ppo)
    return rho

def eospolyT(te,salt,p):
    '''
    The EoS is approximated with polynomial fits for the range
    0 <= p <= 1.e+8 Pa, 
    -2 <= T <= 40 deg C, and 
    0 <= S <= 40 psu (practical salinity units)
   
    reference:
    Daniel G. Wright (1997),
    An Equation of State for Use in Ocean Models: Eckartâs Formula Revisited
    DOI: https://doi.org/10.1175/1520-0426(1997)014<0735:AEOSFU>2.0.CO;2
    
    te: in-situ temp in deg C
    salt: salt in psu units
    p: pressure in Pa
    rho: density in kg/m^3
    '''
    a = np.array([ 6.992096e-4,-1.379636e-7,-1.557360e-7])
    b = np.array([ 5.921983e+8, 4.363083e+6,-4.044072e+4, 1.332455e+2, 6.835412e+5,-6.732489e+3])
    c = np.array([ 1.782008e+5, 1.358366e+3,-6.727308   , 2.162848e-2,-1.812464e+2,-2.567747])

    alpha = a[0] + a[1]*te + a[2]*salt
    po = ((b[3]*te + b[2])*te+b[1])*te + b[0] + (b[4]+b[5]*te) * salt
    la = ((c[3]*te + c[2])*te+c[1])*te + c[0] + (c[4]+c[5]*te) * salt
    
    ppo = p+po
    rho = ppo/(la+alpha*ppo)
    return rho

def CreateFigure(xlabel,ylabel,titleString):
    fig,ax = plt.subplots()   # create figure and axis
    ax.set_xlabel(xlabel)     # set x-label (with units)
    ax.set_ylabel(ylabel)     # set y-label (with units)
    ax.set_title(titleString) # set title
    return fig,ax

def Make2DArray(arraylist, rows, columns):
    array2D = np.full((rows, columns), np.nan)    # fill a 2D array of specified dimensions with NaNs
    for i, a in enumerate(arraylist):             # loop through all arrays in the specified list
       array2D[:len(a), i] = a                    # fill the 2D array with each 1D array
    return array2D
    
def main():
    filenames = glob.glob('ax70519.*')   # use glob package to extract desired files from working directory
    filenames.sort()                     # sort files by cast
    lats, lons = [], []                  # initialzie lat and lon lists
    telist, thlist, saltlist, plist = [], [], [], []   # initialize observations lists
    N = 0                                # initialize a counter for the number of files
    maxdepth = 0                 
    for i, file in enumerate(filenames): # loop through files to extract data
        pressure, te, th, salt, depth, lat, lon = ReadXBTFiles(file, nHeaderLines=12)
        ## append data arrays to lists ##
        if max(depth) > maxdepth:   # identify the longest depth array
            maxdepth = max(depth)   # update maxdepth for next iteration
            depths = depth          # update depths array 
        lats.append(lat) 
        lons.append(lon)
        telist.append(te)
        thlist.append(th)
        saltlist.append(salt)
        plist.append(pressure)
        N += 1  # update the counter to keep track of the number of files

    
    M = len(depths)                  # define the number of rows as the length of the depth array (includes the max depth)
    ta = Make2DArray(telist, M, N)   # make 2D array of temperatures, missing data is filled with NaNs
    tha = Make2DArray(thlist, M, N)  # make 2D array of potential temperatures, missing data is filled with NaNs
    sa = Make2DArray(saltlist, M, N) # make 2D array of salinity, missing data is filled with NaNs
    pa = Make2DArray(plist, M, N)    # make 2D array of pressure, missing data is filled with NaNs
    
    density = np.zeros([M,N])        # initialize density array to have the same shape as the XBT data
    potentdensity = np.zeros([M,N])  # initialize potential density array to have the same shape as the XBT data
    density[:,:] = eospolyT(ta, sa, pa)  # fill density array using density function 
    potentdensity[:,:] = eospolyPT(tha, sa, pa) # fill potential density array using potential density function 
    
    ######## create temperature plot #########
    xlabelT, ylabelT, titleStringT = 'Longitude', 'Depth (m)', 'Temperature Section (ºC)'
    figT, axT = CreateFigure(xlabelT, ylabelT, titleStringT)
    contours = axT.contourf(lons, depths, ta, levels=10, cmap='RdBu_r')
    plt.colorbar(contours)
    plt.gca().invert_yaxis()
    plt.show()
    
    ### create potential temperature plot ####
    xlabelTh, ylabelTh, titleStringTh = 'Longitude', 'Depth (m)', 'Potential Temperature Section (ºC)'
    figTh, axTh = CreateFigure(xlabelTh, ylabelTh, titleStringTh)
    contours = axTh.contourf(lons, depths, tha, levels=10, cmap='RdBu_r')
    plt.colorbar(contours)
    plt.gca().invert_yaxis()
    plt.show()
    
    ######### create salinity plot ###########
    xlabelS, ylabelS, titleStringS = 'Longitude', 'Depth (m)', 'Salinity Section (psu)'
    figS, axS = CreateFigure(xlabelS, ylabelS, titleStringS)
    contours = axS.contourf(lons, depths, sa, levels=10, cmap='RdBu_r')
    plt.colorbar(contours)
    plt.gca().invert_yaxis()
    plt.show()
   
    ########## create density plot ###########
    xlabelD, ylabelD, titleStringD = 'Longitude', 'Depth (m)', 'Density Section ('r'$kg/m^3$'')'
    figD, axD = CreateFigure(xlabelD, ylabelD, titleStringD)
    contours = axD.contourf(lons, depths, density, levels=10, cmap='RdBu_r')
    plt.colorbar(contours)
    plt.gca().invert_yaxis()
    plt.show()
   
    ##### create potential density plot ######
    xlabelPD, ylabelPD, titleStringPD = 'Longitude', 'Depth (m)', 'Potential Density Section ('r'$kg/m^3$'')'
    figPD, axPD = CreateFigure(xlabelPD, ylabelPD, titleStringPD)
    contours = axPD.contourf(lons, depths, density, levels=10, cmap='RdBu_r')
    plt.colorbar(contours)
    plt.gca().invert_yaxis()
    plt.show()
    
    ######## plotting the transect ###########
    #lonlim, latlim = [0, -50], [35, 85]       # define limits for AX1
    lonlim, latlim = [10,-100], [0,60]        # define limits for AX7
    fig = plt.figure()                        # create a figure
    projObj = ccrs.PlateCarree()              # define PlateCarree projection
    ax = plt.axes(projection=projObj)         # generate an axis given the projObj
    ax.stock_img()
    ax.coastlines(resolution='50m')           # draw the coastlines overriding the default 110m resolution
    ax.add_feature(cfeature.LAND)             # add land feature using the default land color
    ax.add_feature(cfeature.OCEAN)            # add ocean feature using the default ocean color
    ax.set_extent(lonlim+latlim)              # define extent of the map
    ax.gridlines(draw_labels=True)            # add grid lines with labels (either gridlines or x,y ticks)
    ax.plot(lons,lats,'r',label='Transect', transform=projObj)  # plot trajectory as a red line
    ax.legend()                               # add a legend
    fig.canvas.draw()
    
main()      
        
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 09:17:16 2024

@author: gabriellemurray
"""

import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import math

def GetCategory(windspeed):
    category = 0
    cat1or2 = 0
    catmajor = 0
    if windspeed >= 64 and windspeed <= 82: 
        category = 1
        cat1or2 += 1
    elif windspeed >= 83 and windspeed <= 95:
        category = 2
        cat1or2 +=1
    elif windspeed >= 96 and windspeed <= 112:
        category = 3
        catmajor += 1
    elif windspeed >= 113 and windspeed <= 136:
        category= 4
        catmajor += 1
    elif windspeed >= 137:
        category = 5
        catmajor += 1
    return category, cat1or2, catmajor

def GetSymbolColour(category):

    symbclr = ''
    if category == 0:
        symbclr = 'go'
    elif category == 1:
        symbclr = 'bo'
    elif category == 2:
        symbclr = 'yo'
    elif category == 3:
        symbclr = 'mo'
    elif category == 4 or category ==5:
        symbclr = 'ro'
    return symbclr

def GetHurVelocity(lon1, lat1, lon2, lat2, deltat):
    R = 6371
    lat1r = math.radians(lat1)
    lat2r = math.radians(lat2) 
    lon1r = math.radians(lon1)
    lon2r = math.radians(lon2)
    lonmid = (lon1 + lon2) / 2
    latmid = (lat1 + lat2) / 2
    latmidr = math.radians(latmid)
    u = R * math.cos(latmidr) * (lon2r - lon1r) / deltat
    v = R * (lat2r - lat1r) / deltat
    s = math.sqrt(u ** 2 + v ** 2)
    return lonmid, latmid, u, v, s

def make_world(): # Sfunction to set up map projection
    fig = plt.figure(figsize=(6,6), facecolor='white') # create the figure
    proj = ccrs.PlateCarree()                   # Choose projection
    ax = plt.axes(projection=proj, facecolor='white')  # create axes specify the projection
    
# the following add FEATURES such as land/ocean colors, political boundaries, lakes, etc
    ax.add_feature(cfeature.LAND)      # add land features
    ax.add_feature(cfeature.OCEAN)     # add ocean features
#   ax.add_feature(cfeature.LAND, facecolor='none', edgecolor='none')  # add LAND features
#   ax.add_feature(cfeature.OCEAN, facecolor='none', edgecolor='none') # add ocean features
    ax.add_feature(cfeature.BORDERS) # add political borders
    LAKES = cfeature.NaturalEarthFeature(category='physical', name='lakes',
                                         scale='10m', facecolor='blue',
                                         edgecolor='blue')
    ax.add_feature(LAKES)
    
    ax.coastlines('50m', color='black', zorder=2, linewidth=1) # drawcoastline in black
    gl = ax.gridlines(crs=proj, draw_labels=True, linewidth=1,
                      color='gray', alpha=0.5, linestyle=':')
    
    return fig,ax,proj


def main():
#define the longitude and latitudes and wmx of Hurricane Matthew 2016
# =============================================================================
    lons= [-59.8,-61.2,-62.6,-64.0,-65.5,-66.9,-68.1,-69.3,-70.4,-71.2,
          -71.9,-72.5,-73.1,-73.3,-73.5,-73.9,-74.3,-74.7,-75.0,-75.0,
          -75.0,-74.9,-74.6,-74.4,-74.3,-74.3,-74.3,-74.4,-74.8,-75.4,
          -76.0,-76.7,-77.5,-78.3,-79.0,-79.7,-80.3,-80.7,-80.6,-80.6,
          -79.9,-79.0,-77.3,-76.0]
    lats = [13.4,13.6,13.9,14.0,14.1,14.2,14.2,14.0,13.8,13.5,
            13.4,13.4,13.4,13.4,13.5,13.7,14.0,14.2,14.5,14.9,
            15.4,15.9,16.6,17.5,18.4,19.3,20.1,20.7,21.4,22.2,
            23.0,23.8,24.7,25.7,26.7,27.7,28.9,29.7,30.7,31.6,
            32.5,33.5,33.9,34.7]
    wmxs = [50,  50,  55,  55,  60,  65,  70,  85, 100, 120, 
            145, 140, 135, 130, 130, 125, 130, 135, 130, 125,
            125, 125, 130, 130, 125, 120, 115, 110, 105, 105,
            105, 110, 120, 120, 115, 110, 105, 100,  95 , 85,
             80,  70,  70, 70]
# =============================================================================
    
    fig, ax,proj = make_world()  # create the plot of the world
    h, = ax.plot(lons, lats, color='r', linestyle='--',linewidth=0.75,transform=proj)
    ax.set_title('Hurricane Matthew 2016 track', fontsize=20)
    ax.legend([h], ['track'])
    plt.savefig('Matthew2016_track.png', bbox_inches='tight')
    plt.show() # make sure to show AFTER saving because show() closes the figure
    
    cminor = 0
    cmajor = 0
    
    prev_lon, prev_lat = None, None
    
    for lon,lat,wmx in zip(lons,lats,wmxs):
        cat, cat1or2, catmajor = GetCategory(wmx)
        cminor += cat1or2
        cmajor += catmajor
        symbclr = GetSymbolColour(cat)
        ax.plot(lon, lat, symbclr, markersize=5, transform=proj)
        if prev_lon is not None and prev_lat is not None: 
            lonmid, latmid, u, v, s = GetHurVelocity(prev_lon, prev_lat, lon, lat, 6)
            print(lonmid, latmid, "deg,", s, "km/hr" )
            ax.quiver(lonmid, latmid, u, v, pivot='mid',color='k', transform=proj)
        prev_lon, prev_lat = lon, lat
    
    

    print("The storm was reported a cat 1 or 2", cminor, "-times")
    print("The storm was reported a major hurricane", cmajor, "-times")
    

    
main()
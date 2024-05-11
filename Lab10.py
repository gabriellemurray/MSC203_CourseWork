#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 12:25:42 2024

@author: gabriellemurray
"""

import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

def InitialPlot(pos, pExact):
    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection=ccrs.PlateCarree())

    # Plot all particles
    if pos.ndim < 2:
        lastPosition, = ax.plot(pos[0:1], pos[1:2], 'ro', label='RK3 prediction')
    else:
        lastPosition, = ax.plot(pos[:, 0], pos[:, 1], 'r*', label='prediction')

    ax.plot(pExact[:, 0], pExact[:, 1], 'b-', linewidth=0.5, label='exact')

    ax.set_global()
    ax.coastlines()
    ax.legend()
    plt.show()
    plt.pause(1e-17)

    return fig, lastPosition

def UpdatePlot(fig,lastPosition,pos):
#### Plot update
    if pos.ndim < 2:                         # check rank of array
      lastPosition.set_data(pos[0],pos[1])   # update single position on the plot
    else:
      lastPosition.set_data(pos[:,0],pos[:,1])   # update multiparticle position on the plot
    fig.canvas.draw()
    plt.pause(0.1)

def RK3(p, dt, timec, GetVelocity): # 3-stage Runge-Kutta integrator, 3rd order accurate but more complex than RK1
    w = GetVelocity(timec,p)       # stage 1 velocity
    pt = p + w*dt                  # stage 1 temp position
    w = GetVelocity(timec+dt, pt)  # stage 2 velocity
    pt = 0.75 * p + 0.25 * (pt + w*dt) # stage 2 temp position 
    w = GetVelocity(timec+0.5*dt, pt) # stage 3 velocity
    p += 2.0 * (pt + w*dt) / 3.0     # final position, note p is MUTABLE
    return

def ExactTrajectory(dt,ntimesteps): # for comparison with approximation
    tt = np.linspace(0,dt*ntimesteps,ntimesteps+1)
    p = np.zeros([ntimesteps+1,2])
#    p[:,0] = 0.2*tt; p[:,1]=1-0.0*tt # constant velocity
    p[:,0] = np.cos(tt+np.pi/2); p[:,1] = np.sin(tt+np.pi/2) # rotating flow
    return p

def GetVelocity(t,p):
    ''' Calculates the time rate of change of p given current time, timec, and state p'''
    R = 6.37122e6 
    Uo = 2 * np.pi * R / (12 * 86400)
    alpha = np.radians(10)
    lambd = np.radians(p[:,0])
    theta = np.radians(p[:,1])
    u = Uo * (np.cos(theta) * np.cos(alpha) + np.sin(theta) * np.cos(lambd) * np.sin(alpha))
    v = -Uo * np.sin(alpha) * np.sin(lambd)
    dlon = u / (R * np.cos(theta))
    dlat = v / R 
    w = np.zeros((len(p), 2))
    w[:,0] = dlon
    w[:,1] = dlat
    return w

##################################################
def main():  
# Inputs 
    nparticles = 3
    p = np.zeros([nparticles,2]) # create 2D array of particle positions
    #p[k,0] longitude of particle number k
    #p[k,1] latitude of particle number k
    #w[k,0] rate of change of longitude of particle number k
    #w[k,1] rate of change of latitude of particle number k    
    dt= 3600                 # timestep
    ntimesteps = 12 * 86400  # number of time steps (12 days)
    
    pExact = ExactTrajectory(dt,ntimesteps)    # for checking
    fig, lastPosition = InitialPlot(p,pExact) # initialize particle position
    
    for it in range(ntimesteps):        # time-loop
        timec = it * dt                 # set current time
        RK3(p, dt, timec, GetVelocity)  # Update position with Runge Kutta 3 integration-step
        UpdatePlot(fig,lastPosition,p)  # update the plot

main()
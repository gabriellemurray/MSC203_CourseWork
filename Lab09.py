#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 20:57:19 2024

@author: gabriellemurray
"""
import numpy as np 
import matplotlib.pyplot as plt

#Step 1
def FDAcd2(f,dt):
    M = len(f)
    df = [0.0] * M
    df[1:M-1] = (f[2:M] - f[0:M-2]) / (2 * dt)
    df[0] = (-3 * f[0] + 4 * f[1] - f[2]) / (2 * dt)
    df[M-1] = (3 * f[M-1] - 4 * f[M-2] + f[M-3]) / (2 * dt)
    return df

def Trajectory(ta):
    ''' sample trajectories'''
    xa = -0.2*ta + (1.0 + 0.50*np.cos(np.pi*ta)) * np.cos(4.0*np.pi*ta)
    ya =           (1.0 + 0.25*np.cos(np.pi*ta)) * np.sin(4.0*np.pi*ta)
    return xa,ya

def main():
    #Steps 2 and 3
    '''
    N = 100 #number of interval
    ta,dt = np.linspace(-1.0,1.0,N+1,retstep=True) # discretize interval t
    #f,dfex = ta**2,2*ta # test function and its exact derivative
    f,dfex = np.sin(np.pi*ta),np.pi*np.cos(np.pi*ta) # test function and its exact derivative
    df = FDAcd2(f, dt)
    plt.plot(ta,df,'k', ta, dfex,'k') # plot exact and approximate derivative
    erms = np.sqrt( ((df-dfex)**2).sum()/len(f) ) # mean-error
    print('N={}, erms = {:7.5g}'.format(N,erms))
    '''
    #Step 4
    N = 1000
    ta,dt = np.linspace(0.0,4.0,N+1,retstep=True) # sample times
    xa,ya = Trajectory(ta)
    fig,ax = plt.subplots()
    ua = FDAcd2(xa,dt)  # x-current estimate, uncomment after developing FDAcd2
    va = FDAcd2(ya,dt)  # y-current estimate, uncomment after developing FDAcd2
    ax.plot(xa,ya,'b') # plot trajectory in blue
    ax.quiver(xa[::20],ya[::20],ua[::20],va[::20]) # plot every 20-th current
    ax.set_aspect('equal')
    # animate the trajectory for fun
    line,mark = ax.plot([],[],'r-',[],[],'ro')
    for i in range(len(xa)):
        mark.set_data(xa[i:i+1],ya[i:i+1])
        line.set_data(xa[:i],ya[:i])
        plt.pause(1.e-3)
main()
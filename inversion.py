#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 16:10:43 2017

@author: bastian
"""

import numpy as np
import Rsta
import RSPIKE as spk
import geometryfunctions as gmf



## R.B.GEORG - 2018
# The DS inversion scheme follows the approach by Siebert et al 2001 G3.
# Standard ratios and spike ratios are defined in Rsta.py and RSPIKE.py,
# respectively. Inputs (Rsam1,Rsam2,RsamX,Rsam3,RsamY,RsamZ) 
# to the inversion function are raw ratios obtained from
# a vectorized input matrix in DS.py. The inversion function returns a few
# outputs to DS.py, where outputs are
# vecorized and some statistics will be executed. 

# Author of this Python3 program: R.Bastian Georg (bastiangeorg@mac.com)


## Double-spike inversion section:

def f(RsamX,RsamY,RsamZ):

#start inversion scheme using arbitrary fractionation values 
    beta = 3      # instrumental fractionation in #
    alpha = 2   # natural fractionation 
    
# start routine here: assign starting variables and isotope ratios

    for n in range (6): #for more iterations increase range
        Rx1 = Rsta.RstaX
        Ry1 = Rsta.RstaY
        Rz1 = Rsta.RstaZ

        Rx2 = Rsta.RstaX * (93.90509 / 99.90747) ** alpha
        Ry2 = Rsta.RstaY * (94.90584 / 99.90747) ** alpha
        Rz2 = Rsta.RstaZ * (97.9054 / 99.90747) ** alpha
    
        # create line (a) - call geometric line function  
        Pd,Pe,Pf,Pg = gmf.line(Rx1,Rx2,Ry1,Ry2,Rz1,Rz2)
  
    #store vaiables of line (a) for later intercept calc.
        P1d = Pd
        P1e = Pe
        P1f = Pf
        P1g = Pg

        Rx3 = spk.RSPIKEX
        Ry3 = spk.RSPIKEY
        Rz3 = spk.RSPIKEZ
    
    
    # construct plane (A) - call geometric plane function
        Pa,Pb,Pc = gmf.plane(Rx1,Rx2,Rx3,Ry1,Ry2,Ry3,Rz1,Rz2,Rz3)
    
      
        for m in range (6): #(nested into n, for more iterations increase 1:m, where m = 2,3,4, ... x.)

            Rx1 = RsamX #measured ratios
            Ry1 = RsamY
            Rz1 = RsamZ

            Rx2 = RsamX * (93.90509 / 99.90747) ** beta
            Ry2 = RsamY * (94.90584 / 99.90747) ** beta
            Rz2 = RsamZ * (97.9054 / 99.90747) ** beta
            
            # create line (b) - call gemometric line function
            Pd,Pe,Pf,Pg = gmf.line(Rx1,Rx2,Ry1,Ry2,Rz1,Rz2)
            
            #Intercept Plane (A) and line (b) call geometric intercept function
            InX,InY,InZ = gmf.intercept(Pa,Pb,Pc,Pd,Pe,Pf,Pg)

            #calculate instrumental mass-bias
            RMTRU = InX    #estimate of real mixture ratios
           
            beta = np.log(RMTRU/RsamX) / np.log(93.90509 / 99.90747) #refine instrumental mass-bias from measured and real mixture ratios

   
   #create plane (B) - call makeplane.m
        Pa,Pb,Pc = gmf.plane(Rx1,Rx2,Rx3,Ry1,Ry2,Ry3,Rz1,Rz2,Rz3)
    
   #recall variables of line (a) 
        Pd = P1d
        Pe = P1e
        Pf = P1f
        Pg = P1g
    
   #Intercept line (a) with plane (B) call makeintercept.m
        InX,InY,InZ = gmf.intercept(Pa,Pb,Pc,Pd,Pe,Pf,Pg)
    
   #calculate new alpha
        RSTRU = InX #estimate of real sample ratio offset by natural fractionation alpha
        alpha = np.log(RSTRU/Rsta.RstaX) / np.log(93.90509 / 99.90747) # refine estimate of natrual fractionation
    
    
   
    
## Calculate corrected ratios:
    
    #print fractionation
    alpha = -alpha
    beta = -beta
   
    
    return [alpha, beta] #all that needs returned - using alpha and beta, all required ratios can be calculated from the standard abundances

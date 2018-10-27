#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 15:48:57 2017

@author: bastian
"""

import numpy as np
import inversion as inv
import pandas as pd
import ratiocalc as rclc
import dcalc

## Info-section
# Double spike inversion program for MATLAB: R B GEORG - 2009,
# bastiangeorg@mac.com
#Results = pd.DataFrame()
def f(B):
#estimate length for vector space from inout matrix B
    L = len(B);
    invout = np.empty([L,14])
    dvalues = np.empty([L,7])
    bias = np.empty([L,2])
    sprop = np.empty([L,1])
#create vector space, length of vector space is number
#of cycles N! 
    #t = np.arange(L)
    #n = len(t);

    #out = np.zeros([L,2])
#loop the input matrix B through and create ratios for each N
    for i in range (L):
    
    #vectorize input matrix & substract zeros from each beam
        Mo92 = B[i,0]
        Mo94 = B[i,1]
        Mo95 = B[i,2]
        Mo96 = B[i,3]
        Mo97 = B[i,4]
        Mo98 = B[i,5]
        Mo00 = B[i,6]
    
    #Mo DoubleSpike inversion - for WQC 98--94 tracer
    #inversion isotopes 94,95,98,100 (for Nu) 92, 94, 98, 100 (For Neptune)
   
        RsamX = Mo94 / Mo00
        RsamY = Mo95 / Mo00 
        RsamZ = Mo98 / Mo00 
        
        #print(RsamX, RsamY, RsamZ)
        #d66Zn, d67Zn, d70Zn, alpha, beta = inv.f(RsamX, RsamY, RsamZ)
        alpha, beta = inv.f(RsamX, RsamY, RsamZ)
        bias[i] = [alpha,beta]
        
        #Results.loc[i,'alpha'] = alpha
        #Results.loc[i,'beta']  = beta
        #Results.loc[i,'d66Zn']  = d66Zn
        #Results.loc[i,'d67Zn']  = d67Zn
        #Results.loc[i,'d70Zn']  = d70Zn
        
        out = [alpha, beta] #data sent to inversion routine and alpha/beta are returned
        
        
        #alpha, beta and ionbeam data are sent to ratio-calc routine, where natural, mix-ratios and spike-sample proportions
        #are calculated.
        ratios,fspk = rclc.f(alpha, beta, Mo92, Mo94, Mo95, Mo96, Mo97, Mo98, Mo00)
        
        #alpha and Rsta data are used to calc required d-values
        dvalues[i] = dcalc.f(ratios)
        
        invout[i] = ratios
        sprop[i] = fspk
#        out = [NR, MR]
    return [invout,sprop, bias, dvalues]    
    
    

 
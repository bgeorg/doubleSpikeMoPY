#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 21:27:13 2017

@author: bastian
"""
import Rsta
import numpy as np



def f(ratios):
    
    L = len(ratios)
    dvalues = np.zeros([L,7])
    
    RN = ratios[:,0:7]
    
    for i in range(L):
        dvalues[i] = (( RN[i] / Rsta.Rdelta ) - 1 ) * 1000
        
    return dvalues
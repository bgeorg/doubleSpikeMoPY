#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 22:42:13 2017

@author: bastian
"""
import numpy as np
import Rsta as st
import RSPIKE as spk
import isotopemasses as amu

NR = np.empty(7)
MR = np.empty(7)
fspk = np.empty([1,7])
ratios = np.empty([1,14])


def f(alpha, beta, Mo92, Mo94, Mo95, Mo96, Mo97, Mo98, Mo00):
    
    Mo=[Mo92, Mo94, Mo95, Mo96, Mo97, Mo98, Mo00]
    
    
    #calculate log ratios of atomic masses times (-1)alpha
    
    udeno = amu.u98  #denominator isotope
    
    for i in range(7):
        P = np.log(amu.amu[i]/udeno)*(alpha)
        NR[i] = (st.STA[i]/st.STA[5]) * np.exp(P)
    fNR = NR / NR.sum()
   
    #calculate mass-bias corrected mixture ratios
    for i in range(7):
        P = np.log(amu.amu[i]/udeno)*(beta)
        MR[i] = (Mo[i]/Mo[5]) * np.exp(P)
    fMR = MR / MR.sum()
    
    #put all ratios into matrix form for export - natral ratios 1-7, measured mix-ratios 8-14
    ratios[0,np.arange(14)] = np.append(NR,MR)
    
    
    #calculate spike-sample mixing proportions and report average value
    for i in range(7):
        fspk[0,i] = (fMR[i] - fNR[i]) / (spk.DSPK[i] - fNR[i])
        
     
    return [ratios,fspk.mean()]
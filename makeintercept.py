#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 16:26:07 2017

@author: bastian
"""

#Makeintercept.m calculates the intercepts of each axis (X,Y,Z stand for isotope ratios!). 
# This follows Siebert et al 2001.

def f(Pa,Pb,Pc,Pd,Pe,Pf,Pg):

#MAKEINTERCEPT 
 
    InX = (Pb * Pg - Pb * Pe + Pe * Pf - Pc * Pf) / (Pa * Pf + Pb * Pd - Pd * Pf)
    InY = (Pa * Pe - Pa * Pg + Pd * Pg - Pc * Pd) / (Pa * Pf + Pb * Pd - Pd * Pf)
    InZ = Pa * InX + Pb * InY + Pc

    return [InX,InY,InZ]
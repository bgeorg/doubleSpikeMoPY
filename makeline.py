#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 16:16:08 2017

@author: bastian
"""

#makeline.m calculates lines in 3D space.
def f(Rx1,Rx2,Ry1,Ry2,Rz1,Rz2):
   


    Pd = (Rz1 - Rz2) / (Rx1 - Rx2);
    Pe = Rz1 - Rx1 * Pd;
    Pf = (Rz1 - Rz2) / (Ry1 - Ry2);
    Pg = Rz1 - Ry1 * Pf;
    
    return [Pd,Pe,Pf,Pg]


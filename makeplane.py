#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 16:24:09 2017

@author: bastian
"""

#makeplane.m calculate plane in the 3D space. See Siebert et al
#2001 for more info.

def f(Rx1,Rx2,Rx3,Ry1,Ry2,Ry3,Rz1,Rz2,Rz3):

  PaUp = Ry1 * (Rz3 - Rz2) + Ry2 * (Rz1 - Rz3) + Ry3 * (Rz2 - Rz1)
  PaDn = Ry1 * (Rx3 - Rx2) + Ry2 * (Rx1 - Rx3) + Ry3 * (Rx2 - Rx1)
  Pa = PaUp / PaDn
  
  PbUp = Rx1 * (Rz2 - Rz3) + Rx2 * (Rz3 - Rz1) + Rx3 * (Rz1 - Rz2)
  PbDn = Rx1 * (Ry2 - Ry3) + Rx2 * (Ry3 - Ry1) + Rx3 * (Ry1 - Ry2)
  Pb = PbUp / PbDn
  
  Pc = Rz1 - Pa * Rx1 - Pb * Ry1
  
  return [Pa,Pb,Pc]


##!/usr/bin/env python3
## -*- coding: utf-8 -*-
#"""
#Created on Sun Sep 10 16:30:58 2017
#
#@author: bastian
#"""
#% calibrated Standard ratios. It is not so important to accurately know the
#% absolute ratios. Only make sure that the same ratios are used for the
#% spike calibration.

import numpy as np

#STA = [0.147900, 0.093473, 0.158751, 0.166236, 0.095243, 0.242446, 0.095951]
STA = [0.148353, 0.092461, 0.159241, 0.166760, 0.095529, 0.241411, 0.096244];
#
RST20 = STA[0] / STA[6] #92/00
RstaX = STA[1] / STA[6] #94/00
RstaY = STA[2] / STA[6] #95/00
RST60 = STA[3] / STA[6] #96/00 
RST70 = STA[4] / STA[6] #97/00 
RstaZ = STA[5] / STA[6] #100/00 


RX = RstaX 
RY = RstaY 
RZ = RstaZ 


Rsta9200 = RST20
Rsta9400 = RstaX
Rsta9500 = RstaY
Rsta9600 = RST60
Rsta9700 = RST70
Rsta9800 = RstaZ
Rsta0000 = STA[6] / STA[6]


Rstds = np.zeros(7)

Rstds[0] = RST20
Rstds[1] = RstaX
Rstds[2] = RstaY
Rstds[3] = RST60
Rstds[4] = RST70
Rstds[5] = RstaZ
Rstds[6] = Rsta0000

Rdelta = np.zeros(7)

Rdelta[0] = STA[0] / STA[5]
Rdelta[1] = STA[1] / STA[5]
Rdelta[2] = STA[2] / STA[5]
Rdelta[3] = STA[3] / STA[5]
Rdelta[4] = STA[4] / STA[5]
Rdelta[5] = STA[5] / STA[5]
Rdelta[6] = STA[6] / STA[5]






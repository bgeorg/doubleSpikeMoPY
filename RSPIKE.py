#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 16:38:09 2017

@author: bastian
"""

#% calibrated spike ratios. Single spikes were calibrated agains
#% gravimetrically prepared SCP-Mo standard using generic isotope abundaces
#% Mixtures of different spike-to-SCP mixing proportions were
#% measured, bracketed by unspiked SCP runs for mass-bias correction (using X/97 ratios). Spike
#% abundances for each isotope were obtained from least-square fitting.


#DSPK = [0.002221, 0.421470, 0.001695, 0.000131, 0.003683, 0.568411, 0.002388]  #SPIKE isotope abundaces [92 94 95 96 97 98 100]
DSPK = [0.001981886, 0.422030313, 0.001433031, -0.000150109, 0.003527761, 0.568949832, 0.002227286]  #SPIKE isotope abundaces [92 94 95 96 97 98 100]


Rspk20    = DSPK[0] / DSPK[6]
RSPIKEX   = DSPK[1] / DSPK[6] #
RSPIKEY   = DSPK[2] / DSPK[6] #
Rspk60    = DSPK[3] / DSPK[6]
Rspk70    = DSPK[4] / DSPK[6] #
RSPIKEZ   = DSPK[5] / DSPK[6] #


Rspk40 = RSPIKEX
Rspk50 = RSPIKEY
Rspk80 = RSPIKEZ
Rspk00 = 1


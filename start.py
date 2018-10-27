#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 15:10:17 2017

@author: bastian
"""
import numpy as np
import os
import pandas as pd
import DS


print('\n')
print('Welcome to offline double-spike inversion program')
print('R. Bastian Georg')
print('-------------------------------------------------')


    
#read and process data from ALL files in the folder 'spkrunfiles'
#create list of all files in folder spkrunfiles
filename_list = os.listdir('/Volumes/SSDData/PythonWork/DoubleSpikeMo/spkrunfiles/')
    
#create header names for dataframe - here for Zn isotopes
header_list = ['Mo92','Mo94','Mo95','Mo96','Mo97', 'Mo98', 'Mo100'] 

#iterate through files, read data and send to processing (csv-files)
for name in filename_list:
    if name.endswith('.xlsx'):
        sourcefile = '/Volumes/SSDData/PythonWork/DoubleSpikeMo/spkrunfiles/'+name
        with open(sourcefile, newline='', encoding="utf8") as MyFile:
            MyFile = pd.read_excel(sourcefile, header=None, names=header_list)
            MyFile.fillna(0, method=None, axis=1, inplace=True)
                
            k = len(MyFile)         #scaling parameter1
            l = len(header_list)    #scaling parameter2
            B = np.zeros([k,l])    #initiate scaled zero matrix
            
            B = MyFile.values      #create numpy matrix from pandas DataFrame
  
        # send IP to data processing and write output file into ../Zn-DS/Results:
            #[bias] = DS.f(B)
            [invout,sprop, bias, dvalues] = DS.f(B)

            
            #add everything into 1 numpy 2-D array
            results = np.concatenate((invout,sprop,bias,dvalues), axis=1)
            
            #convert results into pandas dataframe results and append statistics using .describe() method on results
            cols = ['92/98nat','94/98nat','95/98nat','96/98nat','97/98nat', '98/98nat','100/98nat',
                    '92/98mix','94/98mix','95/98mix','96/98mix','97/98mix', '98/98mix','100/98mix',
                    'fspk','alpha','beta',
                    'd92/98Mo', 'd94/98Mo', 'd95/98Mo', 'd96/98Mo', 'd97/98Mo', 'd98/98Mo', 'd100/98Mo']
            results = pd.DataFrame(results, columns=cols)
            results = results.append(results.describe())
            
            #export data into csv-file
            exportfile_name = '/Volumes/SSDData/PythonWork/DoubleSpikeMo/MoData/results_'+name
            results.to_excel(exportfile_name)
            print('file ' +name +' processed')
    

print('\n')
print('-------------------------------------------------')
print('Data csv-files stored in /Volumes/SSDData/PythonWork/DoubleSpikeMo/MoData')
    
    
    

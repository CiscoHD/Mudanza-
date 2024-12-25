# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 18:04:41 2024

@author: DELL E5430

Intructions:
    
Calculate how many instances of NaN we have in our dataset.

'Typical Hours'
'Annual Salary'
"""

import pandas as pd
pay = pd.read_csv('Current_Employee_Names__Salaries__and_Position_Titles.csv')


list =  pay.isnull().sum()
print (list)
nans = []
for nan in list: 
    print (nan)
    nans.append(nan)
    
print(sum(nans))
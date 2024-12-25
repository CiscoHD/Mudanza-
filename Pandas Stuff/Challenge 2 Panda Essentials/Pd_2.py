# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 17:04:49 2024

@author: DELL E5430

Instructions:

Your method should return a list containing the minimum, maximum, 
and average of typical hours. You can use this order 
[minimum, maximum, average].


'Typical Hours'
'Annual Salary'
"""

import pandas as pd
pay = pd.read_csv('Current_Employee_Names__Salaries__and_Position_Titles.csv')

list = []

list.append(pay['Typical Hours'].min())
list.append(pay['Typical Hours'].max())
list.append(pay['Typical Hours'].mean())


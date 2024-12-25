# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 17:10:08 2024

@author: DELL E5430

Intructions:
    
Return the number of employees who are hourly and salaried.


"""

import pandas as pd
pay = pd.read_csv('Current_Employee_Names__Salaries__and_Position_Titles.csv')

"""
My solution

list = []
list.append(pay[pay['Salary or Hourly'] == 'Hourly'].count()['Salary or Hourly'])
list.append(pay[pay['Salary or Hourly'] == 'Salary'].count()['Salary or Hourly']) 

"""

"""
Educative´s Solution

list = (pay['Salary or Hourly'].groupby(pay['Salary or Hourly']).count())
counts = []
for item in list:
  counts.append(item)

print (list)

"""
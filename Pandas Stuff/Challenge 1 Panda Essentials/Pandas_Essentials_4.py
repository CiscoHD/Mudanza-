# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 2024

@author: DELL E5430

Exercise 4

Calculate how many of the customers that have the profession 
“Structural Engineer” are male.

DONE, NO ERRORS YEII

"""

import pandas as pd
cust = pd.read_csv('Cust_Purch_FakeData.csv')
print(cust)
by_profession = cust[cust['profession'] == 'Structural Engineer']
print (by_profession[by_profession['gender'] == 'Male'].count()['last'])
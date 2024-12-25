# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 14:12:13 2024

@author: DELL E5430

Exercise 3

Intructions: Calculate how many customers have the profession
“Structural Engineer”.


"""

import pandas as pd
cust = pd.read_csv('Cust_Purch_FakeData.csv')
print(cust)


emails = list(cust[cust['price(CAD)'] >= 100]['email'])

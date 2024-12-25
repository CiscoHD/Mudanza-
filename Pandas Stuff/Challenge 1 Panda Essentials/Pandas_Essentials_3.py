# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 21:18:44 2024

@author: DELL E5430

Exercise 3

Intructions: Calculate how many customers have the profession
“Structural Engineer”.


"""

import pandas as pd
cust = pd.read_csv('Cust_Purch_FakeData.csv')
print(cust)

df_cust = pd.DataFrame(cust)

#print(df_cust['profession'])

"""
To filter only those that match the profession 'Structural Engineer,' 
we need to use a Boolean comparison that gives us True/False values only
for the 'profession' column.

---> by_profession = cust['profession'] == 'Structural Engineer'

Now that we kwon which index are True/False for the profession 
'Structural Engineer' its necesary to count the ones we are looking for.

And this  



"""

by_profession = cust['profession'] == 'Structural Engineer'

print (cust[cust['profession'] == 'Structural Engineer'].count()['last'])
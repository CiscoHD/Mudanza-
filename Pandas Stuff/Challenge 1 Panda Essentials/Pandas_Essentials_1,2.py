# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 20:22:52 2024

@author: DELL E5430 Cisco :D



"""

# First thing first, import Pandas :)
import pandas as pd
cust = pd.read_csv('Cust_Purch_FakeData.csv')
print(cust)
"""provides the info of the DataFrame
print(cust.info())
"""

"""
#Exercise 1 

Intructions: To see what the data looks like, display the first five
 rows of the dataset.

-> print(cust.loc[:4])

import pandas as pd
def display_first_5_Rows():
    cust = pd.read_csv('Cust_Purch_FakeData.csv')
    print(cust.loc[:4])
    return cust.head()

"""

"""
Exercise 2

Instructions: Return the max, min, and mean of the ages 
of customers in the dataset. To return all the values, 
store the records in a list like this: [min, max, mean].
Follow this pattern for test cases.

df_ages = (pd.DataFrame(cust[['first', 'age']]))

#print(df_ages)
#print(cust[['first', 'age']])

gby = df_ages.groupby('first')

gby_max = gby.max() 

print (gby_max.max())
print()

gby_min = gby.min()

print (gby_min.min())
print()

gby_mean = gby.mean()

print (gby_mean.mean())
print()

age_max = gby_max.max()

age_min = gby_min.min()

age_mean = gby_mean.mean()

final = list((age_min[0], age_max[0], gby_mean[0]))

print (final)
print()

finished 17/07/2024

The error was to use the GroupBy method, i had only to do 
the operations for the column 'age':
    
  -> Solution <-
  
  def min_max_mean_of_ages():
  list = []
  list.append(cust['age'].min())
  list.append(cust['age'].max())
  list.append(cust['age'].mean())
  return list

"""


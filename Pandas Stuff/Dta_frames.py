# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 14:51:10 2024

Data Frames on Pandas

@author: DELL E5430
"""
import pandas as pd
import numpy as np

index = 'r1 r2 r3 r4 r5 r6 r7 r8 r9 r10'.split()
columns = 'c1 c2 c3 c4 c5 c6 c7 c8 c9 c10'.split()
# just to see what the index looks like, a list from r1 to r10!
print(index)

# and what columns look like, a list from c1 to c10!
print(columns)

array_2d = np.arange(0,100).reshape(10,10) # creating a 2D array "array_2d"
print("\n ",array_2d)
print()

df = pd.DataFrame(data = array_2d, index = index, columns = columns)
print(df)
print()

# Grabbing a single column
print("Column C1 : ", df['c1'])
print()

# checking the type of single column 
print(type(df['c1'])) # It is a pandas Series

# We can grab more than one column, simply pass the list of columns you need!
print(df[['c1', 'c10']])
print()
#We can use df.column_name (for example, df.c1, df.c2, and so on) to grab a column as well.
print(df.c5)

df['new'] = df['c1'] + df['c2'] 
# adding a column "new" which is sum of "c1" and "c2"
print(df)
print ()

#df.drop(['c1'], axis = 1, inplace = True) 
# If we don't pass inplace = True, then change will not be permanent
print(df)
print()

# using loc, this will return rows r2 and r3,
# notice the list [r2, r3] in square ,!brackets
print(df.loc[['r1', 'r3']])
print()
print(df.iloc[[1, 2]]) # remember, index starts with 0
print()

print("Element at r1,c1 : ", df.loc['r1','c1'])
print("Element at r2,c2 : ", df.loc['r2', 'c10'])

# for a subset, pass the list
print("Subset \n",df.loc[['r1','r2'],['c1','c2']])

# another example - random columns and rows in the list
print("Random Columns and Rows \n", df.loc[['r2','r5'],['c3','c4']])
print()

# We can do a conditional selection as well
print(df > 5)
print()

# Return Divisible by 3
bool_mask = df % 3 == 0
# creating the mask for the required condition df[bool_mask] # passing the mask to get the required results
print(bool_mask)
print()

print (df[df % 3 == 0])# Similar to the above 2 lines of code
print()

print(df[['c1']] > 11)
print()
print(df[df['c1']>11]) # df[boolean_mask]
# We will use these sorts of operations frequently in our course.

print()

# bool_ser is our mask
bool_ser = df['c1']>11 
# getting a new DataFrame based on the mask bool_ser 
result = df[bool_ser] 
# final output, grabbing a single column c1 from the filtered DataFrame
print(result['c4'])

print()

# We need two rows, pass in a list of those rows
print("Rows \n",df[df['c1']>11].loc[['r3','r5']])

'''Now, let’s return a row from our 
dataframe that have a value 70 in its column c1
'''
print("\n Row which have 70 in column c1 \n",df[df['c1']==70])

'''
Let’s try to combine two conditions using & 
operator on c1 for a value > 60 and on c2 for a value > 80.
'''
print("\n Combined Conditions \n",df[(df['c1']>60) & (df['c2']>80)])
print()

# inplace = True for permanent change
print("Reset index \n",df.reset_index(inplace = True))
# split at white spaces, newind is our list of alphabets
newind = 'a b c d e f g h i j'.split() 
# let put newind as a new col in the df
df['newind']=newind
print("New column added \n ",df)
#setting newind as an index, needs to be inplaced
df.set_index('newind', inplace = True)
print("Inplaced newint \n", df)

print("First 2 Rows \n ", df.head(n=2)) # n=5 by default
print("Last 2 Rows \n", df.tail(n=2)) # n=2 by default

print("Dataframe info \n", df.info())

print("Described Dataframe \n", df.describe())
print("prueba de live share")
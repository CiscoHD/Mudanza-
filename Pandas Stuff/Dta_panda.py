# first things first, we need to import NumPy and Pandas 
# np and pd are aliases for NumPy and pandas, respectively

import numpy as np
import pandas as pd

# just to check their versions we are using
my_labels = ['X','Y','Z']
my_data = [100,200,300]

#   Converting my_data (Python list) to pandas Series
#print(pd.Series(data = my_data))

#print(pd.Series(data = my_data, index = my_labels))
#pd.Series(my_data, my_labels) 
#   Same as above!, data and index are in order￿

# Let's create NumPy array from my_data and then Series from that array 
my_array = np.array(my_data) # creating numpy's array from list 
series = pd.Series(data = my_array, index = my_labels) # creating Series from numpy's array

#print (series)

# Let's create a dictionary my_dict
my_dict = {'x':100,'y':200,'z':300} # creating a dictionary "my_dict"
series = pd.Series(my_dict) # creating Series from dictionary

#print(series)

# Let's pass my_labels (which is a list of strings) as data now! 
#print(pd.Series(data = my_labels)) # passing list for strings as data

# We can pass a list of built-in functions!
#print(pd.Series([min, max, sum, print]))

# Creating three dictionaries dict_1, dict_2, dict_3
dict_1 = {'Toronto': 500, 'Calgary': 200, 'Vancouver': 300, 'Montreal': 700}
dict_2 = {'Calgary': 200, 'Vancouver': 300, 'Montreal': 700}
dict_3 = {'Calgary': 200, 'Vancouver': 300, 'Montreal': 700, 'Jasper':1000}

# Creating Pandas Series from the dictionaries
ser1 = pd.Series(dict_1)
ser2 = pd.Series(dict_2)
ser3 = pd.Series(dict_3)

print("Series 1 : ",ser1)
print("\nSeries 2 : ",ser2)
print("\nSeries 3 : ",ser3)

print(ser1['Calgary'])

print(ser1) #CMTV are in order
print()
print(ser2) #CMV are in order
print()

ser4 = ser1 + ser2 
# adding Series and assigning/passing results to a new variable ser4
print(ser4)
print()
# What if we add ser4 and ser3, another NaN for Jasper!
ser5 = ser4 + ser3
print(ser5)
print()

print(ser4.isnull())
print(ser5.notnull())

print()

print("Head : ",ser1.head(1)) # head(1) will return the first row only
print("Tail : ",ser1.tail(1)) # tail(1) will return the last row only

print()

# row axis labels (index) list can be obtained
print("Axis : ", ser1.axes)

# returns the values/data
print("Values : ", ser1.values)

print("Size : ", ser1.size)

# True for empty Series
print("Is Empty ? ",ser1.empty)
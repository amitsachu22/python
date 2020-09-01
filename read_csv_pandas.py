# -*- coding: utf-8 -*-
"""
Created on Wed May 13 18:37:18 2020

@author: AKUM55
"""

import pandas as pd
import sys

ip_file = pd.read_csv('size_prices.csv')

print(ip_file.iloc[[0],[0]])


file_size = ip_file.shape[0]


print(file_size)
print(range(file_size))

for i in range(file_size):
   # print(ip_file.loc[i,['productCode']])
    if (i == 3):
        break
    else:
       print('Row :' + str(i))
        
  #      print("hello")
        
        


list1 = [1,3,4]

print(list1)

for i in list1:
    print(i)
    
print(enumerate(list1)   )    
for index, data in enumerate(list1):
    print(str(index) +',' + str(data))
    
print(sys.version)
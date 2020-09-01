# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""
import csv
import pandas as pd
import json
import numpy as np
pd_csv = pd.read_csv('size_prices.csv', dtype=str)
file_size = pd_csv.shape[0]
#print (pd_csv['gtin'])
pd_csv = pd_csv.replace(np.nan, '', regex=True)
d = json.load(open('product_template.json'))
for i in range(file_size):
    print ("creating file no " + str(i))
    file_name = "op/data" + str(i) + ".json"
    d['gtin'] = str(pd_csv['gtin'][i])
    d_weightsAndMeasures = d['weightsAndMeasures']
    d_weightsAndMeasures['netWeight'] = float(pd_csv['netWeight'][i])
    d_weightsAndMeasures['weightUnits'] = pd_csv['weightUnits'][i] 
    d_weightsAndMeasures['dimensionalUnits'] = pd_csv['dimensionalUnits'][i]
    d_weightsAndMeasures['grossPackageWeight'] = float(pd_csv['grossPackageWeight'][i])
    # d_weightsAndMeasures['dimensionalWeight'] = float(pd_csv['dimensionalWeight'][i])
    d_weightsAndMeasures['packageLength'] = float(pd_csv['packageLength'][i])
    d_weightsAndMeasures['packageWidth'] = float(pd_csv['packageWidth'][i])
    d_weightsAndMeasures['packageHeight'] = float(pd_csv['packageHeight'][i])
#    d_weightsAndMeasures['packageQuantity'] = pd_csv['packageQuantity'][i] 
    d['weightsAndMeasures'] = d_weightsAndMeasures 
    d['prices'][0]['amount'] = float(pd_csv['crp'][i])
    d['prices'][1]['amount'] = float(pd_csv['crp'][i])
    d['prices'][0]['currencyCode'] = pd_csv['currencyCode'][i]
    d['prices'][1]['currencyCode'] = pd_csv['currencyCode'][i]
    d['marketplace'] = pd_csv['marketplace'][i]
    # size data change
    d_size = d['size']
    d_size['nikeSize'] = pd_csv['nikeSize'][i] 
    d_size['localizedSize'] = pd_csv['localizedSize'][i]
    d_size['vendorSize'] = pd_csv['vendorSize'][i]
    d['size'] = d_size 
    # legacy data change
    d_legacy = d['legacy']
    d_legacy['pid'] = int(pd_csv['pid'][i]) 
    d_legacy['skuId'] = int(pd_csv['skuId'][i])
    #    
    #
    file_name =str(d['marketplace']) + "-" + str(d['productCode']) + "-" + str(d_size['nikeSize']) + ".json"
    print (file_name)
    file_name = "op/" + file_name
    with open(file_name, 'w') as outfile:
        json.dump(d, outfile)
#
#
#print (d_weightsAndMeasures['netWeight'])
#print (d['gtin'])
#print(pd_csv['gtin'][0])
#
#
##print (d['netWeight'])
#print(pd_csv['netWeight'][0])
#
##d['gtin'] = pd_csv['gtin'][0]
#
#
#
#with open('data.json', 'w') as outfile:
#       json.dump(d, outfile)
#       
    
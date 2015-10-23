# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 21:13:41 2015

@author: Shamir
"""

import re
import json
import numpy as np
import os      


def returnPattern(pattern, content, temp_array):
    """
    """
    for string in pattern.findall(content):
        temp_array.append(string)
    return temp_array        

def storeContent(src_array, dest_array, pattern, content, temp_array):
    """
    """
    for i in range(len(src_array)):
        returnPattern(pattern, str(content[i]), temp_array)
        if np.size(temp_array) == 0:
            pass
        else:
            dest_array.append(src_array[i])
            temp_array = []
    return dest_array
    temp_array = []


filepath = "C:\\Users\\Shamir\\Desktop\Shopify\\1. Shopicruit problem\\"                               # this is the directory where I saved products.json

try:
    os.chdir(filepath)                                                           # go to the specified directory
    file = open('products.json', 'r')  
except WindowsError:                                                           # if the pathname is invalid
    print "Invalid Directory!"
except IOError as e:                                                           # wrong filename
    print e


file_contents = file.read()
contents = json.loads(file_contents)
values = np.array(contents.get('products'))                                      # sort product info into individual arrays


pattern_w = re.compile("((?<=product_type': u'Wallet)(.))", re.I)
pattern_l = re.compile("((?<=product_type': u'Lamp)(.))", re.I)
temp1, temp2, temp3, temp4 = [], [], [], []
wallets = []
lamps = []

storeContent(values, wallets, pattern_w, values, temp1)
storeContent(values, lamps, pattern_l, values, temp2)

price = re.compile("price': u'(\d+.\d+)")
price_wallets = np.array(returnPattern(price, str(wallets), temp3))
price_lamps   = np.array(returnPattern(price, str(lamps), temp4))

# Calculate total price
wallet_total = sum(price_wallets.astype(float))
lamp_total   = sum(price_lamps.astype(float))
GrandTotal = format(wallet_total + lamp_total, '.2f')

display = 'Total price of all lamps and wallets = $' + GrandTotal
print display
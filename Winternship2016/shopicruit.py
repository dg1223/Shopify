# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 21:13:41 2015

@author: Shamir
"""

import re
import numpy as np
import os

def storeObject(pattern, content, List):
    
    for string in pattern.findall(content):
        List.append(string)
    return List
        
        
filepath = "C:\\Users\\Shamir\\Desktop\Shopify\\1. Shopicruit problem\\"       # this is the directory where I saved products.json

try:
    os.chdir(filepath)                                                          # go to the specified directory
    file = open('products.json', 'r')  
except WindowsError:                                                            # if the pathname is invalid
    print "Invalid Directory!"
except IOError as e:                                                            # wrong filename
    print e

file_contents = file.read()

pattern_w = re.compile('(wallet)\"],"(variants)', re.I)
pattern_l = re.compile("(lamp)", re.I)
wallet = []
lamp = []

storeObject(pattern_w, file_contents, wallet)
storeObject(pattern_l, file_contents, lamp)
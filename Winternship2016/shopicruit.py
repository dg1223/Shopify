# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 21:13:41 2015

@author: Shamir
"""

#import re
import numpy as np
import os
import json

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

parsed = json.loads(file_contents)

# '(wallet)\"],"(?:variants":)\[{(?:"id":)(?:\d+)(?:,"title":")(?:\w+)(?:","option1":")(?:\w+)(?:","option2":)(?:\w+)(?:,"option3":)(?:\w+,")(?:\w+)\":"(\d+.\d+)\","(?:\w+":\w+\,"compare_at_price":\w+\,"sku":)(?:"\w+","|"",")(?:requires_shipping":\w+,"taxable":\w+,"position":\d+,"product_id":\d+,"created_at":"\d+\-\d+\-\w+:\d+:\d+\-\d+:\d+","updated_at":"\d+\-\d+\-\w+:\d+:\d+\-\d+:\d+","available":\w+,"featured_image":)(\w+)\},'
## all prices
# '(?:"id":)(?:\d+)(?:,"title":")(?:\w+)(?:","option1":)(?:"\w+"|\w+)(?:,"option2":)(?:"\w+"|\w+)(?:,"option3":)(?:"\w+"|\w+)(?:,"price":")(\d+.\d+)\","(?:\w+":\w+\,"compare_at_price":\w+\,"sku":)(?:"\w+","|"",")(?:requires_shipping":\w+,"taxable":\w+,"position":\d+,"product_id":\d+,"created_at":"\d+\-\d+\-\w+:\d+:\d+\-\d+:\d+","updated_at":"\d+\-\d+\-\w+:\d+:\d+\-\d+:\d+","available":\w+,"featured_image":\w+)\}'

#(?(?=regex)then|else)
#(?(?=product_type":"Wallet)(?:\","tags":\[\))
#pattern_w = re.compile('(?:"id":)(?:\d+)(?:,"title":")(?:\w+)(?:","option1":)(?:"\w+"|\w+)(?:,"option2":)(?:"\w+"|\w+)(?:,"option3":)(?:"\w+"|\w+)(?:,"price":")(\d+.\d+)\","(?:\w+":\w+\,"compare_at_price":\w+\,"sku":)(?:"\w+","|"",")(?:requires_shipping":\w+,"taxable":\w+,"position":\d+,"product_id":\d+,"created_at":"\d+\-\d+\-\w+:\d+:\d+\-\d+:\d+","updated_at":"\d+\-\d+\-\w+:\d+:\d+\-\d+:\d+","available":\w+,"featured_image":\w+)\}', re.I)


#pattern_w1 = re.compile('((?<=product_type":"Wallet)(.*)(?=Wallet.png))', re.I)   # 'price":"\d+\.\d+'
#pattern_l = re.compile("(lamp)", re.I)
#wallet = []
#lamp = []

#storeObject(pattern_w1, file_contents, wallet)
#storeObject(pattern_l, file_contents, lamp)
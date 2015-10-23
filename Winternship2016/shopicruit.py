# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 21:13:41 2015

Problem statement:
You've discovered the Shopify Store 'Shopicruit'. Since you're obsessed with
lamps and wallets, you want to buy every single lamp and wallet variant they
have to offer. By inspecting the Javascript calls on the store you discovered
that the shop lists products at http://shopicruit.myshopify.com/products.json.
Write a program that calculates how much all lamps and wallets would cost you.

@author: Shamir
"""

import Tkinter, tkFileDialog 
import re
import json
import numpy as np   


def returnPattern(pattern, content, temp_list):
    """ Finds and stores all of the strings that matches with the given
    pattern.
    
    input parameters>>
    pattern: regex pattern to match
    content: a list of strings   
    
    output parameters>>
    temp_list: temporary list to store matched strings
    
    Example
    =======
    returnPattern(pattern, string_list, temp)
    """
    
    for string in pattern.findall(content):
        temp_list.append(string)
    return temp_list        


def storeContent(src_list, dest_list, pattern, content, temp_list):
    """ Separates and stores the rows (strings) from the source list for which
    the function 'returnPattern' returns a non-empty list.
    
    input parameters>>
    src_list, dest_list: source and desination lists
    pattern: regex pattern to match
    content: a list of strings   
    
    output parameters>>
    temp_list: temporary list to store matched strings
    
    Example
    =======
    storeContent(values, wallets, pattern_w, values, temp1)
    """
    
    for i in range(len(src_list)):
        returnPattern(pattern, str(content[i]), temp_list)
        if np.size(temp_list) == 0:
            pass
        else:
            dest_list.append(src_list[i])
            temp_list = []
    return dest_list
    temp_list = []

root = Tkinter.Tk()
File = tkFileDialog.askopenfile(mode = 'r', filetypes = [('JSON files', '*.json')])     # ask to open .json files only
file_contents = File.read()                                                             # read file
contents = json.loads(file_contents)                                                    # decode the json file (dtype: dictionary)
values = np.array(contents.get('products'))                                             # store every product info in an array

pattern_w = re.compile("((?<=product_type': u'Wallet)(.))", re.I)                       # regex pattern to find the wallets
pattern_l = re.compile("((?<=product_type': u'Lamp)(.))", re.I)                         # regex pattern to find the lamps
temp1, temp2, temp3, temp4 = [], [], [], []                                             # initialize temporary lists (1st two store all the info for each wallet and lamp resp. and other two only store their prices)
wallets, lamps = [], []                                                                 # the wallets and lamps get places to live

storeContent(values, wallets, pattern_w, values, temp1)                                 # wallets move in
storeContent(values, lamps, pattern_l, values, temp2)                                   # lamps move in

# Find prices
price = re.compile("price': u'(\d+.\d+)")
price_wallets = np.array(returnPattern(price, str(wallets), temp3))
price_lamps   = np.array(returnPattern(price, str(lamps), temp4))

# Calculate and print total price
wallet_total = sum(price_wallets.astype(float))
lamp_total   = sum(price_lamps.astype(float))
GrandTotal = format(wallet_total + lamp_total, '.2f')

display = 'Total price of all lamps and wallets = $' + GrandTotal
print display

root.destroy()                                                                          # close Tkinter dialogue box
'''
Descripttion: 
version: 
Author: ybzhang
Date: 2020-11-24 20:17:35
LastEditors: ybzhang
LastEditTime: 2020-11-24 20:59:21
'''
def accumulate(collection, operation):
    res=[]
    for x in collection:
        res.append(operation(x))
    return res

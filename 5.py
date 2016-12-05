# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 00:01:39 2016

@author: Mike
"""
import hashlib

from collections import Counter
m = hashlib.md5()
inputstr=u"uqwqemis"
length=0
counter = 0
outputstr = [None]*8
while length < 8:
    
    teststr = hashlib.md5((inputstr + str(counter)).encode("utf-8")).hexdigest()
    #print(teststr)
    if teststr[:5] == "00000" and teststr[5] in "01234567" and outputstr[int(teststr[5])] is None:
        outputstr[int(teststr[5])]=teststr[6]
        length+=1
        print(counter, (inputstr + str(counter)), teststr)
    counter+=1

print(outputstr)
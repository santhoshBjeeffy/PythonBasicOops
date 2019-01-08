# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 07:30:04 2019

@author: santhob
"""
import Data as da
myObject = da.Bangalore()      
myObject.add(2) 
myObject.add(5) 
  
# This line causes error 
print (myObject.__hiddenVariable)
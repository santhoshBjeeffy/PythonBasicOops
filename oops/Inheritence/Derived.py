# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 07:21:47 2019

@author: santhob
"""
class pet:
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
class cat(pet):
    
    def __init__(self,name,age):
        super().__init__(name,age)




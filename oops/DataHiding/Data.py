# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 07:30:35 2019

@author: santhob
"""

#we will use double underscore before the attribute name and those will not be directly visible from outside

class Bangalore:
    #hidden member of Bangalore
    __hiddenvariable=0
    #A member that changes the hidden value
    def add(self,increment):
        self.__hiddenvariable+=increment
        print(self.__hiddenvariable)

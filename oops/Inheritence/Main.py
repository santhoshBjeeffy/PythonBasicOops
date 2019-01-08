# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 07:21:08 2019

@author: santhob
"""
import Derived as dr  
if __name__== '__main__':
    
      thepet=dr.pet("pet",1)
      jess=dr.cat("jess",2)
      print("is jess a cat?" +str(isinstance(jess,dr.cat)))
      print("is jess a pet ?" +str(isinstance(jess,dr.pet)))
      print("is thepet a cat ?" +str(isinstance(thepet,dr.cat)))
      print("is thepet a pet ?" +str(isinstance(thepet,dr.pet)))
      print(jess.name)
      print(thepet.name) 
      
    #isinstance(s, str)  isinstance(x,int);
#to check the variable is string or int

       
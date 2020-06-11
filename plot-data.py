# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 01:48:43 2020

@author: prisc
"""

# importing the required module 
import pandas as pd
import matplotlib.pyplot as plt

csv_file = 'f_kognitif.csv'
data = pd.read_csv(csv_file)

score = data["fkognitif"]
student = data["mahasiswa"]

# x axis values 
x = [] 
# corresponding y axis values 
y = [] 

x = list(student)
y = list(score)
  
# plotting the points  
plt.plot(x, y) 
  
# naming the x axis 
plt.xlabel('Students [i]') 
# naming the y axis 
plt.ylabel('Cognitive Score') 
  
# giving a title to my graph 
plt.title('Cognitive Factor') 
  
# function to show the plot 
plt.show()
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 22:28:24 2020

@author: prisc
"""
import pandas as pd
import numpy as np
import FuzzyRules as fr

data_depresi = 'data_depresi_tif.xlsx'
df = pd.read_excel(data_depresi)
df.drop(['sex', 'kategori ipk', 'pkl'], axis = 1, inplace = True)
df.drop([0], axis = 0, inplace = True)
df.iloc[:, :30][df.iloc[:, :30] == 'Ya'] = 1
df.iloc[:, :30][df.iloc[:, :30] == 'Tidak'] = 0
#print (df)
#print (df.iloc[:, :6])
isi = df.values.tolist()
#print (isi)
print ("=======================================")

batas = [14, 21, 30]
mulai = [0, 14, 21]

isi_FM = 0
isi_FA = 0
isi_FK = 0
value_FM = []
value_FA = []
value_FK = []

#isi = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
#       [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1]]


for i in range(len(isi)):
    isi_FM = isi[i][mulai[0]:batas[0]].copy()
    isi_FM = sum(isi[i][mulai[0]:batas[0]])
    
    isi_FA = isi[i][mulai[1]:batas[1]].copy()
    isi_FA = sum(isi[i][mulai[1]:batas[1]])
    
    isi_FK = isi[i][mulai[2]:batas[2]].copy()
    isi_FK = sum(isi[i][mulai[2]:batas[2]])
    
    print ("FM: ", isi_FM, " FA: ", isi_FA, " FK: ", isi_FK)
    
    value_FM.append(isi_FM)
    value_FA.append(isi_FA)
    value_FK.append(isi_FK)
    
print ("===========================")    
print ("Nilai FM: ", value_FM)
print ("Nilai FA: ", value_FA)
print ("Nilai FK: ", value_FK)

print ("==============================================")
data_input = list(map(list, zip(value_FM, value_FA, value_FK)))
print (data_input)
print ("======================================================================")

for i in range(len(data_input)):
    #for j in range(len(data_input[i])):
        nilai_dep = []
        valFM = data_input[i][0]
        valFA = data_input[i][1]
        valFK = data_input[i][2]
        print ("========================")
        
        skor_dep = fr.setRules(valFM, valFA, valFK)
        print (valFM, " ", valFA, " ", valFK, "  ----> ", skor_dep)

    

        
    
    
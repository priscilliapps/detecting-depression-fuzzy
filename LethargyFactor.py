# -*- coding: utf-8 -*-
"""
Created on Mon May 25 21:38:29 2020

@author: prisc
"""


c_low_le = 4 #nilai c faktor lethargy rendah

b_mod_le = 4 #nilai b faktor lethargy sedang
c_mod_le = 7 #nilai c faktor lethargy sedang

a_high_le = 4 #nilai a faktor lethargy tinggi
b_high_le = 7 #nilai b faktor lethargy tinggi
c_high_le = 9 #nilai c faktor lethargy tinggi

a_sev_le = 7 #nilai a faktor lethargy sangat tinggi
b_sev_le = 9 #nilai b faktor lethargy sangat tinggi

def low_lethargy(skor_FK):
    if skor_FK >= 0 and skor_FK <= c_low_le:
        mf_value = round((c_low_le - skor_FK)/(c_low_le - 0), 3)
    else:
        mf_value = 0
    return mf_value

def moderate_lethargy(skor_FK):
    if skor_FK >= 0 and skor_FK <= b_mod_le:
        mf_value = round((skor_FK - 0)/(b_mod_le - 0), 3)
    elif skor_FK >= b_mod_le and skor_FK <= c_mod_le:
        mf_value = round((c_mod_le - skor_FK)/(c_mod_le - b_mod_le), 3)
    else:
        mf_value = 0
    return mf_value

def high_lethargy(skor_FK):
    if skor_FK >= a_high_le and skor_FK <= b_high_le:
        mf_value = round((skor_FK - a_high_le)/(b_high_le - a_high_le), 3)
    elif skor_FK >= b_high_le and skor_FK <= c_high_le:
        mf_value = round((c_high_le - skor_FK)/(c_high_le - b_high_le), 3)
    else:
        mf_value = 0
    return mf_value

def very_high_lethargy(skor_FK):
    if skor_FK >= a_sev_le and skor_FK <= b_sev_le:
        mf_value = round((skor_FK - a_sev_le)/(b_sev_le - a_sev_le), 3)
    else:
        mf_value = 0
    return mf_value

#listFM = [8]
#w = low_lethargy(listFM)
#x = moderate_lethargy(listFM)
#y = high_lethargy(listFM)
#z = severe_lethargy(listFM)
#print (z)

#x1 = []
#y1 = []
#y2 = []
#y3 = []
#y4 = []

#plt.figure()
#for i in range(skor_FM):
#    y1.append(low_motivation(i))
#    y2.append(moderate_motivation(i))
#    y3.append(high_motivation(i))
#    y4.append(severe_motivation(i))
#    x1.append(i)
    
#plt.plot(x1, y1)
#plt.plot(x1, y2)
#plt.plot(x1, y3)
#plt.plot(x1, y4)
#plt.legend(('low', 'moderate', 'high', 'severe'), loc = 'upper right')
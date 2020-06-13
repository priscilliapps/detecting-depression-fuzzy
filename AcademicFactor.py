# -*- coding: utf-8 -*-
"""
Created on Sun May 24 22:38:31 2020

@author: prisc
"""


c_low_ac = 3 #nilai c faktor akademik rendah

b_mod_ac = 3 #nilai b faktor akademik sedang
c_mod_ac = 5 #nilai c faktor akademik sedang

a_high_ac = 3 #nilai a faktor akademik tinggi
b_high_ac = 5 #nilai b faktor akademik tinggi
c_high_ac = 7 #nilai c faktor akademik tinggi

a_sev_ac = 5 #nilai a faktor akademik sangat tinggi
b_sev_ac = 7 #nilai b faktor akademik sangat tinggi

def low_academic(skor_FA):
    if skor_FA >= 0 and skor_FA <= c_low_ac:
        mf_value = round((c_low_ac - skor_FA)/(c_low_ac - 0), 3)
    else:
        mf_value = 0
    return mf_value

def moderate_academic(skor_FA):
    if skor_FA >= 0 and skor_FA <= b_mod_ac:
        mf_value = round((skor_FA - 0)/(b_mod_ac - 0), 3)
    elif skor_FA >= b_mod_ac and skor_FA <= c_mod_ac:
        mf_value = round((c_mod_ac - skor_FA)/(c_mod_ac - b_mod_ac), 3)
    else:
        mf_value = 0
    return mf_value

def high_academic(skor_FA):
    if skor_FA >= a_high_ac and skor_FA <= b_high_ac:
        mf_value = round((skor_FA - a_high_ac)/(b_high_ac - a_high_ac), 3)
    elif skor_FA >= b_high_ac and skor_FA <= c_high_ac:
        mf_value = round((c_high_ac - skor_FA)/(c_high_ac - b_high_ac), 3)
    else:
        mf_value = 0
    return mf_value

def very_high_academic(skor_FA):
    if skor_FA >= a_sev_ac and skor_FA <= b_sev_ac:
        mf_value = round((skor_FA - a_sev_ac)/(b_sev_ac - a_sev_ac), 3)
    else:
        mf_value = 0
    return mf_value

#listFM = [4]
#w = low_academic(listFM)
#x = moderate_academic(listFM)
#y = high_academic(listFM)
#z = severe_academic(listFM)
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
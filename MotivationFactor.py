# -*- coding: utf-8 -*-
"""
Created on Sun May 24 19:32:32 2020

@author: prisc
"""

c_low_mo = 5 #nilai b faktor motivasi rendah

b_mod_mo = 5 #nilai b faktor motivasi sedang
c_mod_mo = 10 #nilai c faktor motivasi sedang

a_high_mo = 5 #nilai a faktor motivasi tinggi
b_high_mo = 10 #nilai b faktor motivasi tinggi
c_high_mo = 14 #nilai c faktor motivasi tinggi

a_sev_mo = 10 #nilai a faktor motivasi sangat tinggi
b_sev_mo = 14 #nilai b faktor motivasi sangat tinggi

def low_motivation(skor_FM):
    #for i in range(len(skor_FM)):
        if skor_FM >= 0 and skor_FM <= c_low_mo:
            mf_value = round((c_low_mo - skor_FM)/(c_low_mo - 0), 3)
        else:
            mf_value = 0
        return mf_value

def moderate_motivation(skor_FM):
    #for i in range(len(skor_FM)):
        if skor_FM >= 0 and skor_FM <= b_mod_mo:
            mf_value = round((skor_FM - 0)/(b_mod_mo - 0), 3)
        elif skor_FM >= b_mod_mo and skor_FM <= c_mod_mo:
            mf_value = round((c_mod_mo - skor_FM)/(c_mod_mo - b_mod_mo), 3)
        else:
            mf_value = 0
        return mf_value

def high_motivation(skor_FM):  
    #for i in range(len(skor_FM)):
        if skor_FM >= a_high_mo and skor_FM <= b_high_mo:
            mf_value = round((skor_FM - a_high_mo)/(b_high_mo - a_high_mo), 3)
        elif skor_FM >= b_high_mo and skor_FM <= c_high_mo:
            mf_value = round((c_high_mo - skor_FM)/(c_high_mo - b_high_mo), 3)
        else:
            mf_value = 0
        return mf_value

def severe_motivation(skor_FM):
    #for i in range(len(skor_FM)):
        if skor_FM >= a_sev_mo and skor_FM <= b_sev_mo:
            mf_value = round((skor_FM - a_sev_mo)/(b_sev_mo - a_sev_mo), 3)
        else:
            mf_value = 0
        return mf_value


#listFM = [13]
#w = low_motivation(listFM)
#x = moderate_motivation(listFM)
#y = high_motivation(listFM)
#z = severe_motivation(listFM)
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
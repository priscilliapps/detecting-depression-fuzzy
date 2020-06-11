# -*- coding: utf-8 -*-
"""
Created on Sat May 23 14:15:31 2020

@author: prisc
"""
import MotivationFactor as fm
import AcademicFactor as fa
import LethargyFactor as fk

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

#def main(value_FK):
    #dk_lethargy_factor = []
    #for i in range(len(value_FK)):
        #valFK = value_FK[i]
        #dk = fk.low_lethargy(valFK)
        #dk_FM_moderate = fm.moderate_motivation(valFM)
        #dk_FM_high = fm.high_motivation(valFM)
        #dk_FM_severe = fm.severe_motivation(valFM)
        #dk_lethargy_factor.append(dk)
        #return dk_motivation_factor
    #return dk_lethargy_factor

#y = main(value_FK)
#print ("===========================")
#print ("Membership Functions FM: ", y)    


#dk_motivation_factor = []
#dk_motivation_factor.append(dk_FM_severe)
#print (dk_motivation_factor)

    #dk_FM_moderate = fm.moderate_motivation(skor_FM)
    #dk_FM_high = fm.high_motivation(skor_FM)
    #dk_FM_severe = fm.severe_motivation(skor_FM)
     

#derajat_keanggotaanFA = fa.moderate_academic(skor_FA)
#print ("Derajat Keanggotaan FA: ", derajat_keanggotaanFA)
#derajat_keanggotaanFK = fk.high_lethargy(skor_FK)
#print ("Derajat Keanggotaan FA: ", derajat_keanggotaanFK)





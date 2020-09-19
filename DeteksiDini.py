# -*- coding: utf-8 -*-
"""
Created on Sat May 16 22:28:24 2020

@author: prisc
"""
import pandas as pd
import FuzzyRules as fr
import Depression as dep
import MotivationFactor as fm
import AcademicFactor as fa
import LethargyFactor as fk

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

kategori_usdi = None
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
print ("Skor Faktor Gejala (Input):")
print (data_input)
print ("======================================================================")

def dk_depresi(skor_dep):
    mf_dict = {'Rendah': dep.low_depression(skor_dep), 'Sedang': dep.moderate_depression(skor_dep), 'Tinggi': dep.high_depression(skor_dep), 'Sangat Tinggi': dep.very_high_depression(skor_dep)}
    max_mf = max(mf_dict, key = mf_dict.get)
    return max_mf

def dk_fMotivasi(skor_FM):
    mf_fMotivasi = {'Rendah': fm.low_motivation(skor_FM), 'Sedang': fm.moderate_motivation(skor_FM), 'Tinggi': fm.high_motivation(skor_FM), 'Sangat Tinggi': fm.very_high_motivation(skor_FM)}
    max_mf = max(mf_fMotivasi, key = mf_fMotivasi.get)
    return max_mf

def dk_fAkademik(skor_FA):
    mf_fAkademik = {'Rendah': fa.low_academic(skor_FA), 'Sedang': fa.moderate_academic(skor_FA), 'Tinggi': fa.high_academic(skor_FA), 'Sangat Tinggi': fa.very_high_academic(skor_FA)}
    max_mf = max(mf_fAkademik, key = mf_fAkademik.get)
    return max_mf

def dk_fLethargy(skor_FK):
    fk_rendah = fk.low_lethargy(skor_FK)
    fk_sedang = fk.moderate_lethargy(skor_FK)
    fk_tinggi = fk.high_lethargy(skor_FK)
    fk_st = fk.very_high_lethargy(skor_FK)
    mf_fLethargy = {'Rendah': fk_rendah, 'Sedang': fk_sedang, 'Tinggi': fk_tinggi, 'Sangat Tinggi': fk_st}
    max_mf = max(mf_fLethargy, key = mf_fLethargy.get)
    return max_mf

for i in range(len(data_input)):
    #for j in range(len(data_input[i])):
        nilai_dep = []
        valFM = data_input[i][0]
        valFA = data_input[i][1]
        valFK = data_input[i][2]
        skor_dep = fr.setRules(valFM, valFA, valFK)
        kategori_fuzzy = dk_depresi(skor_dep)
        #dk_fm = dk_fMotivasi(valFM)
        #dk_fa = dk_fAkademik(valFA)
        #dk_fk = dk_fLethargy(valFK)
        
        skor_usdi = valFM + valFA + valFK
        if skor_usdi <= 13:
            skor_usdi = "Rendah"
        elif skor_usdi > 13 and skor_usdi <= 19:
            skor_usdi = "Sedang"
        elif skor_usdi > 19 and skor_usdi <= 25:
            skor_usdi = "Tinggi"
        else:
            skor_usdi = "Sangat Tinggi"
        
        print ("FM: ", valFM, " ", "FA: ", valFA, " ", "FK: ", valFK, "  ----> ", skor_dep, " ", skor_usdi, kategori_fuzzy)
        #print ("FM ", dk_fm, " FA ", dk_fa, " FK ", dk_fk)
        print (" ")
        
        

        
    
    
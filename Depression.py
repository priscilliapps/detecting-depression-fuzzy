# -*- coding: utf-8 -*-
"""
Created on Fri May 29 23:40:05 2020

@author: prisc
"""
mf_depresi = 0

c_low_dep = 13 #titik c tingkat depresi rendah

a_mod_dep = 12 #titik a tingkat depresi sedang
c_mod_dep = 19 #titik c tingkat depresi sedang

a_high_dep = 18 #titik a tingkat depresi tinggi
c_high_dep = 25 #titik c tingkat depresi tinggi

a_sev_dep = 24 #titik a tingkat depresi sangat tinggi
b_sev_dep = 30 #titik c tingkat depresi sangat tinggi

def low_depression(skor_depresi):
    if skor_depresi >= 0 and skor_depresi <= c_low_dep:
        mf_depresi = round((c_low_dep - skor_depresi)/c_low_dep, 3)
    else:
        mf_depresi = 0
    return mf_depresi

def moderate_depression(skor_depresi):
    if skor_depresi >= a_mod_dep and skor_depresi <= c_mod_dep:
        mf_depresi = round((skor_depresi - c_mod_dep)/(c_mod_dep - ((c_mod_dep + a_mod_dep)/2)), 3)
    else:
        mf_depresi = 0
    return mf_depresi

def high_depression(skor_depresi):
    if skor_depresi >= a_high_dep and skor_depresi <= c_high_dep:
        mf_depresi = round((skor_depresi - c_high_dep)/(c_high_dep - ((c_high_dep + a_high_dep)/2)), 3)
    else:
        mf_depresi = 0
    return mf_depresi

def very_high_depression(skor_depresi):
    if skor_depresi >= a_sev_dep and skor_depresi <= b_sev_dep:
        mf_depresi = round((skor_depresi - a_sev_dep)/(b_sev_dep - a_sev_dep), 3)
    else:
        mf_depresi = 0
    return mf_depresi


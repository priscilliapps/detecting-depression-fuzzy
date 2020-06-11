# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 20:44:55 2020

@author: prisc
"""
from Depression import c_low_dep, a_mod_dep, c_mod_dep, a_high_dep, c_high_dep, a_sev_dep, b_sev_dep


def z_low (alpha):
    z = c_low_dep - (c_low_dep * alpha)
    return z

def z_moderate (alpha):
    z = (alpha * (c_mod_dep - ((c_mod_dep + a_mod_dep)/2))) + c_mod_dep
    return z

def z_high (alpha):
    z = (alpha * (c_high_dep - ((c_high_dep + a_high_dep)/2))) + c_high_dep
    return z

def z_severe (alpha):
    z = (alpha * (b_sev_dep - a_sev_dep)) + a_sev_dep
    return z
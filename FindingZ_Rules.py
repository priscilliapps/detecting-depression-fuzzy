# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 20:44:55 2020

@author: prisc
"""
from Depression import c_low_dep, a_mod_dep, b_mod_dep, c_mod_dep, a_high_dep, b_high_dep, c_high_dep, a_sev_dep, b_sev_dep


def z_low (alpha):
    z = c_low_dep - (c_low_dep * alpha)
    return z

def z_moderate (alpha):
    z_mod_1 = (alpha * (b_mod_dep - a_mod_dep)) + a_mod_dep
    z_mod_2 = c_mod_dep - (alpha * (c_mod_dep - b_mod_dep))
    z = (z_mod_1 + z_mod_2)/2
    return z

def z_high (alpha):
    z_high_1 = (alpha * (b_high_dep - a_high_dep)) + a_high_dep
    z_high_2 = c_high_dep - (alpha * (c_high_dep - b_high_dep))
    z = (z_high_1 + z_high_2)/2
    return z

def z_very_high (alpha):
    z = (alpha * (b_sev_dep - a_sev_dep)) + a_sev_dep
    return z
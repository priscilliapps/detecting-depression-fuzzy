# -*- coding: utf-8 -*-
"""
Created on Sat May 30 00:35:28 2020

@author: prisc
"""
import numpy as np
import MotivationFactor as fm
import AcademicFactor as fa
import LethargyFactor as fk
import FindingZ_Rules as zr

#RULE : 
#alpha = min(fm._motivation(skor_FM), fa._academic(skor_FA), fk._lethargy(skor_FK))
#pre_alpha.append(alpha)
#z = z_(alpha)
#z_rule.append(z)
#az = round((alpha * z), 3)
#alpha_z.append(az)

def setRules (skor_FM, skor_FA, skor_FK):
    pre_alpha = []
    z_rule = []
    alpha_z = []
    
    #RULE 1: IF fm LOW AND fa LOW AND fk LOW THEN depression LOW
    #alpha1 = min(fm.low_motivation(skor_FM), fa.low_academic(skor_FA), fk.low_lethargy(skor_FK))
    #z1 = z_low(alpha1)
    #az1 = round((alpha1 * z1), 3)
    
    #RULE 2: IF fm LOW AND fa LOW AND fk MODERATE THEN depression LOW
    #alpha2 = min(fm.low_motivation(skor_FM), fa.low_academic(skor_FA), fk.moderate_lethargy(skor_FK))
    #z2 = z_low(alpha2)
    #az2 = round((alpha2 * z2), 3)
    
    #RULE 3: LOW - LOW - HIGH =  
    #alpha3 = min(fm.low_motivation(skor_FM), fa.low_academic(skor_FA), fk.high_lethargy(skor_FK)
    #if alpha3 != 0 :
        #pre_alpha.append(alpha3)
        #z3 = z_(alpha3)
        #z_rule.append(z3)
        #az3 = round((alpha3 * z3), 3)
        #alpha_z.append(az3)
    
    #RULE 4: LOW - LOW - SEVERE =  
    #alpha4 = min(fm.low_motivation(skor_FM), fa.low_academic(skor_FA), fk.severe_lethargy(skor_FK))
    #if alpha4 != 0:    
        #pre_alpha.append(alpha4)
        #z4 = z_(alpha4)
        #z_rule.append(z4)
        #az4 = round((alpha4 * z4), 3)
        #alpha_z.append(az4)
    
    #RULE 5: LOW - MODERATE - LOW = 
    #alpha5 = min(fm.low_motivation(skor_FM), fa.moderate_academic(skor_FA), fk.low_lethargy(skor_FK))
    #if alpha5 != 0:
        #pre_alpha.append(alpha5)
        #z5 = z_(alpha5)
        #z_rule.append(z5)
        #az5 = round((alpha5 * z5), 3)
        #alpha_z.append(az5)
    
    #RULE 6: LOW - MODERATE - MODERATE =  
    #alpha6 = min(fm.low_motivation(skor_FM), fa.moderate_academic(skor_FA), fk.moderate_lethargy(skor_FK))
    #if alpha6 != 0:
        #pre_alpha.append(alpha6)
        #z6 = z_(alpha6)
        #z_rule.append(z6)
        #az6 = round((alpha6 * z6), 3)
        #alpha_z.append(az6)
    
    #RULE 7: LOW - MODERATE - HIGH =
    #alpha7 = min(fm.low_motivation(skor_FM), fa.moderate_academic(skor_FA), fk.high_lethargy(skor_FK))
    #if alpha7 != 0:
        #pre_alpha.append(alpha7)
        #z7 = z_(alpha7)
        #z_rule.append(z7)
        #az7 = round((alpha7 * z7), 3)
        #alpha_z.append(az7)
    
    #RULE 8: LOW - MODERATE - SEVERE = 
    #alpha8 = min(fm.low_motivation(skor_FM), fa.moderate_academic(skor_FA), fk.severe_lethargy(skor_FK))
    #if alpha8 != 0:
        #pre_alpha.append(alpha8)
        #z8 = z_(alpha8)
        #z_rule.append(z8)
        #az8 = round((alpha8 * z8), 3)
        #alpha_z.append(az8)
    
    #RULE 9: LOW - HIGH - LOW = 
    #alpha9 = min(fm.low_motivation(skor_FM), fa.high_academic(skor_FA), fk.low_lethargy(skor_FK))
    #if alpha9 != 0:
        #pre_alpha.append(alpha9)
        #z = z_(alpha9)
        #z_rule.append(z9)
        #az9 = round((alpha9 * z9), 3)
        #alpha_z.append(az9)
    
    #RULE 10: LOW - HIGH - MODERATE = 
    #alpha10 = min(fm.low_motivation(skor_FM), fa.high_academic(skor_FA), fk.moderate_lethargy(skor_FK))
    #if alpha10 != 0:
        #pre_alpha.append(alpha10)
        #z10 = z_(alpha10)
        #z_rule.append(z10)
        #az10 = round((alpha10 * z10), 3)
        #alpha_z.append(az10)
    
    #RULE11 : LOW - HIGH - HIGH = 
    #alpha11 = min(fm.low_motivation(skor_FM), fa.high_academic(skor_FA), fk.high_lethargy(skor_FK))
    #if alpha11 != 0:
        #pre_alpha.append(alpha11)
        #z11 = zr.z_(alpha11)
        #z_rule.append(z11)
        #az11 = round((alpha11 * z11), 3)
        #alpha_z.append(az11)
    
    #RULE12 : LOW - HIGH - SEVERE = 
    #alpha12 = min(fm.low_motivation(skor_FM), fa.high_academic(skor_FA), fk.high_lethargy(skor_FK))
    #if alpha12 != 0:
        #pre_alpha.append(alpha12)
        #z12 = zr.z_(alpha12)
        #z_rule.append(z12)
        #az12 = round((alpha12 * z12), 3)
        #alpha_z.append(az12)
    
    #RULE13 : LOW - SEVERE - LOW = 
    #alpha13 = min(fm.low_motivation(skor_FM), fa.severe_academic(skor_FA), fk.low_lethargy(skor_FK))
    #if alpha13 != 0:
        #pre_alpha.append(alpha13)
        #z13 = zr.z_(alpha13)
        #z_rule.append(z13)
        #az13 = round((alpha13 * z13), 3)
        #alpha_z.append(az13)
    
    #RULE14 : LOW - SEVERE - MODERATE = 
    #alpha14 = min(fm.low_motivation(skor_FM), fa.severe_academic(skor_FA), fk.moderate_lethargy(skor_FK))
    #if alpha14 != 0:
        #pre_alpha.append(alpha14)
        #z14 = zr.z_(alpha14)
        #z_rule.append(z14)
        #az14 = round((alpha14 * z14), 3)
        #alpha_z.append(az14)
    
    #RULE15 : LOW - SEVERE - HIGH = 
    #alpha15 = min(fm.low_motivation(skor_FM), fa.severe_academic(skor_FA), fk.high_lethargy(skor_FK))
    #if alpha15 != 0:
        #pre_alpha.append(alpha15)
        #z15 = zr.z_(alpha15)
        #z_rule.append(z15)
        #az15 = round((alpha15 * z15), 3)
        #alpha_z.append(az15)
    
    #RULE16 : LOW - SEVERE - SEVERE = 
    #alpha16 = min(fm.low_motivation(skor_FM), fa.severe_academic(skor_FA), fk.severe_lethargy(skor_FK))
    #if alpha16 != 0:
        #pre_alpha.append(alpha16)
        #z16 = zr.z_(alpha16)
        #z_rule.append(z16)
        #az16 = round((alpha16 * z16), 3)
        #alpha_z.append(az16)
    
    #RULE 17 : MODERATE - LOW - LOW = 
    #alpha17 = min(fm.moderate_motivation(skor_FM), fa.low_academic(skor_FA), fk.low_lethargy(skor_FK))
    #if alpha17 != 0:
        #pre_alpha.append(alpha17)
        #z17 = zr.z_(alpha17)
        #z_rule.append(z17)
        #az17 = round((alpha17 * z17), 3)
        #alpha_z.append(az17)
    
    #RULE18 : MODERATE - LOW - MODERATE = 
    #alpha18 = min(fm.moderate_motivation(skor_FM), fa.low_academic(skor_FA), fk.moderate_lethargy(skor_FK))
    #if alpha18 != 0:
        #pre_alpha.append(alpha18)
        #z18 = zr.z_(alpha18)
        #z_rule.append(z18)
        #az18 = round((alpha18 * z18), 3)
        #alpha_z.append(az18)
    
    #RULE 19 : MODERATE - LOW - HIGH = 
    #alpha19 = min(fm._motivation(skor_FM), fa._academic(skor_FA), fk._lethargy(skor_FK))
    #if alpha19 != 0:
        #pre_alpha.append(alpha19)
        #z19 = zr.z_(alpha19)
        #z_rule.append(z19)
        #az19 = round((alpha19 * z19), 3)
        #alpha_z.append(az19)
    
    #RULE 20 : MODERATE - LOW - SEVERE =  
    #alpha20 = min(fm.moderate_motivation(skor_FM), fa.low_academic(skor_FA), fk.severe_lethargy(skor_FK))
    #if alpha20 != 0:
        #pre_alpha.append(alpha20)
        #z20 = zr.z_(alpha20)
        #z_rule.append(z20)
        #az20 = round((alpha20 * z20), 3)
        #alpha_z.append(az20)
    
    #RULE 21 : MODERATE - MODERATE - LOW = 
    #alpha21 = min(fm.moderate_motivation(skor_FM), fa.moderate_academic(skor_FA), fk.low_lethargy(skor_FK))
    #if alpha21 != 0:
        #pre_alpha.append(alpha21)
        #z21 = zr.z_(alpha21)
        #z_rule.append(z21)
        #az21 = round((alpha21 * z21), 3)
        #alpha_z.append(az21)
    
    #RULE 22 : MODERATE - MODERATE - MODERATE = MODERATE 
    #alpha22 = min(fm.moderate_motivation(skor_FM), fa.moderate_academic(skor_FA), fk.moderate_lethargy(skor_FK))
    #if alpha22 != 0:
        #pre_alpha.append(alpha22)
        #z22 = zr.z_(alpha22)
        #z_rule.append(z22)
        #az22 = round((alpha22 * z22), 3)
        #alpha_z.append(az22)
    
    #RULE 23: MODERATE - MODERATE - HIGH =  
    #alpha23 = min(fm.moderate_motivation(skor_FM), fa.moderate_academic(skor_FA), fk.high_lethargy(skor_FK))
    #if alpha23 != 0:
        #pre_alpha.append(alpha23)
        #z23 = zr.z_(alpha23)
        #z_rule.append(z23)
        #az23 = round((alpha23 * z23), 3)
        #alpha_z.append(az23)
    
    #RULE 24: MODERATE - MODERATE - SEVERE =  
    #alpha24 = min(fm.moderate_motivation(skor_FM), fa.moderate_academic(skor_FA), fk.severe_lethargy(skor_FK))
    #if alpha24 != 0:
        #pre_alpha.append(alpha24)
        #z24 = zr.z_(alpha24)
        #z_rule.append(z24)
        #az24 = round((alpha24 * z24), 3)
        #alpha_z.append(az24)
    
    #RULE 25: MODERATE - HIGH - LOW =  
    #alpha25 = min(fm.moderate_motivation(skor_FM), fa.high_academic(skor_FA), fk.low_lethargy(skor_FK))
    #if alpha25 != 0:
        #pre_alpha.append(alpha25)
        #z25 = zr.z_(alpha25)
        #z_rule.append(z25)
        #az25 = round((alpha25 * z25), 3)
        #alpha_z.append(az25)
    
    #RULE 26: MODERATE - HIGH - MODERATE = 
    #alpha26 = min(fm.moderate_motivation(skor_FM), fa.high_academic(skor_FA), fk.moderate_lethargy(skor_FK))
    #if alpha26 != 0:
        #pre_alpha.append(alpha26)
        #z26 = zr.z_(alpha26)
        #z_rule.append(z26)
        #az26 = round((alpha26 * z26), 3)
        #alpha_z.append(az26)
    
    #RULE 27: MODERATE - HIGH - HIGH =
    alpha27 = min(fm.moderate_motivation(skor_FM), fa.high_academic(skor_FA), fk.high_lethargy(skor_FK))
    if alpha27 != 0:
        pre_alpha.append(alpha27)
        z27 = zr.z_moderate(alpha27)
        z_rule.append(z27)
        az27 = round((alpha27 * z27), 3)
        alpha_z.append(az27)
    
    #RULE 28: MODERATE - HIGH - SEVERE =
    alpha28 = min(fm.moderate_motivation(skor_FM), fa.high_academic(skor_FA), fk.severe_lethargy(skor_FK))
    if alpha28 != 0:
        pre_alpha.append(alpha28)
        z28 = zr.z_moderate(alpha28)
        z_rule.append(z28)
        az28 = round((alpha28 * z28), 3)
        alpha_z.append(az28)
        
    #RULE 29: MODERATE - SEVERE - LOW = 
    #alpha29 = min(fm.moderate_motivation(skor_FM), fa.severe_academic(skor_FA), fk.low_lethargy(skor_FK))
    #if alpha29 != 0:
        #pre_alpha.append(alpha29)
        #z29 = zr.z_(alpha29)
        #z_rule.append(z29)
        #az29 = round((alpha29 * z29), 3)
        #alpha_z.append(az29)
    
    #RULE 30: MODERATE - SEVERE - MODERATE =  
    #alpha30 = min(fm.moderate_motivation(skor_FM), fa.severe_academic(skor_FA), fk.moderate_lethargy(skor_FK))
    #if alpha30 != 0:
        #pre_alpha.append(alpha30)
        #z30 = zr.z_(alpha30)
        #z_rule.append(z30)
        #az30 = round((alpha30 * z30), 3)
        #alpha_z.append(az30)
    
    #RULE 31: MODERATE - SEVERE - HIGH = 
    #alpha31 = min(fm.moderate_motivation(skor_FM), fa.severe_academic(skor_FA), fk.high_lethargy(skor_FK))
    #if alpha31 != 0:
        #pre_alpha.append(alpha31)
        #z31 = zr.z_(alpha31)
        #z_rule.append(z31)
        #az31 = round((alpha31 * z31), 3)
        #alpha_z.append(az31)
    
    #RULE 32: MODERATE - SEVERE - SEVERE =  
    #alpha32 = min(fm.moderate_motivation(skor_FM), fa.severe_academic(skor_FA), fk.severe_lethargy(skor_FK))
    #if alpha32 != 0:
        #pre_alpha.append(alpha32)
        #z32 = zr.z_(alpha32)
        #z_rule.append(z32)
        #az32 = round((alpha32 * z32), 3)
        #alpha_z.append(az32)
    
    #RULE 33: HIGH - LOW - LOW = HIGH 
    alpha33 = min(fm.high_motivation(skor_FM), fa.low_academic(skor_FA), fk.low_lethargy(skor_FK))
    if alpha33 != 0:
        pre_alpha.append(alpha33)
        z33 = zr.z_high(alpha33)
        z_rule.append(z33)
        az33 = round((alpha33 * z33), 3)
        alpha_z.append(az33)
    
    #RULE 34: HIGH - LOW - MODERATE = HIGH 
    alpha34 = min(fm.high_motivation(skor_FM), fa.low_academic(skor_FA), fk.moderate_lethargy(skor_FK))
    if alpha34 != 0:
        pre_alpha.append(alpha34)
        z34 = zr.z_high(alpha34)
        z_rule.append(z34)
        az34 = round((alpha34 * z34), 3)
        alpha_z.append(az34)
    
    #RULE 35: HIGH - LOW - HIGH = SEVERE 
    alpha35 = min(fm.high_motivation(skor_FM), fa.low_academic(skor_FA), fk.high_lethargy(skor_FK))
    if alpha35 != 0:
        pre_alpha.append(alpha35)
        z35 = zr.z_severe(alpha35)
        z_rule.append(z35)
        az35 = round((alpha35 * z35), 3)
        alpha_z.append(az35)
    
    #RULE 36: HIGH - LOW - SEVERE = SEVERE  
    alpha36 = min(fm.high_motivation(skor_FM), fa.low_academic(skor_FA), fk.severe_lethargy(skor_FK))
    if alpha36 != 0:
        pre_alpha.append(alpha36)
        z36 = zr.z_severe(alpha36)
        z_rule.append(z36)
        az36 = round((alpha36 * z36), 3)
        alpha_z.append(az36)
        
    #RULE 37: HIGH - MODERATE - LOW = HIGH  
    alpha37 = min(fm.high_motivation(skor_FM), fa.moderate_academic(skor_FA), fk.low_lethargy(skor_FK))
    if alpha37 != 0:
        pre_alpha.append(alpha37)
        z37 = zr.z_severe(alpha37)
        z_rule.append(z37)
        az37 = round((alpha37 * z37), 3)
        alpha_z.append(az37)
    
    #RULE 38: HIGH - MODERATE - MODERATE = HIGH
    alpha38 = min(fm.high_motivation(skor_FM), fa.moderate_academic(skor_FA), fk.moderate_lethargy(skor_FK))
    if alpha38 != 0:
        pre_alpha.append(alpha38)
        z38 = zr.z_high(alpha38)
        z_rule.append(z38)
        az38 = round((alpha38 * z38), 3)
        alpha_z.append(az38)
    
    #RULE 39: HIGH - MODERATE - HIGH = HIGH
    alpha39 = min(fm.high_motivation(skor_FM), fa.moderate_academic(skor_FA), fk.high_lethargy(skor_FK))
    if alpha39 != 0:
        pre_alpha.append(alpha39)
        z39 = zr.z_high(alpha39)
        z_rule.append(z39)
        az39 = round((alpha39 * z39), 3)
        alpha_z.append(az39)
    
    #RULE 40: HIGH - MODERATE - SEVERE = HIGH
    alpha40 = min(fm.high_motivation(skor_FM), fa.moderate_academic(skor_FA), fk.severe_lethargy(skor_FK))
    if alpha40 != 0:
        pre_alpha.append(alpha40)
        z40 = zr.z_high(alpha40)
        z_rule.append(z40)
        az40 = round((alpha40 * z40), 3)
        alpha_z.append(az40)
    
    #RULE 43: HIGH - HIGH - HIGH = HIGH
    alpha43 = min(fm.high_motivation(skor_FM), fa.high_academic(skor_FA), fk.high_lethargy(skor_FK))
    if alpha43 != 0:
        pre_alpha.append(alpha43)
        z43 = zr.z_high(alpha43)
        z_rule.append(z43)
        az43 = round((alpha43 * z43), 3)
        alpha_z.append(az43)
    
    #RULE 44: HIGH - HIGH - SEVERE = 
    alpha44 = min(fm.high_motivation(skor_FM), fa.high_academic(skor_FA), fk.severe_lethargy(skor_FK))
    if alpha44 != 0:
        pre_alpha.append(alpha44)
        z44 = zr.z_high(alpha44)
        z_rule.append(z44)
        az44 = round((alpha44 * z44), 3)
        alpha_z.append(az44)
    
    #RULE 55: SEVERE - MODERATE - HIGH = HIGH
    alpha55 = min(fm.severe_motivation(skor_FM), fa.moderate_academic(skor_FA), fk.high_lethargy(skor_FK))
    if alpha55 != 0:
        pre_alpha.append(alpha55)
        z55 = zr.z_high(alpha55)
        z_rule.append(z55)
        az55 = round((alpha55 * z55), 3)
        alpha_z.append(az55)
    
    #RULE 56: SEVERE - MODERATE - SEVERE = SEVERE
    alpha56 = min(fm.severe_motivation(skor_FM), fa.moderate_academic(skor_FA), fk.severe_lethargy(skor_FK))
    if alpha56 != 0:
        pre_alpha.append(alpha56)
        z56 = zr.z_severe(alpha56)
        z_rule.append(z56)
        az56 = round((alpha56 * z56), 3)
        alpha_z.append(az56)
    
    #RULE 59: SEVERE - HIGH - HIGH = SEVERE
    alpha59 = min(fm.severe_motivation(skor_FM), fa.high_academic(skor_FA), fk.high_lethargy(skor_FK))
    if alpha59 != 0:
        pre_alpha.append(alpha59)
        z59 = zr.z_severe(alpha59)
        z_rule.append(z59)
        az59 = round((alpha59 * z59), 3)
        alpha_z.append(az59)
    
    #RULE 60: SEVERE - HIGH - SEVERE = SEVERE
    alpha60 = min(fm.severe_motivation(skor_FM), fa.high_academic(skor_FA), fk.severe_lethargy(skor_FK))
    if alpha60 != 0:
        pre_alpha.append(alpha60)
        z60 = zr.z_severe(alpha60)
        z_rule.append(z60)
        az60 = round((alpha60 * z60), 3)
        alpha_z.append(az60)
    
    alpha_sum = round(sum(pre_alpha), 3)
    print ("Alpha Pre      : ", pre_alpha)
    print ("Total Alpha    : ", alpha_sum)
    
    print ("Nilai Z        : ", z_rule)
    
    alphaZ_sum = round(sum(alpha_z), 3)
    print ("Z x Alpha      : ", alpha_z)
    print ("Total Alpha x Z: ", alphaZ_sum)

    try:
        z_total = round((alphaZ_sum/alpha_sum), 3)
        print ("Nilai Skor: ", z_total)
    except:
        z_total = 0
        print ("Nilai Skor: ", 0)
    
    
    #print ("Alpha Predikat: ", pre_alpha)
    #print ("Z Tiap Rule: ", z_rule)
    #print ("Alpha x Z: ", alpha_z)
    #print ("Skor Depresi: ", z_total)

#setRules(13, 4, 8)
#print ("Alpha pre: ", pre_alpha)
#print ("Sum Alpha Pre: ", alpha_sum)
#print ("Z rule: ", z_rule)
#print ("AlphaxZ: ", alpha_z)
#print ("Sum AlphaZ: ", alphaZ_sum)
#print ("Skor: ", z_total)

 
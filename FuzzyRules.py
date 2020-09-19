# -*- coding: utf-8 -*-
"""
Created on Sat May 30 00:35:28 2020

@author: prisc
"""
import MotivationFactor as fm
import AcademicFactor as fa
import LethargyFactor as fk
import FindingZ_Rules as zr


def setRules (skor_FM, skor_FA, skor_FK):
    pre_alpha = []
    z_rule = []
    alpha_z = []
    
    #RULE 1: LOW - LOW - LOW = LOW
    alpha1 = min(fm.low_motivation(skor_FM), fa.low_academic(skor_FA), fk.low_lethargy(skor_FK))
    if alpha1 != 0 :
        pre_alpha.append(alpha1)
        z1 = zr.z_low(alpha1)
        z_rule.append(z1)
        az1 = round((alpha1 * z1), 3)
        alpha_z.append(az1)
    
    #RULE 2: LOW - LOW - MODERATE = LOW
    alpha2 = min(fm.low_motivation(skor_FM), fa.low_academic(skor_FA), fk.moderate_lethargy(skor_FK))
    if alpha2 != 0 :
        pre_alpha.append(alpha2)
        z2 = zr.z_low(alpha2)
        z_rule.append(z2)
        az2 = round((alpha2 * z2), 3)
        alpha_z.append(az2)
    
    #RULE 3: LOW - LOW - HIGH =  LOW
    alpha3 = min(fm.low_motivation(skor_FM), fa.low_academic(skor_FA), fk.high_lethargy(skor_FK))
    if alpha3 != 0 :
        pre_alpha.append(alpha3)
        z3 = zr.z_low(alpha3)
        z_rule.append(z3)
        az3 = round((alpha3 * z3), 3)
        alpha_z.append(az3)
    
    #RULE 4: LOW - LOW - VERY HIGH = LOW 
    alpha4 = min(fm.low_motivation(skor_FM), fa.low_academic(skor_FA), fk.very_high_lethargy(skor_FK))
    if alpha4 != 0:    
        pre_alpha.append(alpha4)
        z4 = zr.z_low(alpha4)
        z_rule.append(z4)
        az4 = round((alpha4 * z4), 3)
        alpha_z.append(az4)
    
    #RULE 5: LOW - MODERATE - LOW = LOW
    alpha5 = min(fm.low_motivation(skor_FM), fa.moderate_academic(skor_FA), fk.low_lethargy(skor_FK))
    if alpha5 != 0:
        pre_alpha.append(alpha5)
        z5 = zr.z_low(alpha5)
        z_rule.append(z5)
        az5 = round((alpha5 * z5), 3)
        alpha_z.append(az5)
    
    #RULE 6: LOW - MODERATE - MODERATE = LOW
    alpha6 = min(fm.low_motivation(skor_FM), fa.moderate_academic(skor_FA), fk.moderate_lethargy(skor_FK))
    if alpha6 != 0:
        pre_alpha.append(alpha6)
        z6 = zr.z_low(alpha6)
        z_rule.append(z6)
        az6 = round((alpha6 * z6), 3)
        alpha_z.append(az6)
    
    #RULE 7: LOW - MODERATE - HIGH = LOW
    alpha7 = min(fm.low_motivation(skor_FM), fa.moderate_academic(skor_FA), fk.high_lethargy(skor_FK))
    if alpha7 != 0:
        pre_alpha.append(alpha7)
        z7 = zr.z_low(alpha7)
        z_rule.append(z7)
        az7 = round((alpha7 * z7), 3)
        alpha_z.append(az7)
    
    #RULE 8: LOW - MODERATE - VERY HIGH = LOW
    alpha8 = min(fm.low_motivation(skor_FM), fa.moderate_academic(skor_FA), fk.very_high_lethargy(skor_FK))
    if alpha8 != 0:
        pre_alpha.append(alpha8)
        z8 = zr.z_low(alpha8)
        z_rule.append(z8)
        az8 = round((alpha8 * z8), 3)
        alpha_z.append(az8)
    
    #RULE 9: LOW - HIGH - LOW = LOW
    alpha9 = min(fm.low_motivation(skor_FM), fa.high_academic(skor_FA), fk.low_lethargy(skor_FK))
    if alpha9 != 0:
        pre_alpha.append(alpha9)
        z9 = zr.z_low(alpha9)
        z_rule.append(z9)
        az9 = round((alpha9 * z9), 3)
        alpha_z.append(az9)
    
    #RULE 10: LOW - HIGH - MODERATE = LOW
    alpha10 = min(fm.low_motivation(skor_FM), fa.high_academic(skor_FA), fk.moderate_lethargy(skor_FK))
    if alpha10 != 0:
        pre_alpha.append(alpha10)
        z10 = zr.z_low(alpha10)
        z_rule.append(z10)
        az10 = round((alpha10 * z10), 3)
        alpha_z.append(az10)
    
    #RULE11 : LOW - HIGH - HIGH = LOW
    alpha11 = min(fm.low_motivation(skor_FM), fa.high_academic(skor_FA), fk.high_lethargy(skor_FK))
    if alpha11 != 0:
        pre_alpha.append(alpha11)
        z11 = zr.z_low(alpha11)
        z_rule.append(z11)
        az11 = round((alpha11 * z11), 3)
        alpha_z.append(az11)
    
    #RULE12 : LOW - HIGH - VERY HIGH = LOW
    alpha12 = min(fm.low_motivation(skor_FM), fa.high_academic(skor_FA), fk.high_lethargy(skor_FK))
    if alpha12 != 0:
        pre_alpha.append(alpha12)
        z12 = zr.z_low(alpha12)
        z_rule.append(z12)
        az12 = round((alpha12 * z12), 3)
        alpha_z.append(az12)
    
    #RULE13 : LOW - VERY HIGH - LOW = LOW
    alpha13 = min(fm.low_motivation(skor_FM), fa.very_high_academic(skor_FA), fk.low_lethargy(skor_FK))
    if alpha13 != 0:
        pre_alpha.append(alpha13)
        z13 = zr.z_low(alpha13)
        z_rule.append(z13)
        az13 = round((alpha13 * z13), 3)
        alpha_z.append(az13)
    
    #RULE14 : LOW - VERY HIGH - MODERATE = LOW
    alpha14 = min(fm.low_motivation(skor_FM), fa.very_high_academic(skor_FA), fk.moderate_lethargy(skor_FK))
    if alpha14 != 0:
        pre_alpha.append(alpha14)
        z14 = zr.z_low(alpha14)
        z_rule.append(z14)
        az14 = round((alpha14 * z14), 3)
        alpha_z.append(az14)
    
    #RULE15 : LOW - VERY HIGH - HIGH = LOW
    alpha15 = min(fm.low_motivation(skor_FM), fa.very_high_academic(skor_FA), fk.high_lethargy(skor_FK))
    if alpha15 != 0:
        pre_alpha.append(alpha15)
        z15 = zr.z_low(alpha15)
        z_rule.append(z15)
        az15 = round((alpha15 * z15), 3)
        alpha_z.append(az15)
    
    #RULE16 : LOW - VERY HIGH - VERY HIGH = LOW
    alpha16 = min(fm.low_motivation(skor_FM), fa.very_high_academic(skor_FA), fk.very_high_lethargy(skor_FK))
    if alpha16 != 0:
        pre_alpha.append(alpha16)
        z16 = zr.z_low(alpha16)
        z_rule.append(z16)
        az16 = round((alpha16 * z16), 3)
        alpha_z.append(az16)
    
    #RULE 17 : MODERATE - LOW - LOW = LOW
    alpha17 = min(fm.moderate_motivation(skor_FM), fa.low_academic(skor_FA), fk.low_lethargy(skor_FK))
    if alpha17 != 0:
        pre_alpha.append(alpha17)
        z17 = zr.z_low(alpha17)
        z_rule.append(z17)
        az17 = round((alpha17 * z17), 3)
        alpha_z.append(az17)
    
    #RULE18 : MODERATE - LOW - MODERATE = LOW
    alpha18 = min(fm.moderate_motivation(skor_FM), fa.low_academic(skor_FA), fk.moderate_lethargy(skor_FK))
    if alpha18 != 0:
        pre_alpha.append(alpha18)
        z18 = zr.z_low(alpha18)
        z_rule.append(z18)
        az18 = round((alpha18 * z18), 3)
        alpha_z.append(az18)
    
    #RULE 19 : MODERATE - LOW - HIGH = LOW
    alpha19 = min(fm.moderate_motivation(skor_FM), fa.low_academic(skor_FA), fk.high_lethargy(skor_FK))
    if alpha19 != 0:
        pre_alpha.append(alpha19)
        z19 = zr.z_low(alpha19)
        z_rule.append(z19)
        az19 = round((alpha19 * z19), 3)
        alpha_z.append(az19)
    
    #RULE 20 : MODERATE - LOW - VERY HIGH =  LOW
    alpha20 = min(fm.moderate_motivation(skor_FM), fa.low_academic(skor_FA), fk.very_high_lethargy(skor_FK))
    if alpha20 != 0:
        pre_alpha.append(alpha20)
        z20 = zr.z_low(alpha20)
        z_rule.append(z20)
        az20 = round((alpha20 * z20), 3)
        alpha_z.append(az20)
    
    #RULE 21 : MODERATE - MODERATE - LOW = LOW
    alpha21 = min(fm.moderate_motivation(skor_FM), fa.moderate_academic(skor_FA), fk.low_lethargy(skor_FK))
    if alpha21 != 0:
        pre_alpha.append(alpha21)
        z21 = zr.z_low(alpha21)
        z_rule.append(z21)
        az21 = round((alpha21 * z21), 3)
        alpha_z.append(az21)
    
    #RULE 22 : MODERATE - MODERATE - MODERATE = MODERATE 
    alpha22 = min(fm.moderate_motivation(skor_FM), fa.moderate_academic(skor_FA), fk.moderate_lethargy(skor_FK))
    if alpha22 != 0:
        pre_alpha.append(alpha22)
        z22 = zr.z_moderate(alpha22)
        z_rule.append(z22)
        az22 = round((alpha22 * z22), 3)
        alpha_z.append(az22)
    
    #RULE 23: MODERATE - MODERATE - HIGH =  MODERATE
    alpha23 = min(fm.moderate_motivation(skor_FM), fa.moderate_academic(skor_FA), fk.high_lethargy(skor_FK))
    if alpha23 != 0:
        pre_alpha.append(alpha23)
        z23 = zr.z_moderate(alpha23)
        z_rule.append(z23)
        az23 = round((alpha23 * z23), 3)
        alpha_z.append(az23)
    
    #RULE 24: MODERATE - MODERATE - VERY HIGH = MODERATE 
    alpha24 = min(fm.moderate_motivation(skor_FM), fa.moderate_academic(skor_FA), fk.very_high_lethargy(skor_FK))
    if alpha24 != 0:
        pre_alpha.append(alpha24)
        z24 = zr.z_moderate(alpha24)
        z_rule.append(z24)
        az24 = round((alpha24 * z24), 3)
        alpha_z.append(az24)
    
    #RULE 25: MODERATE - HIGH - LOW =  LOW
    alpha25 = min(fm.moderate_motivation(skor_FM), fa.high_academic(skor_FA), fk.low_lethargy(skor_FK))
    if alpha25 != 0:
        pre_alpha.append(alpha25)
        z25 = zr.z_low(alpha25)
        z_rule.append(z25)
        az25 = round((alpha25 * z25), 3)
        alpha_z.append(az25)
    
    #RULE 26: MODERATE - HIGH - MODERATE = MODERATE
    alpha26 = min(fm.moderate_motivation(skor_FM), fa.high_academic(skor_FA), fk.moderate_lethargy(skor_FK))
    if alpha26 != 0:
        pre_alpha.append(alpha26)
        z26 = zr.z_moderate(alpha26)
        z_rule.append(z26)
        az26 = round((alpha26 * z26), 3)
        alpha_z.append(az26)
    
    #RULE 27: MODERATE - HIGH - HIGH = MODERATE
    alpha27 = min(fm.moderate_motivation(skor_FM), fa.high_academic(skor_FA), fk.high_lethargy(skor_FK))
    if alpha27 != 0:
        pre_alpha.append(alpha27)
        z27 = zr.z_moderate(alpha27)
        z_rule.append(z27)
        az27 = round((alpha27 * z27), 3)
        alpha_z.append(az27)
    
    #RULE 28: MODERATE - HIGH - VERY HIGH = MODERATE
    alpha28 = min(fm.moderate_motivation(skor_FM), fa.high_academic(skor_FA), fk.very_high_lethargy(skor_FK))
    if alpha28 != 0:
        pre_alpha.append(alpha28)
        z28 = zr.z_moderate(alpha28)
        z_rule.append(z28)
        az28 = round((alpha28 * z28), 3)
        alpha_z.append(az28)
        
    #RULE 29: MODERATE - VERY HIGH - LOW = LOW
    alpha29 = min(fm.moderate_motivation(skor_FM), fa.very_high_academic(skor_FA), fk.low_lethargy(skor_FK))
    if alpha29 != 0:
        pre_alpha.append(alpha29)
        z29 = zr.z_low(alpha29)
        z_rule.append(z29)
        az29 = round((alpha29 * z29), 3)
        alpha_z.append(az29)
    
    #RULE 30: MODERATE - VERY HIGH - MODERATE =  MODERATE
    alpha30 = min(fm.moderate_motivation(skor_FM), fa.very_high_academic(skor_FA), fk.moderate_lethargy(skor_FK))
    if alpha30 != 0:
        pre_alpha.append(alpha30)
        z30 = zr.z_moderate(alpha30)
        z_rule.append(z30)
        az30 = round((alpha30 * z30), 3)
        alpha_z.append(az30)
    
    #RULE 31: MODERATE - VERY HIGH - HIGH = MODERATE
    alpha31 = min(fm.moderate_motivation(skor_FM), fa.very_high_academic(skor_FA), fk.high_lethargy(skor_FK))
    if alpha31 != 0:
        pre_alpha.append(alpha31)
        z31 = zr.z_moderate(alpha31)
        z_rule.append(z31)
        az31 = round((alpha31 * z31), 3)
        alpha_z.append(az31)
    
    #RULE 32: MODERATE - VERY HIGH - VERY HIGH =  MODERATE
    alpha32 = min(fm.moderate_motivation(skor_FM), fa.very_high_academic(skor_FA), fk.very_high_lethargy(skor_FK))
    if alpha32 != 0:
        pre_alpha.append(alpha32)
        z32 = zr.z_moderate(alpha32)
        z_rule.append(z32)
        az32 = round((alpha32 * z32), 3)
        alpha_z.append(az32)
    
    #RULE 33: HIGH - LOW - LOW = MODERATE
    alpha33 = min(fm.high_motivation(skor_FM), fa.low_academic(skor_FA), fk.low_lethargy(skor_FK))
    if alpha33 != 0:
        pre_alpha.append(alpha33)
        z33 = zr.z_moderate(alpha33)
        z_rule.append(z33)
        az33 = round((alpha33 * z33), 3)
        alpha_z.append(az33)
    
    #RULE 34: HIGH - LOW - MODERATE = MODERATE
    alpha34 = min(fm.high_motivation(skor_FM), fa.low_academic(skor_FA), fk.moderate_lethargy(skor_FK))
    if alpha34 != 0:
        pre_alpha.append(alpha34)
        z34 = zr.z_moderate(alpha34)
        z_rule.append(z34)
        az34 = round((alpha34 * z34), 3)
        alpha_z.append(az34)
    
    #RULE 35: HIGH - LOW - HIGH = MODERATE
    alpha35 = min(fm.high_motivation(skor_FM), fa.low_academic(skor_FA), fk.high_lethargy(skor_FK))
    if alpha35 != 0:
        pre_alpha.append(alpha35)
        z35 = zr.z_moderate(alpha35)
        z_rule.append(z35)
        az35 = round((alpha35 * z35), 3)
        alpha_z.append(az35)
    
    #RULE 36: HIGH - LOW - VERY HIGH = HIGH  
    alpha36 = min(fm.high_motivation(skor_FM), fa.low_academic(skor_FA), fk.very_high_lethargy(skor_FK))
    if alpha36 != 0:
        pre_alpha.append(alpha36)
        z36 = zr.z_high(alpha36)
        z_rule.append(z36)
        az36 = round((alpha36 * z36), 3)
        alpha_z.append(az36)
        
    #RULE 37: HIGH - MODERATE - LOW = MODERATE
    alpha37 = min(fm.high_motivation(skor_FM), fa.moderate_academic(skor_FA), fk.low_lethargy(skor_FK))
    if alpha37 != 0:
        pre_alpha.append(alpha37)
        z37 = zr.z_moderate(alpha37)
        z_rule.append(z37)
        az37 = round((alpha37 * z37), 3)
        alpha_z.append(az37)
    
    #RULE 38: HIGH - MODERATE - MODERATE = MODERATE
    alpha38 = min(fm.high_motivation(skor_FM), fa.moderate_academic(skor_FA), fk.moderate_lethargy(skor_FK))
    if alpha38 != 0:
        pre_alpha.append(alpha38)
        z38 = zr.z_moderate(alpha38)
        z_rule.append(z38)
        az38 = round((alpha38 * z38), 3)
        alpha_z.append(az38)
    
    #RULE 39: HIGH - MODERATE - HIGH = MODERATE
    alpha39 = min(fm.high_motivation(skor_FM), fa.moderate_academic(skor_FA), fk.high_lethargy(skor_FK))
    if alpha39 != 0:
        pre_alpha.append(alpha39)
        z39 = zr.z_moderate(alpha39)
        z_rule.append(z39)
        az39 = round((alpha39 * z39), 3)
        alpha_z.append(az39)
    
    #RULE 40: HIGH - MODERATE - SEVERE = HIGH
    alpha40 = min(fm.high_motivation(skor_FM), fa.moderate_academic(skor_FA), fk.very_high_lethargy(skor_FK))
    if alpha40 != 0:
        pre_alpha.append(alpha40)
        z40 = zr.z_high(alpha40)
        z_rule.append(z40)
        az40 = round((alpha40 * z40), 3)
        alpha_z.append(az40)
        
    #RULE 41: HIGH - HIGH - LOW = MODERATE
    alpha41 = min(fm.high_motivation(skor_FM), fa.high_academic(skor_FA), fk.low_lethargy(skor_FK))
    if alpha41 != 0:
        pre_alpha.append(alpha41)
        z41 = zr.z_moderate(alpha41)
        z_rule.append(z41)
        az41 = round((alpha41 * z41), 3)
        alpha_z.append(az41)
    
    #RULE 42: HIGH - HIGH - MODERATE = MODERATE
    alpha42 = min(fm.high_motivation(skor_FM), fa.high_academic(skor_FA), fk.moderate_lethargy(skor_FK))
    if alpha42 != 0:
        pre_alpha.append(alpha42)
        z42 = zr.z_moderate(alpha42)
        z_rule.append(z42)
        az42 = round((alpha42 * z42), 3)
        alpha_z.append(az42)
    
    #RULE 43: HIGH - HIGH - HIGH = HIGH
    alpha43 = min(fm.high_motivation(skor_FM), fa.high_academic(skor_FA), fk.high_lethargy(skor_FK))
    if alpha43 != 0:
        pre_alpha.append(alpha43)
        z43 = zr.z_high(alpha43)
        z_rule.append(z43)
        az43 = round((alpha43 * z43), 3)
        alpha_z.append(az43)
    
    #RULE 44: HIGH - HIGH - SEVERE = HIGH
    alpha44 = min(fm.high_motivation(skor_FM), fa.high_academic(skor_FA), fk.very_high_lethargy(skor_FK))
    if alpha44 != 0:
        pre_alpha.append(alpha44)
        z44 = zr.z_high(alpha44)
        z_rule.append(z44)
        az44 = round((alpha44 * z44), 3)
        alpha_z.append(az44)
    
    #RULE 45: HIGH - VERY HIGH - LOW = MODERATE
    alpha45 = min(fm.high_motivation(skor_FM), fa.very_high_academic(skor_FA), fk.low_lethargy(skor_FK))
    if alpha45 != 0:
        pre_alpha.append(alpha45)
        z45 = zr.z_moderate(alpha45)
        z_rule.append(z45)
        az45 = round((alpha45 * z45), 3)
        alpha_z.append(az45)
    
    #RULE 46: HIGH - VERY HIGH - MODERATE = MODERATE
    alpha46 = min(fm.high_motivation(skor_FM), fa.very_high_academic(skor_FA), fk.moderate_lethargy(skor_FK))
    if alpha46 != 0:
        pre_alpha.append(alpha46)
        z46 = zr.z_moderate(alpha46)
        z_rule.append(z46)
        az46 = round((alpha46 * z46), 3)
        alpha_z.append(az46)
    
    #RULE 47: HIGH - VERY HIGH - HIGH = HIGH  
    alpha47 = min(fm.high_motivation(skor_FM), fa.very_high_academic(skor_FA), fk.high_lethargy(skor_FK))
    if alpha47 != 0:
        pre_alpha.append(alpha47)
        z47 = zr.z_high(alpha47)
        z_rule.append(z47)
        az47 = round((alpha47 * z47), 3)
        alpha_z.append(az47)
    
    #RULE 48: HIGH - VERY HIGH - VERY HIGH = HIGH
    alpha48 = min(fm.high_motivation(skor_FM), fa.very_high_academic(skor_FA), fk.very_high_lethargy(skor_FK))
    if alpha48 != 0:
        pre_alpha.append(alpha48)
        z48 = zr.z_high(alpha48)
        z_rule.append(z48)
        az48 = round((alpha48 * z48), 3)
        alpha_z.append(az48)
    
    #RULE 49: VERY HIGH - LOW - LOW = MODERATE
    alpha49 = min(fm.very_high_motivation(skor_FM), fa.low_academic(skor_FA), fk.low_lethargy(skor_FK))
    if alpha49 != 0:
        pre_alpha.append(alpha49)
        z49 = zr.z_moderate(alpha49)
        z_rule.append(z49)
        az49 = round((alpha49 * z49), 3)
        alpha_z.append(az49)
        
    #RULE 50: VERY HIGH - LOW - MODERATE = MODERATE 
    alpha50 = min(fm.very_high_motivation(skor_FM), fa.low_academic(skor_FA), fk.moderate_lethargy(skor_FK))
    if alpha50 != 0:
        pre_alpha.append(alpha50)
        z50 = zr.z_moderate(alpha50)
        z_rule.append(z50)
        az50 = round((alpha50 * z50), 3)
        alpha_z.append(az50)
    
    #RULE 51:  VERY HIGH - LOW - HIGH = MODERATE
    alpha51 = min(fm.very_high_motivation(skor_FM), fa.low_academic(skor_FA), fk.high_lethargy(skor_FK))
    if alpha51 != 0:
        pre_alpha.append(alpha51)
        z51 = zr.z_moderate(alpha51)
        z_rule.append(z51)
        az51 = round((alpha51 * z51), 3)
        alpha_z.append(az51)
    
    #RULE 52: VERY HIGH - LOW - VERY HIGH = VERY HIGH  
    alpha52 = min(fm.very_high_motivation(skor_FM), fa.low_academic(skor_FA), fk.very_high_lethargy(skor_FK))
    if alpha52 != 0:
        pre_alpha.append(alpha52)
        z52 = zr.z_very_high(alpha52)
        z_rule.append(z52)
        az52 = round((alpha52 * z52), 3)
        alpha_z.append(az52)
    
    #RULE 53: VERY HIGH - MODERATE - LOW = MODERATE
    alpha53 = min(fm.very_high_motivation(skor_FM), fa.moderate_academic(skor_FA), fk.low_lethargy(skor_FK))
    if alpha53 != 0:
        pre_alpha.append(alpha53)
        z53 = zr.z_moderate(alpha53)
        z_rule.append(z53)
        az53 = round((alpha53 * z53), 3)
        alpha_z.append(az53)
    
    #RULE 54: VERY HIGH - MODERATE - MODERATE = MODERATE
    alpha54 = min(fm.very_high_motivation(skor_FM), fa.moderate_academic(skor_FA), fk.moderate_lethargy(skor_FK))
    if alpha54 != 0:
        pre_alpha.append(alpha54)
        z54 = zr.z_moderate(alpha54)
        z_rule.append(z54)
        az54 = round((alpha54 * z54), 3)
        alpha_z.append(az54)
    
    #RULE 55: VERY HIGH - MODERATE - HIGH = HIGH
    alpha55 = min(fm.very_high_motivation(skor_FM), fa.moderate_academic(skor_FA), fk.high_lethargy(skor_FK))
    if alpha55 != 0:
        pre_alpha.append(alpha55)
        z55 = zr.z_high(alpha55)
        z_rule.append(z55)
        az55 = round((alpha55 * z55), 3)
        alpha_z.append(az55)
    
    #RULE 56: VERY HIGH - MODERATE - VERY HIGH = VERY HIGH
    alpha56 = min(fm.very_high_motivation(skor_FM), fa.moderate_academic(skor_FA), fk.very_high_lethargy(skor_FK))
    if alpha56 != 0:
        pre_alpha.append(alpha56)
        z56 = zr.z_very_high(alpha56)
        z_rule.append(z56)
        az56 = round((alpha56 * z56), 3)
        alpha_z.append(az56)
        
    #RULE 57: VERY HIGH - HIGH - LOW = MODERATE 
    alpha57 = min(fm.very_high_motivation(skor_FM), fa.high_academic(skor_FA), fk.low_lethargy(skor_FK))
    if alpha57 != 0:
        pre_alpha.append(alpha57)
        z57 = zr.z_moderate(alpha57)
        z_rule.append(z57)
        az57 = round((alpha57 * z57), 3)
        alpha_z.append(az57)
        
    #RULE 58: VERY HIGH - HIGH - MODERATE = MODERATE
    alpha58 = min(fm.very_high_motivation(skor_FM), fa.high_academic(skor_FA), fk.moderate_lethargy(skor_FK))
    if alpha58 != 0:
        pre_alpha.append(alpha58)
        z58 = zr.z_moderate(alpha58)
        z_rule.append(z58)
        az58 = round((alpha58 * z58), 3)
        alpha_z.append(az58)
    
    #RULE 59: VERY HIGH - HIGH - HIGH = VERY HIGH
    alpha59 = min(fm.very_high_motivation(skor_FM), fa.high_academic(skor_FA), fk.high_lethargy(skor_FK))
    if alpha59 != 0:
        pre_alpha.append(alpha59)
        z59 = zr.z_very_high(alpha59)
        z_rule.append(z59)
        az59 = round((alpha59 * z59), 3)
        alpha_z.append(az59)
    
    #RULE 60: VERY HIGH - HIGH - VERY HIGH = VERY HIGH
    alpha60 = min(fm.very_high_motivation(skor_FM), fa.high_academic(skor_FA), fk.very_high_lethargy(skor_FK))
    if alpha60 != 0:
        pre_alpha.append(alpha60)
        z60 = zr.z_very_high(alpha60)
        z_rule.append(z60)
        az60 = round((alpha60 * z60), 3)
        alpha_z.append(az60)
        
    #RULE 61: VERY HIGH - VERY HIGH - LOW = HIGH  
    alpha61 = min(fm.very_high_motivation(skor_FM), fa.very_high_academic(skor_FA), fk.low_lethargy(skor_FK))
    if alpha61 != 0:
        pre_alpha.append(alpha61)
        z61 = zr.z_high(alpha61)
        z_rule.append(z61)
        az61 = round((alpha61 * z61), 3)
        alpha_z.append(az61)
        
    #RULE 62:  VERY HIGH - VERY HIGH - MODERATE = HIGH
    alpha62 = min(fm.very_high_motivation(skor_FM), fa.very_high_academic(skor_FA), fk.moderate_lethargy(skor_FK))
    if alpha62 != 0:
        pre_alpha.append(alpha62)
        z62 = zr.z_high(alpha62)
        z_rule.append(z62)
        az62 = round((alpha62 * z62), 3)
        alpha_z.append(az62)
        
    #RULE 63: VERY HIGH - VERY HIGH - HIGH = VERY HIGH  
    alpha63 = min(fm.very_high_motivation(skor_FM), fa.very_high_academic(skor_FA), fk.high_lethargy(skor_FK))
    if alpha63 != 0:
        pre_alpha.append(alpha63)
        z63 = zr.z_very_high(alpha63)
        z_rule.append(z63)
        az63 = round((alpha63 * z63), 3)
        alpha_z.append(az63)
        
    #RULE 64: VERY HIGH - VERY HIGH - VERY HIGH = VERY HIGH  
    alpha64 = min(fm.very_high_motivation(skor_FM), fa.very_high_academic(skor_FA), fk.very_high_lethargy(skor_FK))
    if alpha64 != 0:
        pre_alpha.append(alpha64)
        z64 = zr.z_very_high(alpha64)
        z_rule.append(z64)
        az64 = round((alpha64 * z64), 3)
        alpha_z.append(az64)
    
    alpha_sum = round(sum(pre_alpha), 3)
    #print ("Alpha Pre      : ", pre_alpha)
    #print ("Total Alpha    : ", alpha_sum)
    #print ("Nilai Z        : ", z_rule)
    
    alphaZ_sum = round(sum(alpha_z), 3)
    #print ("Z x Alpha      : ", alpha_z)
    #print ("Total Alpha x Z: ", alphaZ_sum)

    try:
        z_total = round((alphaZ_sum/alpha_sum), 3)
        return z_total
        #print ("Nilai Skor: ", z_total)
    except:
        z_total = 0
        #print ("Nilai Skor: ", 0)
    
    
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

 
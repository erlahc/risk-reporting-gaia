#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 16:55:22 2019

@author: charles
"""

import pandas as pd
import numpy as np
from itertools import product,repeat
    
def generate_granting(countries,segments,dates,granting_fields,nb_segments=5):
    prod_mt_i=1000000
    demand_i=1000
    
    fpd_mt_i=0.008
    active={'3M':0.98,'6M':0.93,'12M':0.85}
    risk={'3M':0.01,'6M':0.03,'12M':0.09}
    
    accepte_i=0.9
    refuse_i=0.1
    system={'OK_SYS':0.8,'ETUD_SYS':0.13,'REF_SYS':0.07}
    
    
    segment_tuples=list(product(countries,segments))
    a=[]
    
    for i in range(nb_segments):
        segment_tuple=segment_tuples.pop(int(np.random.randint(0,len(segment_tuples),1)))
        
        segment_tuple=list(repeat(segment_tuple,len(dates)))
        country=list(list(list(zip(*segment_tuple)))[0])
        segment=list(list(list(zip(*segment_tuple)))[1])
        
        prod_mt=(np.random.rand(len(dates))+1)*5*prod_mt_i
        fpd_mt=prod_mt*fpd_mt_i
        
        risk3_mt=prod_mt*risk['3M']
        risk6_mt=prod_mt*risk['6M']
        risk12_mt=prod_mt*risk['12M']
        
        active3_mt=prod_mt*active['3M']
        active6_mt=prod_mt*active['6M']
        active12_mt=prod_mt*active['12M']
        
        demand=(np.random.rand(len(dates))+1)*5*demand_i
        accepte=demand*accepte_i
        refuse=demand*refuse_i
        
        ok_sys=demand*system['OK_SYS']
        etud_sys=demand*system['ETUD_SYS']
        ref_sys=demand*system['REF_SYS']
        
        for i in list(zip(country,dates,segment,prod_mt,fpd_mt,
                             risk3_mt,risk6_mt,risk12_mt,
                             active3_mt,active6_mt,active12_mt,
                             demand,accepte,refuse,ok_sys,etud_sys,ref_sys)):
            a.append(i)
        
    return pd.DataFrame(a,columns=granting_fields)

def generate_stock(countries,segments,dates,stock_fields,nb_segments=5):
    encours_i=1000
    
    #stratas={'R0':0.9,'R1':0.05,'R2':0.03,'R3':0.008,'R4':0.007,'R5':0.003,'R6':0.001,'R7':0.001,'CTX':0.05,'INS':0.05}
    stratas_i=np.array([0.9,0.05,0.03,0.008,0.007,0.003,0.001,0.001,0.05,0.05])
    #transfert={'R0':0.001,'R1':0.002,'R2':0.002,'R3':0.005,'R4':0.02,'R5':0.0,'R6':0.0,'R7':0.0,'CTX':0.0}
    transfert_i=np.array([0.001,0.002,0.002,0.005,0.02,0.0,0.0,0.0,0.0])
    unpaid_i=0.01
    
    segment_tuples=list(product(countries,segments))
    df_stock=pd.DataFrame(columns=stock_fields)
    for i in range(nb_segments):
        segment_tuple=segment_tuples.pop(int(np.random.randint(0,len(segment_tuples),1)))
        
        segment_tuple=list(repeat(segment_tuple,len(dates)))
        country=list(list(list(zip(*segment_tuple)))[0])
        segment=list(list(list(zip(*segment_tuple)))[1])
        
        encours=(np.random.rand(len(dates))+1)*5*encours_i
        
        stratas=stratas_i*encours.reshape(len(encours),1)
        transfert=transfert_i*encours.reshape(len(encours),1)
        unpaid=encours*unpaid_i
 
        temp=list(zip(country,segment,dates))
        df1=pd.concat([pd.DataFrame(temp),pd.DataFrame(stratas).round(4),
                  pd.DataFrame(transfert).round(4),pd.DataFrame(unpaid).round(4)],axis=1)
        df1.columns=stock_fields
        df_stock=pd.concat([df_stock,df1]) 
        
    return df_stock
    
if __name__=='__main__':
    countries=['PITA','PPLK','PPOR','PDEU']
    segments=['Auto','Retail','Direct','Cards']
    dates=['201801','201802','201803','201804','201805','201806','201807','201808',
           '201809','201810','201811','201812','201901','201902','201903','201904']
    
    granting_fields=['COUNTRY','DATE','SEGMENT','Production','FPD',
                             'Risk3M','Risk6M','Risk12M',
                             'Active3M','Active6M','Active12M',
                             'DEMAND','ACCEPTE','REFUSE','OK_SYS','ETUD_SYS','REF_SYS']
    
    stock_fields=['COUNTRY','DATE','SEGMENT',
                  'v_OST_R0','v_OST_R1','v_OST_R2','v_OST_R3','v_OST_R4','v_OST_R5','v_OST_R6','v_OST_R7',
                  'v_OST_CTX','v_OST_INS',
                  'TS0','TS1','TS2','TS3','TS4','TS5','TS6','TS7','TSCTX',
                  '1UNPAID']
    
    df_granting=generate_granting(countries,segments,dates,granting_fields,5)
    df_stock=generate_stock(countries,segments,dates,stock_fields,5)
    df_stock.to_csv('stock_gen.csv',decimal=',',sep=';',index=False)
    df_granting.to_csv('granting_gen.csv',decimal=',',sep=';',index=False)
    
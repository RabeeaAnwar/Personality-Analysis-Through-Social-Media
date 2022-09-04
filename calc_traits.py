# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 12:14:57 2019

@author: MY
"""

#%%
import pandas as pd
import json
import os

#%%
with open('q_division.json','r') as f:
    q_division=json.load(f)



#%%

all_files=os.listdir("u_a_json/")

#%%
#with open('u_a_json/1997_012113.txt.json','r') as f:
#    a=json.load(f)

#%%

traits_mapping={'1':'Extraversion','2':'Agreeableness','3':'Conscientiousness','4':'Neuroticism','5':'Openness'}
neg_ansr_mapping={1:5,2:4,3:3,4:2,5:1}

#%%
for i in all_files:
    traits={'Extraversion':0,'Agreeableness':0,'Conscientiousness':0,'Neuroticism':0,'Openness':0}
    with open(f'u_a_json/{i}','r') as f:
        user_ansrs=json.load(f)
    
    #work for +ve traits
    for j in q_division['+']:
        traits[ traits_mapping[ j[0] ] ] += user_ansrs[j]
    
    #work for +ve traits    
    for j in q_division['-']:
        traits[ traits_mapping[ j[0] ] ] += neg_ansr_mapping[ user_ansrs[j] ]
    
    print(traits)
    
    with open(f'users_classification/{i}','w') as f:
        json.dump(traits,f)
#    break


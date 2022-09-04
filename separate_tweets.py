# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 14:01:24 2019

@author: MY
"""

#%%
import pandas as pd

#%%
data=pd.read_csv('essays.csv',encoding='latin1')

#%%
writer=pd.ExcelWriter('separate_tweets.xlsx',engine='xlsxwriter')

#%%
j=1
for i in range(0,data.shape[0],25):
    df=data.iloc[i:i+25,:]
    df.to_excel(writer,sheet_name=f'sheet{j}',index=False)
    j+=1

#%%
writer.save()












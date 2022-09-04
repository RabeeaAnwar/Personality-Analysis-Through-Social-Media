
# coding: utf-8

# In[12]:


import os,json
import pandas as pd


# In[49]:


essays=pd.read_csv('essays.csv',encoding='latin1')


# In[90]:


essays.head()


# In[83]:


all_files=os.listdir("users_classification/")


# In[87]:


essays['Extraversion']=0
essays['Agreeableness']=0
essays['Conscientiousness']=0
essays['Neuroticism']=0
essays['Openness']=0


# In[89]:


for i in all_files:
    data=0
    
    with open(f'users_classification/{i}','r') as f:
        data=json.load(f)
        #convert values to %
        data={ t: ( ( data[t] / 50 ) * 100 ) for t in data }
    
    essays[essays['#AUTHID']==i.strip('.json')] = essays[essays['#AUTHID']==i.strip('.json')].assign(**data)


# In[92]:


essays.to_csv('traits_essays.csv',index=False)


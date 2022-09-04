
# coding: utf-8

# In[167]:


import pandas as pd
import numpy as np


# In[168]:


import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[173]:


traits_words_samples=pd.read_excel('traits_words_samples.xlsx')


# In[174]:


traits_words_samples_vertical=pd.read_excel('traits_words_samples_vertical.xlsx')


# In[175]:


traits_words_samples.head()


# In[176]:


traits_words_samples_vertical.head()


# In[177]:


word_samples=traits_words_samples
sent_samples=traits_words_samples_vertical


# In[178]:


word_samples.head()


# In[179]:


sent_samples.head()


# In[180]:


O_H=word_samples.iloc[0,1]
O_H


# In[181]:


O_L=word_samples.iloc[1,1]
O_L


# In[182]:


C_H=word_samples.iloc[2,1]
C_H


# In[183]:


C_L=word_samples.iloc[3,1]
C_L


# In[184]:


E_H=word_samples.iloc[4,1]
E_H


# In[185]:


E_L=word_samples.iloc[5,1]
E_L


# In[186]:


A_H=word_samples.iloc[6,1]
A_H


# In[187]:


A_L=word_samples.iloc[7,1]
A_L


# In[188]:


N_H=word_samples.iloc[8,1]
N_H


# In[189]:


N_L=word_samples.iloc[9,1]
N_L


# In[190]:


end_first=100
start_second=101


# In[191]:


sent_samples['open'][:end_first]


# In[192]:


sent_samples['open'][start_second:]


# In[193]:


from functools import reduce


# In[194]:


O_H=list(map(lambda x:x.strip(),O_H.split(',')))+(reduce(lambda x,y:str(x).strip()+','+str(y).strip(),sent_samples['open'][:end_first]).split(','))
O_H


# In[195]:


O_L=list(map(lambda x:x.strip(),O_L.split(',')))+(reduce(lambda x,y:str(x).strip()+','+str(y).strip(),sent_samples['open'][start_second:]).split(','))
O_L


# In[196]:


C_H=list(map(lambda x:x.strip(),C_H.split(',')))+(reduce(lambda x,y:str(x).strip()+','+str(y).strip(),sent_samples['cons'][:end_first]).split(','))
C_H


# In[197]:


C_L=list(map(lambda x:x.strip(),C_L.split(',')))+(reduce(lambda x,y:str(x).strip()+','+str(y).strip(),sent_samples['cons'][start_second:]).split(','))
C_L


# In[198]:


E_H=list(map(lambda x:x.strip(),E_H.split(',')))+(reduce(lambda x,y:str(x).strip()+','+str(y).strip(),sent_samples['ext'][:end_first]).split(','))
E_H


# In[199]:


E_L=list(map(lambda x:x.strip(),E_L.split(',')))+(reduce(lambda x,y:str(x).strip()+','+str(y).strip(),sent_samples['ext'][start_second:]).split(','))
E_L


# In[200]:


A_H=list(map(lambda x:x.strip(),A_H.split(',')))+(reduce(lambda x,y:str(x).strip()+','+str(y).strip(),sent_samples['agr'][:end_first]).split(','))
A_H


# In[201]:


A_L=list(map(lambda x:x.strip(),A_L.split(',')))+(reduce(lambda x,y:str(x).strip()+','+str(y).strip(),sent_samples['agr'][start_second:]).split(','))
A_L


# In[202]:


N_H=list(map(lambda x:x.strip(),N_H.split(',')))+(reduce(lambda x,y:str(x).strip()+','+str(y).strip(),sent_samples['neu'][:end_first]).split(','))
N_H


# In[203]:


N_L=list(map(lambda x:x.strip(),N_L.split(',')))+(reduce(lambda x,y:str(x).strip()+','+str(y).strip(),sent_samples['neu'][start_second:]).split(','))
N_L


# In[204]:


import json


# In[205]:


word_data=json.dumps({'O_H':O_H,'O_L':O_L,'C_H':C_H,'C_L':C_L,'E_H':E_H,'E_L':E_L,'A_H':A_H,'A_L':A_L,'N_H':N_H,'N_L':N_L})


# In[206]:


with open('word_data.json','w') as f:
    f.write(word_data)


# In[207]:


##start it from joining column value as one


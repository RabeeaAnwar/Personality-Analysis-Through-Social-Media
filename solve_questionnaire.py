
# coding: utf-8

# In[41]:


import pandas as pd
import numpy as np


# In[42]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[43]:


import json
from pprint import pprint


# In[44]:

#counting word function
import re
count_words=lambda x:len(re.findall(r'\w+',x))


# In[45]:


word_data=None
with open('word_data.json','r') as f:
    word_data=json.load(f)

# print(word_data)


# In[46]:


df=pd.read_csv('essays.csv',encoding='latin1')


# In[47]:


df.head()


# In[48]:


df.shape


# In[49]:


df_data=df


# In[50]:


# in our problem we may need stopwords to so dont remove them


# In[51]:


from textblob import TextBlob


# In[52]:


blob=TextBlob(df_data['TEXT'][0])


# In[53]:


for sen in blob.sentences:
    print(len(blob.sentences))
    print(len(str(sen)))
    print(sen)
    print(count_words(str(sen)))
    print(sen.sentiment.polarity)
    break


# In[54]:


# blob.sentences.polarity


# In[55]:


blob = TextBlob('I am f9')
blob.correct()


# In[56]:


from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# In[57]:


vsa=SentimentIntensityAnalyzer()


# In[58]:


for sen in df_data['TEXT'][0].split('.'):
    print(str(sen))
    print(vsa.polarity_scores(sen))
    break


# In[59]:


questions=[]
with open('questions.txt','r') as f:
    questions=[line.rstrip('\n') for line in f]
print(questions)


# In[60]:


import os
all_files=os.listdir("q_c/")
all_files.sort(key=lambda x:( int(x[0:1]) , int(x[2:-4]) ) )
print(all_files)


# In[61]:


' df d  '.strip()


# In[62]:


open(f"q_c/3-6.txt",'r').read()


# In[63]:


open(f"aw.txt",'w').write('1,2,4')


# In[64]:

from pdb import set_trace
from math import isnan


# In[65]:


def sentiment_range(value):
    if -1 <= value <= -0.01:
        return value
    elif -0.01 < value < 0.01:
        return 0
    elif 0.01 <= value <= 1:
        return value


# In[66]:


def prob_range(s_a,w_p):
    if s_a < 0:
        if -1 <= s_a*w_p < -0.5:
            return 1
        elif -0.5 <= s_a*w_p <= 0:
            return 2
        
    elif s_a == 0:
        return 3
    
    elif s_a > 0:
        if 0 <= s_a*w_p <= 0.5:
            return 4
        elif 0.5 < s_a*w_p <= 1:
            return 5
        
#     if isnan(w_p) :
    print(f'falto{w_p}')
    return f'falto{w_p}'


# In[72]:


def solve_questions(data):
    users_ansr={}
    print(data)
#    set_trace()
    for i in all_files:
        word_probs=[];sent_probs=[]
        for tweet in TextBlob(data['TEXT']).sentences:
            count=0
#            set_trace()
            for j in open(f"q_c/{i}",'r').read().split(','):
                if j.strip().casefold() in str(tweet).casefold():
                    count+=1
                
#            set_trace()
            word_probs.append( 0 if (count == 0 or count_words(str(tweet)) == 0) else count/count_words(str(tweet)) )
#             word_probs.append( count/count_words(str(tweet)) )
#             print(f't{tweet.sentiment.polarity}')
            sent_probs.append(tweet.sentiment.polarity)
        
#        set_trace()
        sentiment_ansr=sentiment_range(np.mean(sent_probs))
#         if isnan( np.mean(word_probs) / max(word_probs) ):
#             set_trace()

        # divided by max becasue converting it into 0-1 range,
#        set_trace()
        ansr=prob_range( sentiment_ansr , 0 if np.mean(word_probs) == 0 else np.mean(word_probs) / max(word_probs) )
#        users_ansr+=str(ansr)+','
        users_ansr[i]=ansr
        
        
#    open(f"u_a_json/{data['#AUTHID']}",'w').write(users_ansr.strip(','))
    with open(f"u_a_json/{data['#AUTHID']}.json",'w') as f:
        json.dump(users_ansr,f)
#        open(f"u_a_json/{data['#AUTHID']}.json",'w').write(str(users_ansr))
        print('write')
#    set_trace()
        
     
    


# In[73]:


df_data.apply(solve_questions,axis=1)


# In[ ]:


#why give same answer for all questions for one user...

# In[ ]:

print(25454)

# In[]:


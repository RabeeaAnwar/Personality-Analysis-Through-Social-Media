
# coding: utf-8

# In[60]:


import tweepy as tp
import re
from nltk.sentiment.vader import SentimentIntensityAnalyzer


# In[3]:


consumer_key='XTE6RfJK5m1LzD5i5N4Tjoxcu'
consumer_secret='HF0ZpBLxFesoLhlwDPja8COxJS3r4QdZuegkYwnjxCsCrsiu0W'
access_token='751370996964323329-LfGMEaDxZaTB59432PgdAWxNmXpymDJ'
access_token_secret='RntwtUqZZ8XQVNUYXoWqpRVV1mYuO8xzXheUnpEhyqeoQ'

auth=tp.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)


# In[4]:


api=tp.API(auth)


# In[21]:


# for t in api.home_timeline():
#     print(t)


# In[22]:


user=api.get_user('56')


# In[23]:


print(user.screen_name)


# In[24]:


print(user.name)

#%%
for i in range(50000,50005):
    user=api.get_user(i)
    print(user.name)


# In[25]:


print(user.statuses_count)


# In[26]:


#print(user.status._json)


# In[27]:


# user._json

#%%
from pprint import pprint
# In[28]:


#all_tweets=api.user_timeline('7f3bfec0b7228d0900b01fbc8ce9d59f',page=20)
 all_tweets=tp.Cursor(api.user_timeline,id='1165').items()
# len(all_tweets)
print(list(all_tweets))

# In[14]:


users_list=['thebethanyjane','sophiethesmurfy','ZuberiSpeaks','ThestoryofJS','mahatweetz','ZaraLouU','notesfromarshi','ThisIsKristin_','MichaelDewey99','joansenio1','holtbt']


# In[7]:


len(users_list)


# In[59]:


sid = SentimentIntensityAnalyzer()


# In[36]:


#remove hashtags,#remove retweet word,remoe user name which appears after @
for user in users_list:
    with open(f'{user}.txt','wb') as f:
        for status in tp.Cursor(api.user_timeline,id=user).items(limit=50):
            temp=status._json['text']
            print(temp)
            f.write(temp)
        break


# In[43]:


a='RT @holtbt: “Fullstack” developer. https://t.co/yfymQmJJgq'
re.sub(r'^RT[\s]+','',a)


# In[57]:


a=re.sub(r'RT[\s]@[\w]+:[\s]+','',a)


# In[58]:


a


# In[46]:


sid.polarity_scores('I just completed the course "Natural Language Processing Fundamentals in Python"! https://t.co/audYm8Vhjf via @DataCamp')


# In[47]:


sid.polarity_scores('I just completed the course "Natural Language Processing Fundamentals in Python"!')


# In[55]:


'hello' in 'how are you mghellodkfd'.split()


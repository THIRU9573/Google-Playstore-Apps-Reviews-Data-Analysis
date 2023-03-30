#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[10]:


data = pd.read_csv("C:/Users/thiru/Downloads/playstoreliveproj Drive FIle/playstoreliveproj/playstore_reviews.csv",index_col = 'App')


# In[11]:


data


# In[12]:


data.drop_duplicates(keep = False, inplace = True)


# In[13]:


data.info()


# In[14]:


data.isna().sum()


# In[15]:


data


# In[16]:


data.dropna(subset = ['Translated_Review'], inplace = True)


# In[17]:


data['Sentiment'].unique()


# In[18]:


data = data[data['Sentiment'].notnull()]


# In[20]:


data['Sentiment'].unique()


# In[21]:


data['Sentiment_Polarity'].unique()


# In[22]:


data['Sentiment_Subjectivity'].unique()


# In[23]:


data.to_csv("C:/Users/thiru/Downloads/PlaystoreApp_Reviews_TotalCleaned_data.csv")


# In[ ]:





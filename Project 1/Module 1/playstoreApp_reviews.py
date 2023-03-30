#!/usr/bin/env python
# coding: utf-8

# # Import Libraries:

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# # Loading the Dataset:

# In[2]:


data = pd.read_csv("C:/Users/thiru/Downloads/playstoreliveproj Drive FIle/playstoreliveproj/playstore_reviews.csv",index_col = 'App')


# In[3]:


data


# In[4]:


data.shape


# In[5]:


data.isna().sum()


# In[6]:


data.dropna(subset = ['Translated_Review'], inplace = True)


# In[7]:


data.dropna(inplace = True)


# In[8]:


data.isna().sum()


# In[9]:


data


# In[10]:


#data.to_csv("C:/Users/thiru/Downloads/App_Reviews1.csv")


# In[11]:


#!csvsql --db mysql://root:THIru980@DESKTOP-SKKRIKM:3306/hicounselor --insert AppReviews1.csv


#!/usr/bin/env python
# coding: utf-8

# # Import Libraraies:

# In[30]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# # Loading the dataset:

# In[31]:


data = pd.read_csv("C:/Users/thiru/Downloads/playstoreliveproj Drive FIle/playstoreliveproj/playstore_apps.csv", index_col = "App")


# In[32]:


data


# # Drop Duplicate values:

# In[33]:


data.drop_duplicates(keep = False, inplace = True)


# In[34]:


data.info()


# In[35]:


data.isna().sum()


# # Delete Irrevelant data from columns:

# In[36]:


data  = data[data.Category != 'irrevelant_data']


# In[37]:


data  = data[data.Rating != 'irrevelant_data']


# In[38]:


data  = data[data.Reviews != 'irrevelant_data']


# In[39]:


data  = data[data.Size != 'irrevelant_data']


# In[40]:


data  = data[data.Installs != 'irrevelant_data']


# In[41]:


data  = data[data.Type != 'irrevelant_data']


# In[42]:


data  = data[data.Price != 'irrevelant_data']


# In[44]:


data  = data[data.Genres != 'irrevelant_data']


# In[ ]:


#data.dropna(inplace = True)


# In[49]:


#data


# In[50]:


data['Category'].unique()


# In[51]:


data['Rating'].unique()


# In[52]:


data['Size'].unique()


# In[53]:


data['Installs'].unique()


# In[54]:


data['Type'].unique()


# In[55]:


data['Price'].unique()


# In[56]:


data['Content Rating'].unique()


# In[57]:


data['Genres'].unique()


# In[58]:


data['Last Updated'].unique()


# In[59]:


data['Current Ver'].unique()


# In[60]:


data['Android Ver'].unique()


# # Export data into cleaned data:

# In[61]:


data.to_csv("C:/Users/thiru/Downloads/cleaned_data1.csv")


# In[62]:


dataset = pd.read_csv("C:/Users/thiru/Downloads/cleaned_data1.csv")


# In[63]:


dataset


# In[64]:


dataset.isna().sum()


# In[65]:


dataset.dropna(inplace = True)


# In[66]:


dataset.isna().sum()


# In[67]:


dataset.head()


# In[ ]:





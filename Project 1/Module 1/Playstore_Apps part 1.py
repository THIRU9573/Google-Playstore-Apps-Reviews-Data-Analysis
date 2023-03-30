#!/usr/bin/env python
# coding: utf-8

# # import libraries:

# In[94]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# # Loading the dataset:

# In[95]:


data = pd.read_csv("C:/Users/thiru/Downloads/playstoreliveproj Drive FIle/playstoreliveproj/playstore_apps.csv", index_col = "App")


# In[96]:


data = data.copy()


# In[97]:


data


# # Cleaning processing:

# # revome duplicate values:

# In[98]:


x = data.duplicated().sum()
print("the number of duplicatevalues in App datasetis {}".format(x))


# In[99]:


data.drop_duplicates(keep =False, inplace = True)


# In[100]:


y = data.duplicated().sum()
print("the number of duplicatevalues in App datasetis {}".format(y))


# In[101]:


data.info()


# In[102]:


data.isna().sum()


# In[ ]:





# # Delete the irrelevant data from dataset find unique values:

# In[103]:


data['Category'].unique()


# In[ ]:





# In[104]:


#data = data[data.Category != 'irrelevant_data']


# In[105]:


data = data[data['Category'] != '1.9']


# In[106]:


data['Category'].unique()


# In[107]:


data['Rating'].unique()


# In[108]:


data = data[data['Rating'] <=5].replace(np.NaN, 0)


# In[109]:


data['Reviews'].unique()


# In[110]:


data['Size'].unique()


# In[111]:


data = data[data['Size'] != 'Varies with device']


# In[112]:


data['Size'].unique()


# In[113]:


data['Installs'].unique()


# In[ ]:





# In[114]:


data['Type'].unique()


# In[115]:


data = data[data.Type != 'irrelevant_data']


# In[116]:


data = data[data['Price'] >= 0]


# In[117]:


data = data[data.Price != 'irrelevant_data']


# In[118]:


data['Price'].unique()


# In[119]:


data = data[data['Content Rating'] != 'irrelevant_data']


# In[120]:


data['Content Rating'].unique()


# In[121]:


data =data[data['Content Rating'] != 'Everyone 10+']


# In[122]:


data = data[data.Genres != 'irrelevant_data']


# In[123]:


data['Genres'].unique()


# In[124]:


data['Genres'] = data['Genres'].str.replace('Educational', 'Education')


# In[125]:


data['Genres'].unique()


# In[126]:


data = data[data['Last Updated'] != 'irrelevant_data']


# In[127]:


data['Last Updated'].unique()


# In[128]:


data = data[data['Current Ver'] != 'irrelevant_data']


# In[129]:


data['Current Ver'].unique()


# In[130]:


App_ver = data['Current Ver'].replace(np.NaN, '')


# In[132]:


data =data[~App_ver.str.contains(r'\s', r'^a-zA-Z', na = False)]


# In[134]:


data = data[data['Android Ver'] != 'irrelevant_data']


# In[135]:


data['Android Ver'].unique()


# In[136]:


data = data[(data['Android Ver'].notnull()) & (data['Android Ver'] != 'Varies with device')]


# In[137]:


data


# In[138]:


data.to_csv("C:/Users/thiru/Downloads/PlaystoreApp_TotalCleaned_data.csv")


# In[ ]:





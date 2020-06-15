#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Set the styles to Seaborn
sns.set()
# Import the KMeans module so we can perform k-means clustering with sklearn
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler


# In[12]:


data = pd.read_csv('E:/CLASSESS/BCAS/DATA SCIENCE/Jupyter tasks/annual.csv')
data


# In[13]:


x = data.iloc[:,[1,2]]


# In[14]:


x


# In[15]:


kmeans = KMeans(3)


# In[16]:


kmeans.fit(x)


# In[17]:


identified_clusters = kmeans.fit_predict(x)


# In[18]:


identified_clusters


# In[19]:


data_with_clusters = data.copy()
data_with_clusters['Cluster'] = identified_clusters
data_with_clusters


# In[21]:


plt.scatter(data_with_clusters['Year'],data_with_clusters['Mean'],c=data_with_clusters['Cluster'],cmap='rainbow')
plt.show()


# In[22]:


scaler = MinMaxScaler()
scaler.fit(data[['Mean']])
data['Mean'] = scaler.transform(data[['Mean']])

scaler.fit(data[['Year']])
data['Year'] = scaler.transform(data[['Year']])


# In[23]:


km = KMeans(n_clusters=3)
y_predicted = km.fit_predict(data[['Year','Mean']])
y_predicted


# In[24]:


data['cluster']=y_predicted
data


# In[25]:


km.cluster_centers_


# In[28]:


df1 = data[data.cluster==0]
df2 = data[data.cluster==1]
df3 = data[data.cluster==2]

plt.scatter(df1.Year,df1['Mean'],color='green')
plt.scatter(df2.Year,df2['Mean'],color='red')
plt.scatter(df3.Year,df3['Mean'],color='blue')
plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],color='black',marker='*',label='centroid')
plt.legend()


# In[ ]:





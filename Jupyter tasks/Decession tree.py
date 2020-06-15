#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn import tree
import pandas as pd
import pydotplus
from IPython.display import Image


# In[2]:


ground_df = pd.read_csv('E:/CLASSESS/BCAS/DATA SCIENCE/Jupyter tasks/anual_climate.csv')
ground_df


# In[3]:


dummies_data = ground_df.iloc[:, 0:4].values
dummies_data


# In[4]:


ground_data = ground_df[['Source','Year','Mean']]
ground_data


# In[5]:


one_hot_data = pd.get_dummies(ground_data)
one_hot_data


# In[6]:


clf = tree.DecisionTreeClassifier()
clf_train = clf.fit(one_hot_data, ground_df['Rating'])


# In[7]:


dot_data = tree.export_graphviz(clf_train, out_file=None, feature_names=list(one_hot_data.columns.values), 
                                class_names=['GOOD Climate', 'BAD climate'], rounded=True, filled=True)

graph = pydotplus.graph_from_dot_data(dot_data)
Image(graph.create_png())


# In[ ]:





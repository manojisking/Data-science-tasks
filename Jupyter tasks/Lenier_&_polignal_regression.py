#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split


# In[2]:


temperature = pd.read_csv('E:/CLASSESS/BCAS/DATA SCIENCE/Jupyter tasks/anual_climate.csv')
temperature


# In[4]:


X = temperature.iloc[:,1:2].values
y = temperature.iloc[:,2].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


# In[5]:


X_train, X_test, y_train, y_test


# In[6]:


from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)


# In[9]:


def show_linear():
    plt.scatter(X, y, color='red')
    plt.plot(X, lin_reg.predict(X), color='blue')
    plt.title('temperature increase gradually')
    plt.xlabel('year')
    plt.ylabel('mean temperature')
    plt.show()
    return
show_linear()  


# In[10]:


lin_reg.predict([[5.5]])


# In[12]:


from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=4)
X_poly = poly_reg.fit_transform(X)
pol_reg = LinearRegression()
pol_reg.fit(X_poly, y)


# In[13]:


def show_polymonial():
    plt.scatter(X, y, color='red')
    plt.plot(X, pol_reg.predict(poly_reg.fit_transform(X)), color='blue')
    plt.title('Truth or Bluff (Linear Regression)')
    plt.xlabel('Position level')
    plt.ylabel('Salary')
    plt.show()
    return

show_polymonial()


# In[14]:


pol_reg.predict(poly_reg.fit_transform([[2030]]))


# In[15]:


pol_reg.predict(poly_reg.fit_transform([[2050]]))


# In[ ]:





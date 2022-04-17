#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd
import datetime


# In[20]:


April_1222 = pd.read_csv('BTCUSDT-trades-2022-04-12.csv')#data for April 12 2022
April_1322 = pd.read_csv('BTCUSDT-trades-2022-04-13.csv')#data for April 13 2022
April_1422 = pd.read_csv('BTCUSDT-trades-2022-04-14.csv')#data for April 14 2022


# In[21]:


Trade_prices = pd.concat([April_1222.iloc[:,1],April_1322.iloc[:,1],April_1422.iloc[:,1]], axis = 0) #consolidating the trade prices of 3 days into 1 dataframe.


# In[22]:


Trade_prices = pd.DataFrame(Trade_prices, columns = ['Trade Price'])


# In[23]:


print (Trade_prices)


# In[24]:


Trade_prices.to_csv('FalconX Assignment 1.csv')


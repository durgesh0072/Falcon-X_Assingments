#!/usr/bin/env python
# coding: utf-8

# In[40]:


import pandas as pd
import datetime
import json
import requests
import numpy as np


# In[41]:


Trade_prices = pd.read_csv('FalconX Assignment 1.csv')


# # Fetching BTCUSDT live prices from source

# In[42]:


key = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"


# In[43]:


BTCUSDT_0 = requests.get(key) 


# In[44]:


BTCUSDT_0 = BTCUSDT_0.json()


# In[45]:


print(f"{BTCUSDT_0['symbol']} live price is {BTCUSDT_0['price']}")


# In[46]:


BTCUSDT = float(BTCUSDT_0['price'])


# # Steps for converting the offer size BTC equivalent amount according to live prices and also setting Hedge limit

# In[47]:


BID_ASK_size = 1000 #in USD (notional)


# In[48]:


BTC_Amount = (1/BTCUSDT)*BID_ASK_size


# In[49]:


print (BTC_Amount)


# In[50]:


Hedge_limit = 5000 #in USD (notional)


# # Declaring variables for Bid price and Ask price at each live BTCUSDT.

# In[51]:


Bid_price = BTCUSDT - 0.0003*BTCUSDT


# In[52]:


Ask_price = BTCUSDT + 0.0003*BTCUSDT


# In[53]:


B = Hedge_limit/(BTC_Amount*Bid_price)


# In[54]:


A = Hedge_limit/(BTC_Amount*Ask_price)


# In[55]:


#A and B are varibale that help in exiting trade at Hedge limit. This is used because a passive hedging approach was required.
print (Ask_price, Bid_price, A, B)


# # Conversion of Trade Orders dataframe to list for Convenience

# In[56]:


SVB = []


# In[57]:


SVA= []


# In[58]:


SVB_1 = []


# In[59]:


SVA_1 =[]


# In[ ]:


for i in TP:
    if ((i <= Bid_price) and (len(SVB_1) < round(B))):
        SVB.append(Bid_price*BTC_Amount)
        SVB_1.append(Bid_price*BTC_Amount)
    else:
        SVB.append(0)


# In[ ]:


for i in TP:
    if ((i >= Ask_price) and (len(SVA_1) < round(A))):
        SVA.append(Ask_price*BTC_Amount)
        SVA_1.append(Ask_price*BTC_Amount)
    else:
        SVA.append(0)
        


# # Conversion of created arrays to Dataframes

# In[ ]:


df = pd.DataFrame(SVB, columns = ['Buy value'])


# In[ ]:


df1 = pd.DataFrame(SVA, columns = ['Sale value'])


# In[ ]:


df2 = pd.DataFrame(SVB_1, columns = ['Executed Buys'])


# In[ ]:


df3 = pd.DataFrame(SVA_1, columns = ['Executed Sells'])


# In[ ]:


e = pd.DataFrame(TP, columns = ['Order Price'])


# # Compiling data into one Dataframe

# In[ ]:


Trades = pd.concat([e.iloc[:,0], df.iloc[:,0], df1.iloc[:,0], df2.iloc[:,0], df3.iloc[:,0]], axis = 1)


# In[ ]:


print (Trades)


# In[ ]:


Trades.to_csv('FalconX Assignment 2.csv')


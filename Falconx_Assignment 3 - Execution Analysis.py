#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import datetime
import numpy as np


# In[ ]:


Trades = pd.read_csv('FalconX Assignment 2.csv')


# # Processing for NaN values and Retriving PnL statements

# In[ ]:


bd = pd.DataFrame(Trades, columns = ['Executed Buys', 'Executed Sells'])


# In[ ]:


bd['Executed Sells'] = bd['Executed Sells'].fillna(0)


# In[ ]:


bd['Executed Buys'] = bd['Executed Buys'].fillna(0)


# In[ ]:


bd ['PnL'] = bd['Executed Sells'] - bd['Executed Buys']


# In[ ]:


print (bd)


# # Consider the sign of the variable to verify whether profit of Loss

# In[ ]:


Gross_PnL_USD = bd['PnL'].sum()


# In[ ]:


print ('The Gross Profit in the Trade is $', Gross_PnL_USD)


# # Consider the sign of the variable to verify whether profit of Loss

# In[ ]:


if bd['Executed Sells'].sum() == 0:
    Gross_PnL_bps = 0
else:
    Gross_PnL_bps = (Gross_PnL_USD/(bd['Executed Sells'].sum()))*10000
    print ('The Gross Profit in the Trade is', Gross_PnL_bps, 'basis points')


# # Since Maximum Drawdown relates to peak price and trough price of the asset, here the peak price is Peak/Trough (which is ask and bid prices) * BTC Amount price
# 

# In[ ]:


Traded_positions = pd.concat([Trades['Executed Buys'], Trades['Executed Sells']])


# In[ ]:


Traded_positions = Traded_positions.dropna()


# In[ ]:


print (Traded_positions)


# In[ ]:


Peak = max (Traded_positions)


# In[ ]:


Trough = min (Traded_positions)


# In[ ]:


Maximum_Drawdown = (Peak - Trough)/Peak


# In[ ]:


print ('Maximum Drawdown of this trade is', Maximum_Drawdown)


# In[ ]:


Executed_buys = pd.DataFrame(Trades['Executed Buys'])


# In[ ]:


Executed_buys = Executed_buys.dropna()


# In[ ]:


Executed_sells = pd.DataFrame(Trades['Executed Sells'])


# In[ ]:


Executed_sells = Executed_sells.dropna()


# In[ ]:


Number_of_Trades = len(Executed_buys) + len(Executed_sells)


# In[ ]:


print ('Total number of Trades is', Number_of_Trades)


# In[ ]:


PnL = pd.DataFrame(bd['PnL'])
PnL = PnL.dropna()
list_PnL = PnL['PnL'].to_list()
Wins = [max (i, 0) for i in list_PnL]
Losses = [min (i,0) for i in list_PnL]
if len(Executed_sells) == 0:
    Average_Wins_PnL = 0
else: 
    Average_Wins_PnL = sum(Wins)/len(Executed_sells)
if len(Executed_buys) == 0:
    Average_Losses_PnL = 0
else:
    Average_Losses_PnL = sum(Losses)/len(Executed_buys)
print ('Average Wins are', Average_Wins_PnL, 'and Average Losses are', Average_Losses_PnL)


# # Compiling the data into one Dataframe

# In[ ]:


ARR1 = [['Gross Profit/Loss in basis points','Gross Profit/Loss in USD', 'Maximum Drawdown', 'Average Wins in PnL', 'Average Losses in PnL', 'Number of Executed Trades'], [Gross_PnL_bps, Gross_PnL_USD, Maximum_Drawdown, Average_Wins_PnL, Average_Losses_PnL, Number_of_Trades]]
Execution_Analysis = pd.DataFrame(ARR1)
print (Execution_Analysis)
Execution_Analysis.to_csv('FalconX Assignment 3.csv'


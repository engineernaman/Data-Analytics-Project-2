#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


path = r'C:\Users\soumy\OneDrive\Desktop\pyprog\Data Analytics\2-Time Series Data Analysis\individual_stocks_5yr'
company_list = ['AAPL_data.csv', 'GOOG_data.csv', 'MSFT_data.csv', 'AMZN_data.csv']
all_data = pd.DataFrame()
for file in company_list:
    current_df = pd.read_csv(path+'/'+file)
    all_data = pd.concat([all_data,current_df])
all_data.shape


# In[3]:


all_data['date'] = pd.to_datetime(all_data['date'])


# In[4]:


tech_list = all_data['Name'].unique()


# In[5]:


plt.figure(figsize=(20,12))
for i, company in enumerate(tech_list, 1):
    plt.subplot(2,2,i)
    df= all_data[all_data['Name']==company]
    plt.plot(df['date'],df['close'])
    plt.xticks(rotation='vertical')
    plt.title(company)


# In[6]:


import plotly.express as px


# In[7]:


for comapny in tech_list:
    df = all_data[all_data['Name']==company]
    fig = px.line(df, x='date',y='volume',title=company)
    fig.show()


# In[8]:


#______Next___Section_________


# In[9]:


df = pd.read_csv(path+'/AAPL_data.csv')
df.head()


# In[10]:


df['Daily_Price_Change'] = df['close']-df['open']


# In[11]:


df.head()


# In[12]:


df['1Day % Return'] = ((df['close']-df['open'])/df['close'])*100
df.head()


# In[14]:


fig2 = px.line(df, x='date',y='1Day % Return', title='Apple')
fig2.show()


# In[15]:


df2 = df.copy()


# In[16]:


df2.dtypes


# In[17]:


df2['date'] = pd.to_datetime(df2['date'])


# In[18]:


df2.set_index('date', inplace=True)


# In[19]:


df2.head()


# In[21]:


df2['close'].resample('M').mean().plot()


# In[23]:


df2['close'].resample('Y').mean().plot(kind = 'bar')


# In[24]:


#_______NEXT_____________SECTION____________


# In[25]:


aapl = pd.read_csv(path+'/AAPL_data.csv')
aapl.head()


# In[26]:


amzn = pd.read_csv(path+'/AMZN_data.csv')
amzn.head()


# In[27]:


msft = pd.read_csv(path+'/MSFT_data.csv')
msft.head()


# In[28]:


goog = pd.read_csv(path+'/GOOG_data.csv')
goog.head()


# In[29]:


close = pd.DataFrame()


# In[31]:


close['aapl']=aapl['close']
close['amzn']=amzn['close']
close['msft']=msft['close']
close['goog']=goog['close']


# In[32]:


close.head()


# In[33]:


import seaborn as sns


# In[34]:


sns.pairplot(data=close)


# In[36]:


sns.heatmap(close.corr(),annot=True)


# In[37]:


#________NEXT____________SECTION___________


# In[38]:


data = pd.DataFrame()


# In[39]:


data['aapl_change']=((aapl['close']-aapl['open'])/aapl['close'])*100
data['amzn_change']=((amzn['close']-amzn['open'])/amzn['close'])*100
data['msft_change']=((msft['close']-msft['open'])/msft['close'])*100
data['goog_change']=((goog['close']-goog['open'])/goog['close'])*100


# In[40]:


data.head()


# In[41]:


sns.pairplot(data=data)


# In[42]:


sns.heatmap(data.corr(),annot=True)


# In[43]:


sns.distplot(data['aapl_change'])


# In[44]:


data['aapl_change'].std()


# In[46]:


data['aapl_change'].quantile(0.1)


# In[47]:


data.describe().T


# In[48]:


#__________COMPLETED___________________


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# # **COVID-19 pandemic in India**

# In[ ]:


# Importing Required Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
from IPython.display import Image
import warnings
warnings.filterwarnings('ignore')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


data=pd.read_csv('covid-19 INDIA.csv')
data.head()


# In[ ]:


# Dropping unnecessary Columns
data=data[['Date','State/UnionTerritory','Cured','Deaths','Confirmed']]
data.head()


# In[ ]:


# Renaming the Columns

data.columns=['date','state','cured','deaths','confirmed']
data.tail()


# In[ ]:


today=data[data.date=='2021-04-30']
today.head()


# In[ ]:


# Sorting data w.r.t to Confirmed Cases
max_confirmed_cases=today.sort_values(by='confirmed', ascending=False)
max_confirmed_cases.head()


# In[ ]:


top_states_confirmed=max_confirmed_cases[0:5]
top_states_confirmed


# In[ ]:


sns.set(rc={'figure.figsize':(12,6)})
sns.set_theme(style="whitegrid")
sns.barplot(x='state',y='confirmed',data=top_states_confirmed,hue='state')
plt.title(' Top 5 States with Confirmed Cases')
plt.show()


# In[ ]:


max_death=today.sort_values(by='deaths',ascending=False)
top_states_death=max_death[0:5]
sns.barplot(x='state',y='deaths',data=top_states_death, hue='state')
plt.show()


# In[ ]:


max_cured=today.sort_values(by='cured',ascending= False)
top_cured_states=max_cured[0:5]
sns.barplot(x='state',y='cured',data=top_cured_states,hue='state')
plt.show()


# In[ ]:


india_confirmed =max_confirmed_cases['confirmed'].sum()
india_cured =max_cured['cured'].sum()
india_deaths =max_death['deaths'].sum()

labels = ['Confirmed','Cured','Deaths']
sizes = [india_confirmed,india_cured,india_deaths]
color= ['#66b3ff','green','red']
explode = []

for i in labels:
    explode.append(0.05)
    
plt.figure(figsize= (15,10))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=9, explode =explode,colors = color)
centre_circle = plt.Circle((0,0),0.70,fc='white')

fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title('INDIA COVID-19 Cases',fontsize = 20)
plt.axis('equal')  


# # **Statewise Analysis**

#  ## Maharashtra

# In[ ]:


MH=data[data.state=='Maharashtra']
MH.head()


# In[ ]:


MH.shape


# In[ ]:


MH.tail()


# In[ ]:


import plotly.express as px
fig = px.line(MH, x="date", y="confirmed", title='Confirmed Cases in Maharashtra')
fig.show()


# In[ ]:


fig = px.line(MH, x="date", y="deaths", title='Deaths in Maharashtra')
fig.show()


# ## Kerala

# In[ ]:


KL=data[data.state=='Kerala']
KL.head()


# In[ ]:


fig = px.line(KL, x="date", y="confirmed", title='Confirmed Cases in Kerala')
fig.show()


# In[ ]:


fig = px.line(KL, x="date", y="deaths", title='Deaths in Kerala')
fig.show()


# ### Karnataka

# In[ ]:


Kar=data[data.state=='Karnataka']
Kar.head()


# In[ ]:


fig = px.line(Kar, x="date", y="deaths", title='Deaths in Karnataka')
fig.show()


# In[ ]:


fig = px.line(Kar, x="date", y="confirmed", title='Confirmed Cases in Karnataka')
fig.show()


# ### Statewise Deaths

# In[ ]:


x = today.groupby('state')['deaths'].sum().sort_values(ascending=False).to_frame()
x.style.background_gradient(cmap='Reds')


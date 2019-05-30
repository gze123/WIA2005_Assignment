#!/usr/bin/env python
# coding: utf-8

# In[0]:


import plotly


# In[1]:


import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as FF

import numpy as np
import pandas as pd


# In[2]:


df = pd.read_csv('stopwords\TokyoCSV.csv')

sample_data_table = FF.create_table(df.head())
py.iplot(sample_data_table, filename='sample-data-table')


# In[3]:


trace = go.Bar(x = df['Word'], y = df['Frequency'],
                  name='StopWord')
layout = go.Layout(title='StopWord Frequency In Tokyo',
                   plot_bgcolor='rgb(230, 230,230)', 
                   showlegend=True)
fig = go.Figure(data=[trace], layout=layout)

py.iplot(fig, filename='wordfrequency')





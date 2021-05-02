#!/usr/bin/env python
# coding: utf-8

# In[172]:


import gspread
import pandas_gbq
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from gspread_dataframe import get_as_dataframe, set_with_dataframe


# In[173]:


# Fetching the CAMPAIGN RAW sheet
gc = gspread.service_account(filename='C:\\Users\\MSI PC\\Documents\\CPTracking\\credentials.json')
sheet = gc.open('Competitor Tracking Analysis_SO')
# worksheet_list = sheet.worksheets()
worksheet = sheet.worksheet("2021")


# In[174]:


df = get_as_dataframe(worksheet, parse_dates=True, usecols=range(2,23), evaluate_formulas=True)


# In[175]:


df.dropna(subset=['code'], inplace=True)
df.drop_duplicates(inplace=True)
df.reset_index(inplace=True)


# In[176]:


column_names = {
'start date': 'start_date',
'end date': 'end_date',
'active': 'active',
'Player': 'Player',
'code': 'code',
'min': 'min_basket',
'Category': 'promo_type',
'% discount cate': 'bracket_discount',
'% discount max': 'max_percent_discount',
'% discount (discount max)': 'max_percent_discount',
'max cate when min=0': 'max_category',
'min cate': 'min_category',
'Order Value for Discount max (VND)': 'max_order_value',
'Discount max (VND)': 'max_discount_value',
'Min. Order Value (VND)': 'min_order_value',
'Discount amount for min order value (VND)': 'min_discount',
'msg. emphasis': 'msg_emphasis',
'Weekday vs. Weekend': 'day_type',
'City': 'city',
'Specific Menu': 'specific_menu',
'Week Number':'week'
}


# In[177]:


# df['start_date'].unique()


# In[178]:


df.rename(columns=column_names, inplace=True)
df.drop(columns='Discount (%)', inplace=True)


# In[179]:


df['start_date'] = [datetime.strptime(i, '%m/%d/%Y') for i in df['start_date']]
df['end_date'] = [datetime.strptime(i, '%m/%d/%Y') for i in df['end_date']]

# Back-tracking data up until today()
df['end_date_current'] = [datetime.today().strftime("%Y-%m-%d") if x >= datetime.today() else x.strftime("%Y-%m-%d") for x in df['end_date']]

df['date_range'] = [(pd.date_range(df.start_date[x],df.end_date_current[x]).strftime("%Y-%m-%d").tolist()) for x in range(len(df.end_date))]

# Exploding list of dates into separate rows 
def explode_list(df, col):
    s = df[col]
    i = np.arange(len(s)).repeat(s.str.len())
    return df.iloc[i].assign(**{col: np.concatenate(s)})

df = explode_list(df, 'date_range')
df.drop(columns='end_date_current', inplace =True)
df.rename(columns={"date_range": "loading_date"}, inplace=True)


# In[202]:


# Cleaning data
#df.drop(columns='Discount (%)', inplace=True)
df.replace({'All': 'all'}, inplace=True)
df['max_order_value']=df['max_order_value'].round(decimals=1)


# In[181]:


df['start_date'] = [datetime.strftime(i, "%Y-%m-%d") for i in df['start_date']]
df['end_date'] = [datetime.strftime(i, "%Y-%m-%d") for i in df['end_date']]



# In[197]:


#Import data for 2020
worksheet1 = sheet.worksheet("2020")
df1 = get_as_dataframe(worksheet1, parse_dates=True, usecols=range(2,20), evaluate_formulas=True)
df1.dropna(subset=['code'], inplace=True)
df1.drop_duplicates(inplace=True)
df1.reset_index(inplace=True)

df1.rename(columns=column_names, inplace=True)
df1['start_date'] = [datetime.strptime(i, '%m/%d/%Y') for i in df1['start_date']]
df1['active'] = 'EXPIRED'
df1['city'] = 'all'
df1['end_date'] = df1['start_date']+ timedelta(days=7) 


# Back-tracking data up until today()
df1['end_date_current'] = [datetime.today().strftime('%m/%d/%Y') if x >= datetime.today() else x.strftime('%m/%d/%Y') for x in df1['end_date']]

df1['date_range'] = [(pd.date_range(df1.start_date[x],df1.end_date_current[x]).strftime("%Y-%m-%d").tolist()) for x in range(len(df1.end_date))]

# Exploding list of dates into separate rows 
def explode_list(df1, col):
    s = df1[col]
    i = np.arange(len(s)).repeat(s.str.len())
    return df1.iloc[i].assign(**{col: np.concatenate(s)})

df1 = explode_list(df1, 'date_range')
df1.drop(columns='end_date_current', inplace =True)
df1.rename(columns={"date_range": "loading_date"}, inplace=True)


# Cleaning data
df1.drop(columns='Discount (%)', inplace=True)
df1.replace({'All': 'all'}, inplace=True)
df1['start_date'] = [datetime.strftime(i, "%Y-%m-%d") for i in df1['start_date']]
df1['end_date'] = [datetime.strftime(i, "%Y-%m-%d") for i in df1['end_date']]


# In[208]:


df1['max_order_value'] = pd.to_numeric(df1['max_order_value'], errors='coerce')
df1['max_order_value']=df1['max_order_value'].round(decimals=1)


# In[209]:


#Merge 2020 and 2021
full= df.append(df1)


# In[210]:


df1.info()


# In[211]:


# Importing data to BigQuery
pandas_gbq.to_gbq(
    full, 'dept.coupon_tracking', project_id='baemin-vietnam', if_exists='replace',
)


# In[70]:


# Checking for duplicates
# Importing libraries
import pandas as pd

query = 'select * from dept.coupon_tracking'

df = pd.read_gbq(query,
                 project_id = 'baemin-vietnam',
                 dialect='standard')


# In[71]:


df.drop_duplicates(inplace=True)


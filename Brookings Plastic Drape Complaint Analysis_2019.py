# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 11:34:41 2020

@author: a6db5zz
"""

#Import stuff
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime
import dateutil.relativedelta

# Read Excel document with complaint data
df = pd.read_excel('Plastic Complaints_Brookings.xls')
df = df.set_index('Creation Date')
df = df.drop_duplicates(subset=['Complaint Nbr'], keep='first')

# Create time stamps for CQI time frames
d = datetime.datetime.today()

group1_start_month = str(12)
group1_start_year = str(2019)
group1_end_month = str(1)
group1_end_year = str(2019)
group2_start_month = str(d.month - 1)
group2_start_year = str(d.year - 1)
group2_end_month = str(d.month)
group2_end_year = str(d.year - 2)

# Create Dataframes for CQI time frames
date_current = df.loc[group1_end_year + '-' + group1_end_month + '-1':group1_start_year + '-' + group1_start_month + '-1']

# Create cause series for current date range
current_cause_level = date_current.loc[:]['Cause Lvl 3']
current_cause_level_no_dublicates = current_cause_level.drop_duplicates()

# Calculate number of times each cause level appears in the the current time period
current_cause_level_count = current_cause_level.loc[current_cause_level.isin(current_cause_level_no_dublicates)].value_counts()
current_cause_level_count.name = group1_end_month + '/' + group1_end_year + ' - ' + group1_start_month + '/' + group1_start_year

# Plot Data - Bar Plot of Cause Level 3 Complaints
current_cause_level_count.plot.bar(rot=0, color=['#1f77b4'], alpha=0.7, figsize=(10,8))

#combination_zero_sorted.plot.bar(rot=0, color=['#1f77b4'], alpha=0.7, figsize=(10,8))
plt.xlabel('Cause Level 3')
plt.ylabel('Number of Complaints')
plt.xticks(rotation=90)
plt.yticks(np.arange(0, 17, 2.0))
plt.title('Brookings 2019 Plastic Complaint Pareto')
plt.grid(linestyle='dotted')
plt.tight_layout()
plt.savefig('Brookings 2019 Plastic Complaint Pareto')


# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 14:47:04 2020

@author: a6db5zz
"""

#Import stuff
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime
import dateutil.relativedelta

# Read Excel document with complaint data
df = pd.read_excel('Plastic Complaints - Copy (2).xls')
df = df.set_index('Creation Date')
df = df.drop_duplicates(subset=['Complaint Nbr'], keep='first')

# Create time stamps for CQI time frames
d = datetime.datetime.today()

group1_start_month = str(d.month - 1)
group1_start_year = str(d.year)
group1_end_month = str(d.month)
group1_end_year = str(d.year - 1)
group2_start_month = str(d.month - 1)
group2_start_year = str(d.year - 1)
group2_end_month = str(d.month)
group2_end_year = str(d.year - 2)

group1_start_month=str(12)
group2_start_month=str(12)
group1_start_year=str(2019)
group2_start_year=str(2018)

# Create Dataframes for CQI time frames
date_current = df.loc[group1_end_year + '-' + group1_end_month + '-1':group1_start_year + '-' + group1_start_month + '-1']
date_previous = df.loc[group2_end_year + '-' + group2_end_month + '-1':group2_start_year + '-' + group2_start_month + '-1']

# Create cause series for current date range
current_cause_level = date_current.loc[:]['Cause Lvl 3']
current_cause_level_no_dublicates = current_cause_level.drop_duplicates()

# Calculate number of times each cause level appears in the the current time period
current_cause_level_count = current_cause_level.loc[current_cause_level.isin(current_cause_level_no_dublicates)].value_counts()
current_cause_level_count.name = group1_end_month + '/' + group1_end_year + ' - ' + group1_start_month + '/' + group1_start_year

# Create cause series for previous date range
previous_cause_level = date_previous.loc[:]['Cause Lvl 3']
previous_cause_level_no_dublicates = previous_cause_level.drop_duplicates()

# Calculate number of times each cause level appears in the the previous time period
previous_cause_level_count = previous_cause_level.loc[previous_cause_level.isin(previous_cause_level_no_dublicates)].value_counts()
previous_cause_level_count.name = group2_end_month + '/' + group2_end_year + ' - ' + group2_start_month + '/' + group2_start_year


# Combine previous and current cause level series into a data frame with equivalent indexes
combination_NaN = pd.concat([current_cause_level_count, previous_cause_level_count], axis=1, sort=True)
combination_zero = combination_NaN.fillna(0)
combination_zero_sorted = combination_zero.sort_values(by=group1_end_month + '/' + group1_end_year + ' - ' + group1_start_month + '/' + group1_start_year, ascending = False)


# Plot Data - Bar Plot of Cause Level 3 Complaints
current_cause_level_count.plot.bar(rot=0, color=['#1f77b4'], alpha=0.7, figsize=(10,8))
plt.xlabel('Cause Level 3')
plt.ylabel('Number of Complaints')
plt.xticks(rotation=90)
plt.yticks(np.arange(0, 5, 1.0))
plt.title('2019 Brookings Plastic Drape Complaint Pareto')
plt.grid(linestyle='dotted')
plt.tight_layout()
plt.savefig('2019 Brookings Plastic Drape Complaint Pareto')




# Find current date with a format aligned with complaint data
date_current_2 = d.strftime("%Y-%m-%d")
date = datetime.datetime.strptime(date_current_2, "%Y-%m-%d")


"""
#Create a string with the current date minus a specified month (ex: if current month is August, date_1 month is July)
complaint_trending_year_one_months = range(1,13)

#[str(x) for x in range(1,13)]
#complaint_trending_year_two_months = list(range(13,25))

complaint_trending_dates_year_one = str(date - dateutil.relativedelta.relativedelta(months=complaint_trending_year_one_months))
#complaint_trending_dates_year_two = str(date - dateutil.relativedelta.relativedelta(months=complaint_trending_year_two_months))
"""

date_1 = str(date - dateutil.relativedelta.relativedelta(months=1))
date_2 = str(date - dateutil.relativedelta.relativedelta(months=2))
date_3 = str(date - dateutil.relativedelta.relativedelta(months=3))
date_4 = str(date - dateutil.relativedelta.relativedelta(months=4))
date_5 = str(date - dateutil.relativedelta.relativedelta(months=5))
date_6 = str(date - dateutil.relativedelta.relativedelta(months=6))
date_7 = str(date - dateutil.relativedelta.relativedelta(months=7))
date_8 = str(date - dateutil.relativedelta.relativedelta(months=8))
date_9 = str(date - dateutil.relativedelta.relativedelta(months=9))
date_10 = str(date - dateutil.relativedelta.relativedelta(months=10))
date_11 = str(date - dateutil.relativedelta.relativedelta(months=11))
date_12 = str(date - dateutil.relativedelta.relativedelta(months=12))

date_13 = str(date - dateutil.relativedelta.relativedelta(months=13))
date_14 = str(date - dateutil.relativedelta.relativedelta(months=14))
date_15 = str(date - dateutil.relativedelta.relativedelta(months=15))
date_16 = str(date - dateutil.relativedelta.relativedelta(months=16))
date_17 = str(date - dateutil.relativedelta.relativedelta(months=17))
date_18 = str(date - dateutil.relativedelta.relativedelta(months=18))
date_19 = str(date - dateutil.relativedelta.relativedelta(months=19))
date_20 = str(date - dateutil.relativedelta.relativedelta(months=20))
date_21 = str(date - dateutil.relativedelta.relativedelta(months=21))
date_22 = str(date - dateutil.relativedelta.relativedelta(months=22))
date_23 = str(date - dateutil.relativedelta.relativedelta(months=23))
date_24 = str(date - dateutil.relativedelta.relativedelta(months=24))

# Gather the year and month from the date strings: YYYY-MM
date_1 = date_1[:7]
date_2 = date_2[:7]
date_3 = date_3[:7]
date_4 = date_4[:7]
date_5 = date_5[:7]
date_6 = date_6[:7]
date_7 = date_7[:7]
date_8 = date_8[:7]
date_9 = date_9[:7]
date_10 = date_10[:7]
date_11 = date_11[:7]
date_12 = date_12[:7]

date_13 = date_13[:7]
date_14 = date_14[:7]
date_15 = date_15[:7]
date_16 = date_16[:7]
date_17 = date_17[:7]
date_18 = date_18[:7]
date_19 = date_19[:7]
date_20 = date_20[:7]
date_21 = date_21[:7]
date_22 = date_22[:7]
date_23 = date_23[:7]
date_24 = date_24[:7]

# Gather number of complaints for each month in the prior year
date_1_complaints_count = len(df.loc[date_1])
date_2_complaints_count = len(df.loc[date_2])
date_3_complaints_count = len(df.loc[date_3])
date_4_complaints_count = len(df.loc[date_4])
date_5_complaints_count = len(df.loc[date_5])
date_6_complaints_count = len(df.loc[date_6])
date_7_complaints_count = len(df.loc[date_7])
date_8_complaints_count = len(df.loc[date_8])
date_9_complaints_count = len(df.loc[date_9])
date_10_complaints_count = len(df.loc[date_10])
date_11_complaints_count = len(df.loc[date_11])
date_12_complaints_count = len(df.loc[date_12])

date_13_complaints_count = len(df.loc[date_13])
date_14_complaints_count = len(df.loc[date_14])
date_15_complaints_count = len(df.loc[date_15])
date_16_complaints_count = len(df.loc[date_16])
date_17_complaints_count = len(df.loc[date_17])
date_18_complaints_count = len(df.loc[date_18])
date_19_complaints_count = len(df.loc[date_19])
date_20_complaints_count = len(df.loc[date_20])
date_21_complaints_count = len(df.loc[date_21])
date_22_complaints_count = len(df.loc[date_22])
date_23_complaints_count = len(df.loc[date_23])
date_24_complaints_count = len(df.loc[date_24])

# Create y-axis labels for dates in plots
#year_one_month = [date_1, date_2, date_3, date_4, date_5, date_6, date_7, date_8, date_9, date_10, date_11, date_12]
year_one_month = [date_12, date_11, date_10, date_9, date_8, date_7, date_6, date_5, date_4, date_3, date_2, date_1]
year_two_month = [date_24, date_23, date_22, date_21, date_20, date_19, date_18, date_17, date_16, date_15, date_14, date_13]

# Create a DataFrame of previous year of complaints by month and two years previous of complaints by month
year_one_complaints_count = [date_12_complaints_count, date_11_complaints_count, date_10_complaints_count, date_9_complaints_count, date_8_complaints_count, date_7_complaints_count, date_6_complaints_count, date_5_complaints_count, date_4_complaints_count, date_3_complaints_count, date_2_complaints_count, date_1_complaints_count]
year_two_complaints_count = [date_23_complaints_count, date_22_complaints_count, date_21_complaints_count, date_20_complaints_count, date_19_complaints_count, date_18_complaints_count, date_17_complaints_count, date_16_complaints_count, date_15_complaints_count, date_14_complaints_count, date_13_complaints_count, date_12_complaints_count]


# Create a line plot comparing previous 12 months of complaints to previous 12-24 months
plt.figure()
plt.plot(year_one_month, year_one_complaints_count, color='#1f77b4')
plt.xlabel('Date')
plt.ylabel('Number of Complaints')
plt.xticks(rotation=90)
plt.yticks(np.arange(0, 3, 1.0))
plt.title('2019 Brookings Plastic Complaint Trending by Month')
plt.grid(linestyle='dotted')
plt.tight_layout() 
plt.show()
plt.savefig('2019 Brookings Plastic Complaint Trending by Month')

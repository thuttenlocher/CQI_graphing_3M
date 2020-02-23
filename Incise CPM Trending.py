# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 08:06:29 2019

@author: a6db5zz
"""

# Import stuff
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


##### Create CPM Graph ###


# Read Excel document with complaint data
cpm_data = pd.read_excel('Brookings CQI CPM Data.xlsx', sheet_name='Incise')
cpm_data = cpm_data.set_index('Date')
current_year_cpm_data = cpm_data.iloc[76:87]


# Create a line plot comparing previous 12 months of complaints to previous 12-24 months
plt.plot(current_year_cpm_data['CPM'], color='#1f77b4')
plt.plot(current_year_cpm_data['Target'], linestyle='dashed', color='#bdbdbd')
plt.xlabel('Date [YYYY-MM]')
plt.ylabel('Number of Complaints')
plt.xticks(rotation=90)
plt.yticks(np.arange(0, 13, 1.0))
plt.legend()
plt.title('Brookings Incise CPM - Previous 11 Months')
plt.grid(linestyle='dotted')
plt.tight_layout()
plt.savefig('Brookings Incise CPM - Previous 11 Months')






#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 15:11:54 2024

@author: kelly
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the datasets 
ads_df = pd.read_csv('train/train_data_ads.csv')
feeds_df = pd.read_csv('train/train_data_feeds.csv')

#%% TASK 1: Age, Geographic, Device, Content
# Get unique user IDs in each dataset
unique_users_ads_df = ads_df['user_id'].nunique()
unique_users_feeds_df = feeds_df['u_userId'].nunique()

print(f"Unique User IDs in Advertisers Dataset: {unique_users_ads_df}") 
print(f"Unique User IDs in Publishers Dataset: {unique_users_feeds_df}")
    #Ads: 65297   Feeds: 180123
    #180123 users view the ad, 65297 of them clicked.
    

# Select one user from the ads dataset
sample_user_id = ads_df['user_id'].iloc[0]  # This selects the first user ID in the dataset

# Extract all rows for the selected user
user_rows = ads_df[ads_df['user_id'] == sample_user_id]

print(f"All rows for user {sample_user_id}:")
print(user_rows)


# Extract unique user IDs for potential customers (label == 1) from ads_df
potential_customers_ids = ads_df[ads_df['label'] == 1]['user_id'].unique()

# Filter the datasets for these users
potential_customers_df = ads_df[ads_df['user_id'].isin(potential_customers_ids)].drop_duplicates(subset='user_id')

# Plot histograms for potential customers
plt.figure(figsize=(17, 5))

plt.subplot(1, 3, 1)
potential_customers_df['age'].value_counts().plot(kind='bar')
plt.title('Age Distribution (Potential Customers)')
plt.xlabel('Age')
plt.ylabel('Frequency')

plt.subplot(1, 3, 2)
potential_customers_df['residence'].value_counts().plot(kind='bar')
plt.title('Residence Distribution (Potential Customers)')
plt.xlabel('Residence')
plt.ylabel('Frequency')

plt.subplot(1, 3, 3)
top_devices = potential_customers_df['device_name'].value_counts().head(10)
top_devices.plot(kind='bar')
plt.title('Top 10 Device Name Distribution (Potential Customers)')
plt.xlabel('Device Name')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()



#%% Engagement: hour, day of the week, day of the month

# Convert 'pt_d' to datetime
potential_customers_df['pt_d'] = pd.to_datetime(potential_customers_df['pt_d'], format='%Y%m%d%H%M')

# Extract hour, day of the week, and day of the month
potential_customers_df['hour'] = potential_customers_df['pt_d'].dt.hour
potential_customers_df['day_of_week'] = potential_customers_df['pt_d'].dt.dayofweek
potential_customers_df['day_of_month'] = potential_customers_df['pt_d'].dt.day

# Plot histograms for potential customers
plt.figure(figsize=(17, 5))

plt.subplot(1, 3, 1)
potential_customers_df['hour'].value_counts().sort_index().plot(kind='bar')
plt.title('Hourly Distribution (Potential Customers)')
plt.xlabel('Hour of the Day')
plt.ylabel('Frequency')

plt.subplot(1, 3, 2)
potential_customers_df['day_of_week'].value_counts().sort_index().plot(kind='bar')
plt.title('Day of Week Distribution (Potential Customers)')
plt.xlabel('Day of the Week')
plt.ylabel('Frequency')

plt.subplot(1, 3, 3)
potential_customers_df['day_of_month'].value_counts().sort_index().plot(kind='bar')
plt.title('Day of Month Distribution (Potential Customers)')
plt.xlabel('Day of the Month')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()




#%% Content

# Plot histograms for potential customers
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
potential_customers_df['ad_click_list_v001'].value_counts().head(10).plot(kind='bar')
plt.title('Top 10 Ad Clicks (Potential Customers)')
plt.xlabel('Ad Task ID')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
potential_customers_df['u_newsCatInterestsST'].value_counts().head(10).plot(kind='bar')
plt.title('News Category Interests (Potential Customers)')
plt.xlabel('News Category')
plt.ylabel('Frequency')


plt.tight_layout()
plt.show()



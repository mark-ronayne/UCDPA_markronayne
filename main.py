# importing the two csv files for use in PyCharm

import pandas as pd

df = pd.read_csv(r"C:\Users\Mark Ronayne\Desktop\Personal\UCD\Semester 1\Project Data\FraudTest.csv").set_index(
    'trans_num')
df1 = pd.read_csv(r"C:\Users\Mark Ronayne\Desktop\Personal\UCD\Semester 1\Project Data\FraudTrain.csv").set_index(
    'trans_num')
print(df.head())
# finding out the type of data in each column and dataframe
df.info()
df1.info()
# describe the data
print(df.describe())
print(df1.describe())

# both data sets contain the same number of columns and data types, so I will merge them vertically. I will check for duplicate values

total_data = pd.concat([df, df1], verify_integrity=True)

# checking for null values

total_data.isnull()

# creating reusable code to calculate the distance between customer address and merchant
from pyproj import Geod
wgs84_geod = Geod(ellps='WGS84')


def Distance(lat1, lon1, lat2, lon2):
    az12, az21, dist = wgs84_geod.inv(lon1, lat1, lon2, lat2)
    return dist


total_data['dist'] = Distance(total_data['lat'].tolist(), total_data['long'].tolist(), total_data['merch_lat'].tolist(),
                              total_data['merch_long'].tolist())

print(total_data.head())

#splitting the trans_date_trans_time column into two, date and time respectively.

total_data['date'] = pd.to_datetime(total_data['trans_date_trans_time']).dt.date
total_data['time'] = pd.to_datetime(total_data['trans_date_trans_time']).dt.time
total_data['date'] = pd.to_datetime(total_data['date'])

# total_data.info()
print(total_data.head())


# identifying the unique categories which are present in the data
category_columns = total_data['category'].unique()

# printing category columns for reference
print(category_columns)

import matplotlib.pyplot as plt

# looping over the unique categories to find the mean transaction amount per category and presenting this in a bar plot

fig, ax = plt.subplots()
fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()
fig3, ax3 = plt.subplots()

for category in category_columns :
    category_df = df[df['category'] == category]
    ax.bar(category, category_df['amt'].mean())

ax.set_xticklabels(category_columns, rotation=90)
ax.tick_params(axis='both', labelsize=16)
ax.yaxis.set_major_formatter('${x:1.0f}')
ax.set_xlabel('Merchant Categories', fontsize=18)
ax.set_ylabel('Average TX Amount', fontsize=18)

# looping over the unique categories to find the mean fraudulent transaction amount per category and presenting this in a bar plot

for category in category_columns :
    category_df = df[df['category'] == category]
    ax1.bar(category, category_df.query('is_fraud == 1')['amt'].mean())

ax1.set_xticklabels(category_columns, rotation=90)
ax1.tick_params(axis='both', labelsize=16)
ax1.yaxis.set_major_formatter('${x:1.0f}')
ax1.set_xlabel('Merchant Categories', fontsize=18)
ax1.set_ylabel('Average Fraudulent TX Amount', fontsize=18)




# looping over the unique categories to find the % volume fraudulent transactions per category and presenting this in a bar plot - use log scale

for category in category_columns :
    category_df = df[df['category'] == category]
    ax2.bar(category, (category_df.query('is_fraud == 1')['amt'].sum() / category_df['amt'].sum()) * 100)

#plt.yscale('log')
ax2.yaxis.set_major_formatter('{x:1.0f}%')
ax2.set_xticklabels(category_columns, rotation=90)
ax2.tick_params(axis='both', labelsize=16)
ax2.set_xlabel('Merchant Categories', fontsize=18)
ax2.set_ylabel('% Transaction volume which is fraud', fontsize=18)

# looping over the unique categories to find the % count of fraudulent transactions per category and presenting this in a bar plot


for category in category_columns :
    category_df = df[df['category'] == category]
    ax3.bar(category, (category_df.query('is_fraud == 1')['amt'].count() / category_df['amt'].count()) * 100)

ax3.yaxis.set_major_formatter('{x:1.1f}%')
ax3.set_xticklabels(category_columns, rotation=90)
ax3.tick_params(axis='both', labelsize=16)
ax3.set_xlabel('Merchant Categories', fontsize=18)
ax3.set_ylabel('% Transaction count which is fraud', fontsize=18)

plt.show()

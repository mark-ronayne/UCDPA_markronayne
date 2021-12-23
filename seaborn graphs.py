# importing the two csv files for use in PyCharm

import pandas as pd

df = pd.read_csv(r"C:\Users\Mark Ronayne\Desktop\Personal\UCD\Semester 1\Project Data\FraudTest.csv").set_index(
    'trans_num')
df1 = pd.read_csv(r"C:\Users\Mark Ronayne\Desktop\Personal\UCD\Semester 1\Project Data\FraudTrain.csv").set_index(
    'trans_num')

# both data sets contain the same number of columns and data types, so I will merge them vertically. I will check for duplicate values

total_data = pd.concat([df, df1], verify_integrity=True)

# creating reusable code to calculate the distance between customer address and merchant
from pyproj import Geod
wgs84_geod = Geod(ellps='WGS84')


def Distance(lat1, lon1, lat2, lon2):
    az12, az21, dist = wgs84_geod.inv(lon1, lat1, lon2, lat2)
    return dist


total_data['dist'] = Distance(total_data['lat'].tolist(), total_data['long'].tolist(), total_data['merch_lat'].tolist(),
                              total_data['merch_long'].tolist())

#splitting the trans_date_trans_time column into two, date and time respectively.

total_data['date'] = pd.to_datetime(total_data['trans_date_trans_time']).dt.date
total_data['time'] = pd.to_datetime(total_data['trans_date_trans_time']).dt.time
total_data['date'] = pd.to_datetime(total_data['date'])

# checking for correlation between distance and amount of fraudulent and genuine tx

import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style("dark")
sns.set_context('poster')
sns.lmplot(data=total_data, x='dist', y='amt', col="is_fraud", row='gender', hue='category')
plt.ylim(0, 1000)
plt.show()






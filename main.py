#importing the two csv files for use in PyCharm

import pandas as pd

df = pd.read_csv(r"C:\Users\Mark Ronayne\Desktop\Personal\UCD\Semester 1\Project Data\FraudTest.csv")
df1 = pd.read_csv(r"C:\Users\Mark Ronayne\Desktop\Personal\UCD\Semester 1\Project Data\FraudTrain.csv")
#print(df.head())
#finding out the type of data in each column and dataframe
#df.info()
#df1.info()
#describe the data
#print(df.describe())
#print(df1.describe())

#both data sets contain the sme number of columns and data types, so I will merge them vertically. There are no null values

total_data = pd.concat([df, df1], ignore_index=True)

#print(total_data.head())


# splitting the trans_date_trans_time column into two, date and time respectively.

total_data['date'] = pd.to_datetime(total_data['trans_date_trans_time']).dt.date
total_data['time'] = pd.to_datetime(total_data['trans_date_trans_time']).dt.time
total_data['date'] = pd.to_datetime(total_data['date'])

total_data.info()
print(total_data.head())

#querying the df for the number of fraudulent transactions
#print(total_data.query('is_fraud == 1'))

#identifying the unique categories which are present in the data
category_columns = total_data['category'].unique()

#checking for null and/or duplicate values



#printing category columns for reference
print(category_columns)

import matplotlib.pyplot as plt
import seaborn as sns

#looping over the unique categories to find the mean transaction amount per category and presenting this in a bar plot

fig, ax = plt.subplots()

#for #category in category_columns :
    #category_df = df[df['category'] == category]
    #ax.bar(category, category_df['amt'].mean())

#ax.set_xticklabels(category_columns, rotation=45)
#ax.set_xlabel('Merchant Categories')
#ax.set_ylabel('Average TX Amount')

#plt.show()

#looping over the unique categories to find the % volume fraudulent transactions per category and presenting this in a bar plot - use log scale

#for category in category_columns :
    #category_df = df[df['category'] == category]
    #ax.bar(category, (category_df.query('is_fraud == 1')['amt'].sum() / category_df['amt'].sum()) * 100)

ax.set_xticklabels(category_columns, rotation=45)
ax.set_xlabel('Merchant Categories')
ax.set_ylabel('% Transaction volume which is fraud')

plt.yscale('log')
plt.show()

#looping over the unique categories to find the % count of fraudulent transactions per category and presenting this in a bar plot

#for category in category_columns :
    #category_df = df[df['category'] == category]
    #.bar(category, (category_df.query('is_fraud == 1')['amt'].count() / category_df['amt'].count()) * 100)

#ax.set_xticklabels(category_columns, rotation=45)
#ax.set_xlabel('Merchant Categories')
#ax.set_ylabel('% Transaction count which is fraud')

#plt.show()
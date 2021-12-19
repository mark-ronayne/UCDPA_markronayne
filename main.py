#importing the two csv files for use in PyCharm

import pandas as pd

df = pd.read_csv(r"C:\Users\Mark Ronayne\Desktop\Personal\UCD\Semester 1\Project Data\FraudTest.csv")
# df1 = pd.read_csv(r"C:\Users\Mark Ronayne\Desktop\Personal\UCD\Semester 1\Project Data\FraudTrain.csv")
# print(df.head())



# identifying the unique categories which are present in the data
category_columns = df['category'].unique()

# printing category columns for reference
print(category_columns)

import matplotlib.pyplot as plt
import seaborn as sns

#looping over the unique categories to find the mean transaction amount per category and presenting this in a bar plot

fig, ax = plt.subplots()

for category in category_columns :
    category_df = df[df['category'] == category]
    ax.bar(category, category_df['amt'].mean())

ax.set_xticklabels(category_columns, rotation=45)
ax.set_xlabel('Merchant Categories')
ax.set_ylabel('Average TX Amount')

plt.show()




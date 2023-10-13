import pandas as pd
import pandas.core.series

df = pd.read_csv("../99 - Data/titanic.csv")

adult_names = df.loc[(df["Age"] == 35) & (df["Sex"]=="male"), ["Name", "Sex"]]

print(adult_names.head())
print(adult_names.shape)

numeric = df.iloc[0:3,5:7]

print(numeric.head())
print(numeric.shape)
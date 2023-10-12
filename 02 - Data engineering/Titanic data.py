import pandas as pd
import pandas.core.series

df = pd.read_csv("Data/titanic.csv")

ages = df["Age"]
age_sex = df[["Age","Sex","Fare"]]
print(age_sex.head())
print(age_sex.shape)
above_35 = df[df["Age"]==35]
print(above_35.shape)
class_23 = df[df["Pclass"].isin([2 ,3])]
print(class_23.shape)
age_known = df[df["Age"].notna()]
print(age_known.shape)
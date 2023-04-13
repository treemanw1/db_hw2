import pandas as pd
import numpy as np

df = pd.read_csv("./student_files/data/TA_restaurants_curated_cleaned.csv")
print(df.shape)
df = df[df['Number of Reviews'] != 0]
print(df.shape)
df = df[df['Rating'] >= 1]
# print(df.head)
print(df.shape)

df2 = pd.read_csv("./student_files/output/part-00000-bd5b2e4b-fc2f-4e95-8f93-911e804d9059-c000.csv")
print(df2.shape)
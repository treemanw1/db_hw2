import pandas as pd
import numpy as np

df = pd.read_csv("./student_files/data/TA_restaurants_curated_cleaned.csv")
print(df.shape)
df = df[df['Number of Reviews'] != 0]
print(df.shape)
df = df[df['Rating'] >= 1]
# print(df.head)
print(df.shape)
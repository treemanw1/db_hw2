import pandas as pd
import numpy as np

# pandas q1
# df = pd.read_csv("./student_files/data/TA_restaurants_curated_cleaned.csv")
# df = df[df['Number of Reviews'] != 0]
# print(df.shape)
# df = df[df['Rating'] >= 1]
# print(df.shape)

# pandas q2
df = pd.read_csv("./student_files/data/TA_restaurants_curated_cleaned.csv")
print(df.columns)
df = df[df['Number of Reviews'] != 0]
print(df.shape)
df = df[df['Rating'] >= 1]
print(df.shape)


# answer comparison
# df2 = pd.read_csv("./student_files/output/q1_answer.csv")
# print("model answer: ", df2.shape)
# df2 = pd.read_csv("./student_files/output/q1_myans.csv")
# print("my ans: ", df2.shape)
df2 = pd.read_csv("./student_files/output/q1_answer.csv")
print("model answer: ", df2.shape)
df2 = pd.read_csv("./student_files/output/q1_myans.csv")
print("my ans: ", df2.shape)
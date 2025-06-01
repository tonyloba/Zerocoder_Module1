import pandas as pd
# df = pd.read_csv('International_Education_Costs.csv')
#
# print(df.head());
# print(df.info());
# print(df.describe());

df2 = pd.read_csv('dz.csv')

print(df2.head());
print()
print(df2.info());
print()
print(df2.describe());
print()
group = df2.groupby('City')['Salary'].mean()
print(group)
import pandas as pd

df = pd.read_excel("data/Online Retail.xlsx")

print(type(df))
print(df.shape)
print(df.head())
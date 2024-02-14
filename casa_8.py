import pandas as pd

df = pd.read_csv('big-mac-full-index.csv')

print(type(df))
print(df.columns)
print(type(df.columns))


# 1. Method 4: Using iterrows() method

print("Given Dataframe:\n",df)

print("\nIterating over rows using iterrows() method :\n")

for index, row in df.iterrows():
    print(row['iso_a3'],
          row['name'])


# 2. Method 6: Using apply() method

print("Given Dataframe:\n",df)

print("\nIterating over rows using apply() method :\n")

print(df.apply(lambda row: row['iso_a3'] + " " +
                 str(row['name']), axis = 1))
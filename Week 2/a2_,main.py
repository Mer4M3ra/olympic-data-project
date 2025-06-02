
import pandas as pd

# Load the dataset
df = pd.read_csv("athlete_events.csv")

# Show the first 5 rows
print(df.head())

# Show the column names
print(df.columns)
# Shows the count of how much people play the top 5 sports
print(df['Sport'].value_counts().head())
# shows the number of males to the number of females
print(df['Sex'].value_counts())
#shows information about the dataset
print(df.describe())
#shows the names of NOCs (National Olympic Committees)
print(df['NOC'].nunique())
print(df['NOC'].unique())
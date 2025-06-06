import pandas as pd

df = pd.read_csv("athlete_events.csv")

# Filter for female athletes only
female_athletes = df[df['Sex'] == 'F']
print(female_athletes.head())

# Filter for athletes older than 35
older_athletes = df[df['Age'] > 35]
print(older_athletes[['Name', 'Age', 'Sport']].head())

print("there is a total of " + str(len(female_athletes)) + " Female athletes")
print("there is a total of " + str(len(older_athletes)) + " Athletes above the age of 35")

# Female athletes over 30
combo_filter = df[(df['Sex'] == 'F') & (df['Age'] > 30)]
# Prints Female athletes above the age of 30 with the categories Name, Age, Sport
print(combo_filter[['Name', 'Age', 'Sport']].head())

# Male athletes in Basketball
basketball_males = df[(df['Sex'] == 'M') & (df['Sport'] == 'Basketball')]
# Prints Basketball males
print(basketball_males.head())
# Australian swimmers
AustraliaSwimmers = df[(df['Team']== 'Australia') & (df['Sport'] == 'Swimming')]
# Prints the first 5 australian swimmers
print(AustraliaSwimmers.head())

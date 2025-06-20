import pandas as pd

df = pd.read_csv("athlete_events.csv")

# Filter for female athletes only
female_athletes = df[df['Sex'] == 'F']
print(female_athletes.head())

# Filter for athletes older than 35
older_athletes = df[df['Age'] > 35]
print(older_athletes[['Name', 'Age', 'Sport']].head())

print("there is a total of " + str(len(female_athletes.head())) + " Female athletes")
print("there is a total of " + str(len(older_athletes.head())) + " Athletes above the age of 35")

# Female athletes over 30
combo_filter = df[(df['Sex'] == 'F') & (df['Age'] > 30)]
# Prints Female athletes above the age of 30 with the categories Name, Age, Sport
print(combo_filter[['Name', 'Age', 'Sport']].head())

# Male athletes in Basketball
basketball_males = df[(df['Sex'] == 'M') & (df['Sport'] == 'Basketball')]
# Prints Basketball males
print(basketball_males.head())
# Australian swimmers
AustraliaSwimmers = df[(df['Team'] == 'Australia') & (df['Sport'] == 'Swimming')]
# Prints the first 5 australian swimmers
print(AustraliaSwimmers.head())
# Sort by age
sorted_by_age = df.sort_values(by='Age', ascending=False)
print(sorted_by_age[['Name', 'Age', 'Sport']].head())

# Sort by weight
sorted_by_weight = df.sort_values(by='Weight', ascending=False)
print(sorted_by_weight[['Name', 'Weight', 'Sport']].head())

sorted_by_weight_height_10 = df.sort_values(by=['Height', 'Weight'], ascending=False)
print(sorted_by_weight_height_10[['Name', 'Height', 'Weight', 'Sport']].head(10))

# Count participants in each sport
sport_counts = df['Sport'].value_counts()
print(sport_counts.head())

# Count medals per team
medals_by_team = df[df['Medal'].notnull()].groupby('Team')['Medal'].count()
print(medals_by_team.sort_values(ascending=False).head())



top_female_sport = df[df['Sex'] == 'F']['Sport'].value_counts()
print(top_female_sport.head(1))

# Average height per sport
avg_height = df.groupby('Sport')['Height'].mean().sort_values(ascending=False)
print(avg_height.head())

# Median age by year
median_age_by_year = df.groupby('Year')['Age'].median()
print(median_age_by_year.tail())

# average weight by sex and sport
avg_sex_sport = df.groupby(['Sport', 'Sex'])['Weight'].mean().sort_values(ascending=False)
print(avg_sex_sport.head())

# Filter gymnasts and save to new CSV
gymnasts = df[df['Sport'] == 'Gymnastics']
gymnasts.to_csv('gymnastics_athletes.csv', index=False)

#Filter Athletes who are under 18
Athletes_under_18 = df[df['Age'] < 18]
Athletes_under_18.to_csv('Under_18_Athletes.csv', index=False)


#Filter Athletes who won a Gold Medal
Gold_athletes = df[df['Medal'] == 'Gold']
Gold_athletes.to_csv('Gold_medal_Athletes.csv', index=False)

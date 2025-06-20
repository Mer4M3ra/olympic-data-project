# ***Week 2***
## Activity 3
### Activity 1
#### Questions
1. How many columns are in the dataset?
2. Name 3 and explain what they represent?
3. what do the first 5 rows show?
#### Answers
1. Total of **15** columnns in the dataset
2. The following columns "Name, Sex, Age" represent the information about the contestant
3. the first 5 rows show the "head"
### Activity 2
#### Questions
1. What are the top 5 sports?
2. How many male vs female athletes?
#### Answers
1. The top 5 sports are Athletics, Gymnastics, Swimming, Shooting, Cycling with the numbers of 38624, 26707, 23195, 1148, 10859 respectively
2. There are 196594 Males while the Females have 74522
### Activity 3
#### Questions
1. Whats the average age?
2. whats the oldest and youngest athlete?
3. Are there any columns with missing or strange values?
#### Answers
1. The average age of the athletes is around the age of 26
2. the oldest athlete is 97 yearsc old while the youngest being 10 years old
3. Yes there are but instead they are with NA
### Extension
#### Questions
1. Research what three of the lesser known codes stand for, e.g. "URS", "GDR", "FRG"
#### Answers
1. The word URS stands for the former soviet union
2. the word GDR stands for the german democratic republic
3. the word FRG stands for the federal republic of germany
### Reflection
#### Questions
1. What’s one thing you learned about the Olympics dataset?
2. What did you find challenging in setting up or running Pandas?
3. What’s something you'd like to analyse next?
#### Answers
1. something i learned about the olympics is that people by the ages of 10 have competed in the olympics
2. i found it really challenging to actually download pandas as it would always say "pip is not a command" or something by thos words
3. in the future i would like to analyse the popularity of music
# ***Week 3***
## Task 3
### Task 1
#### Questions
1. What do these filters do
2. How many rows were returned use lens() to find out
#### Answers
1. These filters show the first 5 woman in the olympics then they show the first 5 woman above the age of 35 with the categories of "Name", "Age" and "Sport"
2. there is a total of 10 rows returned
### Task 2
#### Qustions
1. Write a filter for athletes from australia in swimming
#### Answers
1. the filter i made is "***AustraliaSwimmers = df[(df['Team'] == 'Australia') & (df['Sport'] == 'Swimming')]***"
### Task 3
#### Questions
1. Sort by height then weight and display top 10
#### Answers
1. the filter i made is "***sorted_by_weight_height_10 = df.sort_values(by=['Height', 'Weight'], ascending=False)***"
### Task 4
#### Questions
1. which sport had the most female particapants?
#### Answers
1. the filter i made is "***top_female_sport = df[df['Sex'] == 'F']['Sport'].value_counts()***"
### Task 5
#### Questions
1. Create a new group  that shows average weight by sex and sport
#### Answers
1. "***avg_sex_sport = df.groupby(['Sport', 'Sex'])['Weight'].mean().sort_values(ascending=False)***"
### Task 6
#### Questions
1. All athletes under 18
2. All athletes who won a gold medal
#### Answers
1. '***Athletes_under_18.to_csv('Under_18_Athletes.csv', index=False)***'
2. '***Gold_athletes.to_csv('Gold_medal_Athletes.csv', index=False)***'
### **📚Reflection**
#### Questions
1. What was the easiest filtering task?
2. What was the most difficult grouping or sorting task?
3. What trends surprised you in the Olympic data?
4. What kinds of real-world questions could this kind of analysis help answer?
#### Answers
1. the easiest was certainly the first task as it was sort of like the basics
2. the most difficult sorting/grouping task was task 5 as i was mostly confused on what to do
3. i was surprised that athletics had the most participants
4. it could help answer questions such as "whos the tallest or heaviest athlete"
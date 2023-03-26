# Fantasy Football Project

## Installing this requirements text will install all packages needed to run my program
## pip install -r requirements.txt. Python Version - 3.11.1

# Read in Data

## I read my data in using pd.read_csv() by importing the pandas module. I read in the first csv titled 'fantasyfootball.csv'. My goal for the project was to make a determination on what positions to priortize in a fantasy football draft so I needed to read in a second csv that would have the average draft position. This csv was 'fantasyfootballrank.csv'. I needed to merge these two datasets to be able analyze them so I used the pd.merge function in pandas.


# Manipulate and Clean Data

## I dropped several columns from my data that weren't useful to my project by using the .drop function. I also renamed columns to make this columns easier to read and more specific using the .rename function.
## I cleaned my data by taking my dataframe and breaking it down into indivual dataframes based on the position a football player plays. For example, I have individual dataframes for Quarterback (qb), Runningback(rb), Wide Reciever(wr), Tight End(te). Then, I created the function transform_columns to add the specific columns I wanted to each dataframe. 


# Analyze Data

## I want to analyze to find trends of what positions to priortize when drafting a fantasy football team. I have created function that take two data columns one usage per game and one fantasy points per game to find out how the amount of times a player gets the ball relates to the amount of fantasy points he scores.

# Interpret Your Data and Graphical Output

## So my results were as expected when I began this project, I knew there would be a regression as you got later into drafts. What I wanted to find from my data was how to prioritize the certain positions when I go into a draft. When looking at the data plots you can definitely see places late in the draft that you can find players that can bring a lot of value to your team. Looking at the tight end (TE) position, I can see that if I can get the top player at this position it can give me a significant advantage but if I miss and the player isn't the top of the position I may be in for a tough season. Looking at the data plots, I believe I should priortize the quarterback (QB) and running back (RB) positions. The value of these positions seem to significantly decrease as the draft progresses. I feel that the Wide Reciever position (WR) is a place where I can find value later and the draft. I think this will allow me to maximize the value of my team during the draft. In the second part of this class, I want to bring in more datasets from past seasons to see if I can identify trends to continue to help me find the best value in fantasy drafts. I'm looking forward to continuing this project and learning more about the trends of my data.


# Fantasy Football Project

## Installing this requirements text will install all packages needed to run my program
## pip install -r requirements.txt. Python Version - 3.11.1

# Read in Data

## I read my data in using pd.read_csv() by importing the pandas module. I read in the first csv titled 'fantasyfootball.csv'. My goal for the project was to make a determination on what positions to priortize in a fantasy football draft so I needed to read in a second csv that would have the average draft position. This csv was 'fantasyfootballrank.csv'. I needed to merge these two datasets to be able analyze them so I used the pd.merge function in pandas.


# Manipulate and Clean Data

## I dropped several columns from my data that weren't useful to my project by using the .drop function. I also renamed columns to make this columns easier to read and more specific using the .rename function.
## I cleaned my data by taking my dataframe and breaking it down into indivual dataframes based on the position a football player plays. For example, I have individual dataframes for Quarterback (qb), Runningback(rb), Wide Reciever(wr), Tight End(te). Then, I created the function transform_columns to add the specific columns I wanted to each dataframe. 


# Analyze Data

## I created a few functions to help me do this. I created a function separate_position_df to allow me to view the data according to the players football position. My project aims to determine which positions to priotize in a draft so this is necessary for the data. The next function, I create is called position_columns. This function puts only the columns that matter to each position into the position specific dataframe. This allows me to focus on only what matters for each position. The next function, I create is calculate_fantasy_points_per_game. This function creates a new column in each positional dataframe called 'FantasyPoints/GM'. This column is base on the total fantasy points scored divided by the number of games a player played. This is very important for my analysis because it is the most important statistic in fantasy football. The final function, I create is called rank_players. This function creates a column called Rank and ranks players based on their fantasy points per game. This is important because this is what the representation of my visualization is going to be.

# Interpret Your Data and Graphical Output

## So my results were as expected when I began this project, I knew there would be a regression as you got later into drafts. What I wanted to find from my data was how to prioritize the certain positions when I go into a draft. When looking at the data plots you can definitely see places late in the draft that you can find players that can bring a lot of value to your team. Looking at the tight end (TE) position, I can see that if I can get the top player at this position it can give me a significant advantage but if I miss and the player isn't the top of the position I may be in for a tough season. Looking at the ranking data vs the average draft position the TE position may be one of the trickier positions to draft because the up and down of players at this position. Looking at the data plots, quarterback (QB) is definitely a position I want to find later in the draft as there are many top finishers in the late parts of the draft. Looking at the data, I would priortize running back (RB) over Wide Reciever (WR) because there are more opportunies to get a top 20 finisher at the WR position in comparison to the RB as the draft progresses. I want to continue to develop this data into a model I can use for fantasy drafts in the future. I plan to build upon this project in the second half this course.


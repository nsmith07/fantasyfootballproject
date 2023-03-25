# Fantasy Football Project

Installing this requirements text will install all packages needed to run my program
pip install -r requirements.txt. Python Version - 3.11.1

## Read in Data
I read my data in using pd.read_csv() by importing the pandas module. I read in the first csv titled 'fantasyfootball.csv'. My goal for the project was to make a determination on what positions to priortize in a fantasy football draft so I needed to read in a second csv that would have the average draft position. This csv was 'fantasyfootballrank.csv'. I needed to merge these two datasets to be able analyze them so I used the pd.merge function in pandas.


## Manipulate and Clean Data
I dropped several columns from my data that weren't useful to my project by using the .drop function. I also renamed columns to make this columns easier to read and more specific using the .rename function.
I cleaned my data by taking my dataframe and breaking it down into indivual dataframes based on the position a football player plays. For example, I have individual dataframes for Quarterback (qb), Runningback(rb), Wide Reciever(wr), Tight End(te). Then, I created the function transform_columns to add the specific columns I wanted to each dataframe. 


## Analyze Data
I want to analyze to find trends of what positions to priortize when drafting a fantasy football team. I have created function that take two data columns one usage per game and one fantasy points per game to find out how the amount of times a player gets the ball relates to the amount of fantasy points he scores.

## Interpret Your Data and Graphical Output



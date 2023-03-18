# Fantasy Football Project

Installing this requirements text will install all packages needed to run my program
pip install -r requirements.txt

## Read in Data
I read my data in using pd.read_csv() by importing the pandas module. I read in my csv containing the fantasy football data for my project.


## Manipulate and Clean Data
I cleaned my data by taking my dataframe and breaking it down into indivual dataframes based on the position a football player plays. For example, I have individual dataframes for Quarterback (qb), Runningback(rb), Wide Reciever(wr), Tight End(te). Then, I created the function transform_columns to add the specific columns I wanted to each dataframe. 


## Analyze Data
I want to analyze to find trends of what positions to priortize when drafting a fantasy football team. I have created function that take two data columns one usage per game and one fantasy points per game to find out how the amount of times a player gets the ball relates to the amount of fantasy points he scores.

## Interpret Your Data and Graphical Output

I want to find a way to use Django or flask to create a website, or use tkinter to visulize my data.
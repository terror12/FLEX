# FLEX
========================
FLEX Project Guidelines:
========================
==================
Mission Statement:
==================

To build a web based daily fantasy football lineup generator using python3 for backend and Django fo UI.

=====================
Methodology:
=====================
Using Fanduels salary system compared with the average of the other top Fantasy prediction engines(NFL.com, Yahoo, ESPN) 
we can construct a standard deviation (STD) value for every player for the upcoming week. With this list and the code in place to generate lineups based on the players standard deviation value, we will use a community driven approach to collect data and find out which standard deviation value for each position yeilds the highest average return.

======================
Action Plan:
======================
 1. Collect database of historical data as far back as possible (3 years currently)
 2. Write python code to scrape webpages to pull down current projections week to week while in season. Save files as xmls or csvs
 3. Depending how files are stored import into Google sheets and automate how to create the STD list
 4. Build webpage that allows you to generate lineups for that weeks players.
    a. Include sliders to change the STD number that you assign for the code to pull players from
    b. Store all generated lineups and evaluate based on post week results save only lineup configuration that yeild a high result.
 5. Send link to community and advertise that using this can help them win $$$
 6. Create Facebook, Instagram, and twitter for Flexproject
 


====================
Leagacy information:
====================
Mission Statement: Build a predictive engine that will output projected best lineups for weekly entries into FanDuel.
	Methodology:  Using top projection platforms, create a standard deviation value for each player based on the average projected points for that week, and the 'FanDuel FLEX value'. With that standard deviation value we will be able to oder the list of players from min to max STD. We will do this for 4 years of past data 2015-2019. Using a python script we will create lineups picking from the top of the list. These lineups will be based off of historical data, therefore we will be able to create lineups under the maximum salary and record the actual points scored by the lineup. A python script will be needed to generate lineups using different variables to generate the ordered STD list and record the results. We will then be able to compare which STD order leads to the highest scoring lineups on an average basis. This will be the lineup that we roll out on gameday.
	
	FanDuel creates a price value for each player. We will be judging a players value by 2-1/2 times their price. This value will be compared with numerous different player ranking platforms (yahoo, espn, nfl.com etc.) The standard deviation will be found between every possibility of each platform, I will most likely be looking at the lowest positive standard deviation. 
		-The idea will be to use the projections of these experts to come up with a system to predict the best starting lineup using 100% of the salary given.
		The players with the highest positive standard deviation will be considered a must start. There will be a program in place that will produce starters by using the players considered must start while using all of the salary given.

	Data: 
		-FanDuel: 
			Rotoguru1.com
			- Holds archives of all past FanDuel player salaries. Dating back to 2011.
			- This will be used to try and identify patterns with our standard deviation model.
			-Google Sheet
				- Google sheets will be used to pull data from Rotoguru1.com to start building our database.
					- We will set up Google sheets to automatically update our database as new information comes out.
					Coding:
						R:
						-Will be using R to perform statistical analysis, and to call in all data from google sheets.
	TO DO LIST:
	•	Collect all data from Rotoguru1.com and enter into google sheets 
	•	Find data archives for all past predictions of yahoo, espn, nfl.com etc.
	•	Create R code to call in data from google sheets and perform data analytics on it
		o	Use capstone project as baseline for R code.
				Insert all data
				Group all data into data groups
				Find standard deviation for all players based on their price value compared with other engines predictions
				Build lineup
				•	Need to rank players from smallest positive STD to largest
				•	Then need to come up with formula to enter in the players starting from top to bottom using all of the salary given.
				Analyze all previous perfect lineups and find what the STD of the projections is
				•	Should be used to analyze which platforms prediction seem to be more succesful
				Create format of 1QB, 2RB, 3WR, 1TE, 1K, 1DEF as template for code to enter players into.

				•	Find the standard deviation statistics based on all past perfect lineups
				•	Create visual model to show how engines will be built
			One model will be Fanduel value compared with yahoo player rankings to find the players with the smallest positive standard deviation
		o	Next model will be Fanduel value compared with espn player rankings to find the players with the smallest positive standard deviation
		o	Another model will be all three of the combined to find that standard deviation and build a line up based on all threes projections.


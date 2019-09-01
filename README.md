FLEX Project Guidelines:
========================

Mission Statement:
==================
To openly share daily fantasy football generated lineups that result in victory atleast 51% of the time.

Methodology:
=====================
Using Fanduels salary system compared with the average of the other top Fantasy prediction engines(NFL.com, Yahoo, ESPN) 
we can construct a standard deviation (STD) value for every player for the upcoming week. With this list and the code in place to generate valid lineups based on the players standard deviation value, we will use a database of previous years actual results to evaluate the success of a lineup. Overtime the optimal STD value for each postion in a lineup will reveal itself. 

We will use a program to generate lineups along with a community driven approach to increase the number of different STD combinations that we can record. This will be accomplished by providing a website for users to control sliders and generate their own lineups, which will be recorded and combined with all other previous runs in the database.

Tickets will be tracked and assigned on the following Trello board
https://trello.com/b/k1UY8kRD/flex-project
======================

High Level Tasks:
======================
 1. Collect database of historical data as far back as possible (3 years currently)
 2. Write python script/library to scrape webpages to pull down current projections week to week while in season. Save files as XMLs or CSVs
 3. Depending how files are stored import into Google sheets and automate how to create the STD list
 4. Build webpage that allows you to generate lineups for that weeks players.
    a. Include sliders to change the STD number that you assign for the code to pull players from
    b. Store all generated lineups and evaluate based on post week results save only lineup configuration that yeild a high result.
 5. Send link to community and advertise that using this can help them win $$$
 6. Create Facebook, Instagram, and twitter for Flexproject

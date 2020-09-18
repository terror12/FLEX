#import rpy2

#wget https://download2.rstudio.org/server/centos6/x86_64/rstudio-server-rhel-1.2.5019-x86_64.rpm
#sudo yum install rstudio-server-rhel-1.2.5019-x86_64.rpm
# sudo dnf install libxml2-devel

args = commandArgs(trailingOnly=TRUE)
#install.packages("XML")
#install.packages("stringr")
# RCODE
# Import XML library to allow for the use of readHTML() function
library(stringr)
library(XML)
# Define an empty variable
y <- NULL
# For loop to call in multiple different urls.
#for(i in seq(from=0, to=400, by=40)){
#num <- as.character(i)
#ESPNa <- paste("http://games.espn.com/ffl/tools/projections?&scoringPeriodId=5&seasonId=2019&startIndex=", num, sep='')


#fd <- "http://rotoguru1.com/cgi-bin/fyday.pl?week=args[1]&year=args[2]&game=fd"
fd <- paste("http://rotoguru1.com/cgi-bin/fyday.pl?week=", args[1], "&year=", args[2], "&game=fd")
print(fd)
fd <- str_replace_all(fd, fixed(" "), "")
#fd <- str_replace_all(fd, space(), "")
#df <- str_squish(df)
print(fd)
#fd.table = readHTMLTable(fd)
fd.table = readHTMLTable(fd, header=F)
playerT <- fd.table[1]
# Convert raw url table into dataframe
playerT <- data.frame(playerT)
# Cuts down the columns into just the two we need
comp <- playerT[,c(1,4,5)]
# Removes the top row
comp <- comp[-1:-10,]
# renames the column names
names(comp)[1] <- "Player"
names(comp)[2] <- "Points"
names(comp)[3] <- "FD_Salary"
comp <- comp[!grepl("RotoGuru", comp$Player),]
comp <- comp[!grepl("Jump", comp$Player),]
comp <- comp[!grepl("Running", comp$Player),]
comp <- comp[!grepl("Wide", comp$Player),]
comp <- comp[!grepl("Tight", comp$Player),]
comp <- comp[!grepl("Kickers", comp$Player),]
comp <- comp[!grepl("Kickers", comp$Player),]
comp <- comp[!grepl("Defenses", comp$Player),]
comp <- comp[!grepl("N/A", comp$FD_Salary),]
#head(comp)
setwd("/home/ascerra/FLEX_dev/FLEX/flex/Revised_Data/FanDuel_proj/post")
write.csv(comp, file = args[3])
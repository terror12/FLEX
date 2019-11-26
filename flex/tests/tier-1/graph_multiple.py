# Executable with python ...
import pandas as pd
import os
import matplotlib.pyplot as plt

### Set your path to the folder containing the .csv files
PATH = './' # Use your path

### Fetch all files in path
fileNames = os.listdir(PATH)

### Filter file name list for files ending with .csv
fileNames = [file for file in fileNames if 'best_Lineup.csv' in file]

### Loop over all files
for file in fileNames:

    ### Read .csv file and append to list
    df = pd.read_csv(PATH + file, index_col = 0)

    ### Create line for every file
    plt.plot(df)

### Generate the plot
plt.show()

# numFiles = 4 #Number of CSV files in your directory
# separator = "," #Character that separates each value inside file
# fExtension = ".csv" #Extension of the file storing the data
#
# def MultiplePlots(xValues, allYValues):
#     'Method to plot multiple times in one figure.'
#
#     for yValues in allYValues:
#         plt.plot(list(map(int, xValues)), list( map(float, yValues) ), label = "file" + str(i))
#
#     plt.legend(loc = 'best')
#     plt.show()
#     return
#
# def GetXandYValues(coordinates):
#     'Method to get all coordinates from all CSV files.'
#     xValues = []
#     yValues = []
#     allYValues = []
#     fst = False
#     for file in coordinates:
#         for coordinate in file:
#             if (fst == False):
#                 xValues.append(coordinate[0])
#             yValues.append(coordinate[1])
#         fst = True
#         allYValues.append( yValues )
#         yValues = []
#     return xValues, allYValues
#
# def GetCoordinates( n , separator , fExtension ):
#     'Iterates through multiple CSV files and storing X values and Y values in different Lists'
#     coordinates = [] #coordinates[0] = x values --- coordinates[1] = y values
#     for i in range(n):
#         coordinates.append( FillList( ReadFile(str(i+1) + 'best_Lineup' + fExtension), separator ) )
#     return coordinates
#
# def ReadFile(path):
#     'Function to read CSV file and store file data rows in list.'
#     try:
#         fileCSV = open(path,"r") #Opens file
#         data = fileCSV.read() #Save file data in string
#         listData = data.splitlines() #Split lines so you have List of all lines in file
#         fileCSV.close() #Close file
#     finally:
#         return listData #Return list with file's rows
#
# def FillList(myList, separator):
#     'With this method you make a list containing every row from CSV file'
#     valueTemp = ""
#     listTemp = []
#     newList = []
#     for line in myList:
#         for c in line:
#             if c != separator:
#                 valueTemp += c
#             else:
#                 listTemp.append( valueTemp )
#                 valueTemp = ""
#         listTemp.append( valueTemp )
#         newList.append(listTemp[:])
#         valueTemp = ""
#         del listTemp[:]
#     return newList
#
# xValues = GetXandYValues( GetCoordinates( numFiles, separator , fExtension) )[0]
# allYValues = GetXandYValues( GetCoordinates( numFiles, separator , fExtension) )[1]
#
# MultiplePlots( xValues, allYValues )
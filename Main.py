# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 13:06:58 2023

@author: Lucas Finney
"""
import csv
import os

path = input("Enter file path (or just the name if it's in this folder): \n")
numCols = int(input("Enter the desired number of columns: \n"))

# Open the file
with open(path,'r') as f:
    data = [line.strip() for line in f] #Iterate over the lines, creating a new list element for each
    
# Group every pair
data = zip(*[iter(data)]*numCols)

# Create the CSV file
with open('output.csv','w', newline = '') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row) # Writing out the pairs in our data as a row of two columns

os.system('cls')

print("Result")
print("-------")
# Print out the "CSV" version to check if it worked
with open('output.csv','r') as f:
    lines = [line.strip() for line in f]
    for line in lines:
        print(line)

print("=====")
input("Press enter to exit")
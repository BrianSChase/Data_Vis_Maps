# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 16:47:48 2021

@author: Brian
"""
import csv

#parse the covid csv to get most recent date for data
#Create a country name and covid cases dict
#Use the country code function from World Map Vis to get
  #the code plus the covid cases
  
#Create map using code and cases dict
  
def get_covid_info(var):
    with open('owid-covid-data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line = 0
        for row in csv_reader:
            if line > 0:
                var[row[2]] = row[4] 
               # print(row[2] + ', ' + row[4]) 
            line += 1



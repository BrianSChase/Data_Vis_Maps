# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 15:31:57 2021

@author: Brian
"""
import pygal
from Covid_Map import get_covid_info
from World_map_vis import get_country_info, get_country_code, grouping



def create_population_map(): 
    """Creates world map of population"""
    
    #create dictionary with country names and population
    country_population = {}            
    get_country_info(country_population)
    
    
    #dict for country codes and population/other data
    country_codes = {}
    
    #create country code and population dictionary
    for key in country_population.keys():
        var = get_country_code(key)
        try:
            country_codes[var] = int(country_population[key])
        except:
            print("error: population section")
       
    
    
    wm = pygal.maps.world.World()
    wm.title = "World Population in 2019"
    wm.add('2019', country_codes)
    
    wm.render_to_file('world_population.svg')
    

def create_covid_map():
    """Creates World Map of covid cases """
    
    covid_data = {}
    get_covid_info(covid_data)
    
    country_codes_covid = {}
    
    #Make dictionary with country codes and covid case data
    for key in covid_data.keys():
        var = get_country_code(key)
        try:
            country_codes_covid[var] = float(covid_data[key])
        except:
            print("error: covid section")
    
    
    #create covid map
    wm = pygal.maps.world.World()
    wm.title = "Covid Cases"
    wm.add('Total Cases', country_codes_covid)
    
    wm.render_to_file('world_covid_map.svg')


def create_grouped_covid_map():
    """Creates World Map of covid cases """
    print("start of groups")
    covid_data = {}
    get_covid_info(covid_data)
    
    country_codes_covid = {}
    
    #Make dictionary with country codes and covid case data
    for key in covid_data.keys():
        var = get_country_code(key)
        try:
            country_codes_covid[var] = float(covid_data[key])
        except:
            print("error: covid section")
    print("prior to calling groups function")
    groups = grouping(country_codes_covid)
    #create covid map
    wm = pygal.maps.world.World()
    wm.title = "Covid Cases"
    wm.add('G1', groups[0])
    wm.add('G2', groups[1])
    wm.add('G3', groups[2])
    wm.add('G4', groups[3])
    wm.add('G5', groups[4])
    print("in grouping")
    wm.render_to_file('world_grouped_covid_map.svg')
  

print("start of main")
create_population_map()
create_covid_map()
print("in main, before calling func")
create_grouped_covid_map()
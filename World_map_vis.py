import csv
from pygal.maps.world import COUNTRIES
import pygal
from Covid_Map import get_covid_info
#Population Data:
#https://databank.worldbank.org/indicator/SP.POP.TOTL/1ff4a498/Popular-Indicators


#Citation for covid Data
#Hasell, J., Mathieu, E., Beltekian, D. et al.
#A cross-country database of COVID-19 testing. Sci Data 7, 345 (2020).
#https://doi.org/10.1038/s41597-020-00688-8

def get_country_info(var):
    """Get country name and population """
    with open('2019_population.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line = 0
        for row in csv_reader:
            if line < 218 and line > 0:
                var[row[2]] = row[4] 
               # print(row[2] + ', ' + row[4]) 
            line += 1



#input country name and return code
def get_country_code(var):
    """Get country codes for map """
    for code, name in COUNTRIES.items():
        if name == var:
            return code
    return None
         

def grouping(var):
    """group countries by their data"""
    g1,g2,g3,g4,g5 = {},{},{},{},{}
    for country, num in var.items():
        if num < 10000:
            g1[country] = num
        elif num < 100000:
            g2[country] = num
        elif num < 300000:
            g3[country] = num
        elif num < 500000:
            g4[country] = num
        else:
            g5[country] = num
    group_list = [g1,g2,g3,g4,g5]
    return group_list
        

########Population map

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


###########Covid map 

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
wm2 = pygal.maps.world.World()
wm2.title = "Covid Cases"
wm2.add('Total Cases', country_codes_covid)

wm2.render_to_file('world_covid_map.svg')



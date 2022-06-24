import haversine as hs
import xlrd
import random
import numpy
import math

def get_bearing(lat1, long1, lat2, long2):
    dLon = (long2 - long1)
    x = math.cos(math.radians(lat2)) * math.sin(math.radians(dLon))
    y = math.cos(math.radians(lat1)) * math.sin(math.radians(lat2)) - math.sin(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.cos(math.radians(dLon))
    brng = numpy.arctan2(x,y)
    brng = numpy.degrees(brng)

    return brng

def cardinal(bearing):
    cardinal=""
    if bearing >-22.5 and bearing <=22.5:
        cardinal="N"
    elif bearing > 22.5 and bearing <=67.5:
        cardinal="NE"
    elif bearing > 67.5 and bearing <=112.5:
        cardinal="E"
    elif bearing >112.5 and bearing <=157.5:
        cardinal="SE"
    elif bearing >-157.5 and bearing <=-112.5:
        cardinal="SW"
    elif bearing >-112.5 and bearing <=-67.5:
        cardinal="W"
    elif bearing >-67.5 and bearing <=-22.5:
        cardinal="NW"
    else:
        cardinal="S"

    return cardinal

wb = xlrd.open_workbook("centroids.xls")
sheet = wb.sheet_by_index(0)

country=random.randint(0,243)

loc1=(sheet.cell_value(country, 1),sheet.cell_value(country, 2))

guess=""

i=0
while i<6:
    guess=input("Input guess: ")
    val=-1
    for x in range(0,244):
        if sheet.cell_value(x,3).lower()==guess.lower() or sheet.cell_value(x,4).lower()==guess.lower():
            val=x
            break;
    if val==-1:
        print("Please input a country")
    else:
        i+=1
        loc2=(sheet.cell_value(val,1),sheet.cell_value(val,2))
        
        distance=hs.haversine(loc2,loc1)
        if distance==0:
            print("You win in",i,"guesses!")
            i=0
            break;
        bearing=get_bearing(loc2[0],loc2[1],loc1[0],loc1[1])

        print("Distance:",distance,"| Direction:",cardinal(bearing))
if i==6:
    print("You lost :( \nThe country was: "+str(sheet.cell_value(country,3)))
    


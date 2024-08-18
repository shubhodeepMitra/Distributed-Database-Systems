"""
    Assignment4 Interface
    Author: Shubhodeep Mitra
    ASU ID: 1225468088
"""

from pymongo import MongoClient
import os
import sys
import json
import math

def FindBusinessBasedOnCity(cityToSearch, minReviewCount, saveLocation1, collection):
    file=open(saveLocation1,'w')
    for entry in collection.find():
        if entry['city'].lower()==cityToSearch.lower() and entry['review_count']>=minReviewCount:
            file.write(entry['name'].upper()+'$'+entry['full_address'].upper()+'$'+entry['city'].upper()+'$'+entry['state'].upper()+'$'+str(entry['stars'])+'\n')
    file.close()
            

def FindBusinessBasedOnLocation(categoriesToSearch, myLocation, minDistance, maxDistance, saveLocation2, collection):
    file=open(saveLocation2,'w')
    for entry in collection.find():
        dist = Distance(entry['latitude'],entry['longitude'],myLocation)
        if dist>=minDistance and dist<=maxDistance:
            for category in categoriesToSearch:
                if category in entry['categories']:
                    file.write(entry['name'].upper()+'\n')
                    break;                   
    file.close()
    
def Distance(latitude1, longitude1,myLocation):
    latitude2=float(myLocation[0])
    longitude2=float(myLocation[1])
    R = 3959; # miles

    phi1 = math.radians(latitude1)
    phi2 = math.radians(latitude2)

    delta_omega = math.radians(latitude2-latitude1)
    delta_lambda = math.radians(longitude2-longitude1)

    a = math.sin(delta_omega / 2) * math.sin(delta_omega / 2) + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) * math.sin(delta_lambda / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = R * c
    return d
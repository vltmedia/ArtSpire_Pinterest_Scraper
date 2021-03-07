
# Scrape a Pintreset Board and write it to a csv

# python ScrapePintresetBoard.py "https://www.pinterest.com/justin_jaro/character-design/" batch board
# python ScrapePintresetBoard.py "https://www.pinterest.com/justin_jaro/character-design/" single board
# python ScrapePintresetBoard.py "https://www.pinterest.com/justin_jaro/character-design/" json E:/Apps/ArtSpire_PintrestWebscraper/python/parsefiles.json single pin
# python ScrapePintresetBoard.py "https://www.pinterest.com/justin_jaro/character-design/" csv E:/Apps/ArtSpire_PintrestWebscraper/python/parsefiles.csv single pin
# python E:/Apps/ArtSpire_PintrestWebscraper/python/ScrapePintresetBoard.py  https://www.pinterest.com/justin_jaro/character-design/ json E:/Apps/ArtSpire_PintrestWebscraper/python/parsefiles.json batch board

# python E:/Apps/ArtSpire_PintrestWebscraper/python/ScrapePintresetBoard.py  https://www.pinterest.com/justin_jaro/character-design/ E:/Apps/ArtSpire_PintrestWebscraper/python/parsefiles.csv batch board
# E:\Apps\ArtSpire_PintrestWebscraper\ScrapePintresetBoard.exe  https://www.pinterest.com/justin_jaro/character-design/ json E:/Apps/ArtSpire_PintrestWebscraper/python/parsefiles.json batch board

import sys
import csv
import json
import requests
from bs4 import BeautifulSoup
from ReadBoard import ReadURL



URL = sys.argv[1]
ExtensionMode = sys.argv[2]
OutputFile = sys.argv[3]
BatchMode = sys.argv[4]
BoardMode = sys.argv[5]

def WriteCSV():
    global OutputFile
    global BatchMode
    global BoardMode
    images = ReadURL(URL)
    csvstring = "Title , Caption , URL"
    with open(OutputFile, 'w', newline='',  encoding="utf-8") as file:
        
        writer = csv.writer(file)
        writer.writerow(["Title","Caption","URL"])

        if BatchMode == "batch":
            for image in images:
                writer.writerow([image[0],image[1],image[2]])
                newlinee = csvstring + "\n" + image[0]  + ","+ image[1] + "," + image[2]
                csvstring = newlinee
        if BatchMode == "single":
            
            randimage = images[randrange(0, len(images) - 1, 1)] 
            writer.writerow([randimage[0],randimage[1],randimage[2]])
            newlinee = csvstring + "\n" + randimage[0]  + ","+ randimage[1] + "," + randimage[2]
            csvstring = newlinee
            
    return csvstring
    
    
def WriteJSON():
    global OutputFile
    global BatchMode
    global BoardMode
    
    images = ReadURL(URL)
    jsonlist = {"Pins":[]}
    pins = []
        

    if BatchMode == "batch":
        for image in images:
            pins.append({"Title":image[0],"Caption":image[2],"URL":image[2] })
    if BatchMode == "single":
        
        randimage = images[randrange(0, len(images) - 1, 1)] 
        pins.append({"Title":randimage[0],"Caption":randimage[2],"URL":randimage[2] })
    
    jss = json.dumps({"Pins": pins})

    with open(OutputFile, 'w',  encoding="utf-8") as file:
        file.write(jss)
    
    return {"Pins": pins}
    
    

outputtext = ""
if ExtensionMode == "csv":
    outputtext = WriteCSV()

if ExtensionMode == "json":
    outputtext = WriteJSON()

        
        


print(outputtext)
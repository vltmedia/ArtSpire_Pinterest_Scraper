
# python E:\Apps\ArtSpire_PinterestWebscraper\python\ScrapePinterestSelenium.py  https://www.pinterest.com/justin_jaro/character-design/ 3 E:/Apps/ArtSpire_PinterestWebscraper/python/parsefiles.json batch board E:\Apps\ArtSpire_PinterestWebscraper\chromedriver88.exe
# E:\Apps\ArtSpire_PinterestWebscraper\ScrapePinterestSelenium.exe  https://www.pinterest.com/justin_jaro/character-design/ 3 E:/Apps/ArtSpire_PinterestWebscraper/python/parsefiles.json batch board E:\Apps\ArtSpire_PinterestWebscraper\chromedriver88.exe
# E:\Apps\ArtSpire_PinterestWebscraper\ScrapePinterestSelenium.exe  https://www.pinterest.com/justin_jaro/character-design/ 3 E:/Apps/ArtSpire_PinterestWebscraper/python/parsefiles.json batch board E:\Apps\ArtSpire_PinterestWebscraper\chromedriver88.exe


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import json
import time


import sys
import csv
import json
import requests



URL = sys.argv[1]
ScrollCount = int(sys.argv[2])
OutputFile = sys.argv[3]
BatchMode = sys.argv[4]
BoardMode = sys.argv[5]
ChromeDriverLocation = sys.argv[6]

if BoardMode == "search":
    newurl = "https://www.pinterest.com/search/pins/?q=" + URL.replace(" ", "%20")
    URL = newurl
# print(ChromeDriverLocation)

def scroll_to_bottom(driver, max):

    old_position = 0
    new_position = None
    count = 0
    while new_position != old_position:
        nextc = count + 1
        count = nextc
        # print("scroll_to_bottom | " + str(count) )
        
        # Get old scroll position
        old_position = driver.execute_script(
            ("return (window.pageYOffset !== undefined) ?"
                " window.pageYOffset : (document.documentElement ||"
                " document.body.parentNode || document.body);"))
        # Sleep and Scroll
        time.sleep(1)
        driver.execute_script((
                "var scrollingElement = (document.scrollingElement ||"
                " document.body);scrollingElement.scrollTop ="
                " scrollingElement.scrollHeight;"))
        # Get new position
        new_position = driver.execute_script(
            ("return (window.pageYOffset !== undefined) ?"
                " window.pageYOffset : (document.documentElement ||"
                " document.body.parentNode || document.body);"))
        if count >= max:
            new_position = old_position
    
def WriteJSON(jsonn):
    

    with open(OutputFile, 'w',  encoding="utf-8") as file:
        file.write(jsonn)
    
URL = URL

def ReadBoard():

    # instantiate a chrome options object so you can set the size and headless preference
    chrome_options = Options()
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")

    # download the chrome driver from https://sites.google.com/a/chromium.org/chromedriver/downloads and put it in the
    # current directory
    chrome_driver = ChromeDriverLocation
    # chrome_driver = os.getcwd() +"\\chromedriver88.exe"

    # go to Google and click the I'm Feeling Lucky button
    driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver)
    driver.get(URL)

    # print("``````````````````````````````````````````````````````````````````````")
    # print("``````````````````````````````````````````````````````````````````````")
    # print("scroll_to_bottom Starting")
    scroll_to_bottom(driver, ScrollCount)
    # print("scroll_to_bottom Ending")

    # print("``````````````````````````````````````````````````````````````````````")
    # print("``````````````````````````````````````````````````````````````````````")
    # print("      ")
    # lucky_button = driver.find_element_by_css_selector("[class=GrowthUnauthPinImage]")
    collections =  driver.find_elements_by_css_selector("div.Collection")
    jsonn = {"Pins" : []}
    pinss = []
    for coll in collections:
        

        # linkss =  driver.find_elements_by_css_selector("div.GrowthUnauthPinImage a")
        linkss =  coll.find_elements_by_css_selector("div.GrowthUnauthPinImage a")
        # linkss =  driver.find_elements_by_css_selector("div.GrowthUnauthPinImage a img")
        # imagess = driver.find_elements_by_class_name("GrowthUnauthPinImage")

        
        # print("``````````````````````````````````````````````````````````````````````")
        # print("``````````````````````````````````````````````````````````````````````")
        # print("Links count | " + str(len(linkss)))
        # print("collections count | " + str(len(collections)))

        for element in linkss:
            js = {"Title":element.get_attribute("title").encode('utf-8').decode('ascii', 'ignore')}
            ments = element.find_elements_by_css_selector("img")
            # print(js)
            for ment in ments:
                caption = ment.get_attribute("alt").encode('utf-8').decode('ascii', 'ignore')
                src = ment.get_attribute("src").encode('utf-8').decode('ascii', 'ignore')
                js = {"Title":element.get_attribute("title").encode('utf-8').decode('ascii', 'ignore'), "Caption": caption,"URL": src }
            jsonn["Pins"].append(js)
            # print(element.get_attribute("title") + "  |  " + element.get_attribute("src"))

    # print("``````````````````````````````````````````````````````````````````````")
    # print("``````````````````````````````````````````````````````````````````````")
    # print("      ")
    WriteJSON(json.dumps(jsonn))

    # print("Wrote JSON")
    # print("``````````````````````````````````````````````````````````````````````")

    driver.close()
    print(json.dumps(jsonn))


if __name__ == '__main__':
    ReadBoard()

# python E:\Apps\ArtSpire_PinterestWebscraper\python\ScrapePinterestSelenium.py  https://www.pinterest.com/justin_jaro/character-design/ 3 E:/Apps/ArtSpire_PinterestWebscraper/python/parsefiles.json batch board E:\Apps\ArtSpire_PinterestWebscraper\chromedriver88.exe
# E:\Apps\ArtSpire_PinterestWebscraper\ScrapePinterestSelenium.exe  https://www.pinterest.com/justin_jaro/character-design/ 3 E:/Apps/ArtSpire_PinterestWebscraper/python/parsefiles.json batch board E:\Apps\ArtSpire_PinterestWebscraper\chromedriver88.exe
# E:\Apps\ArtSpire_PinterestWebscraper\ScrapePinterestSelenium.exe  https://www.pinterest.com/justin_jaro/character-design/ 3 E:/Apps/ArtSpire_PinterestWebscraper/python/parsefiles.json batch board E:\Apps\ArtSpire_PinterestWebscraper\chromedriver88.exe

# python E:\Apps\ArtSpire_PinterestWebscraper\python\ScrapePinterestSelenium.py https://www.pinterest.com/pin/384776361909475578/ 3 E:/Apps/ArtSpire_PinterestWebscraper/python/parsefilespin.json batch pin E:\Apps\ArtSpire_PinterestWebscraper\chromedriver88.exe

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import json
import time
# importing required modules
import urllib.request

import sys
import csv
import json
import requests
from bs4 import BeautifulSoup
import random
import string
from urllib.parse import urlparse

# printing lowercase
letters = string.ascii_lowercase


URL = sys.argv[1]
ScrollCount = int(sys.argv[2])
OutputFile = sys.argv[3]
BatchMode = sys.argv[4]
BoardMode = sys.argv[5]
ChromeDriverLocation = sys.argv[6]
ImageOutputPath = "tempsave"
if BoardMode == "highresdump":
    ImageOutputPath = sys.argv[7]
    

if BoardMode == "search":
    newurl = "https://www.pinterest.com/search/pins/?q=" + URL.replace(" ", "%20")
    URL = newurl
# print(ChromeDriverLocation)
def SaveImageFromURL(url):
    a = urlparse(url)
    print(a.path)                    # Output: /kyle/09-09-201315-47-571378756077.jpg
    print(os.path.basename(a.path))
        # setting filename and image URL
    randomstring = ''.join(random.choice(letters) for i in range(10)) + ".jpg"
        
    filename = ImageOutputPath + '/' + os.path.basename(a.path)
    if os.path.exists(ImageOutputPath) == False:
        os.makedirs(ImageOutputPath)
    if os.path.exists(filename) == True:
        os.remove(filename)
    print(filename)
    image_url = url
    try:
    # calling urlretrieve function to get resource
        urllib.request.urlretrieve(image_url, filename)
    except :
        print("FAILED READING URL! | " + url)
    # if os.path.exists(filename) == True:
    #     print("Skipping already existing downloaded image! | " + filename )
    
    
def CheckFileDownloaded(url):
    a = urlparse(url)
    print(a.path)                    # Output: /kyle/09-09-201315-47-571378756077.jpg
    print(os.path.basename(a.path))
        # setting filename and image URL
    randomstring = ''.join(random.choice(letters) for i in range(10)) + ".jpg"
        
    filename = ImageOutputPath + '/' + os.path.basename(a.path)
    return os.path.exists(filename)
    
    
def scroll_to_bottom(driver, max):

    old_position = 0
    new_position = None
    count = 0
    while new_position != old_position:
        nextc = count + 1
        count = nextc
        print("Scrolling to Load More Info | " + str(round(100 *(count/max))) + "%" )
        
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
    # python E:\Apps\ArtSpire_PinterestWebscraper\python\ScrapePinterestSelenium.py https://www.pinterest.com/justin_jaro/character-design/ 3 E:/Apps/ArtSpire_PinterestWebscraper/python/parsefiledump.json batch board E:\Apps\ArtSpire_PinterestWebscraper\chromedriver88.exe

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
    jsonn = {"Pins" : [], "URL":URL, "ScrollCount": ScrollCount, "BatchMode": BatchMode}
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
    
        count = 0
        for element in linkss:
            newcount = count + 1
            count = newcount
            js = {"Title":element.get_attribute("title").encode('utf-8').decode('ascii', 'ignore'), "PinLink": "https://www.pinterest.com/"+element.get_attribute("href").encode('utf-8').decode('ascii', 'ignore')}
            ments = element.find_elements_by_css_selector("img")
            # print(js)
            for ment in ments:
                print("Parsing found elements | "+ str(count) +"/"+ str(len(linkss)) +" | " + str(round(100 *(count/len(linkss)))) + "%" )
                
                caption = ment.get_attribute("alt").encode('utf-8').decode('ascii', 'ignore')
                src = ment.get_attribute("src").encode('utf-8').decode('ascii', 'ignore')
                
                js = {"Title":element.get_attribute("title").encode('utf-8').decode('ascii', 'ignore'), "Caption": caption,"URL": src , "PinLink": element.get_attribute("href").encode('utf-8').decode('ascii', 'ignore') }
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


def ReadPin():
    print("Scraping Pin Info Please Wait... | 5%")
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
    print("Scraping Pin Info Please Wait... | 25%")
    # print("``````````````````````````````````````````````````````````````````````")
    # print("``````````````````````````````````````````````````````````````````````")
    # print("scroll_to_bottom Starting")
    # scroll_to_bottom(driver, ScrollCount)
    # print("scroll_to_bottom Ending")

    # print("``````````````````````````````````````````````````````````````````````")
    # print("``````````````````````````````````````````````````````````````````````")
    # print("      ")
    # lucky_button = driver.find_element_by_css_selector("[class=GrowthUnauthPinImage]")
    collections =  driver.find_elements_by_css_selector("[data-test-id=pin-closeup-image]")
    ments = collections[0].find_elements_by_css_selector("img")
    jsonn = {"URL":URL, "ScrollCount": ScrollCount, "BatchMode": BatchMode}
    pinss = []
    imgsrc = ments[0].get_attribute("src").encode('utf-8').decode('ascii', 'ignore')
    jsonn["Source"] = imgsrc
    print("Scraping Pin Info Please Wait... | 80%")
    
    # print("`````````````````````````````1`````````````````````````````")
    # print(len(collections))
    # print(imgsrc)
    # print("`````````````````````````````2`````````````````````````````")
    
    # for coll in collections:
        
    #     print("1")
        # linkss =  driver.find_elements_by_css_selector("div.GrowthUnauthPinImage a")
        # linkss =  coll.find_elements_by_css_selector("div.GrowthUnauthPinImage a")
        # linkss =  driver.find_elements_by_css_selector("div.GrowthUnauthPinImage a img")
        # imagess = driver.find_elements_by_class_name("GrowthUnauthPinImage")

        
        # print("``````````````````````````````````````````````````````````````````````")
        # print("``````````````````````````````````````````````````````````````````````")
        # print("Links count | " + str(len(linkss)))
        # print("collections count | " + str(len(collections)))
    
    #     count = 0
    #     for element in linkss:
    #         newcount = count + 1
    #         count = newcount
    #         js = {"Title":element.get_attribute("title").encode('utf-8').decode('ascii', 'ignore'), "PinLink": "https://www.pinterest.com/"+element.get_attribute("href").encode('utf-8').decode('ascii', 'ignore')}
    #         ments = element.find_elements_by_css_selector("img")
    #         # print(js)
    #         for ment in ments:
    #             print("Parsing found elements | "+ str(count) +"/"+ str(len(linkss)) +" | " + str(round(100 *(count/len(linkss)))) + "%" )
                
    #             caption = ment.get_attribute("alt").encode('utf-8').decode('ascii', 'ignore')
    #             src = ment.get_attribute("src").encode('utf-8').decode('ascii', 'ignore')
    #             js = {"Title":element.get_attribute("title").encode('utf-8').decode('ascii', 'ignore'), "Caption": caption,"URL": src , "PinLink": "https://www.pinterest.com/"+element.get_attribute("href").encode('utf-8').decode('ascii', 'ignore') }
    #         jsonn["Pins"].append(js)
    #         # print(element.get_attribute("title") + "  |  " + element.get_attribute("src"))

    # # print("``````````````````````````````````````````````````````````````````````")
    # # print("``````````````````````````````````````````````````````````````````````")
    # # print("      ")
    WriteJSON(json.dumps(jsonn))
    print("Scraping Pin Info Please Wait... | 90%")

    # # print("Wrote JSON")
    # # print("``````````````````````````````````````````````````````````````````````")

    driver.close()
    print(json.dumps(jsonn))
    print("Scraping Pin Info Please Wait... | 100%")


def ReadPinReturn(url):
    print("Scraping Pin Info Please Wait... | 5%")
    print(url["PinLink"])
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
    driver.get(url["PinLink"])
    print("Scraping Highres Pin Info Please Wait... | 25%")
    # print("``````````````````````````````````````````````````````````````````````")
    # print("``````````````````````````````````````````````````````````````````````")
    # print("scroll_to_bottom Starting")
    # scroll_to_bottom(driver, ScrollCount)
    # print("scroll_to_bottom Ending")

    # print("``````````````````````````````````````````````````````````````````````")
    # print("``````````````````````````````````````````````````````````````````````")
    # print("      ")
    # lucky_button = driver.find_element_by_css_selector("[class=GrowthUnauthPinImage]")
    collections =  driver.find_elements_by_css_selector("[data-test-id=pin-closeup-image]")
    try:
        ments = collections[0].find_elements_by_css_selector("img")
        jsonn = {"URL":URL, "ScrollCount": ScrollCount, "BatchMode": BatchMode}
        pinss = []
        imgsrc = ments[0].get_attribute("src").encode('utf-8').decode('ascii', 'ignore')
        jsonn["Source"] = imgsrc
        jsonn["Title"] = url["Title"]
        jsonn["Caption"] = url["Caption"]
        jsonn["URL"] = url["URL"]
        print("Scraping Highres Pin Info Please Wait... | 80%")
        
        # print("`````````````````````````````1`````````````````````````````")
        # print(len(collections))
        # print(imgsrc)
        # print("`````````````````````````````2`````````````````````````````")
        
        # for coll in collections:
            
        #     print("1")
            # linkss =  driver.find_elements_by_css_selector("div.GrowthUnauthPinImage a")
            # linkss =  coll.find_elements_by_css_selector("div.GrowthUnauthPinImage a")
            # linkss =  driver.find_elements_by_css_selector("div.GrowthUnauthPinImage a img")
            # imagess = driver.find_elements_by_class_name("GrowthUnauthPinImage")
            # imagess = driver.find_elements_by_class_name("StoryPinSlide__pageContainer")

            
            # print("``````````````````````````````````````````````````````````````````````")
            # print("``````````````````````````````````````````````````````````````````````")
            # print("Links count | " + str(len(linkss)))
            # print("collections count | " + str(len(collections)))
        
        #     count = 0
        #     for element in linkss:
        #         newcount = count + 1
        #         count = newcount
        #         js = {"Title":element.get_attribute("title").encode('utf-8').decode('ascii', 'ignore'), "PinLink": "https://www.pinterest.com/"+element.get_attribute("href").encode('utf-8').decode('ascii', 'ignore')}
        #         ments = element.find_elements_by_css_selector("img")
        #         # print(js)
        #         for ment in ments:
        #             print("Parsing found elements | "+ str(count) +"/"+ str(len(linkss)) +" | " + str(round(100 *(count/len(linkss)))) + "%" )
                    
        #             caption = ment.get_attribute("alt").encode('utf-8').decode('ascii', 'ignore')
        #             src = ment.get_attribute("src").encode('utf-8').decode('ascii', 'ignore')
        #             js = {"Title":element.get_attribute("title").encode('utf-8').decode('ascii', 'ignore'), "Caption": caption,"URL": src , "PinLink": "https://www.pinterest.com/"+element.get_attribute("href").encode('utf-8').decode('ascii', 'ignore') }
        #         jsonn["Pins"].append(js)
        #         # print(element.get_attribute("title") + "  |  " + element.get_attribute("src"))

        # # print("``````````````````````````````````````````````````````````````````````")
        # # print("``````````````````````````````````````````````````````````````````````")
        # # print("      ")
        # WriteJSON(json.dumps(jsonn))
        print("Scraping Highres Pin Info Please Wait... | 90%")

        # # print("Wrote JSON")
        # # print("``````````````````````````````````````````````````````````````````````")

        driver.close()
        # print(json.dumps(jsonn))
        print("Scraping Pin Info Please Wait... | 100%")
        return jsonn
    except :
        
        try:
            containerr = driver.find_elements_by_class_name("StoryPinSlide__pageContainer")
            ments = containerr[0].find_elements_by_css_selector("img")
            imgsrc = ments[0].get_attribute("src").encode('utf-8').decode('ascii', 'ignore')
            
            jsonn = {"URL":URL, "ScrollCount": ScrollCount, "BatchMode": BatchMode}
            pinss = []
            jsonn["Source"] = imgsrc
            jsonn["Title"] = url["Title"]
            jsonn["Caption"] = url["Caption"]
            jsonn["URL"] = url["URL"]
            jsonn["PinLink"] = url["PinLink"]
            return jsonn
        except :
            print("Failed to Find Image in Pin | " + url["PinLink"] + " | It may be a video ")
            jsonn = {"URL":URL, "ScrollCount": ScrollCount, "BatchMode": BatchMode}
            pinss = []
            
            jsonn["Source"] = "None"
            jsonn["Title"] = url["Title"]
            jsonn["Caption"] = url["Caption"]
            jsonn["URL"] = url["URL"]
            jsonn["PinLink"] = url["PinLink"]
            return jsonn    
        
        
        
        


def HighResDump():
    # python E:\Apps\ArtSpire_PinterestWebscraper\python\ScrapePinterestSelenium.py "E:\Apps\ArtSpire_PinterestWebscraper\parsefiledump.json" 3 E:/Apps/ArtSpire_PinterestWebscraper/parsefilebirdhighres.json batch highresdump E:\Apps\ArtSpire_PinterestWebscraper\chromedriver88.exe E:\Apps\ArtSpire_PinterestWebscraper\temp\HR1
    # E:\Apps\ArtSpire_PinterestWebscraper\ScrapePinterestSelenium.exe "E:\Apps\ArtSpire_PinterestWebscraper\parsefiledump.json" 3 E:/Apps/ArtSpire_PinterestWebscraper/parsefilebirdhighres.json batch highresdump E:\Apps\ArtSpire_PinterestWebscraper\chromedriver88.exe E:\Apps\ArtSpire_PinterestWebscraper\temp\HR1
    # "C:\Users\Justin Jaro\output\ScrapePinterestSelenium.exe" "E:\Apps\ArtSpire_PinterestWebscraper\parsefiledump.json" 3 E:\Apps\ArtSpire_PinterestWebscraper\chromedriver88.exe E:\Apps\ArtSpire_PinterestWebscraper\temp\HR1/parsefilebirdhighres.json batch highresdump E:\Apps\ArtSpire_PinterestWebscraper\chromedriver88.exe E:\Apps\ArtSpire_PinterestWebscraper\temp\HR1
    print("1")
    
    data = {"Pins":[]}
    jsonn = {"Pins" : [], "URL":URL, "ScrollCount": ScrollCount, "BatchMode": BatchMode}
    count = 0
    # maxx = 4
    print("2")
    
    with open(URL) as f:
        data = json.load(f)
        
        maxx = len(data["Pins"]) - 1
        if maxx != 0:
            
            print("3")
            
            for pin in range (0 , maxx):
                perc = str(round(100 *((pin + 1) /maxx))) + "%"
                print("```````````````````````````````````````````````````````")
                print("```````````````````````````````````````````````````````")
                print("Getting Highres Image | " + str(pin)+"/" + str(maxx) + " | " + perc)
                print("```````````````````````````````````````````````````````")
                print("```````````````````````````````````````````````````````")
                hrpin = ReadPinReturn(data["Pins"][pin])
                jsonn["Pins"].append(hrpin)
                
                print("--------------------------------------")
                print("--------------------------------------")
                print("Saving Highres Image | " + str(pin)+"/" + str(maxx) + " | " + perc)
                print("hrpin[Source] | " + hrpin["Source"])
                print("data[Pins][pin] | " + data["Pins"][pin]["PinLink"])
                print("--------------------------------------")
                print("--------------------------------------")
                SaveImageFromURL(hrpin["Source"])
        else:
            pin = 0
            perc =  "90%"
            print("```````````````````````````````````````````````````````")
            print("```````````````````````````````````````````````````````")
            print("Getting Highres Image | " + str(pin)+"/" + str(maxx) + " | " + perc)
            print("```````````````````````````````````````````````````````")
            print("```````````````````````````````````````````````````````")
            hrpin = ReadPinReturn(data["Pins"][pin])
            jsonn["Pins"].append(hrpin)
            
            print("--------------------------------------")
            print("--------------------------------------")
            print("Saving Highres Image | " + str(pin)+"/" + str(maxx) + " | " + perc)
            print("hrpin[Source] | " + hrpin["Source"])
            print("data[Pins][pin] | " + data["Pins"][pin]["PinLink"])
            print("--------------------------------------")
            print("--------------------------------------")
            SaveImageFromURL(hrpin["Source"])
    WriteJSON(json.dumps(jsonn))
        
    # WriteJSON(json.dumps(jsonn))

        # print(pin["PinLink"])

if __name__ == '__main__':
    print(BoardMode)
    if BoardMode == "pin":
        ReadPin()
    if BoardMode == "board":
        ReadBoard()
    if BoardMode == "highresdump":
        HighResDump()
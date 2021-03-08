import requests
from bs4 import BeautifulSoup


def __if_number_get_string(number):
    converted_str = number
    if isinstance(number, int) or \
            isinstance(number, float):
        converted_str = str(number)
    return converted_str
def get_unicode(strOrUnicode, encoding='utf-8'):
    strOrUnicode = __if_number_get_string(strOrUnicode)
    if isinstance(strOrUnicode, unicode):
        return strOrUnicode
    return unicode(strOrUnicode, encoding, errors='ignore')


def get_string(strOrUnicode, encoding='utf-8'):
    strOrUnicode = __if_number_get_string(strOrUnicode)
    if isinstance(strOrUnicode, str):
        return strOrUnicode.encode(encoding)
    return strOrUnicode
def CleanText(textt):
    inStr = textt
    try:
        return str(inStr)
    except:
        pass
    outStr = ""
    for i in inStr:
        try:
            outStr = outStr + str(i)
        except:
            if unicodeToAsciiMap.has_key(i):
                outStr = outStr + unicodeToAsciiMap[i]
            else:
                outStr = outStr + "_"
    return outStr



def ReadURL(url):
    # URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
    # URL = 'https://www.pinterest.com/justin_jaro/character-design/'

    page = requests.get(url)
    # soup = BeautifulSoup(page.content, 'html.parser')
    # soup = BeautifulSoup(page.content, 'html.parser')
    soup = BeautifulSoup(page.content, 'lxml')
    # results = soup.find_all(class_='Collection')
    # images = soup.findAll("img", {"class": "GrowthUnauthPinImage__Image"})  
    # titleinfo = soup.findAll("h1", {"data-test-id": "UnauthBestPinCardTitle"})  
    results = soup.find_all('div', class_='Hvp Jea MtH sLG zI7 iyn Hsu')
    # titleinfo = soup.findAll("div",attrs={"class":"Hvp Jea MtH sLG zI7 iyn Hsu"})
    div = soup.select('div.iyn')

    # titleinfo = soup.prettify().encode('utf-8').decode('ascii', 'ignore')
    # titleinfo = soup.select('[data-test-id="UnauthBestPinCardTitle"]')
    imagesb = soup.find("div", {"data-test-id": "pin-closeup-image"})  
    imagess = []
    imageinfo = {}
    print(imagesb)
    for image in imagesb:
        newimagee = []
        imagesc = image.findAll("a")
        imagesource = image.find("img" )
        imageinfo = {"Url",imagesource["src"].encode('utf-8').decode('ascii', 'ignore'),
                    "Caption",imagesource["alt"].encode('utf-8').decode('ascii', 'ignore'),
                    
                    }
        newimagee.append(imagesc[0]["title"].encode('utf-8').decode('ascii', 'ignore'))
        newimagee.append(imagesource[0]["alt"].encode('utf-8').decode('ascii', 'ignore'))
        newimagee.append(imagesource[0]["src"].encode('utf-8').decode('ascii', 'ignore'))
        imagess.append(newimagee)
        
    print(imageinfo)
    # print(str(get_string(imagess[0][0]), 'UTF-8'))
    # print(str(get_string(imagess[0][1]), 'UTF-8'))
    # print(str(get_string(imagess[0][2]), 'UTF-8'))

    # print(imagess[0][0].encode('ascii', 'ignore'))
    # results = soup.find_all('img', class_='.GrowthUnauthPinImage__Image')
    # results = soup.find_all('img', class_='.GrowthUnauthPinImage__Image')
    # print(results)
    return imagess

        
if __name__ == '__main__':
    print("Read Board is Main")
    ReadURL('https://www.pinterest.com/pin/384776361909475578/')
# job_elems = results.find_all('section', class_='card-content')


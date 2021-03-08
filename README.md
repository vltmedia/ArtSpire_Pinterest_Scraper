

# ARTSPIRE - Pinterest Webscraper

## Introduction
*This is for ScrapePinterestSelenium.exe and ScrapePinterestSelenium.py. Use the other Readme for ScrapePinterestBoard.exe.*

Scrape the first 16 pins from a  Pinterest board along with all the images in the More Like section depending on how may scrolls are done (lazy loading images with Pinterest). The Program will then output to a JSON for later use in another program.

The program will return a JSON string along with writing a new file at the path the user specifies.

## Setup
1. Download a [Chrome Driver](https://chromedriver.chromium.org/downloads) that matches your current Chrome Version. MAKE SURE THEY MATCH!
2. Save it to the same directory in wherever ``ScrapePinterestSelenium.exe`` is located.



## Front End Usage

1. Move the Chrome driver into ``ArtSpire_Data`` 
2. In the Top left field, set a **Search Term** or a **Pinterest URL** then it Search.
3. You will need to wait a bit while the site is scraped for your results.
4. Select the pins you wish to preview when loaded.
- Download any singular pins you want either in lowres or highres. Click the **Save** button to bring up the *Save Info* menu in which you can set the **HighRes Toggle**.
- User can also download either **ALL THE PINS** or **ALL THE PAGE PINS** (Currently viewed pins) to files. 
- You can save your cached results to a json filein the *Save Info* menu.

![Regular Search](https://github.com/vltmedia/ArtSpire_Pinterest_Scraper/raw/master/images/ArtSpire_v0122_01.png)

![Save Info](https://github.com/vltmedia/ArtSpire_Pinterest_Scraper/raw/master/images/ArtSpire_v0122_02.png)

![URL Input](https://github.com/vltmedia/ArtSpire_Pinterest_Scraper/raw/master/images/ArtSpire_v0122_03.png)

![Load Cache](https://github.com/vltmedia/ArtSpire_Pinterest_Scraper/raw/master/images/ArtSpire_v0123_04.png)



## Command Line Usage

#### Template:
```bash
  ScrapePinterestSelenium.exe [PINTEREST_BOARD_URL] [OUTPUT_TYPE] [OUTPUT_PATH] [BATCHTYPE] [PIN_OR_BOARD_OR_SEARCH] [CHROMEDRIVER_PATH]
```

| Argument ID | Key                    | Description                                                  | Examples                                                     |
| ----------- | ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1           | PINTEREST_BOARD_URL    | The Pinterest URL or Search term  (Enclose in quotes for spaces) | *https://www.pinterest.com/justin_jaro/character-design/*  OR <u>"Character Design"</u> |
| 2           | OUTPUT_TYPE            | Sets the output type.                                        | json                                                         |
| 3           | OUTPUT_PATH            | Sets the output path for the formatted json file.            | <u>C:/PinterestScraper/parsedfiles.json</u>                  |
| 4           | BATCHTYPE              | Sets the batch type. Currently only batch.                   | <u>batch</u>                                                 |
| 5           | PIN_OR_BOARD_OR_SEARCH | Sets the url type. Pin, board url or a single search term enclosed in quotes | <u>pin</u> OR <u>board</u> OR <u>search</u>                  |
| 6           | CHROMEDRIVER_PATH      | The Chrome driver path you downloaded earlier.               | *C:/PinterestScraper/chromedriver88.exe*                     |



#### Board Template:

```bash
  ScrapePinterestSelenium.exe https://www.pinterest.com/justin_jaro/character-design/ json E:/Apps/ArtSpire_PinterestWebscraper/python/parsefiles.json batch board E:/Apps/ArtSpire_PinterestWebscraper/chromedriver88.exe
```



#### Search Template:

```bash
  ScrapePinterestSelenium.exe hcharacter design json E:/Apps/ArtSpire_PinterestWebscraper/python/parsefiles.json batch search E:/Apps/ArtSpire_PinterestWebscraper/chromedriver88.exe
```



## Roadmap

- Cleanup Cards UI
- Parse Instagram also
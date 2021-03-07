# ARTSPIRE - Pintrest Webscraper
## Introduction
*This app only grabs the first 16 pins in a board, use ScrapePinterestSelenium.exe isntead for more pins and a search function*
Scrape a Pintreset board for it's pins and output to a CSV or JSON for later use in another program.

The program will return either a CSV or JSON string along with writing a new file out as ``parsefiles.json`` or ``parsefiles.csv``.

## Usage
#### Template:
- ```bash
  ScrapePintrestBoard.exe [PINTRESET_BOARD_URL] [OUTPUT_TYPE] [OUTPUT__PATH] [BATCHTYPE] [PIN_OR_BOARD]
  ```
  
#### JSON Output:

- ```bash
  ScrapePintrestBoard.exe https://www.pinterest.com/justin_jaro/character-design/ json E:/Apps/ArtSpire_PinterestWebscraper/python/parsefiles.json batch board
  ```
  
#### CSV Output:

- ```bash
  ScrapePintrestBoard.exe https://www.pinterest.com/justin_jaro/character-design/ csv E:/Apps/ArtSpire_PinterestWebscraper/python/parsefiles.csv batch board
  ```


[myBotsTable.csv](https://github.com/user-attachments/files/19922835/myBotsTable.csv)# CAI-Bot-Data-Scraper
This repository contains a Python script that scrapes public profile data from Character.AI bots and saves it to a CSV file for easy analysis or record-keeping.

🔍 Features:
Scrapes key details from a bot's profile:

- Name

- Tagline

- Number of likes

- Number of chats

Outputs the data into a structured .csv file.

Easy to configure and extend for batch scraping or additional metadata.

## Installation

Download the 'botPorfileScraper.py' file and in the terminal install the requirements.

```bash
pip install -r requirements.txt
```
## Usage
Run the commands inside the program repository (the location where you have the 'py' file) and enter the link and the name you want to give your csv file.
```bash
python botPorfileScraper.py  
```
##Example
```bash
>> python botPorfileScraper.py
Enter the porfile link:https://character.ai/profile/AlbertCamusLover
Enter the filename:myBotsTable
```
Inside the same folder where the script is, the myBotsTable.csv is.
| character  | tag | chats  | likes |
| ------------- | ------------- |
| Jenson Button  |The night going a little too far  |3,994 | 6  |
| Sebastian Vettel  | """Oh No, I'm Falling in Love Again"""  |2575| 8|
...

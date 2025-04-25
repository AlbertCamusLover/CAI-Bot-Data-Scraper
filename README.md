# CAI-Bot-Data-Scraper
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
Run the commands inside the program repository (the location where you have the 'py' file).
```bash
python botPorfileScraper.py writeBotRecordCSV porfileURL filename  
```
Example:
```bash
python botPorfileScraper.py writeBotRecordCSV https://character.ai/profile/AlbertCamusLover myBots
```

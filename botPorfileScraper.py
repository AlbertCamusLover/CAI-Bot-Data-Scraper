import requests
from bs4 import BeautifulSoup
import csv
import regex


def goodFormat(text):
    # Pattern matches emojis and the pipe character |
    pattern = regex.compile(r'[\p{Emoji_Presentation}\p{Emoji}\u200d\uFE0F|]', flags=regex.UNICODE)
    return (pattern.sub('', text)).strip()

def getRowsandFields(URL):
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser')

    # Gets all the character class
    characters = soup.find_all(class_="flex w-full flex-row gap-3 items-center text-md relative")
    
    chatsLikes = []
    rows = []
    like = 0
    chats = 0
    
    # Scrapes each element inside each character class
    for character in characters:
        
        chatsLikes = character.find_all(class_="text-sm sm:text-md whitespace-nowrap")
        
        likesDone = 0

        try:
            
            chats = (chatsLikes[0].string)
            if chats[-1] == "s" or chats[-1] == "e":
                like = chats.split()[0]
                chats=0
                likesDone = 1
        except:
            chats = 0

        try:
            if likesDone == 0:
                like = (chatsLikes[1].string).split()[0]
        except:
            like = 0


        rows.append([character.find(class_="text-md sm:text-lg").string, goodFormat((character.find(class_="w-full text-sm sm:text-md line-clamp-1 text-ellipsis break-anywhere overflow-hidden whitespace-normal text-muted-foreground").string)), chats, like] )

    return rows

fields = ["character","tag","chats","likes"]


def writeBotRecordCSV(URL, filename):
    
    # Writes to csv file
    with open(filename + ".csv", 'w',newline="") as csvfile:
        # Creates a csv writer object
        csvwriter = csv.writer(csvfile)
        # Writes the fields
        csvwriter.writerow(fields)
        # Writes the data rows
        csvwriter.writerows(getRowsandFields(URL))


url = input('Enter the porfile link:')
filename = input('Enter the filename:')
writeBotRecordCSV(url,filename)

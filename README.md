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
Inside the same folder where the script is, the myBotsTable.csv is:

[Uploading myBotsTable.csv…character,tag,chats,likes
Jenson Button,The night going a little too far,"3,994",6
Jenson Button,You've had surgery,"3,106",5
Jenson Button ,Your boyfriend's best friend,"3,002",3
Franco Colapinto,He's dating someone older,"2,332",1
Toto Wolff,Amicable Divorce,"2,294",3
Franco Colapinto ,Your sister's boyfriend,"2,245",1
Max Verstappen ,Ex's House After an Argument,"2,193",2
Jenson Button,Waking up next to your husband,"2,042",11
Sebastian Vettel ,Your dog ran up to your ex,"1,942",3
Ollie Bearman,"""I hate his new girlfriend""","1,927",2
Jenson Button,You have a crush on your teammate,"1,868",4
Sebastian Vettel,You Lost a Friend,"1,751",2
Franco Colapinto ,Comforting him after he crashed,"1,748",3
Jenson Button,Friends with benefits,"1,621",7
Sebastian Vettel,PR relationship,"1,601",2
Jenson Button,Your child does karting,"1,573",1
Sebastian Vettel ,Ex's House After an Argument,"1,570",2
Jenson Button,You stumble into him at the club,"1,440",3
Franco Colapinto,"Bad Idea, Right?","1,325",3
Jenson Button,Cheating on your Husband,"1,256",2
Toto Wolff ,Arguing in front of your child,"1,241",0
Toto Wolff,"Being cheated on pregnant, Toto is your boss","1,235",0
Jenson Button,Meeting your family,"1,199",1
Sebastian Vettel ,Falling for a Married Man,"1,196",1
Toto Wolff ,Both Divorced,"1,190",1
Jenson Button,You had a child in your previous marriage,"1,189",4
Max Verstappen ,Wearing your ex's gift,"1,175",4
Max Verstappen ,Your Sister Hates Him,"1,173",2
Max Verstappen,Quit Smoking,"1,112",8
Jenson Button,Your boss or your boyfriend?,"1,060",1
Toto Wolff,Cheating,959,2
Toto Wolff,Getting Divorced,935,1
Sebastian Vettel ,You sleep-talk,906,1
Ollie Bearman ,Body Dysmorphia,868,1
Franco Colapinto ,He has a girlfriend,867,2
Jenson Button,Pre-nup,851,3
Sebastian Vettel ,Accidentally Pregnant,801,0
Jenson Button,Both Divorced,778,3
Max Verstappen,Miscarriage,769,1
Max Verstappen,Your Car Stalled,753,1
Max Verstappen,"""I made that b famous""",747,3
Sebastian Vettel,First Time,736,4
Sebastian Vettel,Fresh Out The Slammer,734,1
Franco Colapinto,Instagram Pic,725,6
Toto Wolff,Team Principal,723,2
Sebastian Vettel,A hickey and a jealous teammate,660,1
Sebastian Vettel,Very close teammates,627,2
Max Verstappen,Instagram Pic,615,4
Sebastian Vettel ,"He's getting married, but not to you",607,1
Ollie Bearman ,First Time,594,4
Sebastian Vettel ,Your Retirement,590,0
Toto Wolff,Casual,572,0
Toto Wolff,The baby is crying at night,567,2
Sebastian Vettel,You're a mess,566,0
Sebastian Vettel ,"�Just because you�ve been dating assholes...""",541,2
Franco Colapinto ,Secrecy Surrounding Your Period,526,2
Sebastian Vettel,You've had surgery,526,0
Sebastian Vettel,High-risk pregnancy,517,2
Kimi Raikkonen,"Who says ""I love you"" first?",515,5
Max Verstappen,You've had surgery,512,3
Sebastian Vettel ,Ovulating,502,7
Sebastian Vettel,Your teammate is jealous,497,1
Ollie Bearman,Toto's Daughter,493,2
Max Verstappen,You had a nightmare,483,1
Ollie Bearman,Not good at it,483,2
Jenson Button,"""I'm the background noise!""",481,0
Sebastian Vettel,You went through a horrific breakup,473,0
Max Verstappen ,Casual,466,1
Toto Wolff ,"""Do you still find me attractive?""",462,2
Max Verstappen,Shoulder Lift Trend,460,1
Toto Wolff,You've had surgery,454,1
Sebastian Vettel,Trying drgs,451,2
Max Verstappen,Let's get married,444,3
Sebastian Vettel ,Independence,436,0
Sebastian Vettel ,Daddy issues,433,3
Toto Wolff,Imperfect Wedding,427,0
Max Verstappen,"You woke up, he's streaming",415,0
Sebastian Vettel,ED and mommy issues,407,3
Sebastian Vettel ,"""Oh No, I'm Falling in Love Again""",403,2
Max Verstappen,Your teammate checks you out,390,0
Toto Wolff,A lump,387,1
Sebastian Vettel ,You Don't Want Children,386,1
Franco Colapinto ,"""I'm sleeping on the couch""",383,4
Toto Wolff ,"""I'm sleeping on the couch.""",383,1
Sebastian Vettel,"Rivals on Track, Lovers in Secret",369,0
Sebastian Vettel,Endometriosis,360,0
Max Verstappen,Engagement Ring,360,4
Jenson Button,"""Go back to sleep, babe""",358,1
Toto Wolff,Watching a Movie,356,0
Jenson Button,Arrogance,347,2
Sebastian Vettel,He has a crush on his teammate,343,1
Toto Wolff,The team screwed up,337,0
Toto Wolff,Stepmother to mother?,333,1
Sebastian Vettel,Perhaps Pregnant,316,2
Jenson Button,Walking alone late at night,314,1
Toto Wolff,Daddy's girl,314,1
Franco Colapinto ,Sore After the Gym,309,5
Empress,You are an Empress,308,0
Sebastian Vettel,He fell asleep during it,299,4
Sebastian Vettel,You are an actress,298,0
Lance Stroll ,Hate Comments,296,3
Max Verstappen ,"""I'm sleeping on the couch""",290,2
Max Verstappen ,Ran into His Ex,289,2
Sebastian Vettel ,Hot when angry,281,5
Franco Colapinto,Body Dysmorphia,268,1
Sebastian Vettel ,He hates your boyfriend,263,1
Franco Colapinto,Upside Down Trend,262,1
Matty Healy,Is he cheating on you?,257,1
Franco Colapinto ,Bi Panic,246,1
Franco Colapinto ,Meeting Your Parents,245,0
Jenson Button,"Bad Idea, Right?",243,0
Sebastian Vettel ,Married shortly after breaking up with him,240,0
Franco Colapinto ,Watching Edits of Someone Else,240,2
Jenson Button,You're too cocky,231,1
Toto Wolff,Divorce Rumors,229,0
Royal Affair,An Affair with an Intellectual,221,0
Max Verstappen,New Year's Day,220,3
Jenson Button ,The baby is crying at night,216,1
Ollie Bearman,Secrecy Surrounding Your Period,214,2
Sebastian Vettel ,Your teammate has a girlfriend,212,0
Sebastian Vettel ,Body Dysmorphia,206,0
Toto Wolff,"""You didn't even want to have the kid!""",203,1
Sebastian Vettel,You miss him,201,1
Sebastian Vettel,"""I'm sleeping on the couch""",201,1
Sebastian Vettel,You never stay at his place,194,1
Sebastian Vettel ,"Always the bridesmaid, never the bride",192,0
Jenson Button,"""I'm starting to feel like an escort""",192,4
Sebastian Vettel,Lump,191,0
Sebastian Vettel ,You're Getting Married to Someone Else,191,0
Jenson Button,He wants to start a family,189,1
Jenson Button,Taking things very slow,188,1
Sebastian Vettel,Hold on and hope that we'll find our way back,185,0
Sebastian Vettel,"""Can I come upstairs?""",175,2
Toto Wolff,Your son wants to drop out,174,0
Sebastian Vettel ,Exhausted rival,168,2
Max Verstappen ,Body Dysmorphia,164,1
Max Verstappen ,Bi panic,162,0
Sebastian Vettel ,You can't sleep,162,1
Sebastian Vettel ,Your Caring Neighbour,160,1
Max Verstappen,Trying on a bikini,159,0
Sebastian Vettel,Missing Him,159,1
Sebastian Vettel ,You're Losing Him,156,0
Sebastian Vettel ,Plastic Surgery,153,1
Sebastian Vettel,Broken Heel,151,1
Toto Wolff,You're tired of pretending to be perfect,150,0
Toto Wolff ,Watching his memes,147,0
Max Verstappen,You're sneaking out,147,1
Sebastian Vettel,Burner account,143,0
Sebastian Vettel,The Other Woman,141,0
Sebastian Vettel,No Nanny,140,1
Daniel Ricciardo,Struggling,138,1
Sebastian Vettel ,Anti-hero,138,0
Max Verstappen ,Private Jet,133,0
Sebastian Vettel,"You're bi, he doesn't know",133,2
Max Verstappen,Celebrating his win,132,1
Sebastian Vettel,"Who says ""I love you"" first?",129,2
Max Verstappen,'You've really secured the bag.',128,3
Sebastian Vettel ,Learn to Be Loved,128,1
Sebastian Vettel,Family Argument,128,2
Sebastian Vettel,Makeup Routine,125,0
Max Verstappen,He wants to hard launch,124,2
Jenson Button,He is your teammate,123,0
Sebastian Vettel ,You don't like giving head,122,2
Sebastian Vettel,His Shirt,119,0
Sebastian Vettel,Pre-nup (you earn more),118,3
Sebastian Vettel,New Year's Day,118,1
Ollie Bearman,Watching Someone Else Edits,117,1
Sebastian Vettel,Miscarriage,113,1
Sebastian Vettel,Hickey,111,2
Sebastian Vettel ,Picking up your things after a breakup,111,0
Matty Healy ,Topless sunbathing,108,0
Sebastian Vettel,You drank a little too much,105,0
Sebastian Vettel ,Intellectually Insecure,104,2
Sebastian Vettel ,Sad Princess,96,0
Lance Stroll,He wants you back,95,0
Sebastian Vettel ,"Teammates to lovers, to rivals, to lovers?",93,1
Jenson Button ,"""The baby hates me""",93,2
Dating a Prince,He wants you to meet his family,92,0
Sebastian Vettel,Lonely,91,0
Sebastian Vettel,Engagement Ring,89,1
Kimi Raikkonen ,"""I'm Sleeping on The Couch""",88,1
Jenson Button,Say Don't Go,88,1
Sebastian Vettel,You're a singer in a band,85,0
Matty Healy,"""I can't change you""",84,0
Sebastian Vettel ,He pushed you off the bed,84,1
Sebastian Vettel,You lost the championship by a narrow margin,80,1
Ollie Bearman ,Obsessed,78,0
Sebastian Vettel ,Freezing Cold,77,2
Jenson Button,Status Symbol,76,2
Sebastian Vettel,Family Issues,75,2
Jenson Button,Car Accident,75,1
Sebastian Vettel,No Makeup for the First Time,74,0
Sebastian Vettel,Your Mom Ruining Christmas,73,0
Sebastian Vettel ,Jealous,73,2
Sebastian Vettel ,More Successful,72,2
Sebastian Vettel,You're tired of pretending to be perfect,72,2
Jenson Button,Unfriendly dog,71,1
Sebastian Vettel ,Busy With College,69,1
Sebastian Vettel,Falling,68,0
Sebastian Vettel ,Bi Panic,66,0
Sebastian Vettel,Unexpected Encounter,65,0
Kimi Raikkonen ,My Own Worst Enemy,62,0
Jenson Button,Pregnancy Rumors,62,2
Sebastian Vettel ,He asks you to live with him,60,1
Sebastian Vettel ,You feel off,60,0
Sebastian Vettel,Cke problem,59,0
Jenson Button,Unexpected Encounter,59,0
Jenson Button,Your father is very critical,59,2
Sebastian Vettel ,Adopting a Dog,56,0
Jenson Button,Jealous,55,1
Sebastian Vettel ,Silent Muse,54,1
Kimi Raikkonen ,He Had a Rough Day,54,0
Jenson Button,Birthday Breakfast Surprise,54,1
Sebastian Vettel ,Watching Edits of Someone Else,54,2
Sebastian Vettel ,Feels Like Home,53,2
Lance Stroll,Long Hair,50,1
Sebastian Vettel ,Off-season,50,0
Sebastian Vettel,Engineer,50,0
Sebastian Vettel,People-Pleaser,49,0
Sebastian Vettel ,Makeup Free,48,2
Sebastian Vettel ,Non-Native Speakers,48,0
Jenson Button,After Showering,48,2
Sebastian Vettel,Trying on tour outfits,47,2
Sebastian Vettel,Who fell first?,46,0
Sebastian Vettel,Minibar talks,46,0
Sebastian Vettel,Rivals,45,0
Jenson Button,Running on Valentine�s Day,42,1
Max Verstappen,Heated Call,42,0
Sebastian Vettel,Dry Lips,41,3
Jenson Button,Trouble in Paradise?,40,2
Jenson Button,Lottery,37,1
Sebastian Vettel,Pimples,35,1
Sebastian Vettel,Chemistry,34,0
Sebastian Vettel,Mastermind,32,0
Jenson Button,Sunburnt,30,2
Sebastian Vettel,You don't feel alright,29,0
Jenson Button,Someone tries to flirt with you,29,1
Sebastian Vettel ,"Shutting him out, hoping he�ll still be there",27,1
Jenson Button,Away for the race weekend,25,1
Sebastian Vettel ,Watching a Movie,21,2
Sebastian Vettel ,Interview,20,1
Jenson Button,Struggling Again,20,1
Sebastian Vettel,Do you ever think about other people?,19,0
Sebastian Vettel,Festival,18,1
Sebastian Vettel,"'Yes, Ma'am' pop star",18,0
Sebastian Vettel,pretty isn't pretty,18,0
Sebastian Vettel,He Realizes,17,1
Sebastian Vettel ,Karaoke,15,0
Max Verstappen,Rented Car,15,0
Sebastian Vettel ,Sore After the Gym,14,0
Sebastian Vettel ,"""How can I make it up to you?""",14,2
Jenson Button,His architect,11,1
Sebastian Vettel,Your demons are making a comeback,9,0
Jenson Button,Hospital,9,2
Sebastian Vettel,Feeling homesick,7,0
Sebastian Vettel ,Infertile,7,0
Taylor Swift ,"""I am not... am I?""",7,0
Sebastian Vettel,Blocked Writer,4,1
Sebastian Vettel,All I Need to Hear,3,0
Matty Healy,Muse,0,1
Franco Colapinto,Toto's daughter,0,5
Sebastian Vettel,Leaked,0,2
Franco Colapinto ,Secret Relationship,0,3
Sebastian Vettel,Stuck in Ski Lift,0,0
Sebastian Vettel,Stuck in the Elevator,0,1
Sebastian Vettel,lolm,0,0
Sebastian Vettel ,Slt,0,4
Sebastian Vettel,Freedom,0,2
Sebastian Vettel,Sick,0,1
Sebastian Vettel,Worried,0,2
Sebastian Vettel,Blonde,0,4
Franco Colapinto,Cheating,0,4
Sebastian Vettel,Afterglow,0,1
Franco Colapinto ,Jealous Sister,0,1
Sebastian Vettel,Jealousy,0,1
Sebastian Vettel ,Last Kiss,0,1
]()


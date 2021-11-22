# Trello Runup Chart Generator
The basic concept of the project is that Corello is pay-to-use and want to use Trello To-Do/Doing/Done automation with github for personal projects, I created a webscraper that will collect data of To-Do/Doing/Done lists in trello (without using the api), will generate a run-up chart and assign it into a trello card.

There's a few things that are hard-coded and can be automated, but for me it's not worth the time.

## Set-up

### Trello Set-up
Create 4 lists and create a model for the cards. It should look like this:
![Example](https://user-images.githubusercontent.com/49570622/142889496-d6e18d5b-4530-481e-8959-4e90fc5d61be.png)

What (x) means?
Well, x is the amount of points that card is valuated, in run-up charts we like to attribue some sort of importance or ranking of which task should be priority, points indicate that. Change the x of each card to correlate with the importance of the task.

Also, rememember to change the URL inside the main.py to your trello board URL

### Finding the Lists
I used a webscraper to scrape the cards content, but the index of those lists are hard-coded (see main.py line 50-52), the webScraping(listID) function requires the listID.
To find your lists ID simply count how many lists there are, and their index should be where they're. So change their ID's on code.
Ex:
3 lists, 1: to-do, 2: doing, 3: done, 4: Run-upChart
![Example2](https://user-images.githubusercontent.com/49570622/142889994-cd145cad-227c-4ddc-ba39-eace0b444754.png)

### Trello API SETUP
To use the imageToTrello automation you'll need api tokens/auth to upload image directly to a trello card. Remember to change the card ID and the necessary API keys in the early lines of the main.py code.
If you never used Trello API, google the trello doc or click [here](https://developer.atlassian.com/cloud/trello/).

### Options
Everytime you run the code it will ask you the date that you want to associate with the data retrieved. If you don't want that. change line 85 from:
```
diaAtual = datetime(int(ano), int(mes), int(dia)) 
```
to:
```
diaAtual = datetime.now()
```

## Running
To run it, simply use any bash to run main.py. If everything is set-up correctly you should see no errors and a historic.json should be created with the data gathered.

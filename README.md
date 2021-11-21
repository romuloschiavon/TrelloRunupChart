# Trello Runup Chart Generator
The basic concept of the project is that Corello is pay-to-use and want to use Trello To-Do/Doing/Done automation with github for personal projects, I created a webscraper that will collect data of To-Do/Doing/Done lists in trello (without using the api), will generate a run-up chart and assign it into a trello card.

There's a few things that are hard-coded and can be automated, but for me it's not worth the time.

## Basic Set-up
Change the keys to the api in the ```main.py```, create a ```historico.json``` file using the model, and everytime you run main.py it would ask for the date, you can also use the datetime function to automatic generate the date, but I also hardcoded some inputs.

You'll also need to change what's the ID of your to-do/doing/done lists, and the cardID of where the image will be attached.

## Running
```python main.py```

everything is automated, but if you encounter error or would like to contribute, branch it and have fun :)

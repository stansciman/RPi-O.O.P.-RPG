#RPG info class
class RPGInfo:
    author = "Brendan Stanford"

    #display credits
    @staticmethod
    def info():
        print("Created for the Raspberry Pi O.O.P. course by Brendan Stanford (c)")

    @classmethod
    def credits(cls):
        print("Thanks for playing! This project was created by: " + cls.author)

    #class constructor
    def __init__(self, game_title):
        self.title = game_title

    #Initial game welcome script
    def welcome(self):
        print("Welcome to " + self.title)

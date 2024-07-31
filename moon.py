#room class generator
class Moon:

    def __init__(self, moon_name):
        self.name = moon_name
        self.description = None
        self.linked_moons = {}
        #self.linked_items = []
        self.items = None
        self.character = None

    #set and get moon-specific details
    def set_description(self, moon_description):
        self.description = moon_description

    def get_description(self):
        return self.description

    def set_name(self, moon_name):
        self.name = moon_name

    def get_name(self):
        return self.name

    def set_items(self, moon_items):
        self.items = moon_items

    def get_items(self):
        return self.items

    def set_character(self, moon_characters):
        self.character = moon_characters

    def get_character(self):
        return self.character

    def describe(self):
        print(self.description)
        #print(self.name + " linked moons :" + repr(self.linked_moons))

    #links moons to each other
    def link_moons(self, moon_links, direction):
        self.linked_moons[direction] = moon_links

    """def link_items(self, items):
        self.linked_items.append(items)"""

    #begin game and display details about current moon to the player
    def get_details(self):
        print("Current moon is: " + self.name)
        print(self.description)
        #print("Available resources: " + str(self.items))
        #print("Forms of life: " + str(self.character))
        for direction in self.linked_moons:
            moon = self.linked_moons[direction]
            print(moon.get_name() + " is " + direction)

    #move between moons
    def move(self, direction):
        if direction in self.linked_moons:
            return self.linked_moons[direction]
        else:
            print("No nearby moon available that way; try again!")
            return self

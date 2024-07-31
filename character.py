#game character class constructor
class Character():

    number_aliens = 0

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

        Character.number_aliens = Character.number_aliens + 1

    # Describe this character
    def describe(self):
        print("Lifeforms: " + self.name)
        print(self.description)

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True

#enemy subclassinherits name and description parameters from Character superclass
class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    #getter and setter methods to update enemy weaknesses
    def set_weakness(self, enemy_weaknesses):
        self.weakness = enemy_weaknesses

    def get_weakness(self):
        return self.weakness

    #fight method overides character fight method for enemies
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You fought off " + self.name + " with the " + combat_item )
            #return True
        else:
            print(self.name + " destroys you!")
            #return False


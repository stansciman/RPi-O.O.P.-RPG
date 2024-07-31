#Use Moon constructor to instantiate Jovian moons
from moon import Moon
from item import Item
from character import Character, Enemy
from rpginfo import RPGInfo

#Create a list to store resources found on the moons
pouch = []
collection = []

#Instantiate game setting
jovian_system = RPGInfo("Jovian planetary system")

#Instantiate moon objects
io = Moon("Io")
europa = Moon("Europa")
ganymede = Moon("Ganymede")
callisto = Moon("Callisto")

#Instantiate items and set attributes
silicate = Item("Silicate")
silicate.description = "Silicate crystals are those containing silicone and oxygen; perhaps these are as deadly to silicone-based life as carbon oxides are to us?"
silicate.value = 1000

water = Item("Water")
water.description = "Water is key to your survival this far from earth!"
water.value = 5000

kryptonite = Item("Kryptonite")
kryptonite.description = "A green crystal rumoured to weaken even the most powerful alien species!"
kryptonite.value = 10000

#use setter method to describe each moon object
io.set_description("Io is most volcanically active world in the Jovian system")
europa.set_description("Europa is an icy moon with a subsurface ocean thought to potentially harbour life")
ganymede.set_description("Ganymede is the largest moon in the Jovian system complete with a magnetic field")
callisto.set_description("Callisto is the most heavily cratered object in the Jovian system")

#link moons
io.link_moons(europa, "outward")
europa.link_moons(io, "inward")
europa.link_moons(ganymede, "outward")
ganymede.link_moons(europa, "inward")
ganymede.link_moons(callisto, "outward")
callisto.link_moons(ganymede, "inward")

#create characters and enemies
hectapus = Enemy("Hectapus", "A six-tentacled alien shark with lethal intent!")
hectapus.set_weakness("Silicate")
tardigrade = Character("Tardigrade", "Tardigrades, also known as water-bears, have been known to survive even ater exposure to the vaccum of space; could these loveable lifeforms have originated outside of Earth?")
tardigrade.set_conversation("Slurp, burp, slurp!")
cryofungus = Enemy("Cryofungus", "A parasitic crystal fungus that causes the spontaneous combustion of organic matter! Exposure to liquid compromises its structural integrity!")
cryofungus.set_weakness("Water")


#set items and characters for each moon
europa.set_items(water)
io.set_items(silicate)
europa.set_character(tardigrade)
ganymede.set_character(hectapus)
callisto.set_character(cryofungus)
ganymede.set_items(kryptonite)

#set the current moon, get description and intiate movement
current_moon = io
game_over = False
defeated_enemies = 0
RPGInfo.info()
jovian_system.welcome()
print("There are " + str(Character.number_aliens) + " life signs detected in this system!")
while game_over == False:
    print("\n")
    current_moon.get_details()
    inhabitant = current_moon.get_character()
    itemz = current_moon.get_items()
    if itemz is not None:
        print("Available resources: " + itemz.name)
        print(itemz.description)
        print("Resource value: " + str(itemz.value))
    else:
        print("No resources available!")
    if inhabitant is not None:
        inhabitant.describe()
    else:
        print("No life detected!")
    command = input("inward, outward, collect, or attack? ")
    if command in ["inward", "outward"] and not isinstance(inhabitant, Enemy):
        current_moon = current_moon.move(command)
    elif command in ["inward", "outward"] and isinstance(inhabitant, Enemy):
        print("Threat detected; terminate threat to proceed!")
    elif command == "collect" and itemz is not None:
        pouch.append(itemz.get_name())
        collection.append(itemz)
        print("Resource added to your pouch!")
        current_moon.set_items(None)
    elif command == "collect" and itemz is None:
        print("No resource to collect!")
    elif command == "attack":
        if inhabitant is None:
            print("No threat detected!")
        else:
            print("What do you use to defend yourself?")
            print("Pouch contents: " + str(pouch))
            fight_with = input()
            if fight_with in pouch:
                friend = inhabitant.fight(fight_with)
                if friend == True:
                    print(inhabitant.talk())
                    print("Life form is not a threat!")
                else:
                    weaknezz = inhabitant.get_weakness()
                    if fight_with == weaknezz:
                        print("Threat neutralized!")
                        current_moon.set_character(None)
                        defeated_enemies = defeated_enemies + 1
                        if defeated_enemies == 2:
                            print("All hostile life forms have been terminated! You return to Earth a hero!")
                            game_over = True
                    else:
                        print("Your defense was ineffective and you were swiftly killed!")
                        game_over = True
                        RPGInfo.author = "Raspberry Pi Foundation"
                        RPGInfo.credits()

            elif fight_with not in pouch:
                print("The requested resource is unavailable!")


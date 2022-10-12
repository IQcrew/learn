import random


print ("")

#armor types
light_armor = 0
medium_armor = 0
heavy_armor = 0
shield = 0

#chestplates
chestplate_light = 0
chestplate_medium = 0
chestplate_heavy = 0

#gautlets only give light armor
gauntlets_light = 0
greaves = 0
helmet = 0
cloak = 0

Level = 1
exp = 0

stats = {"Health" : 100, "Magic" : 100,}
total_points = {"Strength" : 0, "Dexterity" : 0, "Intellegence" : 0, "Wisdom" : 0, "Charisma" : 0, "Vitality" : 0}
character_abilitiy = {"Human" : "Intellegence" , "Orc" : "Strength", "Dwarf" : "Vitality", "Undead" : "Wisdom"}

def add_ability(name_of_player):
    total_points[character_abilitiy[name_of_player]] += 1
    print(f"For being {name_of_player} you are given a bonus point on {character_abilitiy[name_of_player]}")


print ("Welcome to something something something pleasse pick your class")
print  ("Human, Orc, Dwarf, Undead")
print ("")

player_race = input()

print ("Your Player Race is " + player_race)

for i in total_points.keys(): 
    print(i, total_points[i], sep= " ")

print ("")

print("These are your starting statistics. You have 3 +1 points available")
print("Allocate your points")

print ("")

for i in range(3):
    if i == 0:
        print ("Where would you like to allocate your first point")
    if i == 1:
        print ("Where would you like to allocate your secound point")
    if i == 2:
        print ("Where would you like to allocate your thrid point")
    point_1 = input("")
    try:
        total_points[point_1] += 1
    except:
        print (f"Point {i+1} skipped")

print ("")

add_ability(player_race)

print ("")

for i in total_points.keys():
    print(i, total_points[i], sep= " ")

a = input("These are your stats ")

print("You wake up in a prison cell, lost in your thoughts on how you got here")
print("You see a fight break out between two guards and a new prisoner")
print("What do you do?")
a = input("Do you attack one of the guards, or bide your time?")


if a ==("Attack one of the guards"):
    print ("You attack one of the guards and knock him out, You gain 23 Experience")
    exp = exp + 23
    if exp > 100:
        print ("")
    else:
        print ("You ")

    

else:
    print ("You sat there and watched it unfold, the prisinors will remember your actions ")
    

    
 
a = input ("Game Over")
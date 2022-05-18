'''

Name: Anthony Iacano

Program: Initiative Tracker v0.1

Program Purpose: To track a number of characters set, and named within the
program, placing them in order based on their initiative rolled. Players and
enemies alike


'''

from Character import Character

# opening print line for program // split into lines to for easier reading
opening = (
    f"|-------------------------------------------|\n\n|   Welcome to the "
    "Initiative Tracker v0.1  |\n\n|---------------------------------------"
    "----|\n"
)
print(opening)

character_num = input('Please input number of characters (including any allies, enemies or any fighting creature): ')
print(character_num)
character_num = int(character_num)

name = input("Name: ")
allign = input("allignment: ")

c1 = Character(name, allign, 0)

characterList = []*int(character_num)

# while loop that contains the turns and creature name/affiliation
while True:

    # for loop that collects data on characters and adds to a list
    for x in range(0, character_num):
         characterList.append(c1)

    break

print(characterList)
print(characterList[0].name)


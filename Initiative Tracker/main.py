'''

Name: Anthony Iacano

Program: Initiative Tracker v0.1

Program Purpose: To track a number of characters set, and named within the
program, placing them in order based on their initiative rolled. Players and
enemies alike

NOTES -
tabulate library could be helpful for formatting
tkinter or kivy could be helpful for creating a gui


'''

from Character import Character

# opening print line for program // split into lines to for easier reading
opening = (
    f"\033[95m|-------------------------------------------|\n\n|   Welcome to the "
    "Initiative Tracker v0.1  |\n\n|---------------------------------------"
    "----|\n\033[0m"
)
print(opening)

#START OF: CHARACTER CREATION CODE
while True: #while statement for initial character count
    try:
        character_num = input('Please input number of characters (including any allies, enemies or any fighting creature): ')
        character_num = int(character_num)
    except ValueError:
        print('\033[1m\033[91m|INVALID RESPONSE: Please answer a valid integer!|\033[0m\n')
    else:
        break

characterList = []*int(character_num)

# while loop that creates the characters with name and affiliation attributes, breaks when finished
while True:
    # for loop that collects inputs on character's attributes and adds characters to a list
    for x in range(0, character_num):
        print ('\nInput Data for Character ' + str(x + 1) + ': ')
        name = input("Name: ")
        
        while(True): #while statement catches errors with user input
            allign = input("Allignment(PC, ENEMY, ALLY): ")
            if (allign == 'PC' or allign == 'ENEMY' or allign == 'ALLY' ):
                break;
            else:
                print('\033[1m\033[91m|INVALID RESPONSE: Please answer PC, ENEMY or ALLY!|\033[0m')
                print('\033[K')
                
        c1 = Character(name, allign, 0) #default value for initiative is 0
        characterList.append(c1)
        
    break

print ("\nAll characters successfully input! There are a total of " + str(len(characterList)) + '! Incredible =)\n')

#For loop that collects initiative on the various characters
for char in characterList:
    while True:
        try:
            real_init = input('Please input the initiative for character ' + char.name + ': ')
            real_init = float(real_init)
            setattr(char, 'initiative', real_init)
        except ValueError:
            print('\033[1m\033[91m|INVALID RESPONSE: Please answer a valid integer!|\033[0m\n')
        else:
            break

print("\nAll character initiatives successfully recorded!\n")

while(True): #while statement catches errors with user input and only continues when combat is ready to begin
    combatStart = input("Ready to start combat? (YES or NO)\n ")
    if (combatStart == 'YES'):
        print('\n')
        break;
    elif combatStart == 'NO':
        print("\nI really can't fathom why you would even answer like this.")
        print("If you aren't ready, try not typing until you are!\n")
    else:
        print('\033[1m\033[91m|INVALID RESPONSE: Please answer YES or NO!|\033[0m')
        print('\033[K')

#START OF: BATTLE CODE

characterList.sort(key = lambda c: c.initiative, reverse = True) #sorts the character list by the record initiatives, greatest to least

roundNum = 0

print('\033[2J\n') 

print("\033[95m ------------------ BATTLE ------------------\033[0m")

while True: #while loop that keeps the rounds from stopping until combat is over
    
    for y in range(0, character_num): #Goes through each character in a round
    
            for x in range(0, character_num): #Prints out each turn
                if y == x:
                    # print('{:<4} {:>4} {:>4}'.format(characterList[y].name, "\033[1m\033[91m", characterList[y].allignment, "\033[0m" "<<"))
                   print(characterList[y].name + ', \033[1m\033[91m' + characterList[y].allignment + "\033[0m<<")
                else:
                    print(characterList[x].name + ', \033[1m\033[91m' + characterList[x].allignment + "\033[0m")
            input("\nNEXT TURN - PRESS ENTER")
            print('\033[2J\n')    

    roundNum = 0
#Program End    
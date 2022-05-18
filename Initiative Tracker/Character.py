'''

Name: Anthony Iacano

Class: Character

Class Definition: A character that has a name, allignment(Enemy, Ally, or PC)
and an initiative.

'''

class Character:
  def __init__(self, name, allignment, initiative):
    self.name = name
    self.allignment = str(allignment)
    self.initiative = float(initiative)

#test character
c1 = Character("Anthony", 'PC', 0)



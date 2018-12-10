from ClassDescriptions.Alien import *
from ClassDescriptions.Cowboy import *

characters = [Alien('Fred', 100, 10), Cowboy(name='Roy')]

for i in range(3):
    for character in characters:
        character.turn()

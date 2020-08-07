# inventory projects, pg. 120 & pg. 121 of Automate the Boring Stuff with Python

import pprint
inventory = {'shield':1, 'gold':60, 'bow':1, 'arrows':15, 'potion':4}
dragonLoot = ['gold', 'gold', 'ruby', 'hammer']

def printInventory(inv):
    print('Inventory:')
    total = 0
    
    for key, value in inventory.items():
        print(str(value) + ' ' + key)
        total += value
        
    print('Total number of items: ' + str(total))

def addToInventory(inventory, dragonLoot):
    for item in dragonLoot:
        inventory.setdefault(item, 0)
        inventory[item] += 1
        
    
inv = addToInventory(inventory, dragonLoot)
printInventory(inv)

from mcpi.minecraft import Minecraft
from random import randint
from time import sleep
mc = Minecraft.create()

buildingblocks = {'air':0,'cobblestone':4,'diamond':57,'road':44, 'sandstone':24, 'water':8}


def destroy():
    pos = mc.player.getTilePos()
    mc.setBlocks(pos.x, pos.y, pos.z, pos.x+50, pos.y+50, pos.z+50, buildingblocks['air'])

def skyscraper():
    mc.postToChat('Building a skyscraper')
    pos = mc.player.getPos()
    x,y,z = pos.x, pos.y, pos.z
    width = randint(4,20)
    height = randint(10,50)
    length = randint(6,20)
    mc.setBlocks(x, y, z, x+width, y+height, z+length, buildingblocks['diamond'])

def building():
    mc.postToChat('Building commencing')
    pos = mc.player.getPos()
    x,y,z = pos.x, pos.y, pos.z
    width = 10
    height = 5
    length = 6
    mc.setBlocks(x, y, z, x+width, y+height, z+length, buildingblocks['cobblestone'])
    mc.setBlocks(x+1, y+1, z+1, x+width-1, y+height-1, z+length-1, buildingblocks['air'])

def road(direction):
    mc.postToChat('Roadworks commencing')
    pos = mc.player.getTilePos()
    x,y,z = pos.x, pos.y, pos.z
    width = 6
    height = 6
    length = 100
    if direction == "north":
        mc.setBlocks(x, y, z, x+width, y, z+length, buildingblocks['road'])
    else:
        mc.setBlocks(x-1, y-1, z-1, x+length, y,z+width, buildingblocks['road'])

def river(direction):
    mc.postToChat('Can I swim?')
    pos = mc.player.getTilePos()
    x,y,z = pos.x, pos.y, pos.z
    width = randint(1,5)
    depth = 6
    length = randint(1,100)
    if direction == "north":
            mc.setBlocks(x, y, z, x+width, y-depth, z+length, buildingblocks['water'])
    else:
            mc.setBlocks(x, y, z, x+length, y-depth, z+width, buildingblocks['water'])
    
mc.postToChat('Welcome to our Simple City.')
mc.postToChat('You are free to destroy and create using the menu')
answer = 0

while answer != "8":
        print('Main Menu \n'
              '1: Create a skyscraper\n'
              '2: Create a building\n'
              '3: Build a road, north to south\n'
              '4: Build a road, east to west\n'
              '5: Create a river, north to south\n'
              '6: Create a river, east to west\n'
              '7: Destroy a 50 cubed area around you\n'
              '8: Exit the menu')
        answer = input('What would you lke to do? ')

        if answer == '1':
                skyscraper()
        elif answer == '2':
                building()
        elif answer == '3':
                road('north')
        elif answer == '4':
                road('east')
        elif answer == '5':
                river('north')
        elif answer == "6":
                river('east')
        elif answer == '7':
                destroy()
        else:
                print('Goodbye')
                break



#Import libraries
import mcpi.minecraft as Minecraft
from random import randint
from time import sleep
mc = Minecraft.create()


#Create Variables

#Create dictionary of blocks

buildingblocks = {'air':0,'cobblestone':4,'diamond':57,'road':44, 'sandstone':24, 'water':8}
#Define Functions

#Destroy The World

def destroy():
	pos = mc.player.getTilePos()
	mc.setBocks(pos.x, pos.y, pos.z, pos.x+50, pos.y+50, pos.z+0, buildingblocks['air'])

#Create a skyscraper

def skyscraper():
	mc.postToChat('Building a skyscraper')
	pos = mc.player.getPos()
	x,y,z = pos.x,pos.y,pos.z
	width = randint(4,20)
	height = randint(10,50)
	length = randint(6,20)
	mc.setBlocks(x,y,z,x+width,y+height,z+length, buildingblocks['diamond'])
	mc.setBlocks(x+1,y+1,z+1,x+width-1,y+height-1,z+length-1, buildingblocks['air'])
#Specify width, height and length along with blocktype passed as a dictionary.
#Windows print every other level?
#range(0,10,2) Prints the evens!

#Create a smaller building
def building():
	mc.postToChat('Building commencing')
	pos = mc.player.getPos()
	x,y,z = pos.x,pos.y,pos.z
	width = 10
	height = 5
	length = 6
	mc.setBlocks(x,y,z,x+width,y+height,z+length, buildingblocks['cobblestone'])
	mc.setBlocks(x+1,y+1,z+1,x+width-1,y+height-1,z+length-1, buildingblocks['air'])

#Create a pyramid
def pyramid():
	mc.postToChat('Building a pyramid')
	height = 10
	levels = range(height)
	pos = mc.player.getTilePos()
	x,y,z = pos.x + height, pos.y, pos.z
	for level in levels:
		mc.setBlocks(x - level, y,z - level, x + level, y, z + level, buildingblocks['sandstone'])
		y +=1

#Create a road
def road():
	mc.postToChat('Roadworks commencing')
	pos = mc.player.getTilePos()
	x,y,z = pos.x,pos.y,pos.z
	width = 6
	height = 1
	length = 100
	blockType = 44
	air = 0
	mc.setBlocks(x-1,y-1,z-1,x+width-1,y+height-1,z+length-1, buildingblocks['air'])
	mc.setBlocks(x-1,y-1,z-1,x+width,y+height,z+length, buildingblocks['road'])
		

#Create a river
def river():
	pos = mc.player.getTilePos()
	x,y,z = pos.x,pos.y,pos.z
	width = 6
	height = 1
	length = 100
	blockType = 44
	air = 0
	mc.setBlocks(x-1,y-6,z-1,x+width-1,y+height-1,z+length-1, buildingblocks['air'])
	mc.setBlocks(x-1,y-6,z-1,x+width,y+height,z+length, buildingblocks['water'])
	
	
#Main body

#Menu Tkinter?


		
	


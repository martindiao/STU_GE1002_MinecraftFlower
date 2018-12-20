from mcpi.minecraft import Minecraft
import time
import mcpi.block as block

mc=Minecraft.create()
#mc=Minecraft.create("10.163.80.195",4711)

pos = mc.player.getTilePos()
mc.player.setTilePos(0,0,0)
#clear all
mc.setBlocks(9,-1,11, -12,-1,11, 2)
mc.setBlocks(10,0,10, -12,11,12, block.AIR.id)
#axis
mc.setBlock(0,8,0, block.STONE.id)
mc.setBlock(0,8,1, block.STONE.id)
mc.setBlock(1,8,0, block.STONE.id)
mc.setBlock(0,9,0, block.STONE.id)
#0 point
mc.setBlock(0,-1,0, 41)
#torches around 0
mc.setBlock(1,0,0, 50)
mc.setBlock(-1,0,0, 50)
mc.setBlocks(1,0,1, -1,0,1, 50)
mc.setBlocks(1,0,-1, -1,0,-1, 50)
stayed_time=0
flag = 0

class flower(object):
    count = 0
    def __init__(self, name, _water):
        self.name = name
        self.water = _water
        flower.count += 1
        self.index = flower.count # start from 1
        #setting the meter
        shift = - ( self.index - 1 ) * 6
        #overwrite
        mc.setBlock(9+shift,-1,11,2)
        mc.setBlocks(10+shift,0,10, 6+shift,11,12, block.AIR.id)
        #glasses
        mc.setBlocks(10+shift,0,10, 10+shift,10,10, block.GLASS.id)
        mc.setBlocks(10+shift,0,11, 10+shift,10,11, block.GLASS.id)
        mc.setBlocks(10+shift,0,12, 10+shift,10,12, block.GLASS.id)
        mc.setBlocks(9+shift,0,12, 9+shift,10,12, block.GLASS.id)
        mc.setBlocks(8+shift,0,12, 8+shift,10,12, block.GLASS.id)
        mc.setBlocks(8+shift,0,11, 8+shift,10,11, block.GLASS.id)
        mc.setBlocks(8+shift,0,10, 8+shift,10,10, block.GLASS.id)
        #the line on the sink
        mc.setBlock(9+shift,-1,11,9+shift,10,11, block.AIR.id)
        #grass
        mc.setBlock(7+shift,0,10, 2)
        #torch
        mc.setBlock(6+shift,0,10, 50)
        #flower
        if (self.name == "Rose"):
            mc.setBlock(7+shift,1,10, 38)
        else:
            mc.setBlock(7+shift,1,10, block.AIR.id)
        #light on
        mc.setBlocks(10+shift,11,10, 8+shift,11,12, 89)
    def light_on(self):
        shift = - ( self.index - 1 ) * 6
        mc.setBlocks(10+shift,11,10, 8+shift,11,12, 89)
        mc.setBlock(6+shift,0,10, 50)
    def light_off(self):
        shift = - ( self.index - 1 ) * 6
        mc.setBlocks(10+shift,11,10, 8+shift,11,12, 123)
        mc.setBlock(6+shift,0,10, block.AIR.id)
    def set_water(self,_water):#0-10
        shift = - ( self.index - 1 ) * 6
        mc.setBlocks(9+shift,0,10, 9+shift,10,10, block.AIR.id)
        mc.setBlocks(9+shift,-1,11, 9+shift,10,11, block.AIR.id)
        if (_water != 0):
            mc.setBlock(9+shift,_water,11, block.WATER.id)
        
f1 = flower("Rose", 0)
f1.set_water(0)

f2 = flower("Nope", 2)
f2.light_off()

while True:
    flag = flag + 1
    flag = flag % 8
    pos = mc.player.getTilePos()
    #print (flag)
    #mc.postToChat("Flower Count:" + str(f1.count) + " " + str(f2.water))
    '''if (flag == 0):
        mc.setBlock(pos.x+3, pos.y + 5, pos.z, block.WATER.id)
    if (flag == 2):
        mc.setBlock(pos.x+3, pos.y + 5, pos.z, block.AIR.id)
    '''
    #mc.timeset(0)
    #print("stay_time"+str(stayed_time))
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    #mc.postToChat("please goto home x=-30 y=-6 z=-40 for 15s to fly")
    #mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z)) 
    if pos.x==-30 and pos.y==-6 and pos.z==-40:
        mc.postToChat("welcome home")
        stayed_time=stayed_time+1
        if stayed_time>=30:
            mc.player.setTilePos(-30,10,-40)
            stayed_time=0
    else:
        stayed_time=0
        
     

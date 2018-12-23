from mcpi.minecraft import Minecraft
import time
import mcpi.block as block

mc=Minecraft.create()
#mc=Minecraft.create("10.19.75.6")

#pos = mc.player.getTilePos()
mc.player.setTilePos(0,0,0)

# clear all
mc.setBlocks(20,-1,6, -20,-1,12, 2)
mc.setBlocks(20,0,6, -20,11,12, block.AIR.id)
# three axis
mc.setBlock(0,8,0, block.STONE.id)
mc.setBlock(0,8,1, block.STONE.id)
mc.setBlock(1,8,0, block.STONE.id)
mc.setBlock(0,9,0, block.STONE.id)
# the 0 point
mc.setBlock(0,-1,0, 41)
# torches around the 0 point
mc.setBlock(1,0,0, 50)
mc.setBlock(-1,0,0, 50)
mc.setBlocks(1,0,1, -1,0,1, 50)
mc.setBlocks(1,0,-1, -1,0,-1, 50)

class flower(object):
    count = -1
    def __init__(self, name, _water):
        self.name = name
        self.water = _water
        self.is_alert_on = False
        flower.count += 1
        self.index = flower.count # starts from 0
        # setting the meter
        self.shift = -self.index * 6
        # overwrite
        mc.setBlock(9+self.shift,-1,11, 2)
        mc.setBlocks(10+self.shift,0,10, 6+self.shift,11,12, block.AIR.id)
        # glasses
        mc.setBlocks(10+self.shift,0,10, 10+self.shift,10,10, block.GLASS.id)
        mc.setBlocks(10+self.shift,0,11, 10+self.shift,10,11, block.GLASS.id)
        mc.setBlocks(10+self.shift,0,12, 10+self.shift,10,12, block.GLASS.id)
        mc.setBlocks(9+self.shift,0,12, 9+self.shift,10,12, block.GLASS.id)
        mc.setBlocks(8+self.shift,0,12, 8+self.shift,10,12, block.GLASS.id)
        mc.setBlocks(8+self.shift,0,11, 8+self.shift,10,11, block.GLASS.id)
        mc.setBlocks(8+self.shift,0,10, 8+self.shift,10,10, block.GLASS.id)
        # the line on the sink
        mc.setBlocks(9+self.shift,-1,11, 9+self.shift,10,11, block.AIR.id)
        # the grass
        mc.setBlock(7+self.shift,0,10, 2)
        # the red torch
        mc.setBlock(7+self.shift,-1,10, 76)
        # the alert torch
        mc.setBlock(7+self.shift,0,9, 76)
        # the water button
        mc.setBlock(9+self.shift,0,8, 70)
        # the torch
        mc.setBlock(6+self.shift,0,10, 50)
        # the flower
        if (self.name == "Rose"):
            mc.setBlock(7+self.shift,1,10, 38)
        elif (self.name == "Lily"):
            mc.setBlock(7+self.shift,1,10, 37)
        else:
            mc.setBlock(7+self.shift,1,10, block.AIR.id)
        # lights on
        mc.setBlocks(10+self.shift,11,10, 8+self.shift,11,12, 89)
    def light_on(self):
        mc.setBlocks(10+self.shift,11,10, 8+self.shift,11,12, 89)
        mc.setBlock(6+self.shift,0,10, 50)
    def light_off(self):
        mc.setBlocks(10+self.shift,11,10, 8+self.shift,11,12, 123)
        mc.setBlock(6+self.shift,0,10, block.AIR.id)
    def alert_on(self):
        mc.setBlock(7+self.shift,-1,10, 2)
        self.is_alert_on = True
    def alert_off(self):
        mc.setBlock(7+self.shift,-1,10, 76)
        self.is_alert_on = False
    def set_water(self, _water): # 0 - 10
        self.water = _water
        mc.setBlocks(9+self.shift,0,10, 9+self.shift,10,10, block.AIR.id)
        mc.setBlocks(9+self.shift,-1,11, 9+self.shift,10,11, block.AIR.id)
        if (_water != 0):
            mc.setBlock(9+self.shift,_water,11, block.WATER.id)
        mc.postToChat("[Debug] Set water of flowers [" + str(self.index) + "] to " + str(self.water))
    def is_alert(self):
        if (self.water <= 2):
            if (self.is_alert_on):
                mc.postToChat("Flower " + str(self.index + 1) + " needs watering !!!")
                self.alert_off()
            else:
                self.alert_on()
flowers = []
flowers.append(flower("Rose", 0))
flowers.append(flower("Lily", 0))
flowers.append(flower("Lily", 0))
flowers[0].set_water(8)
flowers[1].set_water(3)
flowers[2].set_water(1)
flowers[0].alert_off()
while True:
    for i in flowers:
        i.is_alert()
    pos = mc.player.getTilePos()
    #mc.postToChat("Flower Count:" + str(f1.count) + " " + str(f2.water))
    time.sleep(0.5)
    #mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))

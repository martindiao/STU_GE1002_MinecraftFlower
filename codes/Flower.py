from mcpi.minecraft import Minecraft
import time
import mcpi.block as block

mc=Minecraft.create()
#mc=Minecraft.create("10.19.75.6")

#pos = mc.player.getTilePos()
mc.player.setTilePos(0,0,0)

# clear all
mc.setBlocks(20,-1,11, -20,-1,11, 2)
mc.setBlocks(20,0,10, -20,11,12, block.AIR.id)
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
        flower.count += 1
        self.index = flower.count # starts from 0
        # setting the meter
        shift = -self.index * 6
        # overwrite
        mc.setBlock(9+shift,-1,11, 2)
        mc.setBlocks(10+shift,0,10, 6+shift,11,12, block.AIR.id)
        # glasses
        mc.setBlocks(10+shift,0,10, 10+shift,10,10, block.GLASS.id)
        mc.setBlocks(10+shift,0,11, 10+shift,10,11, block.GLASS.id)
        mc.setBlocks(10+shift,0,12, 10+shift,10,12, block.GLASS.id)
        mc.setBlocks(9+shift,0,12, 9+shift,10,12, block.GLASS.id)
        mc.setBlocks(8+shift,0,12, 8+shift,10,12, block.GLASS.id)
        mc.setBlocks(8+shift,0,11, 8+shift,10,11, block.GLASS.id)
        mc.setBlocks(8+shift,0,10, 8+shift,10,10, block.GLASS.id)
        # the line on the sink
        mc.setBlocks(9+shift,-1,11, 9+shift,10,11, block.AIR.id)
        # the grass
        mc.setBlock(7+shift,0,10, 2)
        # the torch
        mc.setBlock(6+shift,0,10, 50)
        # the flower
        if (self.name == "Rose"):
            mc.setBlock(7+shift,1,10, 38)
        else:
            mc.setBlock(7+shift,1,10, block.AIR.id)
        # lights on
        mc.setBlocks(10+shift,11,10, 8+shift,11,12, 89)
    def light_on(self):
        shift = -self.index * 6
        mc.setBlocks(10+shift,11,10, 8+shift,11,12, 89)
        mc.setBlock(6+shift,0,10, 50)
    def light_off(self):
        shift = -self.index * 6
        mc.setBlocks(10+shift,11,10, 8+shift,11,12, 123)
        mc.setBlock(6+shift,0,10, block.AIR.id)
    def set_water(self, _water): # 0 - 10
        shift = -self.index * 6
        self.water = _water
        mc.setBlocks(9+shift,0,10, 9+shift,10,10, block.AIR.id)
        mc.setBlocks(9+shift,-1,11, 9+shift,10,11, block.AIR.id)
        if (_water != 0):
            mc.setBlock(9+shift,_water,11, block.WATER.id)
        mc.postToChat("Set water of flower [" + str(self.index) + "] to " + str(self.water))

flowers = []
flowers.append(flower("Rose", 0))
flowers.append(flower("Nope", 2))
flowers[0].set_water(8)
flowers[1].light_off()

while True:
    pos = mc.player.getTilePos()
    #mc.postToChat("Flower Count:" + str(f1.count) + " " + str(f2.water))
    time.sleep(0.5)
    #mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))

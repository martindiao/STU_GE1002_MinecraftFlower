from mcpi.minecraft import Minecraft
import time
import mcpi.block as block

flowers = []
inlist = []
flower_name = "Air"
flower_count = -1

mc=Minecraft.create()
#mc=Minecraft.create("10.19.75.6")

#pos = mc.player.getTilePos()
mc.player.setTilePos(0,0,0)
server_path = "h:\\\\192.168.0.100\\Share_pi"
# clear all
mc.setBlocks(20,-1,6, -20,-1,12, 2)
mc.setBlocks(20,0,6, -20,11,12, block.AIR.id)
# three axis
#mc.setBlock(0,8,0, block.STONE.id)
#mc.setBlock(0,8,1, block.STONE.id)
#mc.setBlock(1,8,0, block.STONE.id)
#mc.setBlock(0,9,0, block.STONE.id)
# the 0 point
mc.setBlock(0,-1,0, 41)
# torches around the 0 point
mc.setBlock(1,0,0, 50)
mc.setBlock(-1,0,0, 50)
mc.setBlocks(1,0,1, -1,0,1, 50)
mc.setBlocks(1,0,-1, -1,0,-1, 50)

class flower(object):
    def __init__(self, name, _water):
        global flower_count
        self.name = name
        self.water = _water
        self.is_alert_on = False
        flower_count += 1
        self.index = flower_count # starts from 0
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
        mc.setBlocks(8+self.shift,3,10, 8+self.shift,10,10, block.GLASS.id)
        # the line on the sink
        mc.setBlocks(9+self.shift,-1,11, 9+self.shift,10,11, block.AIR.id)
        # the grass block
        if ((self.name == "Cactus") or ("仙人" in self.name)):
            mc.setBlock(7+self.shift,0,10, 12)
        elif (self.name == "Tank"):
            mc.setBlock(7+self.shift,0,10, 120)
        else:
            mc.setBlock(7+self.shift,0,10, 2)
        # the red torch
        mc.setBlock(7+self.shift,-1,10, 76)
        # the alert torch
        mc.setBlock(7+self.shift,0,9, 76)
        # the mode switch
        if (self.name != "Tank"):
            mc.setBlock(9+self.shift,0,8, 69,5)
        # the instruction light
        if (self.name != "Tank"):
            mc.setBlock(10+self.shift,0,8, 123)
        # plunger
        if (self.name != "Tank"):
            mc.setBlock(9+self.shift,-2,8, 29,2)
            mc.setBlock(9+self.shift,-2,7, 3)

        # air
        mc.setBlock(9+self.shift,-2,6, block.AIR.id)
        self._mode = ( mc.getBlock(9+self.shift,-2,6) == 3 )
        # the torch
        mc.setBlock(6+self.shift,0,10, 50)
        # the flower
        if ((self.name == "Rose") or ("玫瑰" in self.name)):
            mc.setBlock(7+self.shift,1,10, 38)
        elif (self.name == "Lily"):
            mc.setBlock(7+self.shift,1,10, 37)
        elif ((self.name == "Cactus") or ("仙人" in self.name)):
            mc.setBlock(7+self.shift,1,10, 81)
        elif ((self.name == "Aloe") or (self.name == "芦荟")):
            mc.setBlock(7+self.shift,1,10, 31,1)

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
    def set_water(self, _water): # 0 ~ 10
        if (self.water != _water):
            self.water = _water
            mc.setBlocks(9+self.shift,0,10, 9+self.shift,10,10, block.AIR.id)
            mc.setBlocks(9+self.shift,-1,11, 9+self.shift,10,11, block.AIR.id)
            if (_water != 0):
                mc.setBlock(9+self.shift,_water,11, block.WATER.id)
            #mc.postToChat("[Debug] Set water of flowers [" + str(self.index) + "] to " + str(self.water))
    def is_alert(self):
        if (self.water <= 2):
            if (self.is_alert_on):
                mc.postToChat("Flower " + str(self.index + 1) + " needs watering !!!")
                self.alert_off()
            else:
                self.alert_on()
    def switch_or_not(self):
        if ( self._mode != ( mc.getBlock(9+i.shift,-2,6) == 3 ) ) :
            mc.postToChat( "Switch mode of Flower " + str(self.index + 1) + " to " + str( mc.getBlock(9+i.shift,-2,6) == 3 ))
    def upd(self):
        self.is_alert()
        self.switch_or_not()
        self._mode = ( mc.getBlock(9+i.shift,-2,6) == 3 )

flowers.append(flower("Tank", 0))
flowers.append(flower(flower_name, 0))

def read_in():
    global flower_name
    global flower_count
    #with open('upload.txt', 'r') as f:
    with open('\\\\192.168.0.100\\Share_pi\\upload.txt', 'r', encoding='UTF-8') as f:
        inlist = f.readlines()
    inlist = inlist[0].split(",")
    #print(inlist)
    if ((flower_name != inlist[2]) and (flowers[1]._mode)):
        flowers.pop()
        flower_count -= 1
        flower_name = inlist[2]
        flowers.append(flower(flower_name, 0))

    if (float(inlist[1]) < 3) :
        flowers[0].set_water(0)
    else:
        flowers[0].set_water(10)
    flowers[1].set_water(10-int(inlist[0]))

read_in()

while True:
    read_in()
    # synchronize the flowers' class
    for i in flowers:
        i.upd()
    # write switch mode
    #with open('switch.txt', 'w') as f:
    with open('\\\\192.168.0.100\\Share_pi\\switch.txt', 'w') as f:
        f.write(str(int(flowers[1]._mode)))
    pos = mc.player.getTilePos()
    time.sleep(0.1)
    #mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))

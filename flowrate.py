#finanal formula Q=pi*r^2*sqrt(2gh)
#flowrate Q=Av
#area A=pi*r^2
#Energy Ep=mgh, Ek=0.5mv^2
#velocity v=sqrt(2gh)
#Volume per second per plan required 0.000015033366402116402116402116402116

import math
pi = 3.1415926535
g = 9.81

def VolumeCube(height, length, width):
    volume = height*length*width
    return volume

def AreaCircle(radius):
    area = pi*radius**2
    return area

def Average(list):
    average = 0
    for item in list:
        average += item
    average /= len(list)
    return average

def VelocityWater(height):
    velocity = math.sqrt(2*g*height)
    return velocity

def Flowrate(height, radius, volumeConstant='true', increment=0, average='false'):
    if volumeConstant == 'false':
        heights = []
        flowrates = []
        i = 0
        while i <= height:
            heights.append(i)
            i += increment
        for h in heights:
            flowrates.append(Flowrate(h, radius))
        if average == 'false':
            return flowrates
        elif average == 'true':
            return Average(flowrates)
    elif volumeConstant == 'true':
        velocity = VelocityWater(height)
        area = AreaCircle(radius)
        flowrate = velocity*area
        return flowrate

def EmptyTime(height, radius, increment, width, length, average='true'):
    time = 0
    if average =='false':
        sectionVolume = VolumeCube(increment, length, width)*1000
        flowrates = Flowrate(height, radius, 'false', increment)
        for f in flowrates:
            if f:
                sectionTime = sectionVolume/f
                time += sectionTime
    elif average == 'true':
        flowrate = Flowrate(height, radius, 'false', increment, 'true')
        volume = VolumeCube(height, length, width)*1000
        time = volume/flowrate
    return time

#With radius=0.02, height=1.105, width=length=0.83
#Actual Time to empty: 242126.58356559995s
#Average Time to empty: 196086.47283224785s
#Average flowrate: 0.0038821367379647687L/s
#Max flowrate: 0.005837887318845878L/s
#Min flowrate: 0.0005566207158750797L/s
#Max Plants support: 388.32867919882657562872710400554‬
#Min Plants support: 37.025686794723399950286949889619
#Avg Plants support: 258.23469169342139176303152822871
#Expected plant support((Avg + Min)/4): 73.815094622036197928329619529583‬
#Days without Refill: 2.802391013490740162037037037037

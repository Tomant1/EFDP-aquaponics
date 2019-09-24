Data = 'data/plants.csv'

ET0 = 300

def GetKc(name, stage, file='data/plants.csv'):
    lookup = open(file, 'r')
    lineNUM = 0
    for line in lookup:
        if lineNUM != 0:
            if name in line:
                array = line.split(',')
                Kc = float(array[stage + 1])
        lineNUM += 1
    return Kc

def KcAverage(file='data/plants.csv'):
    lookup = open(file, 'r')
    lineNUM = 0
    plants = 0
    for line in lookup:
        if lineNUM != 0:
            array = line.split(',')
            plant = float(array[1]) + float(array[2]) + float(array[3])
            plant /= 3
            plants += plant
        lineNUM += 1
    average = plants/(lineNUM - 1)
    return average

def WaterUsage(Kc):
    ETc = ET0*Kc
    return ETc

def PlantSupport(flowrate, Kc):
    flowrate = ((flowrate*60)*60)*24
    ETc = WaterUsage(Kc)
    plantNUM = flowrate/(ETc/1000)
    return plantNUM

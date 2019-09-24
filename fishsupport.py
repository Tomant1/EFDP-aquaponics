Data = 'data/fish.csv'

supportFactor = 27#g of fish per liter of water

calories = 218/170#calories per gram

def AgeToWheight(age, file):
    lookup = open(file, 'r')
    for line in lookup:
        array = line.split(',')
        if age == int(array[0]):
            weight = float(array[1])/100
    return weight

def AvgWheight(file):
    lookup = open(file, 'r')
    average = 0
    lineNUM = 0
    for line in lookup:
        array = line.split(',')
        average += float(array[1])/100
        lineNUM += 1
    average /= lineNUM
    return average

def FishSupport(volume, wheight):
    volume *= supportFactor
    fishNUM = volume/wheight
    return fishNUM

def Calories(number, wheight):
    cal = number*wheight*calories
    return cal

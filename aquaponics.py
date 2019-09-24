import flowrate
import fishsupport
import plantsupport

radius = float(input("Output Radius: "))
outHeight = float(input("Output Height: "))
height = float(input("Container Height: "))
increment = float(input("Height Increment: "))
width = float(input("Container Width: "))
length = float(input("Container Length: "))
fish = input("Fish Type: ")
age = int(input("Fish Age: "))
plant = input("Plant Type: ")
stage = int(input("Plant Growth Stage: "))

heightAbove = height - outHeight
COM = input("Input Command: ")
while COM:
    if COM == "change":
        value = input("Value to Change: ")
        if value == "plant":
            plant = input("Plant Type: ")
        elif value == "fish":
            fish = input("Fish Type: ")
        elif value == "radius":
            radius = float(input("Output Radius: "))
        elif value == "outHeight":
            outHeight = float(input("Output Height: "))
        elif value == "height":
            height = float(input("Container Height: "))
        elif value == "increment":
            increment = float(input("Height Increment: "))
        elif value == "width":
            width = float(input("Container Width: "))
        elif value == "length":
            length = float(input("Container Length: "))
        elif value == "age":
            age = int(input("Fish Age: "))
        elif value == "stage":
            stage = int(input("Plant Growth stage: "))
        elif value == "climate":
            climate = input("Climate: ")

    elif COM == "flowrate":
        COM = input("Input Calculation Value: ")
        if COM == "avg":
            print(flowrate.Flowrate(heightAbove, radius, 'false', increment, 'true'))
        elif COM == "ALL":
            print(flowrate.Flowrate(heightAbove, radius, 'false', increment))
        elif COM == "max":
            flowrates = flowrate.Flowrate(heightAbove, radius, 'false', increment)
            print(flowrates[-1])
        elif COM == "min":
            flowrates = flowrate.Flowrate(heightAbove, radius, 'false', increment)
            print(flowrates[1])

    elif COM == "time":
        COM = input("Input Calculation Value: ")
        if COM == "avg":
            print(flowrate.EmptyTime(heightAbove, radius, increment, width, length))
        elif COM == "actual":
            print(flowrate.EmptyTime(heightAbove, radius, increment, width, length, 'false'))

    elif COM == "fish":
        COM = input("Input Calculation Value: ")
        if COM == "max":
            volume = 1000*flowrate.VolumeCube(height, length, width)
            wheight = fishsupport.AgeToWheight(age, "data/" + fish + ".csv")
            print(fishsupport.FishSupport(volume, wheight))
        elif COM == "min":
            volume = 1000*flowrate.VolumeCube(outHeight, length, width)
            wheight = fishsupport.AgeToWheight(age, "data/" + fish + ".csv")
            print(fishsupport.FishSupport(volume, wheight))
        elif COM == "avg":
            avgHeight = outHeight + (height - outHeight)/2
            volume = 1000*flowrate.VolumeCube(avgHeight, length, width)
            wheight = fishsupport.AvgWheight("data/" + fish + ".csv")
            print(fishsupport.FishSupport(volume, wheight))
        elif COM == "avgcal":
            number = float(input("Number of Fish: "))
            wheight = fishsupport.AvgWheight("data/" + fish + ".csv")
            print(fishsupport.Calories(number, wheight))
        elif COM == "cal":
            number = float(input("Number of Fish: "))
            wheight = fishsupport.AgeToWheight(age, "data/" + fish + ".csv")
            print(fishsupport.Calories(number, wheight))

    elif COM == "plant":
        COM = input("Input Calculation Value: ")
        if COM == "single":
            Kc = plantsupport.GetKc(plant, stage)
            flow = flowrate.Flowrate(heightAbove, radius, 'false', increment, 'true')
            print(plantsupport.PlantSupport(flow, Kc))
        elif COM == "avg":
            Kc = plantsupport.KcAverage()
            flow = flowrate.Flowrate(heightAbove, radius, 'false', increment, 'true')
            print(plantsupport.PlantSupport(flow, Kc))
        elif COM == "min":
            flow = flowrate.Flowrate(heightAbove, radius, 'false', increment)
            Kc = plantsupport.KcAverage()
            print(plantsupport.PlantSupport(flow[1], Kc))
        elif COM == "max":
            flow = flowrate.Flowrate(heightAbove, radius, 'false', increment)
            Kc = plantsupport.KcAverage()
            print(plantsupport.PlantSupport(flow[-1], Kc))
    COM = input("Input Command: ")

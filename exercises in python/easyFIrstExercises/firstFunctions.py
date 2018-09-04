import math

def circle_area(num):
    area = num**2 * math.pi
    print(area)

circle_area(5)

def radians(degrees):
    radians = degrees * math.pi / 180
    return degrees

def cosine(degrees):
    angle_radian = radians(degrees)
    cosine = math.cos(angle_radian)
    print (cosine)
cosine(90)

def sandwich(bread, meat, cheese):
    if cheese is not None:
        print("Order details: " + bread, meat, cheese)
    else:
        print("Order details: " + bread, meat)

def sandwich_details():
    bread = input("please enter type of bread: ")
    sandwich(bread, cheese=input("please enter type of cheese: "), meat=input("please enter type of meat: "))

sandwich_details()





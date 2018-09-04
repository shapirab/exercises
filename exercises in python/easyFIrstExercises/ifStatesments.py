#Create a function that takes an int and returns 1 if positive, -1 if negative, 0 if 0
def check_if_positive(num):
    if int(num) > 0:
        return 1
    elif int(num) < 0:
        return -1
    else:
        return 0
def isPositive():
    print(check_if_positive(input("Please enter an integer: ")))

#isPositive()

#Check if three numbers can create a triangle, that is that the sum of the first two is greater then the third
def is_triangle(num1, num2, num3):
    if int(num1) + int(num2) > int(num3):
        return True
    else:
        return False
def check_if_triangle():
    print(is_triangle(input("enter num1: "), input("enter num2: "), input("enter num3: ")))

#check_if_triangle()

#Write a function that returns True if either one of its parameters, or if their sum or
#difference equals 6

def six_is_great(num1, num2):
    if (int(num1) == 6) or (int(num2) == 6) or ((int(num1) + int(num2)) == 6) or ((int(num1) - int(num2)) == 6) or ((int(num2) - int(num1)) == 6):
        return True
    else:
        return False
#print(six_is_great(input("enter num1: "), input("enter num2: ")))

#Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean
# indicating if we are on vacation, return a string of the form "7:00" indicating when
# #the alarm clock should ring. Weekdays, the alarm should be "7:00" and on the weekend it
# #should be "10:00". Unless we are on vacation -- then on weekdays it should be "10:00" and
# #weekends it should be "off".




# CR: Good method names: is_positive, is_triangle
# CR: It is great that you are documenting your methods. That is the way to go!
# CR: The documentation should be in the format of: The method takes an int, returns 1 if positive and so on.
# Python has a special way to document functions: use """ brackets to create a
# special function comment. Doing this in PyCharm should create a block comment
# with blocks for the parameters and return value, which is essentially what your comment here is explaining.
# Another benefit of using docstrings is that your method will have a __doc__
# attribute, which you can view (try this in IPython)

# Create a function that takes an int and returns 1 if positive, -1 if negative, 0 if 0


def check_if_positive(num):
    # CR: I think it makes more sense to assume that num is a number,
    # and raise exception if it is not. In your case, when you receive input from the user,
    # it is the calling method that needs to convert the input to integers, not this method.
    # It is better that this method assumes it receives a number, and its code should fail
    # in the event that num is not a number. (Think about how confusing it is that
    # check_if_positive('a') will fail, but check_if_positive('1') does not - both are type string)

    # CR: As explained above, I think this is not the correct place to convert input to integers,
    # but for efficiency, the conversion int(num) should happen once, not twice: num1 = int(num),
    # and using num1 throughout the code.
    if int(num) > 0:
        return 1
    elif int(num) < 0:
        return -1
    else:
        return 0


# CR: In these two methods, you have basically the same name -
# it is impossible from the method names to distinguish between the
# functionality of check_if_positive and isPositive. You need to give
# methods names that are indicative to what they do, even if it is
# something along the lines of test_check_if_positive.
# CR: Conventions - isPositive vs. is_positive.
def isPositive():
    print(check_if_positive(input("Please enter an integer: ")))


# CR: NEVER leave commented out code
# isPositive()

# Check if three numbers can create a triangle,
# that is that the sum of the first two is greater then the third
def is_triangle(num1, num2, num3):
    # CR: Again, this method should assume it receives numbers and not convert them itself.
    # CR: Are you sure this code is correct? I remember that the sum
    # of every two sides should be larger than the remaining third, not one set (a+b>c and b+c>a and c+a>b)
    # CR: Use parentheses to be sure expressions like these evaluate the way you want them to.
    if int(num1) + int(num2) > int(num3):
        # CR: Why not just return the boolean term int(num1) + int(num2) > int(num3)? 
        return True
    else:
        return False


def check_if_triangle():
    print(is_triangle(input("enter num1: "), input("enter num2: "), input("enter num3: ")))


# check_if_triangle()

# Write a function that returns True if either one of its parameters, or if their sum or
# difference equals 6

def six_is_great(num1, num2):
    # CR: An if statement like this is extremely confusing, and therefor extremely error prone.
    # You can split it into several lines using \ (defining a multiline statement in Python),
    # or actually create variables:
    # parameter_six = (num1) == 6 or (num2 == 6)
    # difference_six = num1 - num2 etc. , and your if statement being: if parameter_six or difference_six
    # CR: The number 6 repeats itself. Consider the trouble of changing
    # the number 6 to 9 (and also the probability of missing one) - you should save it in a variable: magic = 6.
    # For extra credit, you could also put it as an optional parameter in your method,
    # enabling the same method to generically evaluate different members: magic_is_great(num1, num2, magic=6)
    if (int(num1) == 6) or (int(num2) == 6) or ((int(num1) + int(num2)) == 6) or ((int(num1) - int(num2)) == 6) or (
            (int(num2) - int(num1)) == 6):
        return True
    else:
        return False


# print(six_is_great(input("enter num1: "), input("enter num2: ")))

# CR: What happened here?
# Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean
# indicating if we are on vacation, return a string of the form "7:00" indicating when
# #the alarm clock should ring. Weekdays, the alarm should be "7:00" and on the weekend it
# #should be "10:00". Unless we are on vacation -- then on weekdays it should be "10:00" and
# #weekends it should be "off".


# CR: PEP8: Only one empty line at the end of a source file. Use CTRL+ALT+L

"""
This method takes an int and returns 1 if positive, -1 if negative, 0 if 0
"""


def is_positive(num):
    if int(num) > 0:
        return 1
    elif int(num) < 0:
        return -1
    else:
        return 0


def check_numbers(num1, num2, magic):
    """
    This function takes two numbers and checks it against a check number (magic).
    It returns true if the numbers or their addition/subtruction equals the magic number
    :param num1:
    :param num2:
    :param magic:
    :return:
    """
    comparison = (num1 == magic) or (num2 == magic)
    addition = num1 + num2
    subtruction = 0
    if num1 > num2:
        subtruction = num1 - num2
    elif num2 > num1:
        subtruction = num2 - num1
    else:
        return comparison
    if addition == magic or subtruction == magic:
        return True
    else:
        return comparison


if __name__ == '__main__':
    statement = input("please enter an integer: ")
    num1 = int(statement)
    statement = input("please enter an integer: ")
    num2 = int(statement)
    statement = input("please enter the check number: ")
    magic = int(statement)
    print(check_numbers(num1, num2, magic))


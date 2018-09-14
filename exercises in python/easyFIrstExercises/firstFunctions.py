import math
# CR: PEP8 requires 2 blank lines separating methods
def circle_area(num):
    # CR: You don't want opaque formalae in your code - the code should explain itself, and in cases where it cannot do this, add comments. A mathemetical formula with random constants is confusing. There would be a great difference in this method, for example, if instead of calling the parameter "num" it would have been called "radius":
    # area = (radius ** 2) * math.pi  # Parentheses make this easier to understand
    # I think in this case it is clear enough, however in more complicated cases you might want to add a comment explaining the logic as well.

    # CR: PEP8 requires whitespace between both sides of an operator: a + b - PEP8, a+b - not PEP8
    area = num**2 * math.pi
    print(area)


# CR: this belongs at the bottom of the page as explained.
circle_area(5)

# CR: Good variable name!
def radians(degrees):
    # CR: use parentheses to make this easier to read and ensure that the operations happen the way you want them to: (degrees * math.pi) / 180
    radians = degrees * math.pi / 180
    return degrees

def cosine(degrees):
    angle_radian = radians(degrees)
    cosine = math.cos(angle_radian)
    print (cosine)
cosine(90)

def sandwich(bread, meat, cheese):
    # CR: the statement 
    # if cheese:
    # would have given you the same result in this case. In Python, every statement resolves to True or False. The only cases where you would use notation like this is in cases where you actually have 3 possible values for cheese: True, False, or None.
    if cheese is not None:
        print("Order details: " + bread, meat, cheese)
    else:
        print("Order details: " + bread, meat)
# CR: I am not sure I understand the relationship between sandwich and sandwich_details. It looks like the separation between them is that one is responsible for reading the inputs from the users, and the other for "creating" a sandwich. If that is true, the two methods would be better named along the lines of: read_sandwich_inputs, and create_sandwitch. However, in this case I actually think that it might not be necessary to have two different methods. This is a great example of abstraction level that is not necessary right now, and actually complicates the code, but as the program grows might be necessary to refactor (for example, if there would be a future usage of bread and cheese that did not come from user inputs).
def sandwich_details():
    bread = input("please enter type of bread: ")
    # CR: It would be cleaner to put each input on a separate line, as you did with the bread.
    sandwich(bread, cheese=input("please enter type of cheese: "), meat=input("please enter type of meat: "))

# CR: Python code files can be libraries and scripts at the same time. I believe we discussed the "if __name__ == '__main__' " construct, however even in this case the best practice is to put the methods you are calling at the bottom of the page. This has a logical reason - Python does not compile, it interprets and executes each line. If you reference a method before it is defined, you will get an error. Try running the following code:
# test_method()

# def test_method():
#     pass


sandwich_details()





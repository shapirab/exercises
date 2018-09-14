# CR: This is a problem definition, and not a comment explaining what the method does.

# create a function that takes an integer and and adds all the integers
# between 1 and the number. You will need an accumulator as well as a counter.

# CR: This method does not work. You should not submit for CR code that does not work.
# Notice that your code only iterates over all the numbers between 1 and the number, but never adds them together.
# CR: Bad method name. According to your comment, the method calculates the sum of numbers below the number, it does nothing with adding one.
def add_one(num):
    counter = 0
    # CR: Why do you need to convert counter to int?
    # CR: Use range method to iterate over numbers. It could replace most of the code in this method.
    # CR: A comment about while loops: First do the actions you need, iterate the counter at the end. Your loop would look like (without changing its functionality):
    # counter = 1  # Initialize to first working value
    # while int(counter) < int(num):
    #     print(counter)  # Loop action
    #     counter += 1  # Iterate the counter before the condition is reevaluated.
    while int(counter) < int(num):
        counter += 1
        print(counter)

# add_one(num=input("Please enter an integer: "))

# CR: Excellent, first usage of docstrings!
# CR: I think your choice of name here is confusing. If the method calculates the SUM of all the SQUARES, I feel it would be better named sum_squares, indicating the sum of squares, and not square_sum, which indicates the square of a sum.
def square_sum(num):
    """
    Create a function that takes one parameter and
    calculates the sum of the squares of all the integers from one to that number.
    :param num:
    :return:
    """
    sum_square = 0
    # CR: don't leave TODOs in CR code..
    # CR: What you are doing here is iterating including the final number, for example for num=6 you will return: 1+4+9+16+25+36, while the method documentation would suggest that it does not include the final number.
    # CR: Loops like the one you have written here are very error prone - you would have had to check many times that the loop starts and finishes where you intend it to. First of all, sections like this greately benefit from comments: writing a comment like "Include num in sum of squares, so calculating range for one greater" would probably make this easier to understand.
    # I would suggest running range as normal, and when calculating sum_square using (i+1) 
    # TODO: fix this function, calculates wrong sum
    for i in range(int(num) + int(1)):
        sum_square = sum_square + i ** 2
    print (sum_square)
# square_sum(input("enter an integer: "))

# Write a function that takes a list as input and returns
# the sum of the squares of all the numbers in the list.
# WHY DOES THIS NOT WORK?????
# CR: It seems iteration does exactly what it is supposed to.

# CR: Bad method name. Iteration tells nothing about what the method is supposed to do, other that it has to do with iterating. sum_squares is a fine name for this one as well I think.
def iteration(alist):

    counter = 0
    sum_square = 0
    # CR: I really do not understand why you wrote int(counter) - you know it's an int, you just initialized it, and there is no way it could have changed.
    # CR: I believe that in later methods you were introduced to the for loop, but at any rate - Python offers the functionality to iterate over all members of a list (like foreach in C#). Instead of much of the iteration code in this method, you would have written: for value in alist:
    # Implementation of a for loop
    while int(counter) < len(alist):
        # CR: Convention for index is that it is the index of the cell, not the content of it: current_index = 1, current_value = alist[1]
        current_index = alist[counter]
        sum_square += current_index ** 2
        # sum_square += int(alist[int(counter)])**2
        counter += 1  # Increment counter
    print(sum_square)

# CR: What is the purpose of the name iteration_for_version
# CR: This method calculates the sum of the squares of the length of a list - the contents of the list do not matter to it, only the values: for a list of length 1 it will return 0, for length 2 - 1, for length 3 - 5, and so on.
def iteration_for_version(alist):
    sum_square = 0
    for position in range(len(alist)):
        sum_square += position ** 2
    print(sum_square)


# iteration_for_version(input("enter a list of integers: "))
# iteration(input("please enter a list of integers: ")) - this does not work!!!!

# Add all the natural numbers below n that
# are multiples of 5 or 7. Natural numbers start from 1.

def natural_numbers_added(n):
    # CR: Input validations belong before the method receives the value - it is fair that this method assumes that n is a number, or raises an exception if it isn't.
    if int(n) < 1:
        print("please enter a number greater then 1")
        return
    else:
        # CR: sum is a better name.
        addition = 0
        for position in range(int(n)):
            # CR: You could have written: if not position % 5 or not position % 7, however I am not sure it is clearer than what you have written.
            if position % 5 == 0 or position % 7 == 0:
                addition += position
        print(addition)


# natural_numbers_added(input("please enter a number: "))
# CR: Excellent! You use the main convention in Python!
if __name__ == '__main__':
    print(iteration(range(3)))
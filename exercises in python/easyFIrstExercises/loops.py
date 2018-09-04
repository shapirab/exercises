# create a function that takes an integer and and adds all the integers
# between 1 and the number. You will need an accumulator as well as a counter.

def add_one(num):
    counter = 0
    while int(counter) < int(num):
        counter += 1
        print(counter)

# add_one(num=input("Please enter an integer: "))


def square_sum(num):
    """
    Create a function that takes one parameter and
    calculates the sum of the squares of all the integers from one to that number.
    :param num:
    :return:
    """
    sum_square = 0
    # TODO: fix this function, calculates wrong sum
    for i in range(int(num) + int(1)):
        sum_square = sum_square + i ** 2
    print (sum_square)
# square_sum(input("enter an integer: "))

# Write a function that takes a list as input and returns
# the sum of the squares of all the numbers in the list.
# WHY DOES THIS NOT WORK?????


def iteration(alist):

    counter = 0
    sum_square = 0
    # Implementation of a for loop
    while int(counter) < len(alist):
        current_index = alist[counter]
        sum_square += current_index ** 2
        # sum_square += int(alist[int(counter)])**2
        counter += 1  # Increment counter
    print(sum_square)


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
    if int(n) < 1:
        print("please enter a number greater then 1")
        return
    else:
        addition = 0
        for position in range(int(n)):
            if position % 5 == 0 or position % 7 == 0:
                addition += position
        print(addition)


# natural_numbers_added(input("please enter a number: "))

if __name__ == '__main__':
    print(iteration(range(3)))
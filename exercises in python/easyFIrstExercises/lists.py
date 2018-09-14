def my_first_list():
    """
    Create a list with some values
    :return:
    """
    # CR: why do you not use simply my_list = [1, 2, 3, 4]?
    my_list = []
    item_1 = input("please enter list object 1: ")
    item_2 = input("please enter list object 2: ")
    item_3 = input("please enter list object 3: ")
    item_4 = input("please enter list object 4: ")

    my_list.append(item_1)
    my_list.append(item_2)
    my_list.append(item_3)
    my_list.append(item_4)

    print(my_list)
    return my_list


def return_first_and_last_items(shopping):
    """
    Create a function that takes a list as a parameter
    and returns a list containing the first and the last
    element of the list.
    :param shopping:
    :return:
    """
    # CR: As mentioned, you could use shopping[-1] instead of using the length to extract this.
    new_list = [shopping[0], shopping[len(shopping) - 1]]
    print(new_list)

def unique_list(a_list):
    """
    Create a function that takes a list as input and returns a list of all unique
    elements of the original list.
    The list it returns does not need to be in the same order.
    :param a_list:
    :return:
    """
    # CR: Excellent! 
    # CR: I would prefer unique_list than the name a_unique_list, the 'a' adds nothing to the name.
    a_unique_list = set(a_list)

    # CR: a_unique_list contains a set, not a list - you need to convert it back to a list. Also you never return it.
    print(a_unique_list)


def has_consecutive_2 (new_list):
    """
    Write a function that takes a list of integers and returns True
    if the list contains a 2 in two consecutive spots.
    :param new_list:
    :return:
    """
    is_consecutive = False
    for n in new_list:
        # CR: Notice that n is the item in new_list, not the index. For example, if the list is [4,7,2], n receives the values 4, 7, and 2, which does not help you compare indexes.
        # CR: If n is the current index (like a regular for loop), you would run into a problem at the last index, when the index of n is the last member of the list. Code like this always needs special care for the ends: what happens for the first index? The last index? And of course, you should check the middle case as well.
        if n == 2 and new_list[n + 1] == 2:
            # CR: Notice that once you find the consecutive 2s you do not need to continue running the method - it is enough to return here.
            is_consecutive = True
    return is_consecutive


if __name__ == '__main__':
    # return_first_and_last_items(my_first_list())
    # unique_list(a_list=[1, 2, 3, 1, 2, 5, 6, 7, 8])

    print(has_consecutive_2(new_list=[1, 5, 2, 2, 3, 7]))

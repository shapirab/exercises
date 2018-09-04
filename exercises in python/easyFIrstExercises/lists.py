def my_first_list():
    """
    Create a list with some values
    :return:
    """
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
    a_unique_list = set(a_list)
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
        if n == 2 and new_list[n + 1] == 2:
            is_consecutive = True
    return is_consecutive


if __name__ == '__main__':
    # return_first_and_last_items(my_first_list())
    # unique_list(a_list=[1, 2, 3, 1, 2, 5, 6, 7, 8])

    print(has_consecutive_2(new_list=[1, 5, 2, 2, 3, 7]))

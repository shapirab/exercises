def three_indexed_colors():
    """
    Create a dictionary with three different indexes as shown in the example:
    blue, seven, 7
    :return:
    """
    # CR: Again, don't leave TODOs in code that is for CRs
    # TODO: I am not sure what is required in this exercise

# CR: Docstrings should explain what the function does, not what the exercise wanted you to do. It is perfectly find in my opinion to describe the exercise requirements in a regular comment above the method, but the docstring should describe what the method does.
def sorted_list():
    """
    Create the function sortedList that returns a sorted list of
        the keys for a dictionary that is passed in.
    :return:
    """
    # CR: According to the problem definition, it seems this should be a parameter.
    products = {"Apples": 1, "Oranges": 2, "Bananas": 3, "Peaches": 4}
    # CR: Nice usage of sorted method. However, notice that sorted already returns a list, there is no need to convert it again to a list.
    sorted_products = list(sorted(products))
    return sorted_products


def lookup(dictionary, value):
    """
    Create a function that takes a dictionary and a value.
    It should return a list of all the keys that map to that value.
    The list should be sorted.
    :param dictionary:
    :param value:
    :return:
    """
    # CR: It is considered more Pythonic, and faster, to use the [] notation (only in set() it is better to use the method). You can check out the link: https://stackoverflow.com/questions/5790860/and-vs-list-and-dict-which-is-better (I looked this up)
    # CR: I think it is better to avoid having the variable type in its name, unless it is really necessary. I think this would have been beteter as found_keys, or desired_keys, or many other possible names that indicate the purpose of this variable rather than its type.
    list_of_keys = list()
    # CR: It is almost always better to avoid one letter names. In this case, I would have substituted k and v for key and value, and called the value parameter lookup_value, or something like it. The idea is that one letter names are usually a lot less clear than complete words, even though they are shorter. Only in the classic lst[i] it is acceptable.
    for k, v in dictionary.items():
        if v == value:
            list_of_keys.append(k)
    # CR: It is rarely a good idea to return string messages from a method. According to the exercise definition, returning an empty list should have been OK. In other cases you could raise an exception.
    # Consider that the method's responsibility is to return a list of the keys with this value. When you are returning the string message, you are determining what action the program should do with this information - however, this belongs to the calling method's responsibility.
    if not list_of_keys:
        return "no key found"
    else:
        return sorted(list_of_keys)


if __name__ == "__main__":
    # print(sorted_list())
    dictionary = {'ta': 4, 'hi': 7, 'Hello': 4}
    str_value = input("please enter a number: ")
    value = int(str_value)
    print(lookup(dictionary, value))





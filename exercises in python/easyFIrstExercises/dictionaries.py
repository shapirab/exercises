def three_indexed_colors():
    """
    Create a dictionary with three different indexes as shown in the example:
    blue, seven, 7
    :return:
    """
    # TODO: I am not sure what is required in this exercise


def sorted_list():
    """
    Create the function sortedList that returns a sorted list of
        the keys for a dictionary that is passed in.
    :return:
    """
    products = {"Apples": 1, "Oranges": 2, "Bananas": 3, "Peaches": 4}
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

    list_of_keys = list()
    for k, v in dictionary.items():
        if v == value:
            list_of_keys.append(k)
    if not list_of_keys:
        return "no key found"
    else:
        return sorted(list_of_keys)


def switch_keys_values(dictionary):
    new_dictionary = {}
    for k, v in dictionary.items():
        new_value = k
        new_key = v
        new_dictionary[new_key] = new_value

    return new_dictionary


def create_dictionary():
    a = "a"
    b = "b"
    c = "blue"
    d = "yellow"
    dictionary = dict()
    dictionary[a] = c
    dictionary[b] = d
    return dictionary


if __name__ == "__main__":
    # print(sorted_list())
    dictionary = {"a": "Blue", "b": "Yellow"}
    print(switch_keys_values(dictionary))






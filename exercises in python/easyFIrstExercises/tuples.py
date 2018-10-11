def get_tuple(element):
    """
    Make a function that takes in a string, list, or tuple and
    returns a tuple, where each element of the tuple is an
    element in the value that was passed in.
    Make sure the tuple elements are in the same order is the original.
    :param element:
    :return:
    """
    return tuple(element)


def min_max():
    """
    Create a function that takes a sequence of inputs
    (may be a list, a tuple, or just a bunch of inputs).
    The function should return the minimum and the maximum of the list.
    :param input:
    :return:
    """
    sequence = input("Please enter a value. Enter done when done: ")
    if sequence == "done":
        return "Empty tuple. No minimum or maximum to calculate"
    seq_list = []
    while sequence != "done":
        seq_list.append(sequence)
        sequence = input("Please enter a value. Enter done when done: ")

    seq_tuple = tuple(seq_list)
    minimum = min(seq_tuple)
    maximum = max(seq_tuple)
    return minimum, maximum


def make_dictionary(list_of_tuples):
    """
    This function takes a list of tuples, each containing two values,
    and creates a dictionary where the first value is the key and the second
    is the value. if the key appears more then once it will add
    the values as an imbeded list within the dictionary (car: [ford, fiat])
    :param list_of_tuples:
    :return:
    """


if __name__ == "__main__":
    print(min_max())



# Create a function that takes a string and a number
# as a parameter. It should return the
# character that is in the position given


def get_char(word, location):
    char = word[int(location)]
    print(char)

# get_char(input("please enter a word: "), input("please enter a number: "))

# Create a function that searches a string for a given character
# and returns the position that the letter first occurs.
# If the letter doesn't occur, return -1.


def search_string(word):
    char = input("please enter a letter to search: ")
    for aLetter in word:
        if aLetter == char:
            print(word.index(aLetter))


# search_string(input("please enter a word: "))

def is_reverse(word, drow):
    """
    compare two words and return True if the
    words are reverses of each other. Fix the semantic error(s).
    :return:
    """
    if len(word) == len(drow):
        for char in word:
            if word[0] == drow[len(drow) - 1]:
                word = word[0: len(word) - 1]
                drow = drow[1:]
                return True
            else:
                return False
    else:
        return False

if __name__ == '__main__':
    word = input("please enter a word: ")
    drow = input("please enter a second word: ")
    print(is_reverse(word, drow))




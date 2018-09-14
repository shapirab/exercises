# Create a function that takes a string and a number
# as a parameter. It should return the
# character that is in the position given
# CR: Notice that the problem definition is to RETURN the character - you are only printing it. (If the problem is that you wanted to print it, you print in the main function calling it: print(get_char(...)))
def get_char(word, location):
    char = word[int(location)]
    # CR: this should have been return char
    print(char)

# get_char(input("please enter a word: "), input("please enter a number: "))

# Create a function that searches a string for a given character
# and returns the position that the letter first occurs.
# If the letter doesn't occur, return -1.
# CR: You could have used the string find method. ("some_string".find)

def search_string(word):
	# CR: I don't like the inconsistency here - word is received as a parameter but you receive char from the user. I think that in a method like this it is best to receive both as parameters, but even if you decide to read from user consistency is important. (Imagine that something like this leaves the reader wondering WHY char is read here but word is read from the main function. Things like this should have a good reason behind them)
    char = input("please enter a letter to search: ")
    # CR: I think letter is a better variable name, I don't see the benefits of aLetter. (for letter in word reads better than for aletter in word). Notice that in variable names, every letter matters - you don't want letters that do not have meaning.
    for aLetter in word:
        if aLetter == char:
        	# CR: Again, notice that you are not returning the index, you are printing it. This should have been return word.index(aLetter)
        	# CR: Also, notice that this code does not meet the requirements of the exercise: 1) The requirement was "return the position the letter FIRST occurs", while this prints ALL the positions the letter occurs. 2) The requirement was "if the letter doesn't occur, return -1", while this does not do anything if the letter does not occur.
            print(word.index(aLetter))


# search_string(input("please enter a word: "))
# CR: while the word/drow is clever, I think more generic names would be better here, for example str1 and str2, or word1 and word2
def is_reverse(word, drow):
    """
    compare two words and return True if the
    words are reverses of each other. Fix the semantic error(s).
    :return:
    """
    # CR: Code like this would greatly benefit from comments explaining the logic behind what you are doing here. For example: 
    # if len(word) == len(drow):  # Length must be equal for words to be reverses of each other
    #     for char in word:
    #     	# Compare letters at both ends
    #         if word[0] == drow[len(drow) - 1]:  
    #         	# Set for comparing the next two ends
    #             word = word[0: len(word) - 1]
    #             drow = drow[1:]
    #             return True
    #         else:
    #             return False
    if len(word) == len(drow):
        for char in word:
        	# CR: You can use advantage of Python's ability to access indexes from the right as well: drow[len(drow) - 1] == drow[-1], word[0: len(word) - 1] == word[:-1]
            if word[0] == drow[len(drow) - 1]:
                word = word[0: len(word) - 1]
                drow = drow[1:]
                # CR: As far as I see, this is a bug - consider the first iteration of the loop. At this point, the code has asserted that the two leters at opposing ends are the same. If they are not, you can indeed return False, but if they are, it does not mean that the other two letters will be equal - is_reverse('abc', 'eea') returns True! This is a regular case where in order to know this isn't true, one failure is enough, but for it to be true you need to iterate the entire loop.
                return True
            else:
                return False
    else:
    	# CR: It is great that you are returning instead of printing!
        return False

    # CR: Code like this benefits greatly from being structured a little bit differently. It is often much easier to read and understand (and less buggy) to eliminate the False statements first, and then if the end of the method is reached, it must be True. This offers for less levels of indentation - most of your method is written inside an if statement, which is usually better to avoid. Consider this rewrite of your method: 
  #   def is_reverse(word, drow):
  #   	if len(word) != len(drow):  # If this is False, there is no reason to continue the method.
		#     return False

	 #    for char in word:
		#     # len(word) == len(drow), so it doesn't matter from which you take the length
		#     last_index = len(word) - 1
		#     if word[0] != drow(last_index):  # Again, once one set of characters is not equal there is no reason to continue the method
		#         return False

		#     # Prepare the next slices to check
		#     word = word[:last_index]
		#     drow = drow[1:]
		# # If we got here, it means the only option left is that the two are equal.
		# return True


if __name__ == '__main__':
    word = input("please enter a word: ")
    drow = input("please enter a second word: ")
    print(is_reverse(word, drow))



# CR: Extra credit: The is_reverse method could actually be rewritten using the list reverse method and the string join method:
# def is_reverse_library_implementation(str1, str2):
# 	if len(str1) != len(str2):
# 		return False

# 	# Reverse one string
# 	as_list = list(str1)
# 	as_list.reverse()
# 	reverse_str1 = "".join(as_list)  # Create a reversed string from as_list

# 	return str2 == reverse_str1


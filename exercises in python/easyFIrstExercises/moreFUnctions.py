# CR: I don't understand why this needed a separate file
def curry_puffs(puff_num, puff_type):
    chicken_cost = 1.20
    fish_cost = 1.40
    total_sale = None

    if puff_type == "chicken":
        total_sale = chicken_cost * int(puff_num)
    # CR: PEP8: blank line between if statements
    elif puff_type == "fish":
        total_sale = fish_cost * int(puff_num)
    else:
        print("This is not a valid puff. Please enter fish or chicken")
        return

    # CR: This is a good place to put a comment explaining what the purpose of rounding the total sale is. For example:
    # Print relevant cost - rounded to two digits only.
    print(round(total_sale,2))

# CR: I think this should be refactored so each input is on a separate line:
# puff_num=input("number of puffs: ")
# puff_type=input("please enter fish or chicken: ")
# curry_puffs(puff_num, puff_type)
# I also don't understand why you switched the argument order, it seems there is
# no good reason to mix the variable order and then call them explicitly
curry_puffs(puff_type=input("please enter fish or chicken: "), puff_num=input("number of puffs: "))

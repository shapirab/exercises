def curry_puffs(puff_num, puff_type):
    chicken_cost = 1.20
    fish_cost = 1.40
    total_sale = None

    if puff_type == "chicken":
        total_sale = chicken_cost * int(puff_num)
    elif puff_type == "fish":
        total_sale = fish_cost * int(puff_num)
    else:
        print("This is not a valid puff. Please enter fish or chicken")
        return

    print(round(total_sale,2))


curry_puffs(puff_type=input("please enter fish or chicken: "), puff_num=input("number of puffs: "))

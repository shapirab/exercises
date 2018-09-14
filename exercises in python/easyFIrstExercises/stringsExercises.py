item1 = "salad"
item2 = "eggs"
# CR: Extra credit: String formatting can be very useful in these cases. There are two ways to do this, both of which indicate placholders in the original string.
# breakfast = "{0}, {1}".format(item1, item2)  # The indexes are indexes to the list in the format method
# breakfast = "{item1}, {item2}".format(item1=item1, item2=item2) # The keywords are arguments to the format method
# The decision which type of formatting to use (if any) depends on your needs.
breakfast = item1 + ", " + item2
print (breakfast)

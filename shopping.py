shopping = [ ]
count = 0
how_many = input("how many items of shopping do you have? > ")
how_many = int(how_many)

for item_number in range(how_many):
    item = input("What is item number " + str(item_number + 1) + "? ")
    shopping.append(item)
    count = count + 1
print(shopping)
print("You have added " + str(count) + " items to your shopping list.")
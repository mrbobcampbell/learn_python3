the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 'dimes', 3, 'quarters']

# this first kind of for loop goe through a list
for number in the_count:
    print(f"This is the {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

# we can alos build lists, first start with an empty one
elements = []

# then use the range functions to do 0 to 5 counts
for i in range(1, 11):
    print(f"Adding {i} to the list.")
    # append is a functin that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print(f"Element was {i}")

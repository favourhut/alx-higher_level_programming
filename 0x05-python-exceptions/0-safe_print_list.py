#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed_elements = 0

    # Iterate through the list to count elements
    for element in my_list:
        printed_elements += 1

    # Check if x is greater than the length of the list
    if x > printed_elements:
        x = printed_elements

    # Print the specified number of elements
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
        print()
    except IndexError:
        pass

    return printed_elements

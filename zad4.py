#Write a Python program to get the smallest number from a list
def smallest_in_list(list):
    min = list[0]
    for x in list:
        if x < min:
            min = x

    return min

print(smallest_in_list([-1,2,3,4,5]))
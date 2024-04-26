#Write a Python program to get the largest number from a list
def max_in_list(list):
    max = list[0]
    for x in list:
        if x > max:
            max = x

    return max

print(max_in_list([1,2,7,4,5]))
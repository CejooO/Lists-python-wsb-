#Write a Python program to multiply all the items in a list
def multiply_list(list):
    out = 1
    for x in list:
        out = out * x
    return out


print(multiply_list([1,2,3]))
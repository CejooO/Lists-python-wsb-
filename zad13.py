#10
def longer_words(n,string):

    word_length = []

    text = string.split(' ')

    for x in text:
        if len(x) > n:
            word_length.append(x)

    return word_length

print(longer_words(3,"hello world no"))
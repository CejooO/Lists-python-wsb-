#6

def by_last(n):
    return n[-1]

def sort_by_last(tuples):
    return sorted(tuples, key=by_last)

print(sort_by_last([(2, 2), (7, 5), (5, 1)]))
# lst = [1, 7, 3, 4]

# result = [84, 12, 28, 21]

# [7*3*4, 1*3*4, 1*7*4, 1*7*3]

def all_ints_except_at_index(lst):
    all_except = []
    for index, value in enumerate(lst):
        lst.pop(index)
        product = reduce(lambda x, y: x * y, lst)
        all_except.append(product)
        lst.insert(index,value)
    return all_except

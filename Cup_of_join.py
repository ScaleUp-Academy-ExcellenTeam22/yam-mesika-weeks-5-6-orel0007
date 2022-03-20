
def join(*lists, sep="-"):
    """
    The function get numbers of lists and return 1 list includes all lists objects separate by sign
    :param lists:
    :param sep: sign to insert between each list
    :return:list with all the given lists separate by "sep" sign
    """
    if not lists:
        return None
    new_list = []
    for x in lists:
        for y in x:
            new_list.append(y)
        new_list.append(sep)
    new_list.pop()
    return new_list


print(join([1, 2], [8], [9, 5, 6], sep='@'))
print(join([1, 2], [8], [9, 5, 6]))
print(join([1]))
print(join())


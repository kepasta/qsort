def sort(array = [43,52,1,23,75,2,22,32,53,12,11,32]):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        core = array[0]
        for x in array:
            if x < core:
                less.append(x)
            if x == core:
                equal.append(x)
            if x > core:
                greater.append(x)
        return sort(less) + equal + sort(greater)
    else:
        return array
print(sort())
# divide and conquer

def divide_and_conquer(fun):
    def decorate(elements):
        if (len(elements) < 2):
            return elements
        mid = len(elements) // 2
        return fun(decorate(elements[:mid]), decorate(elements[mid:]))
    return decorate

# mergesort

@divide_and_conquer
def merge_lists(list1, list2):
    result = []
    pos1, pos2 = 0, 0
    while pos1 < len(list1) or pos2 < len(list2):
        if pos2 >= len(list2) or (pos1 < len(list1) and list1[pos1] < list2[pos2]):
            result.append(list1[pos1])
            pos1 += 1
        else:
            result.append(list2[pos2])
            pos2 += 1
    return result

print(merge_lists([9, 4, 3, 8, 6, 5, 2, 7, 1]))

# revert

@divide_and_conquer
def reorder_lists(list1, list2):
    return list2 + list1

print(reorder_lists([9, 4, 3, 8, 6, 5, 2, 7, 1]))

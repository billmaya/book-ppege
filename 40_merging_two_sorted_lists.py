# Exercise 40 - Merging Two Sorted Lists

def mergeTwoLists(list1, list2):

    if list1 == [] and list2 == []:
        return []

    if len(list1) > 0 and len(list2) > 0:
        if list1[0] < list2[0]:
            merged = list1 + list2 
        else:
            merged = list2 + list1
    else:
        merged = list1 + list2

    for i in range(0, len(merged) - 1):

        if merged[i] > merged[i + 1]:
           merged[i], merged[i + 1] = merged[i + 1], merged[i]

    return merged



'''
list1 = [1, 3, 6]
list2 = [5, 7, 8, 9]

while list1 != [] and list2 != []:
    list1 = input('Enter first list elements separated by spaces: ').split()
    list2 = input('Enter second list elements separated by spaces: ').split()
    print(list1, list2)
    print(mergeTwoLists(list1, list2))

'''
assert mergeTwoLists([1, 3, 6], [5, 7, 8, 9]) == [1, 3, 5, 6, 7, 8, 9]
assert mergeTwoLists([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]
assert mergeTwoLists([4, 5], [1, 2, 3]) == [1, 2, 3, 4, 5]
assert mergeTwoLists([2, 2, 2], [2, 2, 2]) == [2, 2, 2, 2, 2, 2]
assert mergeTwoLists([1, 2, 3], []) == [1, 2, 3]
assert mergeTwoLists([], [1, 2, 3]) == [1, 2, 3]

def sum_of_list(list1):
    s = 0
    for i in range(len(list1)):
        s += list1[i]
    return s


l = [3,5,7,3,6]
print(sum_of_list(l))
print(sum(l))
l2 = [3,6,8,4,4,7,8]
print(sum_of_list(l2))
print(sum(l))
l3 = [3,5,6]
print(sum_of_list(l3))
print(sum(l))
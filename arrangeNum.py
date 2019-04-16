'''
Arrange the array so that the negative numbers are at the front and positive after. Do not change the order of the elements.
'''

def arrange(lst):

    for i in range(len(lst)):
        if lst[i] < 0:
            for j in range(i - 1, -1, -1):
                if lst[j] >= 0:
                    temp = lst[j]
                    lst[j] = lst[i]
                    lst[i] = temp
                    i = j

    return lst

print(arrange([]))
print(arrange([-1, -2, -3]))
print(arrange([0, 1, -3, 5, -1, 0]))
print(arrange([1, 2, 3, 4]))

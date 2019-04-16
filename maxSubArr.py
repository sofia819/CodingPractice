'''
Find max sum of subarray.
'''


def maxSubArr(lst):
    maxSoFar = lst[0]
    maxHere = lst[0]

    print(maxSoFar, maxHere, lst)
    
    for i in range(1, len(lst)):
        
        maxHere = max(maxHere + lst[i], lst[i])

        maxSoFar = max(maxSoFar, maxHere)

        print(maxSoFar, maxHere, lst)
        
    return maxSoFar

print(maxSubArr([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

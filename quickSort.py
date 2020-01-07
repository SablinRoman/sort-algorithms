from random import randint, choice

def qsort(arr):
    if len(arr) > 1:
        value = choice(arr)

        less = [x for x in arr if x < value]
        greater = [x for x in arr if x > value]
        equal = [x for x in arr if x == value]

        return qsort(less) + equal + qsort(greater)
    else:
        return arr

arr = [randint(0,100) for i in range(10)]
print(arr)
print(qsort(arr))

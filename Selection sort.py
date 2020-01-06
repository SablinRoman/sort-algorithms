from random import randint

def sort(arr):
    for index, elem in enumerate(arr):

        id_min_value = arr[index: ].index(min(arr[index: ]))
        arr[index], arr[id_min_value + index] = arr[id_min_value + index], elem

arr = [randint(0, 10) for i in range(10)]
print(arr)

sort(arr)
print(arr)
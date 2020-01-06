from random import randint

def sort(arr):
    for index, elem in enumerate(arr):
        last_index = index - 1
        while elem < arr[last_index] and last_index >= 0:
                arr[last_index + 1] = arr [last_index]
                last_index -= 1

        arr[last_index + 1] = elem
        print(arr)






arr = [randint(0,10) for i in range(10)]
print(arr)

sort(arr)

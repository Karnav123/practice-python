import random
import time

def crete_random_list(n):
    list = []
    for x in range(n):
        list.append(random.randint(1,101))
    return list

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

def bubble_sort(array):
    length = len(array)
    for i in range(length):
        for j in range(0, length - i - 1):
            if array[j] > array[j+1]:
                swap(array, j, j + 1)

def test_find1():
    array = crete_random_list(20)
    print(array)
    start_time1 = time.time()
    bubble_sort(array)
    print("--- %s seconds ---" % (time.time() - start_time1))
    print(array)

def main():
    test_find1()
    print("Tests complete.")


if __name__ == "__main__":
    main()
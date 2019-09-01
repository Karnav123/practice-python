import random
import time
def crete_random_list(n):
    list = []
    for x in range(n):
        list.append(random.randint(1,101))
    return list

def insertion_sort(array):
    length = len(array)
    for i in range(length):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key
        #print(array)

def test_find1():
    array = crete_random_list(10)
    print(array)
    insertion_sort(array)
    print(array)

def main():
    test_find1()
    print("Tests complete.")


if __name__ == "__main__":
    main()
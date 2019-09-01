import random
import time
def crete_random_list(n):
    list = []
    for x in range(n):
        list.append(random.randint(1,101))
    return list

def max_sum_subarray_brute(array): # O(n^2)
    max_sum = -99999
    start = 0
    end = 0
    length = len(array)
    for i in range(0, length):
        sum = 0
        for j in range(i, length):
            sum += array[j]
            if sum > max_sum:
                max_sum = sum
                start = i
                end = j
    return (start, end, max_sum)

# Divide and conquer approach to solve this problem
""" 
    1. mid = (high + low) / 2
    2. The subarray can be in A[0,...,mid]
    3. It can be in A[mid + 1,..., N]
    4. It can crossover the two parts including A[mid]
    Time complexity: O(nlogn)
"""
def max_sum_subarray_cross(array, low, mid, high):
    left_sum = -99999
    sum1 = 0
    max_left = -1
    for i in range(mid, low - 1, -1):
        sum1 += array[i]
        if sum1 > left_sum:
            left_sum = sum1
            max_left = i
    right_sum = -999999
    sum2 = 0
    max_right = -1
    for i in range(mid + 1, high + 1):
        sum2 += array[i]
        if sum2 > right_sum:
            right_sum = sum2
            max_right = i
    return (max_left, max_right, left_sum + right_sum)

def max_sum_subarray_divide_and_conquer(array, low, high):
    # Base case
    if high < 0:
        return (-1, -1, -1)
    if low == high:
        return (low, high, array[low])
    else:
        mid = (high + low) // 2
        left_low, left_high, left_sum = max_sum_subarray_divide_and_conquer(array, low, mid)
        right_low, right_high, right_sum = max_sum_subarray_divide_and_conquer(array, mid + 1, high)
        cross_low, cross_high, cross_sum = max_sum_subarray_cross(array, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)

def max_sum_subarray_dp(array):
    if len(array) == 0:
        return -1
    current_max = array[0]
    max_so_far = array[0]
    for i in range(1, len(array)):
        current_max = max(array[i], current_max + array[i])
        max_so_far = max(max_so_far, current_max)
    return max_so_far

def test_find1():
    array = crete_random_list(100000)
    #print(array)
    high = len(array) - 1
    start_time1 = time.time()
    start, end, max_sum = max_sum_subarray_divide_and_conquer(array, 0, high)
    print("--- %s seconds ---" % (time.time() - start_time1))
    start_time2 = time.time()
    max_sum2 = max_sum_subarray_dp(array)
    print("--- %s seconds ---" % (time.time() - start_time2))
    start_time3 = time.time()
    max_sum3 = max_sum_subarray_brute(array)
    print("--- %s seconds ---" % (time.time() - start_time3))
   
# All negative elements
def test_find2():
    array = [-13, -3, -25, -20, -3, -16, -23, -18, -20, -7, -12, -5, -22, -15, -4, -7]
    high = len(array) - 1
    start, end, max_sum = max_sum_subarray_divide_and_conquer(array, 0, high)
    max_sum2 = max_sum_subarray_dp(array)
    print(start)
    print(end)
    print(max_sum)
    print("==================")
    #print(start2)
    #print(end2)
    print(max_sum2)

def main():
    test_find1()
    print("Tests complete.")


if __name__ == "__main__":
    main()
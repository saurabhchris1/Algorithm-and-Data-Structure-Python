# Selection Sort
# arr[] = 64 25 12 22 11

# Find the minimum element in arr[0...4]
# and place it at beginning
# 11 25 12 22 64

# Find the minimum element in arr[1...4]
# and place it at beginning of arr[1...4]
# 11 12 25 22 64

# Find the minimum element in arr[2...4]
# and place it at beginning of arr[2...4]
# 11 12 22 25 64

# Find the minimum element in arr[3...4]
# and place it at beginning of arr[3...4]
# 11 12 22 25 64
# In every iteration of selection sort, the minimum element
# from the unsorted subarray is picked and moved to the sorted subarray.
# The time complexity of Selection Sort is O(n^2)

num = [64, 25, 12, 22, 11]


def selection_sort(num):

    for i in range(len(num)):

        min_idx = i

        for j in range(i + 1, len(num)):

            if num[min_idx] > num[j]:
                min_idx = j

        num[i], num[min_idx] = num[min_idx], num[i]
    return num


if __name__ == "__main__":
    num_arr = [64, 25, 12, 22, 11]

    sorted_array = selection_sort(num_arr)
    print("The sorted array is " + str(sorted_array))

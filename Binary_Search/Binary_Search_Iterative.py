# Given a sorted array arr[] of n elements, write a function to search a given element x in arr[].

# A simple approach is to do linear search.
# The time complexity of this algorithm is O(n).

# Another approach to perform the same task is using Binary Search.
# We basically ignore half of the elements just after one comparison.

# Compare x with the middle element.
# If x matches with middle element, we return the mid index.
# Else If x is greater than the mid element, then x can only lie in right half subarray after the mid element.
# So we recur for right half.
# Else (x is smaller) recur for the left half.
# Time Complexity is O(log(n))

# Binary Search Iterative Solution

# array of num[l,...,r] and finding x


def binary_search(num_arr, target):
    left = 0
    right = len(num_arr) - 1

    while right >= left:

        mid = int((left + right) / 2)

        if num_arr[mid] == target:
            return mid

        elif num_arr[mid] > target:
            right = mid - 1

        else:
            left = mid + 1

    return -1


if __name__ == "__main__":
    num = [1, 4, 5, 6, 7, 8]
    x = 6
    l = 0
    r = 5
    index_of_number = binary_search(num, x)
    if index_of_number != -1:
        print("The number " + str(x) + " is at index " + str(index_of_number) + " in array " + str(num))
    else:
        print("The number is not present")
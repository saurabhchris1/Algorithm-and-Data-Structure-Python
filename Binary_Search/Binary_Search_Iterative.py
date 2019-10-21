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

###### Binary Search Iterative Solution ######

# array of num[l,...,r] and finding x
def binarySearch(num, l, r, x):
    while (r >= l):

        mid = int((l + r) / 2)

        if num[mid] == x:
            return mid

        elif num[mid] > x:
            r = mid - 1

        else:
            l = mid + 1

    return -1


if __name__ == "__main__":
    num = [2, 4, 6, 8, 10, 11]
    x = 10
    l = 0
    r = 5
    index_of_number = binarySearch(num, l, r, x)
    print("The number " + str(x) + " is at index " + str(index_of_number) + " in array " + str(num))

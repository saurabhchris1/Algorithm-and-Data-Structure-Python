# Merge Sort
# MergeSort(arr[], l,  r)
# If r > l
#      1. Find the middle point to divide the array into two halves:
#              middle m = (l+r)/2
#      2. Call mergeSort for first half:
#              Call mergeSort(arr, l, m)
#      3. Call mergeSort for second half:
#              Call mergeSort(arr, m+1, r)
#      4. Merge the two halves sorted in step 2 and 3:
#              Call merge(arr, l, m, r)


def merge_sort(arr):
    if len(arr) > 1:
        m = len(arr) // 2

        left = arr[:m]
        right = arr[m:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):

            if left[i] < right[j]:

                arr[k] = left[i]
                i += 1

            else:

                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


if __name__ == '__main__':
    unsorted_arr = [9, 6, 4, 2, 0]
    merge_sort(unsorted_arr)
    print ("The sorted array is : " + str(unsorted_arr))

# Bubble Sort in recursive way
# Input array and size of the array


def bubble_sort_recursive(num_arr, is_sorted, size):
    len_arr = len(num_arr)
    is_swapped = is_sorted

    if size >= 0 and is_sorted == False:
        for i in range(len_arr - 1):

            if num_arr[i + 1] < num_arr[i]:
                num_arr[i], num_arr[i + 1] = num_arr[i + 1], num_arr[i]
                is_swapped = True

        if is_swapped:
            return bubble_sort_recursive(num_arr, False, size - 1)
        else:
            return num_arr
    else:
        return num_arr


if __name__ == '__main__':
    num = [2, 11, 6, 4, 7, 8]

    sorted_arr = bubble_sort_recursive(num, False, 5)

    print ("The sorted array is : " + str(sorted_arr))


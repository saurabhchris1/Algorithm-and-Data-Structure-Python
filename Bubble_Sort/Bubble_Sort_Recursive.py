# Bubble Sort in recursive way
# Input array and size of the array


def bubble_sort_recursive(num_arr, size):
    len_arr = len(num_arr)

    if size >= 0:
        for i in range(len_arr - 1):

            if num_arr[i + 1] < num_arr[i]:
                num_arr[i], num_arr[i + 1] = num_arr[i + 1], num_arr[i]

        return bubble_sort_recursive(num_arr, size - 1)

    else:
        return num_arr


if __name__ == '__main__':
    num = [2, 11, 6, 4, 7, 8]

    sorted_arr = bubble_sort_recursive(num, 5)

    print ("The sorted array is : " + str(sorted_arr))


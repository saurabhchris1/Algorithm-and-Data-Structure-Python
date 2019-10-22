# Bubble Sort is the simplest sorting algorithm that works by
# repeatedly swapping the adjacent elements if they are in wrong order


def bubble_sort(num_arr):
    len_arr = len(num_arr)

    for i in range(len_arr):

        for j in range(len_arr - i - 1):

            if num_arr[j] > num_arr[j + 1]:
                num_arr[j], num_arr[j + 1] = num_arr[j + 1], num_arr[j]

    return num_arr


if __name__ == '__main__':
    num = [64, 25, 12, 22, 11]

    sorted_arr = bubble_sort(num)

    print ("The sorted array is : " + str(sorted_arr))

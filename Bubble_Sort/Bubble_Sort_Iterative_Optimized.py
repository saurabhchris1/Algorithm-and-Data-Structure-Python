# Bubble Sort Iterative Optimized
# Print i,j will help you figure out calculations


def bubble_sort_iterative(num_arr):
    len_arr = len(num_arr)
    flag = True
    for i in range(len_arr):
        if not flag:
            break
        flag = False
        for j in range(len_arr - i - 1):
            print(i, j)

            if num_arr[j] > num_arr[j + 1]:
                flag = True
                num_arr[j], num_arr[j + 1] = num_arr[j + 1], num_arr[j]

    return num_arr


if __name__ == '__main__':
    num = [2, 11, 6, 4, 7, 8]

    sorted_arr = bubble_sort_iterative(num)

    print ("The sorted array is : " + str(sorted_arr))

# Insertion sort is a simple sorting algorithm that works the way
# we sort playing cards in our hands


def insertion_sort(arr):
    for i in range(1, len(arr)):

        key = arr[i]

        for j in range(i - 1, -1, -1):

            if key < arr[j]:

                arr[j + 1] = arr[j]
                arr[j] = key
            else:
                break

    return arr


if __name__ == '__main__':
    num = [2, 11, 6, 4, 7, 8]

    sorted_arr = insertion_sort(num)

    print ("The sorted array is : " + str(sorted_arr))

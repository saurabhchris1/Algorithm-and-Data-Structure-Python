# Insertion sort is a simple sorting algorithm that works the way
# we sort playing cards in our hands


def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


if __name__ == '__main__':
    num = [2, 11, 6, 4, 7, 8]

    sorted_arr = insertion_sort(num)

    print ("The sorted array is : " + str(sorted_arr))

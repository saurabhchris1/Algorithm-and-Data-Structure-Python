# Insertion sort is a simple sorting algorithm that works the way
# we sort playing cards in our hands


def insertion_sort(unsorted_arr):
    for i in range(1, len(unsorted_arr)):

        select_element = unsorted_arr[i]

        for j in range(i):

            select_before_element = unsorted_arr[i - j - 1]

            if select_element < select_before_element:
                unsorted_arr[i - j] = unsorted_arr[i - j - 1]
                unsorted_arr[i - j - 1] = select_element
    return unsorted_arr


if __name__ == '__main__':
    num = [2, 11, 6, 4, 7, 8]

    sorted_arr = insertion_sort(num)

    print ("The sorted array is : " + str(sorted_arr))

# Quick Sort


def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):

        if pivot > arr[j]:
            i = i + 1

            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


if __name__ == '__main__':
    num = [10, 7, 8, 9, 1, 5]

    num_len = len(num)

    quick_sort(num, 0, num_len - 1)

    print ("The sorted array is : " + str(num))

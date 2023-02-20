import numpy as np
import timeit
import matplotlib.pyplot as plt
from prettytable import PrettyTable

def partition(nums, low, high):

    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        nums[i], nums[j] = nums[j], nums[i]

def quick_sort(items, low, high):
    if low < high:
        split_index = partition(items, low, high)
        quick_sort(items, low, split_index)
        quick_sort(items, split_index + 1, high)


def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1

        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list

def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    return merge(left_list, right_list)


def heapify(nums, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heapify(nums, heap_size, largest)

def heap_sort(nums):
    n = len(nums)

    for i in range(n, -1, -1):
        heapify(nums, n, i)

    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)

def counting_sort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]
    i = size - 1

    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]

def radix_sort(array):
    max_element = max(array)
    place = 1
    while max_element // place > 0:
        counting_sort(array, place)
        place *= 10


sortings = [
    {
        "name": "Merge Sort",
        "algo": lambda arr: merge_sort(arr),
        "color": "b"
    },
    {
        "name": "Quick Sort",
        "algo": lambda arr: quick_sort(arr, 0, len(arr) - 1),
        "color": "r"
    },
    {
        "name": "Heap Sort",
        "algo": lambda arr: heap_sort(arr),
        "color": "g"
    },
    {
        "name": "Radix Sort",
        "algo": lambda arr: radix_sort(arr),
        "color": "y"
    }
]

for algo in sortings:
    elements = list()
    elements1 = list()
    start_all = timeit.default_timer()
    for i in range(10, 101):
        start = timeit.default_timer()
        a = np.random.randint(1, 1000 * i, 1000 * i)
        algo["algo"](a)
        end = timeit.default_timer()
        elements.append(len(a))
        elements1.append(end - start)

    plt.plot(elements, elements1, label=algo["name"], color = algo["color"])

# x = PrettyTable()
# x.title = ""
# x.field_names = [i*1000 for i in range(10, 101, 10)]
# elements1_r = np.round(elements1, 5)
# x.add_row(elements1_r)
# print(x)
plt.title("Sorting Algorithms")
plt.xlabel('List Length')
plt.ylabel('Time Complexity (s)')
plt.grid()
plt.legend()
plt.show()
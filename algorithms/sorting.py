def insertion_sort(data):
    """
    Simple implementation of insert_sort algorithm.

    :param list data: unsorted list

    :rtype list
    :return: sorted list
    """

    for idx_1 in range(2, len(data)):
        key = data[idx_1]
        idx_2 = idx_1 - 1
        while idx_2 > 0 and data[idx_2] > key:
            data[idx_2 + 1] = data[idx_2]
        data[idx_2 + 1] = key

    return data

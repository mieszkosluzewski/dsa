def insertion_sort(data, reverse=False):
    """
    Simple implementation of insert_sort algorithm.

    :param list data: unsorted list

    :rtype list
    :return: sorted list
    """

    for idx_1 in range(1, len(data)):
        key = data[idx_1]
        idx_2 = idx_1 - 1

        def check_key(idx):
            """
            Check if key is greater/smaller than item in idx position.

            :param int idx: index of item

            :rtype bool
            :return True if key is greater and reverse is False or if key is smaller and reverse is True
            """
            return data[idx] > key if not reverse else data[idx] < key

        while idx_2 >= 0 and check_key(idx_2):
            data[idx_2 + 1] = data[idx_2]
            idx_2 -= 1
        data[idx_2 + 1] = key

    return data

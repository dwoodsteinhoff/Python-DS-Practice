def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    list_counter = {}
    for num in nums:
        if not num in list_counter:
            list_counter[num] = 1
        else:
            list_counter[num] += 1

    max_val = max(list_counter.values())

    for (num,val) in list_counter.items():
        if val == max_val:
            return num

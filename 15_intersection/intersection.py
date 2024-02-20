def intersection(l1, l2):
    """Return intersection of two lists as a new list::
    
        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]
        
        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]
        
        >>> intersection([1, 2, 3], [3, 4])
        [3]
        
        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """
    set_l1 = {val for val in l1}
    set_l2 = {val for val in l2}
    intersection_set = set_l1 & set_l2
    intersection_list = [val for val in intersection_set]

    return intersection_list
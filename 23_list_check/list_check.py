def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    true_list=[]
    for item in lst:
        if isinstance(item,list):
            true_list.append(item)
        else:
            return False
    if len(true_list) == len(lst):
        return True
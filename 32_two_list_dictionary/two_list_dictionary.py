def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """
    if len(keys) > len(values):
        key_val_dict = {}
        for key in keys:
            if keys.index(key) > len(values) - 1:
                key_val_dict.update({key : None})
            else:
                key_val_dict.update({key : values[keys.index(key)]})
        return key_val_dict
    else:
        return {key : values[keys.index(key)] for key in keys}
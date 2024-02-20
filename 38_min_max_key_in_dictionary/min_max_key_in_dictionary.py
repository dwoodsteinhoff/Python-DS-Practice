dictionary_1 = {2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'}
dictionary_2 = {"apple": "red", "cherry": "red", "berry": "blue"}

def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """
    d_list = [key for key in d.keys()]
    d_list.sort()
    return (d_list[0],d_list[-1])
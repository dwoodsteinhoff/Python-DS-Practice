def triple_and_filter(nums):
    """Return new list of tripled nums for those nums divisible by 4.

    Return every number in list that is divisible by 4 in a new list,
    except multipled by 3.
    
        >>> triple_and_filter([1, 2, 3, 4])
        [12]
        
        >>> triple_and_filter([6, 8, 10, 12])
        [24, 36]
        
        >>> triple_and_filter([1, 2])
        []
    """
    # even_nums = []
    # even_multiplier = 1
    # for num in nums:
    #     if num % 2 == 0:
    #         even_nums.append(num)
    # if len(even_nums) == 0:
    #     return 1
    # else:
    #     for even in even_nums:
    #         even_multiplier = even * even_multiplier
    # return even_multiplier

    nums_div_4 = []
    nums_div4_mult3 = []
    for num in nums:
        if num % 4 == 0:
            nums_div_4.append(num)

    if len(nums_div_4) == 0:
        return nums_div_4
    else:
        for num in nums_div_4:
           nums_div4_mult3.append(num * 3)
    return nums_div4_mult3
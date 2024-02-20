def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """

    # minus 2 because you will be adding the values at indexes up to +2 from the index of num as you iterate through nums. If you go above the maximum index in the list nums - an error will return (aka can't use len(nums)-1 because you will go past the last index in the list).

    for num in range(len(nums)-2):
        if (nums[num] + nums[num+1] + nums[num+2]) % 2 == 1:
            return True
        
    return False
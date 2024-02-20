def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1_list = list(str(num1))
    num2_list = list(str(num2))

    num1_freq = list({num: num1_list.count(num) for num in num1_list}.items())
    num2_freq = list({num: num2_list.count(num) for num in num2_list}.items())

    list_check = []

    for value1 in num1_freq:
        for value2 in num2_freq:
            if value1 == value2:
                list_check.append((value1,value2))

    if len(list_check) == len(num2_freq) and len(num1_freq) == len(list_check):
        return True
    else:
        return False
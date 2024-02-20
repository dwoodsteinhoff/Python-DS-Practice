def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    string_list = [char for char in s]
    string_list_vowels = [char for char in s if char in 'aeiouAEIOU']
    string_list_vowels.reverse()

    reverse_vowels_list = []

    for ltr in string_list:
        if ltr not in 'aeiouAEIOU':
            reverse_vowels_list.append(ltr)
        if ltr in 'aeiouAEIOU' and len(string_list_vowels) > 0:
            reverse_vowels_list.append(string_list_vowels[0])
            string_list_vowels.pop(0)

    return "".join(reverse_vowels_list)

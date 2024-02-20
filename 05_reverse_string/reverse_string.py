def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    if isinstance(phrase,str) == True:
        return phrase[::-1]
    else:
        return None

names = [
{'first': 'Ada', 'last': 'Lovelace'},
{'first': 'Grace', 'last': 'Hopper'},
]

def extract_full_names(people):
    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names.

        >>> names = [
        ...     {'first': 'Ada', 'last': 'Lovelace'},
        ...     {'first': 'Grace', 'last': 'Hopper'},
        ... ]

        >>> extract_full_names(names)
        ['Ada Lovelace', 'Grace Hopper']
    """
    people_list = []
    for person in people:  
        person_list = [value for value in person.values()]
        people_list.append(f'{person_list[0]} {person_list[1]}')
    return people_list

        
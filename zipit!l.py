def zip_lists(list1, list2):
    """
    Returns:
    1. Zipped list of tuples from both lists
    2. Zipped list with the second list in reverse
    3. Dictionary zipped from both lists
    """
 
    zipped_list = list(zip(list1, list2))

    zipped_reversed = list(zip(list1, reversed(list2)))

    zipped_dict = dict(zip(list1, list2))

    return zipped_list, zipped_reversed, zipped_dict


list_a = ['a', 'b', 'c']
list_b = [1, 2, 3]

zipped, zipped_rev, zipped_dict = zip_lists(list_a, list_b)

print("1. Zipped List:", zipped)
print("2. Zipped with Reversed Second List:", zipped_rev)
print("3. Zipped into Dictionary:", zipped_dict)

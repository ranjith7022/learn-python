def sum_nested_list(lst):
    count = 0
    for item in lst:
        if isinstance(item, list):
            count += sum_nested_list(item)
        else:
            count += item
    return count
def sum_nested_list(lst):
    if len(lst) == 0:
        return 0
    return sum(i if isinstance(i, int) else sum_nested_list(i) for i in lst )

def sum_nested_list(lst):
    if isinstance(lst,list) and len(lst) == 0 :
        return 0
    if isinstance(lst,list) and len(lst) > 1:
        return sum_nested_list(lst[0]) + sum_nested_list(lst[1:])
    elif isinstance(lst,int):
        return lst
    elif isinstance(lst,list) and len(lst) == 1:
        return sum_nested_list(lst[0])
    
    import functools

    def sum_nested_list(lst):
        return functools.reduce(lambda sum, item: sum + item if isinstance(item, int) else sum + sum_nested_list(item), lst, 0)
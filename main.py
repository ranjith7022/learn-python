def sum_of_odd_numbers(end):
    total = 0
    for i in range(1, end):
        if i%2 == 1:
           total += i
    return total

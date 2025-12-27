def recursion_helper(days, i):
    if days < i:
        return
    else:
        print("Day ", i)
    recursion_helper(days, i + 1)


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    i = 1
    recursion_helper(days, i)

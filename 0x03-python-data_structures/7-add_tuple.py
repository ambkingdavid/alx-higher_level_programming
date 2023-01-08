#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    add_list = []
    if len(tuple_a) > 2:
        tuple_a = (tuple_a[0], tuple_a[1])
    if len(tuple_b) > 3:
        tuple_b = (tuple_b[0], tuple_b[1])
    for i in range(min(len(tuple_a), len(tuple_b))):
        add_list.append(tuple_a[i] + tuple_b[i])
    for i in range(len(tuple_a) - len(tuple_b)):
        add_list.append(tuple_a[len(tuple_b) + i])
    for i in range(len(tuple_b) - len(tuple_a)):
        add_list.append(tuple_b[len(tuple_a) + i])
    return tuple(add_list)

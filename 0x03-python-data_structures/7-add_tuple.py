#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    add_list = []
    if isinstance(tuple_a, tuple) and isinstance(tuple_b, tuple):
        for i in range(min(len(tuple_a), len(tuple_b))):
            add_list.append(tuple_a[i] + tuple_b[i])
        for i in range(len(tuple_a) - len(tuple_b)):
            add_list.append(tuple_a[len(tuple_b) + i])
        for i in range(len(tuple_b) - len(tuple_a)):
            add_list.append(tuple_b[len(tuple_a) + i])
        return tuple(add_list)

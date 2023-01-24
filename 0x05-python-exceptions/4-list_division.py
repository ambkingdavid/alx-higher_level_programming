#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = 0
    new_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            new_list.append(result)
    return new_list
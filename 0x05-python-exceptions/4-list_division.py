#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    
    for i in range(list_length):
        try:
            div_result = 0
            if type(my_list_1[i]) not in (int, float) or type(my_list_2[i]) not in (int, float):
                print("wrong type")
            else:
                if my_list_2[i] == 0:
                    print("division by 0")
                else:
                    div_result = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")
        finally:
            result.append(div_result)
    
    return result


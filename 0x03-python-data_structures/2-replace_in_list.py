#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list

# Example usage
if __name__ == "__main__":
    my_list = [10, 20, 30, 40, 50]
    index = 2
    new_element = 35
    result = replace_in_list(my_list, index, new_element)
    print("Updated list:", result)

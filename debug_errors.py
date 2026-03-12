def get_list_element(my_list, index):
    try:
        return my_list[index]
    except IndexError:
        print(f"Error: Index {index} is out of bounds")
        return None
    except TypeError:
        print("Error: Input is not a list")
        return None


# Example calls
my_list = [10, 20, 30]

print(get_list_element(my_list, 1))   # valid index
print(get_list_element(my_list, 5))   # out-of-bounds
print(get_list_element("hello", 0))   # wrong type
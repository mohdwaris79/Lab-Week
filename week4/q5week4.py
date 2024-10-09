def same_last(lst):
    if len(lst) > 0:
        return lst[0] == lst[-1]  # Check if first and last elements are the same
    return False  # Return False if the list is empty

# Example usage
my_list = [1, 2, 3, 1]  # Example list to test
print(same_last(my_list))  # Call the function and print the result

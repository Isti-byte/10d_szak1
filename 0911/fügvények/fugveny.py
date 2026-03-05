import random

Lista =[]

def generate_random_list(size, lower_bound, upper_bound):
    """Generates a list of random integers."""
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]

def delete_duplicates(input_list):
    """Removes duplicates from a list."""
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list
 
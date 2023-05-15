import random

# create a list with 100 random numbers
my_list = [random.randint(1, 1000) for _ in range(100)]

# sort the list in ascending order using built-in function
my_list_asc = sorted(my_list)

# sort the list in descending order using built-in function
my_list_desc = sorted(my_list, reverse=True)

print(my_list_asc)
print(my_list_desc)

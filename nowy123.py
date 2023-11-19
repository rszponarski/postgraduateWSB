

my_list = [1, 2, 3, 1, 1, 3, 6]
my_set = set(my_list)

my_set.add(55)
my_set.remove(1)

new_list = list(my_set)
print(new_list)
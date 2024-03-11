my_list = [1, 2, 3, 4, "test", True, False]

print(my_list[0])
print(my_list[2:])
print(my_list[:6])

my_list.append(6)

print("index: ", my_list.index(6))

my_list.insert(2, 10)
print(my_list)

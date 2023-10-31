from task_1 import input_list

h = input_list()

print(list(filter(lambda x: x >= 0, h)))

print(list(filter(lambda g: g % 2 == 0, h)))

l1 = len(list(filter(lambda g: g > 0, h)))
l2 = len(list(filter(lambda g: g == 0, h)))
l3 = len(list(filter(lambda g: g < 0, h)))
print(l1, l2, l3)


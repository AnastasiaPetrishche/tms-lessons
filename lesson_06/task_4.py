from task_1 import input_list
from functools import reduce

p = input_list()

print(reduce(lambda x, y: x + y, p))
print(reduce(lambda x, y: min(x, y), p))
print(reduce(lambda x, y: x * y, p))

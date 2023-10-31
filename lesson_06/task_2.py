from task_1 import input_list

l = input_list()

print(list(map(lambda x: x * 100, l)))

print(list(map(lambda a: str(a), l)))

print(list(map(lambda d: round(d / 100), l)))






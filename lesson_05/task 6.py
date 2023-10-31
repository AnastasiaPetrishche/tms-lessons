def list_sum(sp):
    s = 0
    for i in sp:
        s += i
    return s

assert list_sum([1, 2, 3]) == 6

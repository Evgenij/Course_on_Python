def extra_enumerate(lst):
    curr_sum = 0
    s = sum(lst)
    for i in range(len(lst)):
        curr_sum += lst[i]
        frac = curr_sum/s
        yield (i, lst[i], curr_sum, frac)

source_list = [1,3,4,2]
for i, elem, sum, frac in extra_enumerate(source_list):
    print(elem, sum, frac)
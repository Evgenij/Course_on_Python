
def frange(start, end, step):
    while start + step < end:
        start = start + step
        yield start

for x in frange(1, 5, 0.1):
    print('{:.1f}'.format(x))
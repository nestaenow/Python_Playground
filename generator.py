def my_range(x):
    i = 0
    while i < x:
        yield i
        i += 1
for x in my_range(5):
    print(x)

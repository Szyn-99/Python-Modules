def a_function(*a, **k):
    print("hado kwargs", k)
    print("hado args", a)


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        old_a = a
        a = b
        b = old_a + b


a_function("ak", "1337", 42, hada="ayman")

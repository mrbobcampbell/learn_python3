def line_counter(x):
    lines = 0
    with open(x) as f:
        for line in f:
            lines += 1
    print(lines)
    return lines


def bob(x):
    lines = line_counter(x)
    with open(x) as f:
        for i in range(0, lines):
            print(f.readline())


def fma(x):
    with open(x) as f:
        ab = 3
        for i in range(0, ab):
            print(f.readline())


fma("test.txt")
bob("test.txt")

a = 7
b = 5
def baba(a, b):
    if a + b == 0:
        return 0
    if a > b:
        return b + baba(a-1, b)
    return a + baba(a, b-1)
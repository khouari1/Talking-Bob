def squared(x):
    total = 0
    x = int(x)
    total = x**2
    return total
def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    else:
        y = x - 1
        while y > 1:
            if x % y == 0:
                return False
            else:
                y -=1
        else:
            return True

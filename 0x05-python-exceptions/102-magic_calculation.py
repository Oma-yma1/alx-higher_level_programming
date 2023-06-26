def magic_calculation(a, b):
    result = 0
    for j in range(1, 3):
        try:
            if j > a:
                raise Exception("Too far")
            else:
                res = += (a ** b) / j
        except:
            res = a + b
            break
    return (result)

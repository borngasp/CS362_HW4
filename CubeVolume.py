
def volume(x):

    if ((type(x) == int or type(x) == float) and x >= 0):
        return x * x * x

    else:
        return "Not a valid cube"
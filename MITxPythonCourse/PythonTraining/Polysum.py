
def polysum(n,s):
    """
    n: number of sides
    s: side lengh

    return: sum of area and perimeter of polysum
    """
    import math
    area = (0.25*n*s**2.0)/math.tan((math.pi/n))
    perimeter = n*s

    return round ((area + perimeter**2), 4)


print (polysum (35,30))

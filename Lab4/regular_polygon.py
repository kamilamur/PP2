import math
def polygon_area(n, s):
    return (n * s**2) / (4 * math.tan(math.pi / n))


n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))
area = polygon_area(n, s)
print(f"The area of the polygon is: {area:.0f}")
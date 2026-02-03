from math import sqrt

# Returning a tuple – stable output
def parse_status():
    return (200, "OK", {"Content-Type": "text/html"})

code, message, headers = parse_status()
print("Parsed:", code, message)

# Accepting tuples – promise not to modify
def calculate_distance(point_a: tuple[float, float], point_b: tuple[float, float]) -> float:
    x1, y1 = point_a
    x2, y2 = point_b
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

dist = calculate_distance((10, 20), (30, 40))
print("Distance:", dist)

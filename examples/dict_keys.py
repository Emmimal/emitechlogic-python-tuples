# This fails with lists
try:
    cache = {}
    key = [1, 2, 3]
    cache[key] = "value"
except TypeError as e:
    print("List as key fails:", e)

# This works with tuples
cache = {}
cache_key = (1, 2, 3)
cache[cache_key] = "cached value"
print("Tuple as key works:", cache[(1, 2, 3)])

# Real-world example: coordinates
grid = {}
position = (10, 25)
grid[position] = "treasure"
print("Treasure at (10, 25):", grid[(10, 25)])

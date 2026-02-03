import sys

# Compare memory usage
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)

print("Memory Comparison:")
print(f"List size: {sys.getsizeof(my_list)} bytes")
print(f"Tuple size: {sys.getsizeof(my_tuple)} bytes")
print(f"Savings: {sys.getsizeof(my_list) - sys.getsizeof(my_tuple)} bytes\n")

# Larger example
large_list = list(range(1000))
large_tuple = tuple(range(1000))

print("With 1000 elements:")
print(f"List size: {sys.getsizeof(large_list)} bytes")
print(f"Tuple size: {sys.getsizeof(large_tuple)} bytes")

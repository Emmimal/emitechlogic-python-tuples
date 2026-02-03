# Tuple with mutable content
data = (1, [2, 3])
print("Original:", data)

# Cannot reassign element
try:
    data[1] = [4, 5]
except TypeError as e:
    print("Cannot reassign:", e)

# But can mutate the list inside
data[1].append(4)
print("After mutating inner list:", data)

# Best practice: only immutable contents for true immutability
safe_tuple = (1, "hello", (2, 3))
print("Safe tuple:", safe_tuple)

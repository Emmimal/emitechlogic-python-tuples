# Bad: building tuple by concatenation (slow)
def bad_collect(n):
    scores = ()
    for i in range(n):
        scores = scores + (i,)
    return scores

# Good: use list then convert
def good_collect(n):
    scores = []
    for i in range(n):
        scores.append(i)
    return tuple(scores)

print("Bad way (small n):", bad_collect(5))
print("Good way:", good_collect(5))

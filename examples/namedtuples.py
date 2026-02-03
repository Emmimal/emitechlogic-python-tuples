from collections import namedtuple
from datetime import date

# Regular tuple – unclear
user = (42, "active", 1.5)
print("Regular tuple index 1:", user[1])

# Named tuple – self-documenting
User = namedtuple('User', ['id', 'status', 'rating'])
user_named = User(id=42, status="active", rating=1.5)
print("Named tuple status:", user_named.status)

# Another example
Quarter = namedtuple('Quarter', ['start', 'end'])
q1 = Quarter(date(2024, 1, 1), date(2024, 3, 31))
print("Q1 dates:", q1.start, "to", q1.end)

import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3


# What did you see on line 1?
# What was the smallest number you could have seen, what was the largest?
# 5.
# The smallest number could have seen is 5, largest is 20.

# What did you see on line 2?
# What was the smallest number you could have seen, what was the largest?
# Could line 2 have produced a 4?
# 5.
# The smallest number could have seen is 3, largest is 9.
# No. The result only could have been odd number from 3 to 9.

# What did you see on line 3?
# What was the smallest number you could have seen, what was the largest?
# 4.700498670772694
# The smallest number could have seen is 2.5, largest is close to, but not exactly, 5.5.

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100))

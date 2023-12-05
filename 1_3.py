# Importing the whole module
import math

# Using functions from the math module
print(math.sqrt(16))  # Output: 4.0

# Importing specific functions from a module
from random import randint

# Using the imported function
random_number = randint(1, 10)
print(f"Random number between 1 and 10: {random_number}")

# Importing with an alias
import datetime as dt

# Using the alias to access functions/classes
current_time = dt.datetime.now()
print(f"Current time: {current_time}")



# Using functions/classes from the module

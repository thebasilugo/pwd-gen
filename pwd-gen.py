import random
import string

# Define the set of characters to choose from
# They include 'string.ascii_uppercase', 'string.ascii_lowercase', 'string.digits'

characters = string.ascii_uppercase + string.ascii_lowercase + string.digits

# Generate a random password of length '8'
password = ''.join(random.choice(characters) for i in range(8))

# Print the password
print(password)


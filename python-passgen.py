import random
import string

def randompass():
    chars = string.ascii_letters + string.digits 
    size = 3
    return ''.join (random.choice(chars) for x in range(size,27))

n = 0
while n < 50: 
    print (randompass())
    n=n+1 
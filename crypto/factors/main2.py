from factors import factors
from time import time

minimum = int(input( "Enter a minimum number: " ))

maximum = int(input( "Enter a minimum number: " ))

increment = int(input( "Enter a number to increment by: " ))

for i in range(minimum, maximum, increment):
    
    # Start the timer
    start = time()

    result = factors(i)

    # Start the timer
    end = time()
    total = end - start

    print("%s, %s" % (i, total))



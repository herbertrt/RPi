from factors import factors
from time import time

number = 0

number = int(input( "Enter a number: " ))

    
# Start the timer
start = time()

result = factors(number)

# Start the timer
end = time()

print(result)


print( str(end - start) + " seconds" )

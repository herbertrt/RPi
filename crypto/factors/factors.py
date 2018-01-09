import math

def factors( number ):

    factors = []

    index = 0

    # check up to  
    for i in range(2, math.floor(math.sqrt(number)) + 1):
        
        if number % i == 0:

            factors += [[i, number//i]]

    return( factors )

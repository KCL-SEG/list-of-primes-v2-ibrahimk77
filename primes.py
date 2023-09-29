"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []

    if number_of_primes <= 0:
        raise ValueError("Number can't be 0 or less")


    num = 2
    list.append(num)

    while(len(list) < number_of_primes):

        prime = True
        num+=1
        for i in list:
            if num%i == 0:
                prime = False
            
        if prime:
            list.append(num)
        


    
    return list
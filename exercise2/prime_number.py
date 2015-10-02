def is_prime(n):
    '''Check if integer n is a prime'''

    n = abs(int(n))    # make sure n is a positive integer
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    

    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True



class Number():
    def __init__(self, n):
        self.value = n

    def is_prime(self):
        return is_prime(self.value)

    def __repr__(self):
        return self.value
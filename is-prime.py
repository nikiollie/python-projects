def is_prime(num):

    if num <= 1:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False 
    return True

def is_prime_optimized(num):
    if num <= 1:
        return False
    
    #from 2 to square root of num
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
                

print(is_prime_optimized(11))
print(is_prime_optimized(13))
print(is_prime_optimized(16))
print(is_prime_optimized(4))
print(is_prime_optimized(1))
print(is_prime_optimized(3))
print(is_prime_optimized(5))
print(is_prime_optimized(17))        
print(is_prime_optimized(169))

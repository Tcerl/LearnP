from collections import deque

def is_prime(n):
    if n <=1:
        return False
    if n == 2:
        return True
    if n % 2 ==0:
        return False
    p = 3
    while p * p <= n:
        if n % p ==0:
            return False
        p += 2
    return True

def is_super_prime(n):
    innitial_super_prime = [2,3,5,7]
    super_prime = []
    
    queue = deque(innitial_super_prime)
    
    while queue:
        current = queue.popleft()
        if current <= n:
            super_prime.append(current)
        for i in range(1,10):
            new_number = current*10+i
        if new_number <= n and is_prime(new_number):
            queue.append(new_number)
            
    return sorted(super_prime)

n = int(input())
super_find_primes = is_super_prime(n)
print(super_find_primes)
    
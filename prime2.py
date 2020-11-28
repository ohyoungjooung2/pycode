import math
import time
def is_prime_v1(n):
    """Return prime"""
    if n == 1:
        return False
    for d in range(2,n):
        if n % d == 0:
           return False
    return True

def is_prime_v2(n):
    """Return prime"""
    if n == 1:
        return False # 1 is not prime

    max_divisor = math.ceil(math.sqrt(n))
    for d in range(2,max_divisor):
        if n % d == 0:
            return False
    return True

def is_prime_v3(n):
    """Return prime"""
    if n == 1:
      return False

    # It it's even and not 2, then it's not prime
    if n == 2:
      return True

    if n > 2 and n % 2 == 0:
      return False

    max_divi = math.ceil(math.sqrt(n))
    for d in range(3,max_divi,2):
        if n % d == 0:
            return False
    return True


t0 = time.time()
for n in range(1,21):
    print(n,is_prime_v2(n))
t1 = time.time()
print(f"Time required: {t1 - t0}")

import os
os.system('sleep 3')
t3 = time.time()
for n in range(1,21):
    print(n,is_prime_v3(n))
t4 = time.time()
print(f"Time required: {t4 - t3}")

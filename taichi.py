import taichi as ti
import time

ti.init()

@ti.func
def is_prime(n: int):
    result = True
    for k in range(2, int(n ** 0.5) + 1):
        if n % k == 0:
            result = False
            break
    return result

@ti.kernel
def count_primes(n: int) -> int:
    count = 0
    for k in range(2, n):
        if is_prime(k):
            count += 1
    return count





time1=time.time()
count_primes(100000)
time2=time.time()
time=time2-time1
print(time)

# 无装饰器前耗时:   3.6s(1000000)      太久了,一个小时+ (100000000);
# 用了装饰器后耗时: 0.09s(1000000)   36s(100000000)







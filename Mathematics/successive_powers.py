from math import gcd
from sympy import isprime

# 주어진 정수 배열
nums = [588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237]

# 1. p 찾기: 모든 숫자의 차이를 계산하고 GCD를 구함
differences = [abs(nums[i] - nums[i + 1]) for i in range(len(nums) - 1)]
p_candidate = gcd(*differences)

# p_candidate가 소수인지 확인하고 소수가 아니면 다음 GCD 계산
if not isprime(p_candidate):
    raise ValueError("p_candidate is not prime")

p = p_candidate
print(f"Found p: {p}")

# 2. x 찾기: nums[0] = x^1 % p, nums[1] = x^2 % p ... 를 사용
x = None
for candidate in range(2, p):
    valid = True
    for i, num in enumerate(nums):
        if pow(candidate, i + 1, p) != num:  # i+1은 지수 k
            valid = False
            break
    if valid:
        x = candidate
        break

if x is None:
    raise ValueError("x not found")

print(f"Found x: {x}")

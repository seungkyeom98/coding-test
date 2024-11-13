# from functools import reduce
def gcd(a, b):  # 최대공약수
    while b > 0:
        a,b = b, a % b
    return a


# def lcm(a, b): #최대공배수
#     return a * b / gcd(a, b) 

# def solution(arr):
#     # answer = 0
# #     multiply=1
# #     for i in arr:
# #         multiply*=i
# #     for i in range(max(arr), multiply + 1):
# #         for j in arr:
            
# #         if i % a == 0 and i % b == 0:
# #             answer= i
# #             break
           
#     return reduce(lcm, arr)
# from math import gcd
from functools import reduce

# 두 수의 최소공배수 계산 함수
def lcm(a, b):
    return a * b // gcd(a, b)

# 리스트의 모든 원소에 대한 최소공배수를 구하는 solution 함수
def solution(arr):
    return reduce(lcm, arr)

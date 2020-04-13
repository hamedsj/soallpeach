import math
import sys

file_input = sys.argv[1]

def check_is_prime(number: int):
    root = int(math.sqrt(number))
    for n in range(2, number):
        if number % n == 0:
            print("0")
            return
    print("1")


with open(str(file_input)) as nums:
    for num in nums:
        check_is_prime(int(num))

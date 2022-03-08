# Per trovare le combinazioni possibili troviamo prima il massimo comune divisore (gcd)
# e troviamo tutti i numeri che lo dividono.

from fractions import gcd
from functools import reduce

def find_gcd(list):
    x = reduce(gcd, list)
    return x

fi = open("input.txt")

T = int(fi.readline())

fo = open("output.txt", "w")

for k in range(0, T):
    fi.readline()
    num = ()
    nums = [int(n) for n in fi.readline().split()]

    gdc = find_gcd(nums)
    divisorNumber = 1

    for i in range(1, gdc):
        if gdc % i == 0:
            divisorNumber = divisorNumber + 1


    fo.write("Case #{}: {}\n".format(k + 1, divisorNumber))
    print(divisorNumber)

fo.close()
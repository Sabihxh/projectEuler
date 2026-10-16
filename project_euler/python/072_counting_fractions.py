from utils import timeit


@timeit
def run(n: int):
    total = 0
    for denominator in range(1, n + 1):
        for numerator in range(1, denominator):
            # if math.gcd(numerator, denominator) == 1:
            total += 1
    print(total)


run(8)

run(10_000)

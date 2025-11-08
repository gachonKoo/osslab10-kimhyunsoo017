def divisors(n):
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result

if __name__ == "__main__":
    n = int(input())
    result = divisors(n)
    for i in result:
        print(i, end=' ')

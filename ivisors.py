import sys
from math import isqrt

def read_int() -> int:
    # 1) 명령행 인자 우선
    if len(sys.argv) > 1 and sys.argv[1].strip():
        return int(sys.argv[1])
    # 2) 없으면 stdin에서 읽기
    data = sys.stdin.read().strip()
    return int(data)

def main():
    n = read_int()
    divisors = []
    for i in range(1, isqrt(n) + 1):
        if n % i == 0:
            divisors.append(i)
            j = n // i
            if j != i:
                divisors.append(j)
    divisors.sort()
    print(" ".join(str(x) for x in divisors))

if __name__ == "__main__":
    main()

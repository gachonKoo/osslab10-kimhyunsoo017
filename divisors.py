import sys

def divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

if __name__ == "__main__":
    # 표준입력/파일리다이렉트/테스트 모두 대응
    raw = sys.stdin.read().strip().split()
    if raw:
        n = int(raw[0])
    else:
        n = int(input().strip())
    ds = divisors(n)
    # 한 줄, 공백 구분 출력 (여분 공백/문구 금지)
    print(" ".join(str(x) for x in ds))

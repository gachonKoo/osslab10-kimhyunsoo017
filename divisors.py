import sys

number = int(sys.argv[1])   # 명령줄 인자로 숫자 입력받기

for i in range(1, number + 1):  # 1부터 number까지 반복
    if number % i == 0:         # 나머지가 0이면 약수
        print(i, end=" ")       # 공백으로 구분하여 출력

print()  # 마지막 줄바꿈

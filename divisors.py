import sys

number = int(sys.argv[1])

divs = []
for i in range(1, number + 1):
    if number % i == 0:
        divs.append(str(i))

print(" ".join(divs))

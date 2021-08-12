import sys

case = int(sys.stdin.readline())
results = []
while case > 0:
    string = sys.stdin.readline()
    case -= 1
    digit = string.split()
    result = int(digit[0]) + int(digit[1])
    results.append(result)

for r in results:
    print(r)
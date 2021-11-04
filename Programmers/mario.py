'''
Mario Game
LG careers coding test sample 2

버섯의 개수 1 <= N <= 150,000
0번에서 N-1번까지의 나열됨
버섯에 써 있는 숫자 1<= P <=500

1. 버섯은 0번부터 순서대로 먹을지 먹지 않을지 결정해야함
2. 첫 번째로 먹은 버섯의 숫자만큼 키가 커짐
3. 두 번째로 먹은 버섯의 숫자만큼 키가 작아짐
4. 홀수 번째는 커지고 짝수 번째는 작아짐
ex)
7 2 1 8 4 3 5 6
7 -2 +1 -8 +4 -3 +5 -6 = -2

첫 번째 줄 버섯의 개수 N
두 번째 줄 버섯의 값 P가 N개 적힘

8
7 2 1 8 4 3 5 6

최대로 키울 수 있는 최대값
출력 17
+ : 7,8,6
- : 1,3

'''

N = int(input())
P = list(map(int,input().split()))
print('P:',P)
if N % 2 == 0:
    cnt = N//2
else:
    cnt = N//2 + 1

size = 0
plus = True
# 먹을 수 있는 기회는 짝수는 N/2번 홀수는 N//2+1 번
for idx in range(N):
    if plus and cnt != 0:
        if idx == N-1:
            size += P[idx]
            break
        if P[idx] in sorted(P)[N//2:] and P[idx] > P[idx+1]:
            size += P[idx]
            cnt -= 1
            plus = False
    if not plus and cnt != 0:
        if idx == N-1:
            break
        if P[idx] in sorted(P)[:N//2] and P[idx] < P[idx+1]:
            size -= P[idx]
            plus = True
print('size:',size)
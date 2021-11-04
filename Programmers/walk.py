'''
산책로 문제

직원 수 1<= N <= 100,000
산책 시간 1< T<= 1,000,000,000
직원 i 출발 위치 0 <= Pi <=1,000,000,000
직원 i 산책 속도 0 <= Si <=1,000,000,000

첫째 줄 직원 수 N, 산책 시간 T
N회 입력 받고 현재 위치와 산책 속도 입력
'''
from collections import Counter

N, T = map(int,input().split())
position = []
speed = []
predict = []
current = []
for _ in range(N):
    p, s = map(int,input().split())
    position.append(p)
    speed.append(s)

print("pos:",position)
print('spd:',speed)


for idx in range(N):
    pre = position[idx] + speed[idx] * T
    predict.append(pre)

print("predict:",predict)


max = predict[-1]
for idx in range(-2,-1*N-1, -1):
    if predict[idx] >= max:
        predict[idx] = max
    elif predict[idx] < max:
        max = predict[idx]

print('current:',predict)

print(len(dict(Counter(predict)).keys()))
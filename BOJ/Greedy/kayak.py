'''
2891번 카약과 강풍
바로 앞 뒤 팀에게만 카약을 빌려줄 수 있음
출발하지 못한 팀의 최솟값

N 팀의 수 S 카약이 손상된 팀의 수 R 카약을 하나 더 가져온 팀의 수 (2<= N <= 10, 1<= S, R<=N)
카약이 손상된 팀의 번호
카약을 더 가져온 팀의 수


입력 1
5 2 1
2 4
3

출력 1
1

입력 2
5 2 3
2 4
1 3 5

출력 2
0
'''
# N,S,R = map(int,input().split())
# dmg = list(map(int,input().split()))
# spare = list(map(int,input().split()))
# dmg_copy = dmg.copy()

# for idx in range(len(dmg)):
#     if dmg[idx] - 1 in spare: 
#         spare.remove(dmg[idx]-1)
#         dmg_copy.remove(dmg[idx])
#         continue
#     if dmg[idx] + 1 in spare:
#         spare.remove(dmg[idx]+1)
#         dmg_copy.remove(dmg[idx])
#         continue

# print(len(dmg_copy))

N,S,R = map(int,input().split())
dmg = list(map(int,input().split()))
spare = list(map(int,input().split()))
dmg_copy = dmg.copy()

for idx in range(len(dmg)):
    if dmg[idx] in spare:
        spare.remove(dmg[idx])
        dmg_copy.remove(dmg[idx])

dmg = dmg_copy.copy()

for idx in range(len(dmg)):
    if dmg[idx] - 1 in spare: 
        spare.remove(dmg[idx]-1)
        dmg_copy.remove(dmg[idx])
    elif dmg[idx] + 1 in spare:
        spare.remove(dmg[idx]+1)
        dmg_copy.remove(dmg[idx])

print(len(dmg_copy))
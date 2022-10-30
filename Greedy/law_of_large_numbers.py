#2019 국가 교육기관 코딩 테스트
#풀이시간: 30분/ 제한시간: 1초/ 메모리 제한: 128MB/ 난이도: 하
import sys

n, m, k = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
cnt = 0 ; ans = 0

def big_and_next_big(list_in):          #가장 큰수랑 두번째로 큰수 구하는 함수
    big = 0; next_big = 0

    for i in list_in:
        if big <= i:
            next_big = big
            big = i
    return big, next_big

big, next_big = big_and_next_big(num)

for i in range(0,m):
    for j in range(0,k):
        ans += big
        cnt += 1
        if cnt == m:        #2중 for문 탈출용 
          break
    if cnt == m:            #for문 탈출용
        break
    ans += next_big
    cnt += 1
    if cnt == m:            #for문 탈출용
        break

print(ans)










"""
def find_big_num(num):
    big = 0
    for i in num:
        if big < i:
            big = i
    return big

for i in range(0,m):
    big = find_big_num(num)
    for j in range(0,k):
        ans += big
    """
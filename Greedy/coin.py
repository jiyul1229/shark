# 준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.

# 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)

# 둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)

N, K = map(int, input().split())

coins = []
#동전을 list 형태로 입력받음
for i in range(N):
    coins.append(int(input()))
coins.sort(reverse=True)
#내림차순으로 정리함

answer = 0

for coin in coins:     
    if K >= coin:  
        answer += K // coin      
        K %= coin                   
        if K <= 0:
            break 
print(answer) 

#다른 사람 숏코딩
a,*b=open(c:=0);k=int(a[2:])
while b:*b,p=b;p=int(p);c+=k//p;k%=p
print(c)

#또 다른 숏코딩
p,*o=open(0)
k=int(p[2:])
c=0
for i in map(int,o[::-1]):c+=k//i;k=k%i
print(c)
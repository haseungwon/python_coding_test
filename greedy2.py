''' 
큰수의 법칙
'''
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse = True)
first = data[0]
second = data[1]

p = m // (k+1)
q = m % (k+1)

result = p*(first*k + second) + q*first
print(result)


''' 
가장 큰 단위가 항상 작은 단위의 배수이므로 작은 단위의 동전들을 조합해서 다른 해를 만들 수 없다
'''
n = 1200
count = 0

list = [500, 100, 50, 10]

for coin in list:
  count += n // coin
  n = n % coin

print(count)

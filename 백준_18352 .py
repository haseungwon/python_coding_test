from collections import deque
import sys

def bfs(graph, start):
  queue = deque()
  queue.append(start-1)
  visited[start-1] = 1
  distance[start-1] = 0

  while queue:
    vertex = queue.popleft()
    for nv in graph[vertex]:
      if visited[nv-1] ==0:
        queue.append(nv-1)
        visited[nv-1]= 1
        distance[nv-1] = distance[vertex]+1




n, m, k, x = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n)]
visited=[0]*n
distance = [0]*n

for _ in range(m):
  start, end = map(int,sys.stdin.readline().rstrip().split())
  graph[start-1].append(end)

bfs(graph, x)

for i in range(n):
  if(distance[i]==k):
    print(i+1)
if k not in distance:
  print(-1)
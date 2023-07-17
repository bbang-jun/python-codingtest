from collections import deque

N, M = map(int, input().split())

px = (0, 0, -1, 1)
py = (1, -1, 0, 0)

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            tx = px[i] + x
            ty = py[i] + y

            if tx < 0 or tx >= N or ty < 0 or ty >= M:
                continue
            elif graph[tx][ty] == 0:
                continue
            elif graph[tx][ty] == 1:
                graph[tx][ty] = graph[x][y] + 1
                queue.append((tx, ty))
    return graph[N-1][M-1]

print(bfs(0, 0))
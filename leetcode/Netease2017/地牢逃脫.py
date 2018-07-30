'''
地牢逃脱
https://www.nowcoder.com/practice/0385945b7d834a99bc0010e67f892e38?tpId=85&tqId=29831&rp=1&ru=/ta/2017test&qru=/ta/2017test/question-ranking
'''


def check(x, y):
    return 0 <= x < n and 0 <= y < m and pointMap[x][y] == '.'


def bfs():
    vis = [[0 for _ in range(m)] for _ in range(n)]
    vis[x0][y0] = 1

    queue = [x0 * n + y0]

    order = [[-1 for _ in range(m)] for _ in range(n)]
    order[x0][y0] = 0

    while queue:
        point = queue.pop(0)

        x, y = point // m, point % m
        for direc in direction:
            dx,dy = direc
            if check(x + dx, y + dy) and vis[x + dx][y + dy] == 0:
                vis[x + dx][y+dy] = 1
                queue.append((x + dx) * m + y + dy)
                order[x + dx][ y + dy] = order[x][y]+1
    return order

if __name__ == '__main__':
    n, m = map(int, input().split())

    pointMap = [list(input()) for i in range(n)]

    x0, y0 = map(int, input().split())

    k = int(input())

    direction = [list(map(int, input().split())) for i in range(k)]

    order = bfs()
    max_step=0
    for i in range(n):
        for j in range(m):
            if order[i][j]==-1 and pointMap[i][j] == '.':
                max_step = -1
                break
            if order[i][j]>max_step:
                max_step = order[i][j]
    print(max_step)

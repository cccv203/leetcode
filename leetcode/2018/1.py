

def solve():
    max_x = array[0][0]
    print(*array[0])
    for i in range(0,len(array)):
        if array[i][0]>max_x:
            max_x = array[i][0]
            print(*array[i])

if __name__=='__main__':
    n = int(input())
    array = [list(map(int,input().split())) for _ in range(n)]
    array = sorted(array, key=lambda element: element[1],reverse=True)
    solve()


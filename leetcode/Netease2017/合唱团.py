'''
合唱团
https://www.nowcoder.com/practice/661c49118ca241909add3a11c96408c8?tpId=85&tqId=29830&tPage=1&rp=1&ru=/ta/2017test&qru=/ta/2017test/question-ranking
'''



def solve(n,array,k,d):

    resArray = [[[0] * 2 for _ in range(k + 1)] for _ in range(n)]
    result = 0

    # i表示最后一个数位于array数组位置下标i处，j表示当前乘积的数字个数，0、1分别记录最大值和最小值
    # 遍历个数和位置
    for i in range(0, n):
        # 当乘积个数为1时，结果为当前这个数。
        resArray[i][1][0], resArray[i][1][1] = array[i], array[i]
        for j in range(2, k + 1):
            # 考虑间隔d
            for m in range(max(i - d, 0), i):
                resArray[i][j][0] = max(resArray[i][j][0]
                                        , resArray[m][j - 1][0] * array[i], resArray[m][j - 1][1] * array[i])
                resArray[i][j][1] = min(resArray[i][j][1]
                                        , resArray[m][j - 1][0] * array[i], resArray[m][j - 1][1] * array[i])

        result = max(result, resArray[i][k][0], resArray[i][k][1])
    return result

if __name__ == '__main__':
    n = int(input())
    array = [int(each) for each in input().split()]
    k, d = [int(each) for each in input().split()]

    print(solve(n,array,k,d))



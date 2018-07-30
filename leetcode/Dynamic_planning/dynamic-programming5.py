'''
candy
https://www.nowcoder.com/practice/74a62e876ec341de8ab5c8662e866aef?tpId=46&tqId=29045&tPage=1&rp=1&ru=/ta/leetcode&qru=/ta/leetcode/question-ranking
'''


'''
原先设想为 f(n) = 2*f(n-1) - f(n-2) +1 if array[n]>array[n-1] else f(n-1)+1
忽视了逆序,第n个学生的糖果应该比n-1和n+1都要大

def solve(n):
    result = [0]*len(n)
    if len(n)==1:
        result[0] = 1
    if n[1]>n[0]:
        result[1] = 3
    else:
        result[1] = 2
    for i in range(2,len(n)):
        if n[i]>n[i-1]:
            result[i] = 2*result[i-1] - result[n-2] +1
        else:
            result[i] = result[n-1] + 1
'''

'''
第n个学生的糖果数是max(正序数,逆序数)
'''

def solve(n):
    result = [0]*len(n)
    for i in range(1,len(n)):
        if n[i]>n[i-1]:
            result[i] = result[i-1]+1
    for i in range(len(n)-1,0,-1):
        if n[i-1]>n[i]:
            result[i-1] = max(result[i-1],result[i]+1)
    return sum(result) + len(n)


if __name__ == '__main__':
    # arr = [int(each) for each in input().split()]
    arr = [1,0,2]
    print(solve(arr))

















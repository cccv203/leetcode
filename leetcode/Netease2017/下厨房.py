'''
下厨房
https://www.nowcoder.com/practice/ca5c9ba9ebac4fd5ae9ba46114b0f476?tpId=85&tqId=29832&rp=1&ru=%2Fta%2F2017test&qru=%2Fta%2F2017test%2Fquestion-ranking&tPage=1
'''


import sys
# 定义一个空列表，记录所有料理包含的所有材料；
need = [] # 依次读取系统输入;
for line in sys.stdin:
    needline = line.split()
    need.extend(needline)
    pass
# 通过将列表格式转换为集合格式，去除列表中重复的元素；
lastNeed = set(need)

print(len(lastNeed))
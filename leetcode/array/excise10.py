'''
有效的数独
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/1/array/30/
'''


class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(len(board)):
            row = [int(board[i][j]) for j in range(len(board)) if board[i][j] != '.']
            col = [int(board[j][i]) for j in range(len(board)) if board[j][i] != '.']
            mat = [int(board[j // 3 + (i//3)*3][(i + j) % 3 + (i%3)*3]) for j in range(len(board))
                   if board[j // 3 + (i//3)*3][(i + j) % 3 + (i%3)*3] != '.']
            for nums in [row,col,mat]:
                nums_tuple = dict(zip(nums, [0] * len(nums)))
                if len(nums_tuple.keys()) != len(nums):
                    return False
        return True

if __name__=='__main__':
    nums=[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
    i = Solution().isValidSudoku(nums)
    print(i)       # False
'''
Fizz Buzz
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/25/math/60/
'''


class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n<1:
            return
        fizzbuzz = []
        for i in range(n):
            i += 1
            if (i%3)==0 and (i%5)==0:
                fizzbuzz.append('FizzBuzz')
            elif (i%3)==0:
                fizzbuzz.append('Fizz')
            elif (i%5)==0:
                fizzbuzz.append('Buzz')
            else:
                fizzbuzz.append(str(i))
        return fizzbuzz

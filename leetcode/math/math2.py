'''
计数质数
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/25/math/61/
'''


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<2:
            return 0
        is_primes = [1]*n
        is_primes[0],is_primes[1] = 0,0
        if n <5:
            return sum(is_primes)

        for i in range(2,int(n**0.5)+1):
            j=i
            while i*j<n:
                is_primes[i*j] = 0
                j += 1
        return sum(is_primes)


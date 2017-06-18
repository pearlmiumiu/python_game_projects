# We are playing the Guess Game. The game is as follows:

# I pick a number from 1 to n. You have to guess which number I picked.

# Every time you guess wrong, I'll tell you whether the number is higher or lower.

# You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):



# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# you can call Guess.guess(num)

class Solution:
    # @param {int} n an integer
    # @return {int} the number you guess
    def guessNumber(self, n):
        # Write your code here
        lo=1
        hi=n
        while lo<=hi:
            mid=(hi+lo)/2
            if Guess.guess(mid)==1:
                lo=mid+1
            elif Guess.guess(mid)==-1:
                hi=mid-1
            else:
                return mid
            
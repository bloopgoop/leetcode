class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        
        a_count = 0
        b_count = 0
        lesser = min(x, y)
        result = 0

        for c in s:
            if c > 'b': # reset counters, make as many pairs as possible
                result += min(a_count, b_count) * lesser # lesser bc lines 20-31 will guarentee greater pairs are counted for
                a_count = 0
                b_count = 0
            elif c == 'a':
                if x < y and b_count > 0: # "ba" is more valuable and we've seen b before
                    b_count -= 1
                    result += y # make the pair and increment result
                else:
                    a_count += 1 # "ab" is more valuable or no b's before
            elif c == 'b':
                if x > y and a_count > 0:
                    a_count -= 1
                    result += x
                else:
                    b_count += 1

        result += min(a_count, b_count) * lesser 
        return result
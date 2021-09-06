class Solution:
    # this function expands a string s with left start and right start pointers
    # returns the 
    def expand(self, s, left, right) -> int:
        R = right
        L = left
        #print("init R: ", R)
        #print("init L: ", L)
        
        while((L>=0 and R<len(s)) and s[L] == s[R]):
            #print("in loop while: ")
            
            L-=1
            #print("L dec :", L)
            R+=1
            #print("R inc :", R)
        #print(R-L-1)
        # note: -(-l) becomes +l
        
        return R-L-1
    def longestPalindrome(self, s: str) -> str:
        # we return a string
        # substring of s from start to end indices
        start = 0
        end = 0
        # initially 0
        
        # expand around center
        for i in range(len(s)):
            # if the string is odd then center is singular n-1/2 
            # ex: n=5 center= (5-1)/2 = 2 [a,b,c,d,e] 
            #                             [0,1,2,3,4]
            # if the string is even then center is shared
            #print("iteration: ", i, "char as mid", s[i])
            side_len_odd = self.expand(s, i, i)
            #print("side len odd ", side_len_odd)
            #print("iteration: ", i, "chars as mid", s[i], s[i+1])
            side_len_even = self.expand(s, i, (i+1))
            #print("side len even ", side_len_even)
            
            best_len = max(side_len_odd, side_len_even)
            #print("best len", best_len)
            
            if(best_len>end-start):
                
                start = i - int((best_len-1)/2)
                end = i + int((best_len/2))
                #print("start: ", start)
                #print("end: ", end+1)
        end+=1
        return s[start:end]
            
            
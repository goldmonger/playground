class Solution:
    def expandAroundCenter(self, s, left, right):
        L = left 
        R = right
        while(L>=0 and R<len(s)):
            if s[L] == s[R]:
                #print(L)
                #print(R)
                L-=1
                R+=1
            else: break
            
        return R - L -1
        
        
    def longestPalindrome(self, s: str) -> str:
        if(s == None or len(s) < 1):
            return ""
        else:
            start = 0
            end = 0
            for i in range(0,len(s)):
                len1 = self.expandAroundCenter(s, i, i)
                len2 = self.expandAroundCenter(s, i , (i+1))
                lenn = max(len1, len2)
                if(lenn > end - start):
                    start = i - int((lenn-1)/2)
                    end = i + int(lenn/2)
                #print(start)
                #print(end)
                #print(s[int(start):int(end+1)])
                #print(lenn)
                #print()
                
            end +=1
            return s[round(int(start)):round(int(end))]
                

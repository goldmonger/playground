class Solution:
    def mySqrt(self, x: int) -> int:
        # binary search
        if x==0 or x==1:
            return x
        l,r = 1,x
        while(l<=r):
            mid = (l+r)//2
            if(mid*mid <= x < (mid+1)*(mid+1)):
                return mid
            elif(mid*mid > x):
                r=mid-1
            else:
                l=mid+1
            
        
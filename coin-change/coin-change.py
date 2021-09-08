class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #memo = [[0] * int(amount+1) ] * int(len(coins)+1)
        memo = []
        for i in range(len(coins)+1):
            temp = []
            for j in range(amount+1):
                temp.append(0)
            memo.append(temp)
            
        #print (memo)
        #print()
        for j in range(1,amount+1):
            memo[0][j] = 9999
        #print (memo)
        
        for i in range(1, len(coins)+1):
            for j in range(1, amount+1):
                if(j<coins[i-1]):
                    memo[i][j] = memo[i-1][j]
                else:
                    memo[i][j] = min(memo[i-1][j], 1+memo[i][j-coins[i-1]])
        if(memo[len(coins)][amount] >= 9999):
            return(-1)
        else:
            return (memo[len(coins)][amount])
                
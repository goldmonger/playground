class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        #print(time)
        # (a+b) %60 = ( a%60 + b%60 ) % 60 = 0
        remList = [0] * 60
        counter = 0
        for i in range(len(time)):
            # in this loop we are iterating over the aray and finding out the mod
            # result and storing into a remainder array at the remainders index
            # in increments
            # ex if remainder is 10
            # rem[10] += 1
            
            rem = time[i] % 60
            if(rem == 0):
                #print(rem, " a is a multiple of 60")
                # after the second pass all the zero elements need to be tracked
                counter += remList[0]
            else:
                #print(rem, " a is not a multiple, b: ", 60-rem)
                # check if 60-rem has any count of encountered
                # remainders
                counter += remList[60 - rem]
            #print(rem)
            
            remList[rem] += 1
        #print (remList)
        return (counter)

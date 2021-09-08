class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = ''
        shortestLen = 9999
        for strng in strs:
            if len(strng) < shortestLen:
                shortest = strng
                shortestLen = len(strng)
        print(shortest)
        #print(shortestLen)
        com = ""
        ref= shortest
        for i in range(shortestLen):
            complete = True
            for word in strs:
                #print(word[i])
                #print(ref)
                #pass
                if word[i] != ref[i]:
                    complete = False
                    break
            if complete:
                com += ref[i]
            else:
                break
            
        return com
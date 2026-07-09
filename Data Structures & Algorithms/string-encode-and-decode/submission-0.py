class Solution:

    def encode(self, strs: List[str]) -> str:
        answer = ""
        for word in strs:
            answer += str(len(word)) + "#" + word
        return answer

    def decode(self, s: str) -> List[str]:
        i = 0
        aList = []

        while i < len(s):
            j = i
            aStr = ""

            while s[j] != "#":
                j = j + 1
            
            l = int(s[i:j])

            i = j + 1

            for n in range(l):
                aStr += s[i]
                i = i + 1
            
            aList.append(aStr)
            aStr = ""
        
        return aList


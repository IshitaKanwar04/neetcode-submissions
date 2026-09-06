class Solution:

    delimiter = '#'

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for i in range(len(strs)):
            length = len(strs[i])
            encoded_string += str(length) + Solution.delimiter + strs[i]
        return encoded_string





    def decode(self, s: str) -> List[str]:
        l = []
        while s:
            #if s[i] == Solution.delimiter and type(s[i-1]) is int:
            result = s.split("#", maxsplit = 1)
            s = result[1]
            word = s[:int(result[0])]
            l.append(word)
            s = s[int(result[0]):]
        return l



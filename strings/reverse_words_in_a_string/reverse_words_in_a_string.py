class Solution:
    def reverse_words(self, s: str) -> str:

        word=[]
        output=[]
        for c in s:
            if c !=" ":
               word.append(c)
            elif word:
                output.append("".join(word))
                word=[]
        if word:
           output.append("".join(word))
        result= " ".join(reversed(output))
        return result

s = "  hello world  "
obj= Solution()

print(obj.reverse_words(s))
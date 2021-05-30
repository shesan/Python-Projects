# 804. Unique Morse Code Words
 
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        import string

        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alpha = string.ascii_lowercase
        alpha2 = list(alpha)
        #print(alpha2)
        result = []

        for word in words:
            s = ""
            for letter in word:
                index = alpha2.index(letter)
                s += morse[index]
            result.append(s)
        return len(set(result))


test = Solution()
words = ["gin", "zen", "gig", "msg"]
print(test.uniqueMorseRepresentations(words))
        
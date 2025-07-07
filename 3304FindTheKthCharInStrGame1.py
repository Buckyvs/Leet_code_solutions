class Solution(object):
    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """
        word = ['a']
        while len(word) < k:
            size = len(word)
            for i in range(size):
                next_char = chr(ord('a') + ((ord(word[i]) - ord('a') + 1) % 26))
                word.append(next_char)
        return word[k-1]
        
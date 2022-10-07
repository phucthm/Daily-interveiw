def longestPalindrome(s):
    result = ""
    max_length = 0
    for i in range(len(s)):
        for j in range(len(s)):
            temp = s[j:i]
            if (temp[::-1] == temp):
                if (max_length < len(temp)):
                    max_length = len(temp)
                    result = temp
    return result

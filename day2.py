class Solution:
    def lengthOfLongestSubString(s):
        seen = ""
        max_length = 0

        start_index = 0

        for i in range(len(s)):

            if s[i] in seen:
                start_index = i
                seen = s[i]

            seen += s[i]
            max_length = max(max_length, i - start_index + 1)

        return max_length


result = Solution
print(result.lengthOfLongestSubString("geeksforgeeks"))

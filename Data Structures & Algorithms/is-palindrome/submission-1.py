class Solution:
    def isPalindrome(self, s: str) -> bool:
        combine = ""
        for char in s:
            if char.isalnum():
                combine += char.lower()
        return combine == combine[::-1]

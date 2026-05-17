class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            #print("Here")
            return False
        else:
            s = ("".join(e for e in s if e.isalnum())).lower()
        back = len(s)-1
        for front in range(len(s)):
            print(f"Front: {s[front]} Back: {s[back]}")
            print(f"Front index: {front} Back index: {back}")
            if s[front] != s[back]:
                return False
            elif front > back:
                return True
            else:
                back = back - 1
        return True
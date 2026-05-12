class Solution:

    def encode(self, strs: List[str]) -> str:
        res =""
        for each in strs:
            res = res + each + ":-;"
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = s.split(":-;")
        return res[:-1]
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        pre = []
        suf = []
        for n in nums:
            if len(pre) != 0:
                pre.append(n * pre[-1])
            else:
                pre.append(n)

        for i in reversed(nums):
            if len(suf) != 0:
                suf.append(i * suf[-1])
            else:
                suf.append(i)

        revsuf = []
        for a in reversed(suf):
            revsuf.append(a)

        print(pre)
        print(suf)
        print(revsuf)
        

        res = []
        for i in range(len(nums)):
            ans = 1
            if i>0:
                ans *= pre[i-1]
            if i<len(nums)-1:
                ans *= revsuf[i+1]
            res.append(ans)

        return res
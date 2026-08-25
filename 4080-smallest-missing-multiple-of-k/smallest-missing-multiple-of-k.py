class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        arr=set(nums)
        multiple=k
        while multiple in arr:
            multiple+=k
        return multiple

        
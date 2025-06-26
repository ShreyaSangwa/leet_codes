class NumArray:

    def __init__(self, nums: List[int]):
        self.a=nums

    def sumRange(self, left: int, right: int) -> int:
        summ=0
        for i in range(left,right+1):
            summ+=self.a[i]
        return summ


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
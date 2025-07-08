class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(arr, counter):
            if len(arr) == len(nums):
                res.append(list(arr))
                return

            for num in counter:
                if counter[num] > 0:
                    arr.append(num)
                    counter[num] -= 1
                    backtrack(arr, counter)
                    arr.pop()
                    counter[num] += 1

        backtrack([], Counter(nums))

        return res
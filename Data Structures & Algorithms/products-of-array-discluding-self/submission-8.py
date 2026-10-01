class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) > 1:
            return [0 for i in range(len(nums))]
        t_no_zero = 1
        t = 1
        for n in nums:
            if n != 0:
                t_no_zero *= n
            t *= n


        output = []

        for n in nums:
            if n != 0:
                output.append(int(t // n))
            else:
                output.append(t_no_zero)
        return output



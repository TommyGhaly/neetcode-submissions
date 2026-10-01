class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s_nums = sorted(set(nums))
        if len(s_nums) == 1:
            return 1
        elif len(s_nums) == 0:
            return 0

        g_consec = 1
        streak = 0
        for i in range(len(s_nums)-1):
            diff = s_nums[i + 1] - s_nums[i]
            if diff == 1:
                if streak == 0:
                    streak = 2
                else:
                    streak += 1
                if g_consec <= streak:
                    g_consec = streak
            else: 
                    streak = 0
        return g_consec 
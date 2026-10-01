class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        c1 = 0
        c2 = len(numbers) - 1

        while c2 > c1:
            total = numbers[c1] + numbers[c2]
            if total < target:
                c1 += 1 
            elif total > target:
                c2 -= 1
            else:
                return [c1 + 1, c2 + 1] 
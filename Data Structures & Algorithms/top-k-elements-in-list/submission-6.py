class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        tuples = []
        for n in nums:
            if n in map:
                map[n] += 1
            else:
                map[n] = 1

        for key, value in map.items():
            tuples.append((key, value))
        
        tuples.sort(key= lambda x: x[1], reverse=True)
        rank = [x[0] for x in tuples[:k]]

        return rank
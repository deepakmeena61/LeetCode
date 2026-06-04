class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #dictionary
        freq = [[] for i in range(len(nums)+1)] #bucket with size of list
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num) #giving each frequency as key and appending num
        result = []
        for i in range(len(freq)-1, 0, -1): #iterate from the back
            for num in freq[i]: #only if a freq[i] has multiple values
                result.append(num)
                if len(result) == k: #to break and give result
                    return result
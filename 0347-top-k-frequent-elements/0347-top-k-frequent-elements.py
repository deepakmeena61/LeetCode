class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #dictionary
        for num in nums:
            count[num] = 1 + count.get(num, 0) # getting frequency of num
        heap = [] # list inititation for heap
        for num, cnt in count.items():
            heapq.heappush(heap, (cnt, num)) # putting values in heap
            if len(heap) > k: # minheap
                heapq.heappop(heap) 
        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1]) #final result popping at index 1
        return result
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_num={ }
        for i in range(len(nums)):
            num=nums[i]
            count_num[num]=count_num.get(num,0) +1
        sorted_items = sorted(count_num.items(),key=lambda x:x[1],reverse=True)
        result=[]
        for j in range(len(count_num)):
            if j < k:
                result.append(sorted_items[j][0])
        return result
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        dic = collections.Counter()
        result = 0

        for num in deliciousness:
            for j in range(22):
                val = 2**int(j) - num
                if val in dic:
                    result += dic[val]
            dic[num] +=1

        return result % (10**9 +7)

        
        

                           
        




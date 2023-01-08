class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic =collections.Counter()

        for val in cpdomains:
            num,web = val.split()
            dic[web] += int(num)

            for i in range(len(web)):
                if web[i] == ".":
                    dic[web[i+1:]] +=int(num)
        
        result = []
        
        for web,num in dic.items():
            level =""
            level +=str(num)
            level += ' '+web
            result.append(level)
        return result 
        
            

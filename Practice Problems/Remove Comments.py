class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        opened , stack ,val = False , [] , ""

        for string in source:
            idx = 0
            while idx < len(string):
                s = string[idx]
                if idx+1< len(string):
                    if string[idx] == "/" and string[idx + 1] == "/" and not opened:
                        break
                    elif string[idx] == "/" and string[idx + 1] == "*" and not opened:
                        idx += 2
                        opened = True
                        continue
                    
                    elif opened and string[idx] == "*" and string[idx + 1] == "/":
                        idx +=2
                        opened = False
                        continue
                idx +=1  
                if not opened :
                    val += s
                
            if opened == False and val:
                stack.append(val)
                val = ""
        return stack




        
        

n = int(input())

for i in range(n):
    num = int(input())
    val = input().split()
    ch = input()
    dic = {}
    flag =  False
    for j in range(num):
        if val[j] in dic:
            if dic[val[j]] != ch[j]:
                print("NO")
                flag = True
                break
            
        else:
            dic[val[j]] = ch[j]
    if flag == False:
        print("YES")
    

        
        
    



    
            
            
        
    
            
            
        
    
        
            
        
        
    

    
    
    


                
                

        
    
                

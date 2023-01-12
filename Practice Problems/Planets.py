from collections import Counter
n = int(input())


for i in range(n):
    
    m , n = map(int,input().split())
    val = input().split()
    dic = Counter(val)
    cnt = 0
    
    for value , fre in dic.items():
        if fre > n:
            cnt += n
        else:
            cnt += fre
    print(cnt)
     
 

        
        
    



    
            
            
        
    
            
            
        
    
        
            
        
        
    

    
    
    


                
                

        
    
                

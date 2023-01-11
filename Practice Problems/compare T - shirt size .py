n = int(input())

for i in range(n):
    m , n = input().split()
    idxm = len(m) - 1
    idxn = len(n) - 1
    if m[idxm] == n[idxn]:
        if idxm == idxn:
            print("=")
        if m[idxm] =="S":
            if idxm > idxn:
                print("<")
            elif idxm < idxn:
                print(">")
        
        else:
            if idxm > idxn:
                print(">")
            elif idxm < idxn:
                print("<")
    elif m[idxm] > n[idxn]:
        print("<")
    else:
        print(">")

        
        
    



    
            
            
        
    
            
            
        
    
        
            
        
        
    

    
    
    


                
                

        
    
                

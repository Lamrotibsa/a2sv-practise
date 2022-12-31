n = int(input())

for i in range(n):
    m = int(input())
    nums = list(map(int,input().split()))
    
    val = "Yes"
    l = 0
    r = len(nums) - 1
    while r > l:
        if nums[l] >= nums[r]:
            greatest_num = nums[l]
            l+=1
            
        else:
            greatest_num =nums[r]
            r-=1
            
        if greatest_num < nums[r] or greatest_num < nums[l]:
            val = "No"
            break
            
    print(val)

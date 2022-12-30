# Enter your code here. Read input from STDIN. Print output to STDOUT
n , m = map(int,input().split())
s = list(input().split())
cnt=0

val1=set(input().split())
val2=set(input().split())

for i in range(n):
    
    if s[i] in val1:
        cnt += 1
    elif s[i] in val2:
        cnt -= 1
    
print(cnt)

def findtheproduct( n ):
    ans = [1 for _ in range(len(n))]
    length = len(n)
    prefix = 1
    postfix = 1
    for i in range(len(n)):
        ans[i] = prefix;
        prefix=n[i]*prefix
    
    for i in range(len(n)-1,-1,-1):
        ans[i] =ans[i] * postfix
        postfix = postfix * n[i]
    
    return ans
    
lists = [1,2,4,5,6]
print(findtheproduct(lists))
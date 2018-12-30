# binary search method from JMB p.234-235

def lst4(num, num_lis):
    if num_lis == 0 or (num_lis > 0 and cache[num_lis - 1] <= num):
        cache[num_lis] = num
        num_lis += 1
        return num_lis

    lo = 0
    hi = num_lis - 1
    
    # binary search
    while lo <= hi:
        mid = (lo + hi) / 2
        if cache[mid] < num:
            lo = mid + 1
        else:
            hi = mid - 1
    cache[hi + 1] = num
    
    return num_lis


C = input()
for _ in xrange(C):
    N = input()
    cache = {}
    S = map(int, raw_input().strip().split())
    
    num_lis = 0
    for i in xrange(N):
        num_lis = lst4(S[i], num_lis)
        
    print num_lis


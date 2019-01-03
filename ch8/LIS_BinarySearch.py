# binary search method from JMB p.234-235

def lst4(num, num_lis):
    if num_lis == 0 or (num_lis > 0 and cache[num_lis - 1] <= num):
        cache[num_lis] = num
        num_lis += 1
        return num_lis

    # lo ~ hi is the floor ~ ceiling interval for possible answers to the problem.
    lo = -1
    hi = num_lis # in this case, num_lis may also represent the size of cache.
    
    # invariant 1: lo < hi.
    # Since hi can be 0 when num_lis = 0, lo starts with -1.
    
    # invariant 2: cache[lo] < x <= cache[hi].

    
    # binary search to locate the position 'hi' closest to (and always greater or equal to) given num.
    while lo + 1 < hi:
        mid = (lo + hi) / 2
        if cache[mid] < num:
            lo = mid
        else:
            hi = mid

    # save num in the 'hi'th position in cache instead of 'lo'th position due to invariant 2.
    cache[hi] = num
    
    return num_lis


C = input()
for _ in xrange(C):
    N = input()
    # cache[i] refers to the lowest among last values of increasing subsequences
    # of length 'i' that we made so far.
    cache = {}
    S = map(int, raw_input().strip().split())
    
    num_lis = 0
    for i in xrange(N):
        num_lis = lst4(S[i], num_lis)
        
    print num_lis


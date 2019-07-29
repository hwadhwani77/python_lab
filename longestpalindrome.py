def longestPalindrome(s):
    if len(s) <1:
        return ""
    start = end = 0
    for i in range(0, len(s)):
        len1 = expandCenter(s, i, i)
        len2 = expandCenter(s, i, i+1)
        m_len = max(len1, len2)
        print("MaxLen: %d" %(m_len))
        if(m_len > end - start):
            start = int(i - int((m_len  - 1)/2))
            end = int(i + m_len/2)
            print("Start: %d, End: %d" %(start, end))
    return s[start:end+1]

def expandCenter(s, l, r):
    L = l
    R = r
    print(L, R)
    while(L >=0 and R < len(s) and s[L] == s[R]):
        L -= 1
        R += 1
    return R - L -1


print(longestPalindrome("cbbd"))

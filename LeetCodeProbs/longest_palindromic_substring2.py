def longestPalindrome(s):
    l_P = ''
    c_P = ''
    if len(s)==1:
        l_P = s
    for i in range(1,len(s)):
        if s[i-1]==s[i] or s[i-2]==s[i]:
            for j in range(len(s)-i):
                if i-1-j>=0 and s[i-1-j]==s[i+j]:
                    c_P = s[i-1-j:i+1+j]
                    continue
                if i-2-j>=0 and s[i-2-j]==s[i+j]:
                    c_P = s[i-2-j:i+1+j]
                    continue
                else:
                    break
        if len(l_P)<len(c_P):
            l_P = c_P
    return l_P

if __name__=='__main__':
#    s = 'abcdcba'
    s = 'baaag'
    print(longestPalindrome(s))
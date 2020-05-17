def longestPalindrome(s):
    l_P = ''
    c_P = ''
    if len(s)==0:
        return l_P
    else:
        l_P = s[0]
    for i in range(1,len(s)):
            if s[i-1] == s[i] and i-1>=0:
                for j in range(len(s)-i):
                    if s[i-1-j]==s[i+j] and ((i-1-j)>=0):
                        c_P = s[i-1-j:i+1+j]
                        if len(l_P)<len(c_P):
                            l_P = c_P
                    else:
                        break

            if s[i-2] == s[i] and i-2>=0:
                for j in range(len(s)-i):
                    if s[i-2-j]==s[i+j] and ((i-2-j)>=0):
                        c_P = s[i-2-j:i+1+j]
                        if len(l_P) < len(c_P):
                            l_P = c_P
                    else:
                        break

            if len(l_P)<len(c_P):
                l_P = c_P
    return l_P

if __name__=='__main__':
#    s = 'yyygdfgsdfsabcddddddddddcbazz'
    s = 'ac'
#    s = 'babad'
#    s = 'baaaaag'
#    s = 'cbbd'

    print(longestPalindrome(s))
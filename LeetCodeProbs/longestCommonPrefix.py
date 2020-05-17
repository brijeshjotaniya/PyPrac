#!/Users/brijeshjotaniya/.conda/envs/RoughProject/bin/python

def longestCommonPrefix(strs):
    res = ''
    diff_c = False
    if strs:
        smallest_str = min(strs, key=len)
    else:
        return ''
    for c in range(len(smallest_str)):
        for i in range(len(strs) - 1):
            if strs[i][c] == strs[i + 1][c]:
                continue
            else:
                diff_c = True
        if diff_c == True:
            break
        res += smallest_str[c]
    return res

ip_lst_str = ['flower', 'flow']
lcp = longestCommonPrefix(ip_lst_str)
print(lcp)
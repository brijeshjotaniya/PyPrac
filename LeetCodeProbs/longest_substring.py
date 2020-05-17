def lengthOfLongestSubstring(s):
    sub_s = ''
    length = 0
    for c in s:
        if c not in sub_s:
            sub_s += c
            if length < len(sub_s):
                length = len(sub_s)
        else:
            while c in sub_s:
                sub_s = sub_s[1:]
            sub_s += c
            # if length < len(sub_s):
            #     length = len(sub_s)
    return length

if __name__=='__main__':
    my_s = 'dvcgiczdf'
    print(lengthOfLongestSubstring(my_s))
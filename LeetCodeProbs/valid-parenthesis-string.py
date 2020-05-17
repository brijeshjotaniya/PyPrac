# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
# Example 1:
#
# Input: "()"
# Output: true
# Example 2:
#
# Input: "()[]{}"
# Output: true
# Example 3:
#
# Input: "(]"
# Output: false
# Example 4:
#
# Input: "([)]"
# Output: false
# Example 5:
#
# Input: "{[]}"
# Output: true

def isValid(s):
    if not s:
        return True
    else:
        l_c = list(s)
    o_b_set = {'(', '{', '['}
    c_b_set = {')', '}', ']'}
    b_dict = {')':'(', '}':'{', ']':'['}
    opened_brackets = []
    closed_brackets = []
    for c in l_c:
        if c in o_b_set:
            opened_brackets.append(c)
        elif c in c_b_set:
            closed_brackets.append(c)
            if len(closed_brackets)>len(opened_brackets):
                return False
            elif (c in c_b_set) and (b_dict[c] == opened_brackets[-1]):
                opened_brackets.pop()
                closed_brackets.pop()
    return len(opened_brackets)==0

ip_str = '([)]'

print(isValid(ip_str))
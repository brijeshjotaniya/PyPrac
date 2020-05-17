#!/Users/brijeshjotaniya/.conda/envs/RoughProject/bin/python
import collections
# from collections import Counter
#
# s = 'askdjfh akljdhf askdhfasdhf'
# c = Counter(s)
# print(c['a'])

def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    my_x = x
    if my_x<0:
        return False
    else:
        rx = 0
        while (x//10) > 0:
            rx *= 10
            rx += (x%10)
            x //= 10
#            rx *= 10
        rx *= 10
        rx += x
    return rx == my_x

def main():
    return isPalindrome(121)

if __name__ == '__main__':
        print(main())
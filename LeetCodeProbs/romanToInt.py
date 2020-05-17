def romanToInt(s: str) -> int:
    R2i = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    val = R2i[s[0]]

    for i in range(1, len(s)):
        if R2i[s[i]] <= R2i[s[i - 1]]:
            val += R2i[s[i]]
        else:
            val += R2i[s[i]]
            val -= (2 * R2i[s[i - 1]])
    return val

s = input('Enter a Roman number\n')

print(f'The value of your Roman number {s} is {romanToInt(s)}')
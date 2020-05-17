import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    pangram_status = False
    abcd = list(alphabet)
    for letter in alphabet:
        if letter in str1:
            abcd.remove(letter)
            # continue
        else:
            pangram_status = False
            break
        pangram_status = len(abcd)==0
    return pangram_status

print(ispangram(string.ascii_lowercase))
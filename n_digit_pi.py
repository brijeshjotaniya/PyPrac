#!/Users/brijeshjotaniya/opt/anaconda3/bin/python
import math

def get_n():
    while True:
        try:
            n = int(input('How many digits after decimal you want for pi value? Select between 1 and 100\n'))
        except:
            print('Please enter an integer between 1 and 100')
        else:
            break
    return n

def calc_pi(n):
    return f'Pi value with {n} digits after decimal is {math.pi:{1}.{n+1}}'


if __name__ == "__main__":
    n = get_n()
    pi_n = calc_pi(n)
    print(pi_n)
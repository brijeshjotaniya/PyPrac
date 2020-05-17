# Fibonacci implementation

def fib_h(n):
	if n==0:
		return 0
	elif n==1:
		return 1

	# f1 = fib_h(n-1)
	# f2 = fib_h(n-2)
	# res = f1+f2
	# return res

	return fib_h(n-1)+fib_h(n-2)


def fib_t(n,a=0,b=1):
	if n==0:
		return a
	elif n==1:
		return b

	return fib_t(n-1,b,a+b)


if __name__ == '__main__':
	print(fib_t(10))
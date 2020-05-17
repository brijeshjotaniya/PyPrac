#Factorial implementation

def fact_h(n):
	if n==1:
		return 1
#	sub_res1 = fact_h(n-1)
#	sub_res2 = n*sub_res1
#	So, below return statement is similar to return sub_res2
#	And as we can see this is a head recursion since 
#	we call recursively first and then do some operation
#	(multiplication of current function param n with result of the recursive call).
#	return sub_res2
	return n*fact_h(n-1)


def fact_t(n,tmp_res=1):
	if n==1:
		return tmp_res
#	 
#	Tail recusion needs the operation(multiplication with param 'n') done before recursive call
#	So we'll need a way to send the result of the operation along with the next param n-1 in to the recursive call.
#	Hence, requires defining additional param called tmp_res. 
#	This tmp_res or accumulator must be assigned to be unary operator for the operation, 1 for multiplication and 0 for addition, null string for string concatenation etc.
#	It should also be updated along with the param n during the recursive call.
#	sub_res1 = n*tmp_res
#	tmp_res  = sub_res1
#	sub_res2 = fact_t(n-1,tmp_res)
#	return sub_res2 which is what happens when we write below statement.
#	Very imp, since the operations are already done when we reach the base case, base case should return the cumulative result instead of a fixed value like in fact_h
	return fact_t(n-1, n*tmp_res)

if __name__ == '__main__':
	print(fact_h(10))
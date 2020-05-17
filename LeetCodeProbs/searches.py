import random

# Linear Search
def LinSrch(n, num_list):
	steps = 0
	for index,val in enumerate(num_list):
		steps +=1
		if val == n:
			break
	return steps,index

# Binary Search
def BinSrch(n, num_list, steps=0):
	l_index = 0
	u_index = len(num_list)
	mid_index = (l_index+u_index)//2
	index = mid_index
	if n == num_list[mid_index]:
		steps += 1
		print(f'Step: {steps}, index: {mid_index}, value: {num_list[mid_index]}')
		return steps,index
	elif n < num_list[mid_index]:
		steps += 1
		print(f'Step: {steps}, index: {mid_index}, value: {num_list[mid_index]}')
		steps,tmp_index = BinSrch(n, num_list[l_index:mid_index], steps)
		index -= tmp_index
	else:
		steps += 1
		print(f'Step: {steps}, index: {mid_index}, value: {num_list[mid_index]}')
		steps,tmp_index = BinSrch(n, num_list[mid_index+1:u_index], steps)
		index += tmp_index
	return steps,index

def get_input_algo():
	while True:
		try:
			srch_algo = input('Which search do you want to try? Press "L" for linear or "B" for binary\n')
		except:
			print('Invalid input.\n')
		if srch_algo[0].lower()!='l' and srch_algo[0].lower()!='b':
			print('Invalid input. Please press either "L" or "B" only')
			continue
		else:
			break
	return srch_algo[0].lower()

def get_num_to_search():
	while True:
		try:
			num_selected = int(input('Which number do you want to search in range 0 to 100?\n'))
		except:
			print('Invalid input.\n')
		if num_selected not in range(101):
			print('Invalid input. Please enter an integer between 0 and 100 (inclusive) only')
			continue
		else:
			break
	return num_selected

def main():
	srch_algo_dict = {'l':'linear search', 'b':'binary search'}
	algo_selected = get_input_algo()
	num_selected = get_num_to_search()
	num_list = [i for i in range(101)]
	random.shuffle(num_list)
	print(f'Your random list of 101 integers is {num_list}')

	if algo_selected == 'l':
		steps,index = LinSrch(num_selected, num_list)
	else:
		num_list.sort()
		print(f'Now the sorted list of 101 integers is {num_list}')
		steps,index = BinSrch(num_selected, num_list)

	print(f'Your {srch_algo_dict[algo_selected]} for {num_selected} in a list of 101 integers took {steps} steps.\nThe number is located at index {index}')

if __name__=='__main__':
	main()
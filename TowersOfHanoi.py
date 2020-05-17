# Tower of Hanoi

def hanoi(n, frm, mid, fin):

	if n==1:
		print(f'Moving plate {n} from {frm} to {fin}')
		return

	else:
		hanoi(n-1, frm, fin, mid)						#Step 1: Move top n-1 plates from 'frm' to 'mid' with help of 'fin'.
		print(f'Moving plate {n} from {frm} to {fin}')	#Step 2: Move the n-1th (largest) plate from 'frm' to 'fin'.
		hanoi(n-1, mid, frm, fin)						#Step 3: Move the n-1 plates from 'mid' to 'fin' with help of 'frm'.

if __name__ == '__main__':
	hanoi(4, 'a', 'b', 'c')
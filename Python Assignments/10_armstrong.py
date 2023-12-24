# Armstrong Number Checking
def is_armstrong(num):
	num_str = str(num)
	n = len(num_str)
	sum = 0
	for digit in num_str:
		sum += int(digit)**n
	if sum == num:
		return True
	else:
		return False
num=int(input("Enter the number"))
print(is_armstrong(num))

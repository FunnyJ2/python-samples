#algorithm => n = last + 2nd last
one = 1
two = 0
fib=1

amount = raw_input("How many numbers do you want? ")
amount = int(amount)

for x in range(0,amount):
	fib = one+two
	print fib
	two = one
	one = fib

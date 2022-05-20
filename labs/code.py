def f(a, b):
	if(a < b):
		return a
	return f(a - b, b)
print(f(int(input()), int(input())))
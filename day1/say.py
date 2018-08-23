
def say(i):
	if (i % 15) == 0:
		print("Fuzz Buzz")
	elif (i % 5) == 0:
		print("Buzz")
	elif (i % 3) == 0:
		print("Fuzz")
	else:
		print(i)
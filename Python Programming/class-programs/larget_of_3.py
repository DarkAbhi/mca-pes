a = int(input("First number = "))
b = int(input("Second number = "))
c = int(input("Third number = "))
if a==b==c:
	print("3 numbers are equal.")
	exit()
if a>b:
	print("First number is largest.")
elif b>c:
	print("Second number is largest.")
else:
	print("Third number is largest.")

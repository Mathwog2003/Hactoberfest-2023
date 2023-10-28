class Cal:

	def add(a,b):
		print(a+b)

	def sub(a,b):
		print(a-b)

	def mul(a,b):
		print(a*b)

	def div(a,b):
		print(a/b)



	print("Enter a Choice\n1:ADD\n2:SUB\n3:MUL\n4:DIV")
	choice=int(input("Enter a Choice "))
	try:
		if choice==1:
			a=int(input("enter a num:"))
			b=int(input("enter a num:"))
			add(a,b)
		elif choice==2:
			a=int(input("enter a num:"))
			b=int(input("enter a num:"))
			sub(a,b)
		elif choice==3:
			a=int(input("enter a num:"))
			b=int(input("enter a num:"))
			mul(a,b)
		elif choice==4:
			a=int(input("enter a num:"))
			b=int(input("enter a num:"))
			div(a,b)
	except ValueError:
		print("invalid choice\npls enter a number")

c=Cal()




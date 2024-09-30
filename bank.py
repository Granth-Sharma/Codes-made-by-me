def pasw():
	global passw
	b = True
	while b:
		passw = int(input("Enter your password(Password should only contain numbers and not greater than 4 digits): "))
		if len(a) <= 4:
			b=False
		else:
			continue
#------------------------------------------------------------------------
class Bank:
	def __init__(self,name,balance):
		self.name = name.lower()
		self.bal = balance

	def __str__(self):
		return "Owner's name: {} \nBalance: {}".format(name.capitalize(),self.bal)	
	
	def deposit(self,dep):
		if dep > 0:
			self.bal += dep
			print("${} has been successfully been deposited. Your current balance is ${}".format(dep,self.bal))
		else:
			print("Requested amount should be greater than 0")

	def withdraw(self,wit):
		if wit > 0:
			if wit <= self.bal:
				self.bal -= wit
				print("${} has successfully been withdrawn. The current balance is ${}".format(wit,self.bal))
			else:
				print("Sufficent funds aren't available in your account.")
		else:
			print("withdrawn amount should be greater than zero!")
#----------------------------------------------------------------------------------------------------------------------
x = True
while x:
	print("Let's start with opening an account!")
	name = input("Please state your name: ")
	balance = int(input("Enter your starting balance: "))
	acc = Bank(name,balance)
	print("Your account has been created with following details:-")
	print(acc)
	ask = input("Are you ready to start?(yes/no): ")
	ask = ask.lower()
	ask = ask.capitalize()
	if ask[0] == "Y":
		print("Your account has been finalised!")
		x=False
	elif ask[0] == "N":
		print("So let's start again")
#---------------------------------------------------------------------------------------------------------------------
x = True
z = True
while x:
	ask = input("Do you want to perform any further tasks?(Yes/No): ")
	ask = ask.lower()
	ask = ask.capitalize()
	if ask[0] == "Y":
		pass
	elif ask[0] == "N":
		print("Okay, closing the dialog!")
		x=False
		break
	#------------------------------------------------------------------------------------
	while z:
		ask = input("What is it that you want to do?(Deposit/Withdrawl): ")
		ask = ask.lower()
		ask = ask.capitalize()
		if ask == 'Deposit':
			depos = input("Enter the amount to be deposited: $")
			if depos.isdigit() == True:
				depos = int(depos)
				acc.deposit(depos)
				print("Now your current account status is:-")
				print(acc)
			else:
				print("Enter numbers only!")
				continue
		elif ask == "Withdrawl" or ask == "Withdraw":
			withdr = input("Enter the amount to be withdrawl: $")
			if withdr.isdigit() == True:
				withdr = int(withdr)
				acc.withdraw(withdr)
				print("Now your current account status is:-")
				print(acc)
			else:
				print("Enter numbers only!")
				continue
		else:
			print("Write deposit or withdrawl only ")
			continue
		ask2 = input("Do you wish to perform any further tasks?(Yes/No): ")
		ask2 = ask2.lower()
		ask2 = ask2.capitalize()
		if ask2[0] == 'Y':
			continue
		elif ask2[0] == 'N':
			print('Okay, closing the dialog!')
			x=False
			z=False
			break
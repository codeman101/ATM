f = open('balance', 'r')
balance = float(f.read()) # get current balance
f.close()
print('Welcome your current balance is ' + str(balance))
done = False
while not done: # loop to keep program going until user wants to stop
	choice = input('would you like to deposit or withdraw\n Type d for deposit or w for withdraw\n')
	while choice is not 'w' and choice is not 'd':
		choice = input('invaild please try again')
	if choice is 'w':
		f = open('fee', 'r')
		ans = f.read() # check if user is already withdrawn
		if ans == 'yes':
			choice = input('you are overdrawn and are therefore not allowed it withdraw anymore' +
			' would you like to restart so you can pay off the $10 now?[y/n]')
			if choice is 'y':
				continue # restart main prompt
			else:
				done = True
				continue # force program to restart at main prompt since user is overdrawn
		valid = False
		while not valid: # loop to make sure input is valid and force a repeat otherwise
			amount = input('how mucch would you like to withdraw?\n')
			try:
				amount = float(amount)
			except ValueError:
				print("amount wasn't a numerical type please try again")
				continue # force repeat
			if balance - amount < 0:
				print('you are overdrawn. You will not be able to withdraw anymore until you pay off the $10 fee')
				f = open('fee', 'w') # write to file to keep track of if user owe a fee for being overdrawn
				f.write('yes')
				f.close()
			balance -= amount
			f = open('balance', 'w')
			f.write(str(balance))
			f.close()
			valid = True # new balance was entered so no need to loop anymore
		again = input('Success your new balance is ' + str(balance) + ' are you done?[y/n]')
		while again is not 'y' and again is not 'n':
			again = input('invalid choice please try again')
		if again is 'y':
			done = True # end program
	else:
		f = open('fee', 'r')
		ans = f.read() # checking if user ows a $10 fee which will be accounted for below
		f.close()
		valid = False
		while not valid: # checking for vaild input
			choice = input('would you like to deposit a denomination that is not dollars?[y/n]')
			if choice == 'y':
				denomination = input('which one? type euros, yen, or pounds\n')
				if denomination == 'euros':
					try:
						amount = float(input('what amount?\n'))
					except ValueError:
						print('invalid input try again')
						continue
					amount *= 1.12 # coversion for euros
				elif denomination == 'yen':
						try:
							amount = float(input('what amount?\n'))
						except ValueError:
							print('invalid input try again')
							continue
						amount *= 0.009 # conversion for yen
				elif denomination == 'pounds':
					try:
						amount  = float(input('what mount?\n'))
					except ValueError:
						print('invalid try again')
						continue
					amount *= 1.32 # conversion for pounds
				else:
					print('invalid choice try again')
					continue

			else:
				amount = input('how much would you like to deposit?\n')
				try:
					amount = float(amount)
				except ValueError:
					print("amount wasn't a numerical type please try again")
					continue
			if ans == 'yes': # if user has a fee to pay off the fee is deducted from how much they deposited.
				amount -= 10 # if they only deposit the amount for the fee not including enough to get out of having a balance less than 0
			balance += amount # a fee of $10 will be subtracted from what they deposit until they clear their negative balance
			f = open('balance', 'w')
			f.write(str(balance))
			f.close()
			if balance > 0:
				f = open('fee', 'w')
				f.write('no')
				f.close()
			valid = True
			again = input('Success your balance is now ' + str(balance) + ' are you done?[y/n]')
			while again is not 'y' and again is not 'n':
				again = input('invalid choice please try again')
			if again is 'y':
				done = True

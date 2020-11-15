import random
number_dict={"number":0}
guess=5
guess_used=0
def number_generator(lower=1,upper=20):
	number=random.randint(int(lower),int(upper))
	number_dict["number"]=number
	return(number_dict)

def code1(answer):
	if str(answer)=="y":
		lower=input("Kindly set lower limit.")
		upper=input("Kindly set upper limit.")
		var=number_generator(lower,upper)
	if str(answer)=='n':
		number_generator()

print("Hello 'User'. Welcome to this short game. You have got "+str(guess)+" guesses to guess the number that I am thinking of.")
value_change=input("Would you like to change the values temporarily before playing? (y/n)"+"\n"+"(Defalut value is '1-20')"+"\n"+">>")
code1(value_change)
print("let's begin!"+"\n"+"\n")
print("Guess the number which I am thinking of.\n")

while guess!=0:
	trial=int(input("You have "+str(guess)+" guesses left."))
	if trial < number_dict["number"]:
		guess=guess-1
		guess_used=guess_used+1
		print("Too low, try again")
	if trial>number_dict["number"]:
		guess=guess-1
		guess_used=guess_used+1
		print("Too high, try again")
	if trial==number_dict["number"]:
		print("Well done 'User'! You have guessed correctly in "+str(guess_used)+" guesses.")
		break
if trial!=number_dict["number"]:
	print("Hard luck 'User'! You have lost. The number which I was thinking of was "+str(number_dict["number"])+". \n Better luck next-time!")
	
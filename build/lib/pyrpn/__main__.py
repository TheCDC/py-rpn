import __init__

def main():
	"""\nRun in interactive mode"""
	# create an instance of RPN
	instance = stackRPN()
	try:
		with open("settings.json") as f:
			# print(f.read())
			settings = json.load(f)
	except FileNotFoundError:
		print("Settings file not found. Creating it with defaults...")
		with open("settings.json",'w') as f:
			settings = {'prompt':'>>>','goodbye':'Have a nice day!'}
			f.write(json.dumps(settings))

		
	prompt = settings['prompt']
	goodbye = settings['goodbye']


	print("Welcome the command line RPN calculator!\nType 'help' for a list of functions.")
	while True:
		toExit = False
		# get input from the user
		try:
			userinput = input('>>>')
			if userinput in ['exit','quit']:
				print("Have a nice day!")
				toExit = True
		except:
			print("\nHave a nice day!")
			exit()
			toExit = True
		# give that input to the stack
		try:
			instance.interpret(userinput)
		except (StackError, ValueError) as e:
			print(e)
		# get the current stack
		newlist = instance.getStack()
		# print out the stack
		print("Current stack:")
		print(instance)

		if toExit:
			logging.info(instance)
			exit()

if __name__ == '__main__':
	# logging.basicConfig(level=logging.DEBUG)
	main()

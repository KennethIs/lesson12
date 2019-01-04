import time
import random

print('-'*65)
print('I am a Magic Eight Ball!')
print()

question = input("What's your question? ")
time.sleep(0.7)
print('...thinking...')
time.sleep(0.7)
print('...thinking...')
time.sleep(0.7)
print('...thinking...')
time.sleep(0.7)

choice = random.randint(1,6)

if choice == 1:
	print('Ya')
elif choice == 2:
	print('Nah')
elif choice == 3:
	print('idk')
elif choice == 4:
	print('Ask later')
elif choice == 5:
	print("Can't help ya there xD")
else:
	print("Maybe?")

print('-'*65)
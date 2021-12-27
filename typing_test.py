import time
import random

# Define some sentences:
sentences = [
	"bill gates developped microsoft",
	"you are a senior python developper",
	"isaac newton is a well known physician",
	"python is a programming language"
]

# Choose one sentence randomly:
sentence = random.choice(sentences)

# Greetings:
print("Welcome to Zacktype, a speed type test by Zakaria")
print("\nRULES:")
print("You'll see a sentence at the screen, you have to type it as fast as you can and correctly.")

# Give user some time to read rules:
time.sleep(5)
print("Ready...")
time.sleep(2)
print("Set...")
time.sleep(2)

# Define start time:
start= time.time()

# Print the sentence
print(sentence)
pinput = input("-> ")

# Check if user input was right:
if pinput == sentence:
	print("Correct!")
	# Print time elapsed:
	print(f"You made it in {time.time() - start}secs")
elif pinput != sentence:
	print("Incorrect")
	print("Retry, you typed the sentence wrong.")

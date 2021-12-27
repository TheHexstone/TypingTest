import time
import random
sentences = [
	"bill gates developped microsoft",
	"you are a senior python developper",
	"isaac newton is a well known physician",
	"python is a programming language"
]
sentence = random.choice(sentences)
print("Welcome to Zacktype, a speed type test by Zakaria")
print("\nRULES:")
print("You'll see a sentence at the screen, you have to type it as fast as you can and correctly.")
time.sleep(5)
print("Ready...")
time.sleep(2)
print("Set...")
time.sleep(2)
start= time.time()
print(sentence)
pinput = input("-> ")
if pinput == sentence:
	print("Correct!")
	print(f"You made it in {time.time() - start}secs")
elif pinput != sentence:
  print("Incorrect")
  print("Retry, you typed the sentence wrong.")

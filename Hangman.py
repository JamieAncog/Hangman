import random
print("Hangman:\nKeep guessing until you win!\nDon't make over 26 guesses\n")
words = ["butterfly", "ocean", "windmill", "castle", "orchestra", "imagination", "wallpaper"]
word = random.choice(words)
length = len(word)
attempts = 0
spaces = ["__"] * length
print(" ".join(spaces) + "\n")
while "__" in spaces and attempts < 26:
	attempts += 1
	guess = input("letter: ")
	if guess in word:
		for n in range(len(word)):
			if word[n] == guess:
				spaces[n] = guess
	print(" ".join(spaces))
if "__" in spaces:
	print("\nword = " + word + "\n\nYou Lose!")
else:
	print("\nword = " + word + "\n\nYou Win!")

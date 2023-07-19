import random
print("Hangman:\nKeep guessing until you win!\nDon't make over 26 guesses\n")
words = ["fox", "tin", "hat", "bug", "lid", "ice", "art", "fly", "ore", "red", "kelp", "such", "clam", "trip", "ship", "swap", "able", "quit", "exit", "poem", "upset", "snake", "laugh", "venom", "stone", "ocean", "after", "share", "could", "bring"]
word = "butterfly"#random.choice(words)
length = len(word)
attempts = 0
spaces = ["__"] * length
print(" ".join(spaces) + "\n")
while "__" in spaces and attempts < 26:
	attempts += 1
	guess = input("letter: ")
	if guess in word:
		place = word.index(guess)
		spaces[place] = guess
	print(" ".join(spaces))
if "__" in spaces:
	print("\nword = " + word + "\n\nYou Lose!")
else:
	print("\nword = " + word + "\n\nYou Win!")

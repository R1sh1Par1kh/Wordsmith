import random
import time

# reads words into list
f = open("valid_words.txt")
validWords = f.readlines()
validWords = [x.strip() for x in validWords]
f.close()

input("Welcome to Wordsmith! In this game, come up with as many words as you can using the 7 letters you are given. You have 60 seconds to create your valid word. Press Enter to begin!")
print("Ready...")
time.sleep(1)
print("Set...")
time.sleep(1)
print("Go!")

alphabet = ["q","w","r","t","y","p","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
vowels = ["a","e","i","o","u"]
seven = set()
for i in range(2):
  randVowel = random.randint(0,4)
  seven.add(vowels[int(randVowel)])

while (len(seven)<7):
  randNum = random.randint(0,20)
  seven.add(alphabet[int(randNum)])
print(seven)
startTime = time.time()
score = 0

finalTime = 0

correctWords = set()
while finalTime < 60:
  finalTime = time.time() - startTime
  validWord = True
  guess = input("Enter a word: ")
  for letter in guess:
      if letter not in seven:
        validWord = False
        print("You cannot use letters that arent in the list!")
        break
  if not validWord:
    continue
  if guess not in validWords:
    print("That word is not valid. Your score: " + str(score))
  else:
    if guess in correctWords:
      print("You already used this word! Input another!")
      continue
    correctWords.add(guess)
    score += int(len(guess))
    print("Valid word! Your score: " + str(score))

print("Your time is up! Your final score: " + str(score) + ". Great work!")
print(correctWords)

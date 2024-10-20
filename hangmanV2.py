import random
word_file = "wordlist.txt"
WORD = open(word_file).read().splitlines()
secret = random.choice(WORD)

name = input("Enter name : ")
print("Hello, "+ name + ". Welcome to Hangman Game!")
print("Your word has " , len(secret) , " characters. You will get 5 lives.")
list1 = list(secret)
list2 = ["_"] * len(list1)
lives = 5

while lives >= 0 :
    if(lives == 0):
        print("Game over! Better luck next time!")
        print("Word is " , secret)
        break
    if (list1 == list2):
        print("You won! Congratulations!")
        break
    guess = input("Enter a character : ")
    print("You entered "+ guess)
    if guess in list1:
        print("You guessed correct!")
        for index,value in enumerate(list1):
            if(guess == value):
                list2[index] = value
                print("Word is ", list2)                    
    else:
        print("Incorrect guess!")
        lives -= 1
        print("You have " , lives , " lives left")
        print("Word is ", list2)
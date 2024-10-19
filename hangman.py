name = input("Enter name : ")
print("Hello, "+ name)
secret = "apple"
print("Your word has " , len(secret) , " characters")
list1 = list(secret)
list2 = ["_"] * len(list1)
lives = 5

while lives >= 0 :
    if(lives == 0):
        print("Game over! Better luck next time!")
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
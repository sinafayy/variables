secret = 22

guess = int(input("Guess the secret number between 1 and 30: "))
if guess == secret:
    print("Congratulations")
elif guess == 21:
    print("Close, a little bit higher")
elif guess == 23:
    print("Close, a littble bit lower number.")
else:
    print("Better luck next time. The secret number is not " + str(guess))
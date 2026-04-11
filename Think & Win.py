import random
print("Welcome to Guess the Number Game!")
# Random number generate
number = random.randint(1, 10)
# User guess
guess = int(input("Enter a number between 1 and 10: "))
# Check
if guess == number:
    print("🎉 Correct! You guessed it right!")
else:
    print("❌ Wrong! The number was", number)

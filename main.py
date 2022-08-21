# Have a while loop running as long as the person guesses incorrectly 
# Once the person guesses incorrectly, stop the game and show the ending screen

# To start, show the starting logo, pick two random choices from the data and describe them
# Print the first option, the vs logo, and then the second option 
# Clear the screen
# Keep the correct guess and choose another random option from the data 

from replit import clear
import random 
from art import logo, vs
from game_data import data 

SCORE = 0 

end = False

def get_account_info():
  return random.choice(data)

option_one = get_account_info()
option_two = get_account_info()

print(logo)
while not end: 
  # print(logo)
  if option_one == option_two:
    while option_two != option_one:
      option_two = get_account_info()

  name_one = option_one["name"]
  description_one = option_one["description"]
  country_one = option_one["country"]
  print(f"Compare A: {name_one}, {description_one}, from {country_one}")

  print(vs)

  name_two = option_two["name"]
  description_two = option_two["description"]
  country_two = option_two["country"]
  print(f"Against B: {name_two}, {description_two}, from {country_two}.")

  correct_answer = "A" if option_one["follower_count"] > option_two["follower_count"] else "B"
  
  guess = input("Who has more followers? Type 'A' or 'B': ").upper()

  if guess == correct_answer:
    SCORE += 1
    clear()
    print(logo)
    print(f"Your guess is correct! Current score: {SCORE}. Keep Going!")
    # option_one = option_one if correct_answer == "A" else option_two
    option_one = option_two
    option_two = get_account_info()
  # elif guess != "A" or guess != "B":
  #   guess = input("Uh Oh, I didn't understand that. Try again: ")
  #   if guess == correct_answer:
  #       SCORE += 1
  #       clear()
  #       print(logo)
  #       print(f"Your guess is correct! Current score: {SCORE}. Keep Going!")
  #       # option_one = option_one if correct_answer == "A" else option_two
  #       option_one = option_two
  #       option_two = get_account_info()
  #   else:
  #     end = True
  #     print(f"Oh no, you lost! Your final score is {SCORE}.")
  else:
    end = True
    print(f"Oh no, you lost! Your final score is {SCORE}.")
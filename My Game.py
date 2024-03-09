#File:CS112_T2-1-20220985.py
#purpose:game1 
#auther:mohamed ahmed abdalla mohamed
#Id:20220985
def get_player_input(player_name):
  """Gets valid input from a player."""
  while True:
    try:
      choice = int(input(f"{player_name}, choose a number from 1 to 9: "))
      if 1 <= choice <= 9:
        return choice
      else:
        print("Invalid input. Please choose a number between 1 and 9.")
    except ValueError:
      print("Invalid input. Please enter a number.")

def play_game():
  """The main game loop."""
  sum = 0
  player_turn = "Player 1"

  while sum < 100:
    choice = get_player_input(player_turn)
    sum += choice
    print(f"The sum is now: {sum}")

    if sum == 100:
      print(f"{player_turn} wins!")
      break
    else:
      player_turn = "Player 2" if player_turn == "Player 1" else "Player 1"

  # Randomly choose the starting player for the next game
  starting_player = random.choice(["Player 1", "Player 2"])
  print(f"Next game starts with {starting_player}.")

if __name__ == "__main__":
  play_game()

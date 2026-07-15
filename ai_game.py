import random

# Possible moves
moves = ["rock", "paper", "scissors"]

# Scores
player_score = 0
ai_score = 0

print("=== Rock Paper Scissors AI ===")

while True:
    # Player input
    player = input("\nChoose Rock, Paper, or Scissors: ").lower()

    # Check if input is valid
    if player not in moves:
        print("Invalid choice! Try again.")
        continue

    # AI chooses randomly
    ai = random.choice(moves)

    print("You chose:", player)
    print("AI chose:", ai)

    # Decide winner
    if player == ai:
        print("It's a tie!")

    elif (
        (player == "rock" and ai == "scissors") or
        (player == "paper" and ai == "rock") or
        (player == "scissors" and ai == "paper")
    ):
        print("You win!")
        player_score += 1

    else:
        print("AI wins!")
        ai_score += 1

    # Show scores
    print("\nScore")
    print("You:", player_score)
    print("AI :", ai_score)

    # Play again?
    again = input("\nPlay again? (yes/no): ").lower()

    if again != "yes":
        print("\nFinal Score")
        print("You:", player_score)
        print("AI :", ai_score)
        print("Thanks for playing!")
        break

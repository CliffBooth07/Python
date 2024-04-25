
# Snake Water Gun Game

## Introduction
The Snake Water Gun game is a simple command-line game where the user competes against the computer. The user has three lives and needs to win ten rounds to emerge victorious. The game is based on the classic "Rock, Paper, Scissors" concept.

## Rules
- The user selects either "snake," "water," or "gun."
- The computer randomly selects one of these options.
- The winner of each round is determined as follows:
    - Snake vs. Water: Snake wins (Snake drinks water)
    - Water vs. Gun: Water wins (Gun gets wet)
    - Gun vs. Snake: Gun wins (Gun kills snake)
- The game continues until one of the following conditions is met:
    - The user wins ten rounds.
    - The user runs out of lives (three lives in total).

## Implementation
- The program uses a 2D list (matrix) to store the rules for each combination.
- User input and computer selection are used as indices to access the corresponding rule.
- The game loop continues until the user wins or loses.

## How to Play
1. Clone this repository to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the project directory.
4. Run the following command to start the game:
    ```
    python snake_water_gun.py
    ```
5. Follow the on-screen instructions to play the game.

## Example Output
```
Welcome to Snake Water Gun Game!
You have 3 lives. Win 10 rounds to win the game.

Round 1:
Enter your choice (snake/water/gun): snake
Computer chose: water
You win this round! 🎉

Round 2:
Enter your choice (snake/water/gun): gun
Computer chose: gun
It's a tie!

...


You have won the game. Congratulations! 🏆
```

Feel free to customize the code file with additional details specific to your thought/implementation. Good luck with your game! 🐍🌊🔫
---


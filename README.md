# Python_projects

# Snake, Water, Gun Game

A simple command-line implementation of the classic **Snake, Water, Gun** game — a well-known childhood variant of Rock-Paper-Scissors. The program plays a single round against you: it picks a random choice, you enter yours, and the winner is determined and printed to the console.

## Game Rules

Each round, one of three items is chosen: Snake, Water, or Gun. The winner is decided by the following cycle:

| Choice 1 | Beats | Choice 2 | Reason |
|----------|-------|----------|--------|
| Snake | beats | Water | The snake drinks the water |
| Water | beats | Gun | The water rusts/destroys the gun |
| Gun | beats | Snake | The gun kills the snake |

If both players pick the same item, the round ends in a **tie**.

## How It Works

1. The computer randomly selects one of three values using `random.choice()`: `1` (Snake), `-1` (Water), or `0` (Gun).
2. The user is prompted to enter a single letter: `s` for Snake, `w` for Water, or `g` for Gun.
3. The two choices are mapped to readable labels and printed.
4. An `if/elif` chain compares both choices and announces the result — a win, a loss, or a tie.
5. Any input other than `s`, `w`, or `g` is rejected with an "Invalid choice!" message.

## Requirements

- Python 3.x
- No external libraries — only the built-in `random` module is used.

## How to Run

1. Save the script as `snake_water_gun.py`.
2. Run it from a terminal:

```bash
   python snake_water_gun.py
```

3. Enter your choice when prompted:

```
   Enter your choice(s/w/g): s
```

## Example Output

```
Enter your choice(s/w/g): s
YOU CHOICES: Snake 
COMPUTER CHOICES: Water
YOU WIN!
```

If an invalid letter is entered:

```
Enter your choice(s/w/g): x
Invalid choice!
```

## Code Structure

| Component | Purpose |
|-----------|---------|
| `youDict` | Maps input letters (`s`, `w`, `g`) to numeric values (`1`, `-1`, `0`) |
| `reverseDict` | Maps numeric values back to readable names for display |
| `random.choice((-1, 1, 0))` | Generates the computer's move |
| `if/elif` chain | Compares both choices and prints the outcome |

## Possible Improvements

- Wrap the game in a loop so multiple rounds can be played without restarting the script.
- Track and display a running score across rounds.
- Replace the long `if/elif` chain with a lookup table or modular arithmetic for cleaner win/lose logic.
- Make input matching case-insensitive (accept `S` as well as `s`).
- Add a "play again?" prompt after each round.

## License

This project is free to use and modify for personal or educational purposes.


# Simple Calculator

A beginner-friendly command-line calculator built in Python that performs basic arithmetic operations on two numbers.

## Features

- Addition
- Subtraction
- Multiplication
- Division (with divide-by-zero protection)

## How It Works

1. The user enters two numbers.
2. The user selects an operation (`+`, `-`, `*`, `/`).
3. The result is calculated and printed.
4. If division by zero is attempted, a safe error message is shown instead of crashing.
5. If an invalid operation is entered, the program notifies the user.

## Requirements

- Python 3.x
- No external libraries — only built-in Python is used.

## How to Run

1. Save the script as `calculator.py`.
2. Run it from a terminal:

```bash
   python calculator.py
```

## Example Output

**Valid operation:**
```
Simple Calculator
Enter first number: 10
Enter second number: 5
Choose operation: +  -  *  /
Enter operation: *
Result: 50.0
```

**Division by zero:**
```
Simple Calculator
Enter first number: 8
Enter second number: 0
Choose operation: +  -  *  /
Enter operation: /
Cannot divide by zero
```

**Invalid operation:**
```
Choose operation: +  -  *  /
Enter operation: %
Invalid operation
```

## Code Structure

| Component | Purpose |
|-----------|---------|
| `float(input())` | Accepts decimal numbers from the user |
| `if/elif` chain | Checks which operation the user selected |
| `if num2 != 0` | Prevents crash on division by zero |
| `else` block | Handles invalid operation input |

## Possible Improvements

- Add support for modulus (`%`) and exponentiation (`**`).
- Wrap in a loop so user can calculate multiple times without restarting.
- Add a history feature to show previous calculations.
- Build a GUI version using `tkinter`.

## License

This project is free to use and modify for personal or educational purposes.
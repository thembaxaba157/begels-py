# 🎯 Bagels - Deductive Logic Game in Python

A classic number-guessing game based on deduction. This is a Python implementation of the **Bagels** puzzle, inspired by *The Big Book of Small Python Projects*.

> Guess a secret 3-digit number using logic. You have 10 tries — no repeated digits allowed!

---

## 🧠 Game Description

**Bagels** is a logic game where the player must guess a secret 3-digit number with **no repeated digits**.

Each guess provides clues:
- `Fermi`: A digit is correct and in the right position.
- `Pico`: A digit is correct but in the wrong position.
- `Bagels`: No digits are correct.

You get **10 tries** to guess the number.

---

## 🖥️ Example Gameplay

```
I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say:     That means:
    Pico        One digit is correct but in the wrong position.
    Fermi       One digit is correct and in the right position.
    Bagels      No digit is correct.

I have thought up a number.
You have 10 guesses to get it.
Guess #1
> 123
Pico
Guess #2
> 456
Bagels
...
Guess #6
> 789
Fermi Fermi Pico
...
You got it!
Do you want to play again? (yes or no):
```

---

## 📁 Project Structure

```text
bagels/
├── bagels.py            # Main game logic
├── test_functions.py    # (Optional) Unit tests for helper functions
└── README.md            # Project documentation
```

---

## 🛠️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/thembaxaba157/bagels-game.git
   cd bagels-game
   ```

2. Run the game:
   ```bash
   python3 bagels.py
   ```

3. Follow the on-screen prompts to guess the number!

---

## ✅ Features

- Fully interactive terminal gameplay
- Validates player input
- No repeated digits in guesses or secret numbers
- Play-again support
- Simple and readable structure

---

## 🧪 Tests

If `test_functions.py` is included:
```bash
python3 test_functions.py
```

---

## 🔍 Key Concepts

- Random number generation with unique digits
- User input validation
- String and list manipulation
- Game loop control and feedback
- Clean CLI output

---

## 📜 License

MIT License — use freely for learning or modification.

---

## 👨‍💻 Author

Coded by [@thembaxaba157](https://github.com/thembaxaba157)  
Based on the puzzle by [Al Sweigart](https://inventwithpython.com/).

---

⭐️ *If you enjoyed this project, consider starring the repo or checking out more Python logic games!*

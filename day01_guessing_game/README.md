# 🎯 Day 1 – Guessing Game

Welcome to Day 1 of my **100 Days of Python** challenge! 🐍🚀  

Today’s goal was to build a simple command-line guessing game

---

## 🕹️ The Game

The computer randomly chooses a number between **1 and 100**.  
Your job is to guess!

After every guess, the program tells you whether your number was was correct and gives you a hint if it was too big or too small

---

## ▶️ How to Run

From inside this folder:

```bash
python main.py

---

## 💡 What I Learned

- I learned that implementing logic inside functions and classes makes testing much easier. So next time I would extract the logic into a check_guess function.
- I used `__name__ == "__main__"` to make sure that `main()` only runs when the file is executed directly and not when it is imported.
- I learned how to generate a random number and how to get user input from the terminal.
- I clarified some Python syntax, such as writing `True` and `False` with capital letters, and using colons and indentation instead of parentheses when writing `if` statements.
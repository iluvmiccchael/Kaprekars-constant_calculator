# Kaprekars-constant_calculator
implementing kaprekar's constant with python
This project is a simple Python program that demonstrates the Kaprekar routine — the fascinating number process discovered by the Indian mathematician Dattatreya Ramchandra Kaprekar.

It allows a user to input a 4-digit number and automatically computes the steps required to reach the Kaprekar constant (6174).

🚀 Features

✔ Works with any 4-digit number (with at least two distinct digits)

✔ Displays each step of the Kaprekar routine

✔ Simple, beginner-friendly Python code

✔ Command-line interface (no GUI needed)

🛠️ How to Run

Make sure Python 3.8+ is installed.

Save the script as kaprekar.py.

Run the script in the terminal:

python kaprekar.py


Enter any 4-digit number when prompted.
Avoid numbers where all digits are identical (e.g., 1111, 2222), because they will not reach 6174.

🧠 Understanding Kaprekar’s Constant (6174)

Kaprekar’s constant is 6174, known for its intriguing mathematical property:

Take any 4-digit number with at least two different digits.

Rearrange the digits in descending order.

Rearrange the digits in ascending order.

Subtract the smaller number from the larger.

Repeat the process.

No matter what number you start with (with at least two distinct digits), you will always eventually reach 6174, after which the process loops:

7641 − 1467 = 6174


This iterative process is called the Kaprekar routine.

📜 Example Run

Starting with 3512:

Step 1: 5321 - 1235 = 4086
Step 2: 8640 - 0468 = 8172
Step 3: 8721 - 1278 = 7443
Step 4: 7443 - 3447 = 3996
Step 5: 9963 - 3699 = 6264
Step 6: 6642 - 2466 = 4176
Step 7: 7641 - 1467 = 6174
Reached Kaprekar's Constant: 6174 🎉

👤 About D. R. Kaprekar

Dattatreya Ramchandra Kaprekar (1905–1986) was an Indian mathematician known for his recreational math discoveries.

Despite being a schoolteacher and not formally a professional mathematician, he discovered:

Kaprekar’s constant (6174)

Kaprekar numbers

Self-numbers

Demlo numbers

His work demonstrates how simple arithmetic can reveal surprising mathematical patterns, and how curiosity and persistence lead to remarkable discoveries.

🧑‍💻 Program Logic

The program implements the Kaprekar routine:

Convert the number to a 4-digit string (preserving leading zeros).

Sort digits descending → largest number.

Sort digits ascending → smallest number.

Subtract: result = big - small.

Repeat until the number reaches 6174.

Print each step to the console.

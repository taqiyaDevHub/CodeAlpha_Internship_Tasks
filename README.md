# 🚀 CodeAlpha Internship Tasks

This repository contains four Python projects completed as part of the **CodeAlpha Internship Program**.

Each task demonstrates core programming concepts including:

- Conditional logic  
- Loops  
- Dictionaries  
- File handling  
- Regular expressions  
- User input handling  
- Basic automation  

---

## 📌 Project Overview

| Task | Project Name | Description |
|------|-------------|------------|
| Task 1 | Hangman Game | A console-based word guessing game with ASCII visualization |
| Task 2 | Stock Portfolio Tracker | Tracks stock investments and calculates total portfolio value |
| Task 3 | Task Automation with Python Scripts | Extracts valid email addresses from a text file using regex |
| Task 4 | Basic Chatbot | A simple rule-based interactive chatbot |

---

# Task 1: Hangman Game

## Description

A console-based Hangman game where the program randomly selects one word from a predefined list of 5 words.

The player guesses one letter at a time.

- Maximum 6 incorrect guesses are allowed.
- ASCII art updates after every wrong attempt.
- The game ends when the word is guessed correctly or attempts run out.

## Key Concepts Used

- `random` module  
- `while` loop  
- `if-else` conditions  
- Strings and lists  
- Input validation  

## How to Run

```bash
python Task01_HangmanGame.py
```

---

# Task 2: Stock Portfolio Tracker

## Description

A stock tracker that calculates total investment based on manually entered stock names and quantities.

Stock prices are stored in a hardcoded dictionary.

Users:

- Enter stock name
- Enter quantity
- Program calculates investment value
- Portfolio summary is displayed

Portfolio data is also saved to a file.

## Key Concepts Used

- Dictionary  
- User input  
- Basic arithmetic  
- Loops  
- File handling (optional but implemented)  

## How to Run

```bash
python Task02_StockPortfolioTracker.py
```

## Output File (Auto Generated)

When executed, the program automatically creates:

```
stock_tracker_file.txt
```

This file stores:

- Stock name  
- Price per share  
- Quantity entered  
- Total investment value  

---

# Task 3: Task Automation with Python Scripts (Email Extractor)

## Description

This program automates a repetitive task — extracting email addresses from a text file and saving them to another file.

It:

- Reads `sample_text.txt`
- Uses regular expressions (regex) to detect valid email patterns
- Removes duplicate emails
- Sorts them
- Saves results into a new file

## Key Concepts Used

- Regular expressions (`re`)  
- File reading & writing  
- Sets (for removing duplicates)  
- Sorting  
- Error handling  

## How to Run

```bash
python Task03_TaskAutomationWithPythonScripts.py
```

## Required Input File

```
sample_text.txt
```

## Output File (Auto Generated)

When executed, the program automatically creates:

```
extracted_emails.txt
```

This file contains:

- All unique extracted email addresses  
- Total number of emails found  

---

# Task 4: Basic Chatbot

## Description

A rule-based chatbot that responds to user input using predefined keyword detection.

The chatbot understands:

- Greetings
- Questions about identity
- Jokes
- Motivation
- Simple conversation
- Exit command ("bye")

The program runs continuously until the user types "bye".

## Key Concepts Used

- Conditional statements  
- Functions  
- Loops  
- String matching  
- Random response selection  

## How to Run

```bash
python Task04_BasicChatbot.py
```

---

# 📁 Project Structure

```
CodeAlpha-Internship-Tasks
│
├── Task01_HangmanGame.py
├── Task02_StockPortfolioTracker.py
├── Task03_TaskAutomationWithPythonScripts.py
├── sample_text.txt
├── Task04_BasicChatbot.py
└── README.md
```

---

# 🛠 Skills Demonstrated

Through these projects, the following skills were practiced:

- Python programming fundamentals  
- Data structures (lists, dictionaries, sets)  
- File handling operations  
- Regular expressions for text processing  
- Automation scripting  
- Game logic implementation  
- Interactive console application development  

---

# 👩‍💻 Author

**Syeda Taqiya Noman**

📧 Email: nomantaqiya31@gmail.com  
🔗 LinkedIn: https://www.linkedin.com/in/syeda-taqiya-noman

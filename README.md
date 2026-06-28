<div align="center">

# 🏛️ CS 61A: Structure and Interpretation of Computer Programs

### My complete coursework from UC Berkeley's legendary CS 61A

[![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=flat&logo=python&logoColor=ffdd54)](https://python.org)
[![Scheme](https://img.shields.io/badge/Scheme-LISP-1e4d2b?style=flat&logo=sublime&logoColor=white)](<#>)
[![SQL](https://img.shields.io/badge/SQL-336791?style=flat&logo=postgresql&logoColor=white)](<#>)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![UC Berkeley](https://img.shields.io/badge/UC%20Berkeley-CS%2061A-003262?style=flat&logo=university&logoColor=white)](https://cs61a.org)

</div>

---

## 📋 Overview

This repository contains my completed coursework for **CS 61A: Structure and Interpretation of Computer Programs** at UC Berkeley — widely regarded as one of the best introductory computer science courses in the world.

The course explores the **fundamental concepts of programming** through multiple paradigms:

- **Functional programming** — building abstractions with functions, lambda expressions, and recursion
- **Data abstraction** — compound data, sequences, and generic operations
- **Object-oriented programming** — classes, inheritance, and polymorphism
- **Metalinguistic abstraction** — interpreters, the Scheme dialect of Lisp
- **Declarative programming** — SQL and relational databases
- **Program design** — testing, modularity, and incremental development

---

## 📂 Repository Structure

```
cs61a/
├── 📓 lec/          # Lecture code & in-class exercises
│   ├── *.py         #   Python lecture examples
│   ├── *.ipynb      #   Jupyter notebook lectures
│   ├── *.scm        #   Scheme lecture examples
│   └── ucb.py / link.py / tree.py   # Course-provided utilities
│
├── 🧪 lab/          # Weekly lab assignments (hands-on practice)
│   ├── lab00–lab08  #   From setup through Scheme & interpreters
│   └── includes classes, cards, tree, and Scheme exercises
│
├── 💬 disc/         # Discussion section worksheets
│   ├── disc01–08    #   Python fundamentals through OOP & linked lists
│   ├── disc05.ipynb #   Jupyter notebook discussion
│   └── disc10.scm   #   Scheme discussion
│
├── 📝 hw/           # Homework assignments
│   ├── hw01–hw06    #   Ranging from basic expressions to Scheme
│   └── includes both Spring 2025 and Summer 2025 semesters
│
├── 🚀 projects/     # Major programming projects
│   ├── 🎲 hog/      #   The Game of Hog — dice strategy simulation
│   ├── 🐱 cats/     #   Cats — autocorrective typing speed tester
│   └── 🐜 ants/     #   Ants vs. SomeBees — Plants vs. Zombies clone
│
├── .gitignore       # Version control hygiene
├── pyproject.toml   # Python project metadata
├── .python-version  # Python version pinning
└── README.md        # You are here
```

---

## 🚀 Projects

### 🐜 Ants vs. SomeBees
> *A tower-defense game inspired by Plants vs. Zombies*

Build a full game with a web UI using **Flask + WebSocket**. Implemented insect classes, game mechanics, and a turn-based simulation engine. Features multiple ant types with unique abilities, a bee AI system, and an interactive web interface.

**Topics:** Object-oriented design, simulation, game logic, web frameworks

### 🐱 Cats: Typing Speed Trainer
> *An autocorrective typing tutor*

A multi-armed bandit-inspired typing game with **autocorrect**, **multiplayer leaderboards**, and **real-time typing analysis**. Implements string algorithms (minimum edit distance, autocorrect), a scoring engine, and a Flask web application with WebSocket-based multiplayer.

**Topics:** String algorithms, web development, real-time multiplayer, data structures

### 🎲 The Game of Hog
> *A dice-based strategy game*

A simulation of the classic dice game "Hog" with strategic AI players. Features dice probability analysis, optimal strategy computation, and both terminal and graphical UIs.

**Topics:** Higher-order functions, control abstractions, simulation, strategy optimization

---

## 🧠 Skills & Concepts Covered

| Category | Topics |
|---|---|
| **Python Fundamentals** | Expressions, control, higher-order functions, recursion, lambda calculus |
| **Data Structures** | Lists, tuples, dictionaries, sets, linked lists, trees, mutable sequences |
| **Object-Oriented** | Classes, inheritance, composition, special methods, design patterns |
| **Functional Programming** | Pure functions, immutability, map/reduce/filter, closures, decorators |
| **Scheme / Lisp** | S-expressions, recursive definitions, symbolic programming, interpreters |
| **SQL & Databases** | Queries, joins, aggregation, declarative programming paradigm |
| **Testing & Debugging** | Doctests, unit tests, iterative development, edge case analysis |
| **Algorithms** | String algorithms (edit distance), search, simulation, optimization |
| **Web Development** | Flask, WebSocket, HTML/CSS templating, real-time communication |

---

## 🛠️ Getting Started

```bash
# Clone the repository
git clone https://github.com/ac0033/cs61a.git
cd cs61a

# Ensure you have Python 3.14+
python --version

# Run a specific project (e.g., Hog)
python -m projects.hog.hog

# Run a homework solution
python -m hw.hw02.hw02

# Run tests for an assignment
python -m pytest lab/lab02/tests/
```

> **Note:** Some assignments use the course's `ok` autograder, which has been excluded from this repository in accordance with course policy.

---

## 📜 Academic Integrity & Attribution

### Course Materials

All assignment specifications, test cases, and starter code are the intellectual property of **UC Berkeley's CS 61A course staff**. They are included here for reference and educational context only.

- **Course Website:** [cs61a.org](https://cs61a.org)
- **License:** Course materials are © UC Berkeley and used under their educational license.

### My Solutions

The solution implementations in this repository are **my own work**, completed during my study of CS 61A. They are shared publicly as a **portfolio of my learning journey** and are not intended for use by current students to circumvent academic integrity policies.

### Usage

You are welcome to:
- ✅ Browse and learn from the code
- ✅ Use it as inspiration for your own solutions
- ❌ Submit it as your own coursework
- ❌ Redistribute the autograder (`ok`) infrastructure

If you are a current CS 61A student, please respect the course's [academic honesty policy](https://cs61a.org/articles/about.html) and complete assignments on your own.

---

## ✨ About Me

This repository is part of my programming portfolio, demonstrating proficiency in:

- Multiple programming paradigms (functional, OOP, declarative)
- Algorithm design and implementation
- Full-stack project development
- Version control and project organization
- Self-directed learning of rigorous computer science concepts

> *"The programmer of the future will be a generalist who is comfortable with many different paradigms and approaches to problem solving."*

---

<div align="center">

**📫 Connect & Feedback**

⭐ Star this repo if you found it useful or interesting!

*Built with dedication and a lot of recursion.* 🌀

</div>

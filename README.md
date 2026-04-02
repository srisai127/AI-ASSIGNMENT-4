# Assignment 4 (Artificial Intelligence)

## Overview
In this assignment, I solved different problems using the concept of 
Constraint Satisfaction Problems (CSP) from Russell and Norvig's book.

A CSP problem mainly has:
- Variables (things we need to assign values to)
- Domains (possible values)
- Constraints (rules that must be followed)

All problems are solved using the Backtracking algorithm.

---

## 1. Australia Map Coloring

In this problem, I assigned colors to different regions of Australia.

### Goal:
No two neighboring regions should have the same color.

### Approach:
- Each state is treated as a variable
- Colors like Red, Green, Blue are used
- Constraints ensure neighbors have different colors

---

## 2. Telangana Map Coloring (33 Districts)

In this problem, I extended map coloring to Telangana districts.

### Goal:
Assign colors to all districts such that no adjacent districts have the same color.

### Approach:
- Each district is a variable
- Used 4 colors (based on 4-color theorem)
- Applied Backtracking with MRV heuristic for better performance

---

## 3. Sudoku Solver

In this problem, I solved a 9x9 Sudoku puzzle.

### Goal:
Fill all empty cells so that:
- Each row has numbers 1 to 9 without repetition
- Each column has numbers 1 to 9 without repetition
- Each 3x3 box has numbers 1 to 9 without repetition

### Approach:
- Each empty cell is treated as a variable
- Numbers 1 to 9 are possible values
- Constraints check row, column, and box conditions

---

## 4. Cryptarithmetic Puzzle (SEND + MORE = MONEY)

In this puzzle, each letter represents a unique digit.

### Goal:
Find digits such that the equation is correct.

### Approach:
- Each letter is treated as a variable
- Digits 0–9 are assigned
- Ensured all digits are unique
- Checked the arithmetic condition

---

## Algorithm Used

### Backtracking
This is a trial-and-error method:
1. Assign a value
2. Check if it satisfies constraints
3. If not, backtrack and try another value

---

## Heuristic Used

### MRV (Minimum Remaining Values)
This helps choose the variable with the least possible options,
which makes the solution faster.

---

## Conclusion
All problems were solved successfully using CSP techniques.
Backtracking helped in finding correct solutions, and MRV improved efficiency.

This assignment helped me understand how CSP works in real-world problems.

---

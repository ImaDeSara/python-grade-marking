Overview

This Python program allows university staff to predict student progression outcomes at the end of each academic year based on their credits for pass, defer, and fail modules.
The program validates user input, displays the appropriate progression outcome, supports multiple students, generates a histogram, and provides options to store data in lists, text files, and dictionaries.

Part 1 – Basic Outcome Prediction

Accepts the number of credits at Pass, Defer, and Fail.
Calculates and displays the correct progression outcome:
Progress – Student passes all required modules.
Progress (Module Trailer) – Student progresses but has minor trailing modules.
Module Retriever – Student needs to retake failed/deferred modules.
Exclude – Student is excluded due to excessive failed credits.

Part 2 – List Storage

Stores all student outcomes and credit inputs in a nested list.
Displays saved outcomes in a structured format.

Part 3 – Text File Handling

Saves all student outcomes to a .txt file.
Reads the stored data and displays it in the required format.

Part 4 – Dictionary Storage

Stores progression outcomes using a nested dictionary with unique student IDs.
Displays stored outcomes alongside student IDs.

Input Validation

The program performs strict input validation:
Integer Validation → Displays Integer required if the input is not an integer.
Range Validation → Displays Out of range if the entered credits are not one of:
0, 20, 40, 60, 80, 100, 120.
Total Validation → Displays Total incorrect if the total of pass + defer + fail ≠ 120.

Histogram Generation

After entering multiple students’ data, the program displays a horizontal histogram summarizing all progression outcomes.
Each * represents one student in the corresponding category.

Technologies Used

Language: Python 3.x
Data Structures: Lists, Nested Lists, Dictionaries
File Handling: Reading & Writing .txt files
Control Flow: Efficient use of conditional statements


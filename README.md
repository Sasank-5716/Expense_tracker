# Expense Tracker
A simple desktop application built with Python and Tkinter to help you track your daily expenses by adding, viewing, and deleting expense entries. The app categorizes expenses and provides a summary of total spending.

## Features
Add new expenses with amount, category, date, and description.

View all expenses in a tabular format.

Delete selected expenses.

Automatically saves expenses to a JSON file (expenses.json) and loads them on startup.

Displays a summary showing total expenses and number of entries.

## Categories
Food

Transport

Entertainment

Bills

Shopping

Others

## Installation
Make sure you have Python 3 installed.

No external dependencies are required as it uses built-in tkinter and json modules.

## Clone the project
```bash
git clone https://github.com/Sasank-5716/Expense_tracker
```

## Usage
1. Run the script:

```bash
python expense_tracker.py
```
2. Use the input fields to add a new expense:

Enter the amount (numeric).

Select a category.

Enter the date in YYYY-MM-DD format.

Add a description.

3. Click Add Expense to save the entry.

4. View all expenses in the list below.

5. Select an expense and click Delete Selected to remove it.

6. The summary at the bottom shows the total expenses and count.

## File Structure
expense_tracker.py    
expenses.json            

## Error Handling
Validates amount input to ensure it is numeric.

Checks date format to be YYYY-MM-DD.

Ensures all fields are filled before adding an expense.

Displays appropriate error or warning messages for invalid inputs or operations.

### Created with Python Tkinter for easy expense management and tracking.
import tkinter as tk
from tkinter import ttk
import json
import os

class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.root.geometry("600x400")
        
        self.categories = ["Food", "Transport", "Entertainment", "Bills", "Shopping", "Others"]
        self.expenses = []
        self.load_data()
        
        self.create_widgets()
        self.update_expense_list()
        self.update_summary()


    # Expense list display
    def create_widgets(self):
        input_frame = ttk.LabelFrame(self.root, text="Add New Expense")
        input_frame.pack(pady=10, padx=10, fill="x")
        
        # Amount
        ttk.Label(input_frame, text="Amount:").grid(row=0, column=0, padx=5, pady=5)
        self.amount_entry = ttk.Entry(input_frame)
        self.amount_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Category
        ttk.Label(input_frame, text="Category:").grid(row=1, column=0, padx=5, pady=5)
        self.category_combo = ttk.Combobox(input_frame, values=self.categories)
        self.category_combo.grid(row=1, column=1, padx=5, pady=5)
        self.category_combo.set(self.categories[0])
        
        # Date
        ttk.Label(input_frame, text="Date (YYYY-MM-DD):").grid(row=2, column=0, padx=5, pady=5)
        self.date_entry = ttk.Entry(input_frame)
        self.date_entry.grid(row=2, column=1, padx=5, pady=5)
        
        # Description
        ttk.Label(input_frame, text="Description:").grid(row=3, column=0, padx=5, pady=5)
        self.desc_entry = ttk.Entry(input_frame)
        self.desc_entry.grid(row=3, column=1, padx=5, pady=5)
        
        # Add Button
        add_btn = ttk.Button(input_frame, text="Add Expense", command=self.add_expense)
        add_btn.grid(row=4, column=0, columnspan=2, pady=10)
        
        # Expense List Frame
        list_frame = ttk.LabelFrame(self.root, text="Expense List")
        list_frame.pack(pady=10, padx=10, fill="both", expand=True)
        
        # Treeview
        columns = ("ID", "Amount", "Category", "Date", "Description")
        self.expense_tree = ttk.Treeview(list_frame, columns=columns, show="headings", selectmode="browse")
        
        for col in columns:
            self.expense_tree.heading(col, text=col)
            self.expense_tree.column(col, width=100, anchor="center")
        
        self.expense_tree.pack(fill="both", expand=True)
        
        # Delete Button
        delete_btn = ttk.Button(list_frame, text="Delete Selected", command=self.delete_expense)
        delete_btn.pack(pady=5)
        
        # Summary Frame
        summary_frame = ttk.LabelFrame(self.root, text="Summary")
        summary_frame.pack(pady=10, padx=10, fill="x")
        
        self.summary_label = ttk.Label(summary_frame, text="")
        self.summary_label.pack()

        # Add save/load functionality
        def save_data(self):
            with open("expenses.json", "w") as f:
                json.dump(self.expenses, f)

        def load_data(self):
            if os.path.exists("expenses.json"):
                with open("expenses.json", "r") as f:
                    self.expenses = json.load(f)

        # Add expense functionality
        def add_expense(self):
            try:
                amount = float(self.amount_entry.get())
                category = self.category_combo.get()
                date = self.date_entry.get()
                description = self.desc_entry.get()

                # Input validation
                if not date or not description:
                    messagebox.showerror("Error", "Please fill all fields")
                    return
            
                # Date format validation (basic check)
                if len(date) != 10 or date[4] != '-' or date[7] != '-':
                    messagebox.showerror("Error", "Please enter date in YYYY-MM-DD format")
                    return
            
                expense = {
                    "id": len(self.expenses) + 1,
                    "amount": amount,
                    "category": category,
                    "date": date,
                    "description": description
                }
        
                self.expenses.append(expense)
                self.update_expense_list()
        
                # Clear fields
                self.amount_entry.delete(0, tk.END)
                self.date_entry.delete(0, tk.END)
                self.desc_entry.delete(0, tk.END)
        
            except ValueError:
                print("Please enter valid values")
            self.save_data()

        def update_expense_list(self):
            self.expense_tree.delete(*self.expense_tree.get_children())
            for exp in self.expenses:
                self.expense_tree.insert("", "end", values=(
                    exp['id'],
                    f"${exp['amount']:.2f}",
                    exp['category'],
                    exp['date'],
                    exp['description']
                ))
    
            # Delete Button
            delete_btn = ttk.Button(list_frame, text="Delete Selected", command=self.delete_expense)
            delete_btn.pack(pady=5)

        def delete_expense(self):
            selected = self.expense_tree.selection()
            if not selected:
                return
        
            item = self.expense_tree.item(selected[0])
            expense_id = item['values'][0]
    
            self.expenses = [exp for exp in self.expenses if exp['id'] != expense_id]
            self.update_expense_list() 
            self.save_data()

        # Add summary functionality
        # Summary Frame
        summary_frame = ttk.LabelFrame(self.root, text="Summary")
        summary_frame.pack(pady=10, padx=10, fill="x")
    
        self.summary_label = ttk.Label(summary_frame, text="")
        self.summary_label.pack()

    def update_summary(self):
        total = sum(exp['amount'] for exp in self.expenses)
        summary_text = f"Total Expenses: ${total:.2f} | Number of Expenses: {len(self.expenses)}"
        self.summary_label.config(text=summary_text)
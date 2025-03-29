import tkinter as tk
from tkinter import ttk

class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.root.geometry("600x400")
        
        self.categories = ["Food", "Transport", "Entertainment", "Bills", "Shopping", "Others"]
        self.expenses = []
        
if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()


# Expense list display
def create_widgets(self):
    # Add expense functionality
    def add_expense(self):
        try:
            amount = float(self.amount_entry.get())
            category = self.category_combo.get()
            date = self.date_entry.get()
            description = self.desc_entry.get()
        
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
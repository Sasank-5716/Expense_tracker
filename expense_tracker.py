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
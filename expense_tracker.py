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
    
    #input frame
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
    add_btn = ttk.Button(input_frame, text="Add Expense")
    add_btn.grid(row=4, column=0, columnspan=2, pady=10)
    
    # Expense List Frame
    list_frame = ttk.LabelFrame(self.root, text="Expense List")
    list_frame.pack(pady=10, padx=10, fill="both", expand=True)
    
    # Treeview
    columns = ("ID", "Amount", "Category", "Date", "Description")
    self.expense_tree = ttk.Treeview(list_frame, columns=columns, show="headings")
    
    for col in columns:
        self.expense_tree.heading(col, text=col)
        self.expense_tree.column(col, width=100, anchor="center")
    
    self.expense_tree.pack(fill="both", expand=True)
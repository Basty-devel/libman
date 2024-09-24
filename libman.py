import tkinter as tk
from tkinter import messagebox
import sys

class LibraryGUI:
    def __init__(self, root, library):
        self.library = library
        self.root = root
        self.root.title(f"{library.name} - Library System")
        self.root.geometry("600x500")
        self.root.configure(bg="#2C2F33")  # Dark grey background
        
        # Title
        self.title_label = tk.Label(root, text=f"Welcome to {library.name} Library", font=("Helvetica", 18, "bold"), bg="#2C2F33", fg="white")
        self.title_label.pack(pady=10)
        
        # Display Area for Books and Info
        self.info_area = tk.Text(root, height=15, width=60, font=("Courier", 10), bg="#23272A", fg="white", state="disabled", wrap="word")
        self.info_area.pack(pady=10)

        # Book Entry
        self.book_label = tk.Label(root, text="Book Name:", font=("Helvetica", 12), bg="#2C2F33", fg="white")
        self.book_label.pack()
        self.book_entry = tk.Entry(root, font=("Helvetica", 12), width=30)
        self.book_entry.pack(pady=5)
        
        # User Entry (for lending books)
        self.user_label = tk.Label(root, text="Borrower Name:", font=("Helvetica", 12), bg="#2C2F33", fg="white")
        self.user_label.pack()
        self.user_entry = tk.Entry(root, font=("Helvetica", 12), width=30)
        self.user_entry.pack(pady=5)
        
        # Buttons for operations
        self.create_buttons()

    def create_buttons(self):
        button_frame = tk.Frame(self.root, bg="#2C2F33")
        button_frame.pack(pady=10)

        button_style = {
            'bg': "#7289DA",  # Light blue
            'fg': 'white',
            'font': ("Helvetica", 12),
            'width': 15,
            'bd': 0,
            'highlightthickness': 0
        }

        # Buttons for different actions
        self.display_btn = tk.Button(button_frame, text="Display Books", command=self.display_books, **button_style)
        self.display_btn.grid(row=0, column=0, padx=10, pady=5)

        self.lend_btn = tk.Button(button_frame, text="Lend Book", command=self.lend_book, **button_style)
        self.lend_btn.grid(row=0, column=1, padx=10, pady=5)

        self.add_btn = tk.Button(button_frame, text="Add Book", command=self.add_book, **button_style)
        self.add_btn.grid(row=1, column=0, padx=10, pady=5)

        self.return_btn = tk.Button(button_frame, text="Return Book", command=self.return_book, **button_style)
        self.return_btn.grid(row=1, column=1, padx=10, pady=5)

    def display_books(self):
        self.update_info_area(f"We have the following books in the library '{self.library.name}':\n")
        for book in self.library.booklist:
            self.update_info_area(f" - {book}")
    
    def lend_book(self):
        book = self.book_entry.get().strip()
        user = self.user_entry.get().strip()

        if not book:
            messagebox.showerror("Error", "Please enter a book name.")
            return
        if not user:
            messagebox.showerror("Error", "Please enter the borrower's name.")
            return

        if book in self.library.booklist:
            if book not in self.library.lendDict:
                self.library.lendDict[book] = user
                self.update_info_area(f"\n'{book}' has been lent to {user}.")
            else:
                self.update_info_area(f"\n'{book}' is already lent to {self.library.lendDict[book]}.")
        else:
            messagebox.showerror("Error", f"The book '{book}' is not available in the library.")
    
    def add_book(self):
        book = self.book_entry.get().strip()

        if not book:
            messagebox.showerror("Error", "Please enter a book name.")
            return

        if book in self.library.booklist:
            self.update_info_area(f"\n'{book}' is already in the library.")
        else:
            self.library.booklist.append(book)
            with open(databaseName, "a") as bookDatabase:
                bookDatabase.write(f"{book}\n")
            self.update_info_area(f"\n'{book}' has been added to the library.")
    
    def return_book(self):
        book = self.book_entry.get().strip()

        if not book:
            messagebox.showerror("Error", "Please enter a book name.")
            return

        if book in self.library.lendDict:
            self.library.lendDict.pop(book)
            self.update_info_area(f"\n'{book}' has been successfully returned.")
        else:
            self.update_info_area(f"\n'{book}' was not lent from this library.")
    
    def update_info_area(self, message):
        self.info_area.configure(state="normal")
        self.info_area.insert(tk.END, message + "\n")
        self.info_area.configure(state="disabled")
        self.info_area.see(tk.END)  # Scroll to the end of the text

# The Library class (logic remains the same)
class Library:
    def __init__(self, name, booklist):
        self.name = name
        self.booklist = booklist
        self.lendDict = {}

def main():
    # Initialize the root window
    root = tk.Tk()

    # Create the library system
    library = Library("LibMan", booklist)

    # Initialize the GUI
    gui = LibraryGUI(root, library)

    # Start the GUI main loop
    root.mainloop()

if __name__ == "__main__":
    booklist = []
    databaseName = input("Enter the name of the database file with extension (e.g., books.txt): ")

    # Load books from the file into booklist
    try:
        with open(databaseName, "r") as bookDatabase:
            booklist = [book.strip() for book in bookDatabase.readlines()]  # Strip newlines from book names
    except FileNotFoundError:
        print(f"Error: The file '{databaseName}' does not exist. Starting with an empty book list.")

    main()

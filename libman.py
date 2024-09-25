from PIL import Image, ImageTk, ImageDraw
import tkinter as tk
from tkinter import messagebox

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

        # Set rounded-corner image for all buttons
        self.display_btn = self.create_custom_button(button_frame, "Display Books", self.display_books)
        self.display_btn.grid(row=0, column=0, padx=10, pady=5)

        self.lend_btn = self.create_custom_button(button_frame, "Lend Book", self.lend_book)
        self.lend_btn.grid(row=0, column=1, padx=10, pady=5)

        self.add_btn = self.create_custom_button(button_frame, "Add Book", self.add_book)
        self.add_btn.grid(row=1, column=0, padx=10, pady=5)

        self.return_btn = self.create_custom_button(button_frame, "Return Book", self.return_book)
        self.return_btn.grid(row=1, column=1, padx=10, pady=5)

        button_frame.pack(pady=10)

    def create_custom_button(self, frame, text, command):
        # Create a rounded-corner button image with Pillow
        button_img = self.create_rounded_rectangle_image(width=150, height=40, radius=20, color="#7289DA")
        button_image = ImageTk.PhotoImage(button_img)

        button = tk.Button(frame, text=text, command=command, image=button_image, compound="center", bg="#7289DA", fg="white", font=("Helvetica", 12), borderwidth=0)
        button.image = button_image  # Keep reference to the image to prevent garbage collection
        return button

    def create_rounded_rectangle_image(self, width, height, radius, color):
        """Create an image with rounded corners to use as a button."""
        image = Image.new("RGBA", (width, height), (255, 255, 255, 0))  # Transparent background
        draw = ImageDraw.Draw(image)

        # Draw the rounded rectangle
        draw.rounded_rectangle((0, 0, width, height), radius=radius, fill=color)
        return image

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

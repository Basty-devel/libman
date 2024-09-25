LibMan: A Simple & Elegant Library Management System

LibMan is a powerful yet simple-to-use library management system designed for personal libraries, small educational institutions, or anyone looking to manage books efficiently. It combines modern UX design with a seamless user interface, making book management a breeze!

Features
🏷️ Add Books: Easily add new books to your library with just one click.
📖 Lend Books: Keep track of who has borrowed which books with real-time updates.
🔄 Return Books: Simplify the process of returning books and keep your library in order.
📚 Display Books: View all the available books in your collection in an organized and easy-to-read format.
💡 Interactive GUI: Enjoy a clean, intuitive graphical interface with an elegant dark mode for comfortable usage.
🚀 Real-time Feedback: Receive immediate feedback for every action taken—whether adding, lending, or returning books.
📂 Database Integration: Manage your book collection using a simple text file for storing and retrieving data.
Why Choose LibMan?
In a world full of complicated library management systems, LibMan focuses on simplicity and elegance. Whether you're running a small school library or managing your personal book collection, LibMan provides a minimalistic, stress-free way to keep everything organized. Here's why you'll love using LibMan:

User-Centric Design: LibMan has a clean and user-friendly interface to ensure the best user experience (UX). No more clunky forms or difficult navigation—just smooth, intuitive interactions.

Fast & Efficient: With quick actions, you'll spend less time managing your books and more time reading.

No Learning Curve: You don't need to be tech-savvy to use LibMan. Simply open the app, and you’re ready to start managing your library!

Extendable & Open Source: Developers are welcome! Modify and expand LibMan to fit your needs—it's open-source and highly customizable.


How to Install
1. Clone the Repository
First, clone the repository from GitHub to your local machine:

bash

git clone https://github.com/Basty-devel/libman.git
cd libman

2. Install Dependencies
LibMan requires Python 3.x and tkinter plus Pillow which is included in standard Python installations. If you're missing a module, you can run it as follows:

For Ubuntu/Debian:

bash libman.sh


For MacOS:

tkinter is included with Python, but you may need to ensure that you have the latest version installed from python.org and the module Pillow.

3. Prepare the Database
LibMan uses a simple text file to store your books. If you already have a collection, create a file (e.g., books.txt) with one book name per line:

books.txt

The Great Gatsby
1984
Moby Dick
Pride and Prejudice
When you run LibMan, it will ask you for this file to load the existing books.

4. Run the Application
Run the following command to start LibMan:

bash libman.sh
Once launched, you'll be greeted with the modern and intuitive GUI to manage your library. Just follow the on-screen instructions to add, lend, return, and view books!

How to Use
Add Books: Input the book name and click 'Add Book' to add it to your collection.
Lend Books: Enter the book name and the borrower’s name, and click 'Lend Book' to record the lending.
Return Books: To return a book, simply enter the book name and click 'Return Book'.
Display Books: Click 'Display Books' to view all available books in the library.
The system provides real-time updates in the text area, showing the status of each operation and current library data.

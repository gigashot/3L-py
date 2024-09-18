# Library Management System

This is a simple Library Management System written in Python. The system allows users to register, log in, borrow books, return books, and add new books to the library.

## Features

- **User Registration**: New users can register by providing a username and password.
- **User Login**: Registered users can log in using their username and password.
- **Borrow Books**: Users can borrow available books from the library.
- **Return Books**: Users can return borrowed books.
- **Add Books**: Admins can add new books to the library.
- **View Available Books**: Users can view a list of available books.

## Files

- `app.py`: The main application file containing all the functions for the library management system.
- `knihy.csv`: A CSV file containing the list of books in the library.
- `uzivatele.csv`: A CSV file containing the list of registered users.

## How to Run

1. Ensure you have Python installed on your system.
2. Place `app.py`, `knihy.csv`, and `uzivatele.csv` in the same directory.
3. Open a terminal or command prompt and navigate to the directory containing the files.
4. Run the application by executing:
    ```sh
    python app.py
    ```

## Usage

1. **Menu**: The program starts by displaying a menu with options to view available books, borrow a book, return a book, add a new book, or exit the program.
2. **Login/Registration**: Users need to log in or register to borrow or return books.
3. **Borrow Books**: Users can borrow books by providing the book's title.
4. **Return Books**: Users can return books they have borrowed.
5. **Add Books**: Admins can add new books to the library by providing the book's title, author, and ISBN.





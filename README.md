# BookStore Project

BookStore is a full-featured Django web application for managing books in an online store. It allows users to add, edit, delete, and view books through a clean and responsive Bootstrap interface. Ideal for learning CRUD operations and Django fundamentals.

## Live Demo
Check out the project here [Demo 🡕](https://www.salankatuwal.com.np/bookstore.html)

## How the web app works

- **Home Page** – Displays total number of books and shows 3 random books
![Home](/photos/home.png) 

- **Add Book** – Form to add new books
![Add](/photos/add.png) 

- **Book List** – All books currently in the store
![App Screenshot](/photos/list.png) 

- **Book Details** – View detailed information of a specific book
![App Screenshot](/photos/details.png) 

- **Edit Book** – Update existing book information
![App Screenshot](/photos/edit.png) 

- **Delete Book** – Remove a book from the store
![App Screenshot](/photos/delete.png) 

- **Duplicate Book Restriction** – Prevents duplicate entries
![App Screenshot](/photos/same.png) 


## Features

- Add, update, and delete books (admin functionality).
- Responsive design using Bootstrap.
- View book details and descriptions.

## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/SalanKatuwal/Django-Book-Store
    cd BookStore
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```bash
    python manage.py migrate
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```

6. Open your browser and navigate to `http://127.0.0.1:8000`.

## Usage

- **Admin Panel**: Access the admin panel at `/admin` to manage books and users.
- **Browse Books**: View the list of available books and search for specific titles or authors.
- **Responsive Design**: The application is mobile-friendly and adapts to different screen sizes.


## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- Django documentation
- Bootstrap framework  
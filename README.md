# Django Todolist App


The Django TodoList App is a simple web application built using the Django framework that allows users to manage their tasks and to-do lists. This app provides an intuitive and user-friendly interface for adding and deleting tasks.

## Features

- **Task Management**: Add and delete tasks easily.
- **Task Status**: Mark tasks as complete or incomplete.
- **User-Friendly Interface**: Intuitive design for smooth user experience.
- **Responsive**: The app is responsive and works well on various screen sizes.
- **Data Persistence**: Tasks are stored in a database, ensuring data persistence.

## Getting Started

To run the Django TodoList App on your local machine, follow these steps:

1. **Clone the Repository**: 
   ```sh
   git clone https://github.com/ali-aj/django-todolist-app.git
   cd django-todolist-app
   ```

2. **Create Virtual Environment** (Recommended):
   ```sh
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:
   ```sh
   python manage.py migrate
   ```

5. **Create Superuser** (Admin):
   ```sh
   python manage.py createsuperuser
   ```

6. **Run Development Server**:
   ```sh
   python manage.py runserver
   ```

7. Open your web browser and go to `http://127.0.0.1:8000/` to access the TodoList app.

## Configuration

You can customize the behaviour of the app by modifying the `settings.py` file in the `todolist` directory. Here are some important configurations:

- **SECRET_KEY**: Change this to a strong and unique secret key for security.
- **DEBUG**: Set to `True` during development; change to `False` in production.
- **ALLOWED_HOSTS**: Add the list of allowed hosts when `DEBUG` is `False`.
- **DATABASES**: Configure your database settings (default is SQLite).

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.


**Disclaimer**: This app is developed for educational purposes and as a demonstration of Django usage. It may not be suitable for production use without further modifications and security considerations.

For more information about Django, visit the official [Django documentation](https://docs.djangoproject.com/).

Feel free to contact me for any questions or inquiries.

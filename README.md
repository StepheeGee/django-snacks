
# Lab 26: Django Snacks

This lab explores the Django web framework by building a simple web application called "Django Snacks." The application showcases the use of Django's views, templates, and static files to create a basic website with multiple pages. (2.12.24)

## Author: Stephanie G. Johnson

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd django-snacks
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

On Windows:

```bash
.\.venv\Scripts\activate
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply Migrations

```bash
python manage.py migrate
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

The application will be accessible at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Project Structure

- `snacks/`: Django application directory.
  - `urls.py`: Define URL patterns for the application.
  - `views.py`: Contains view classes for rendering HTML pages.
  - `templates/`: Directory for HTML templates.
  - `static/`: Directory for static files such as CSS.

- `snacks_project/`: Project-level directory.
  - `settings.py`: Project settings including installed apps and configurations.
  - `urls.py`: Project-level URL configurations.

## Pages

- **Home:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **About:** [http://127.0.0.1:8000/about/](http://127.0.0.1:8000/about/)

## Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django Tutorial](https://docs.djangoproject.com/en/3.2/intro/tutorial01/)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)

## Additional Notes

- The application uses Tailwind CSS for styling.
- Ensure that the virtual environment is activated when running Django commands.

Feel free to explore, modify, and extend the project as part of the learning process.

Happy coding!


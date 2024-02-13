# Lab 26: Django Snacks

2.12.24

## Overview

Django Snacks is a simple Django project showcasing the use of templates, static files, and Django applications.

## Author: Stephanie G. Johnson

## Project Structure

- **django-snacks/:** Project-level directory.
  - **snacks/:** Django application directory.
    - **urls.py:** Define URL patterns for the application.
    - **views.py:** Contains view classes for rendering HTML pages.
  - **snacks_project/:** Project settings and configurations.
    - **settings.py:** Project settings including installed apps and configurations.
    - **urls.py:** Project-level URL configurations.
  - **static/:** Directory for static files such as CSS.
    - **output.css:** Compiled CSS file for styling.

  - **templates/:** Directory for HTML templates.
    - **about.html:** Template for the about page.
    - **base.html:** Base template with common structure.
    - **home.html:** Template for the home page.

## Usage

1. Clone the repository: `git clone https://github.com/your-username/django-snacks.git`
2. Navigate to the project directory: `cd django-snacks`
3. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install dependencies: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Start the development server: `python manage.py runserver`

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to view the Django Snacks project.

## Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django Templates](https://docs.djangoproject.com/en/3.2/topics/templates/)
- [Django Static Files](https://docs.djangoproject.com/en/3.2/howto/static-files/)
- [Tailwind CSS](https://tailwindcss.com/)

Happy coding!

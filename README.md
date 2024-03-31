# Recipe Sharing Website

Welcome to the RecipeSite Repository! This Django project was developed as part of my Level 6 Software Development course. This project is dedicated to providing a platform for food enjoyers to explore, share, and celebrate the art of creating various foods.

## Project Objectives

* Utilize the Django framework to create a comprehensive culinary website.
* Implement a user-friendly interface with a clean, attractive design.
* Ensure the website is responsive and accessible on various devices.

## Dependencies

* python3.12.2
* sqllite
* Django 5.0.3
* pillow 10.2.0
* venv
* Bootstrap 5.3.3

## Cloning & Setup

1. Clone the repository
```bash
git clone https://github.com/MaxFairfield/RecipeSite.git
```

2. Activate the virtual environment
```bash
.venv/Scripts/activate
```

3. Navigate to the project directory
```bash
cd recipeinfo
```

4. Apply migrations
```bash
py manage.py migrate
```

5. Create superuser
```bash
py manage.py createsuperuser
```

6. Run the server
```bash
py manage.py runserver ( <address>:<port> )
```


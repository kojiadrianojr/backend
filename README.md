## Introduction:
Blogsite BE is the backend service for blogsite-fe, a simple web application blogging platform. Built with Django, Blogsite BE provides robust and scalable RESTful APIs to support user authentication, and blog post management.

## Requirements
- Python
- Django
- Django Rest Framework
- Djoser 

> [!NOTE]
> This repository is the backend for the application [blogsite-fe](https://github.com/kojiadrianojr/blogsite-fe/tree/master)

## Setup
Follow these steps to get a local copy of the project up and running.

1. Close this repository
```
git clone https://github.com/kojiadrianojr/backend.git
```
2. Create and activate a veritual environment
3. Copy the ```requirements.txt``` to your virtual environment
4. Activate your virtual environment
5. Install the dependencies
```
pip install -r requirements.txt
```
> [!NOTE]
> You can read more about virtualenv here: https://virtualenv.pypa.io/en/latest/user_guide.html

## Running the server
1. Apply migration
```
python manage.py migrate
```
2. Run the development server
```
python manage.py runserver
```

## Live URL
The api is deployed on https://www.pythonanywhere.com/, and can be accessed here:
- [Blogsite API](https://kojiadrianojr.pythonanywhere.com/)


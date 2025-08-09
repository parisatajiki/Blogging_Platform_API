# Blogging Platform RESTful API

This is a simple RESTful API for a personal blogging platform built with Django and Django REST Framework (DRF). The API allows users to perform basic CRUD operations on blog posts, including creating, reading, updating, deleting, and searching posts.

https://roadmap.sh/projects/blogging-platform-api

## Features

- Create a new blog post
- Retrieve all blog posts
- Retrieve a single blog post by ID
- Update an existing blog post
- Delete a blog post
- Search blog posts by a term in title, content, or category

## Technologies Used

- Python 3.x
- Django 5.x
- Django REST Framework
- SQLite (default) or any other supported database

## API Endpoints

| Method | Endpoint                   | Description                           |
|--------|----------------------------|-------------------------------------|
| GET    | `/posts/`                  | Get all blog posts                   |
| GET    | `/posts/<id>/`             | Get a single blog post by ID         |
| POST   | `/posts/`                  | Create a new blog post               |
| PUT    | `/posts/<id>/`             | Update an existing blog post by ID  |
| DELETE | `/posts/<id>/`             | Delete a blog post by ID             |
| GET    | `/posts/search/<term>/`    | Search blog posts by a search term  |



```bash
python manage.py runserver

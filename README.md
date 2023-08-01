# TODO list API

![todo Logo](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSR8oWPV84lpAndX08f9COYfNXMAuWNOEAmFA&usqp=CAU)

- This is an Application Programming Interface for a todo-list built in [django](https://docs.djangoproject.com/) and [django rest framework](https://www.django-rest-framework.org/) with [python](https://www.python.org/).

![](https://img.shields.io/badge/python-3.11.0-red)
![](https://img.shields.io/badge/django-4.0.3-blue)

## Table Of Contents

- [Project Folder Structure](#folder-structure)
- [Django Apps](#django-apps)
- [How to Run API Locally](./docs/installation.md)

## Folder Structure

```sh
C:.
├───todolist
├───docs
├───.vscode
├───api
```

### Django Apps

- [**todolist**](./todolist/)
  - App containing django project settings and project configurations.
- [**api**](./accounts)
  - App containing all todo-list api logic.

## How to Run Project

- [👉🏿Click Me👈🏿](./docs/installation.md) to get project installation instructions.

## Python Version

- `python 3.11.0`
- Check the `runtime.txt` file

## Features
- [x] API Documentation with Swagger
- [x] CRUD Functionality
- [x] linting with Black
- [x] Documentation with MKDOCS

## Important URLs

After [Installation]() and starting the server, visit the following URLs

1. Visit the browsable API at [http://localhost:8000/api/v1/](http://localhost:8000/api/v1/)

2. Access the Django admin at [http://localhost:8000/admin](http://localhost:8000/admin/)

3. Visit reDoc documentation [http://localhost:8000/](http://localhost:8000/)

4. Visit Swagger documentation [http://localhost:8000/doc](http://localhost:8000/doc)

5. - `mkdocs serve` - Start the live-reloading docs server.

## Concept Diagrams

- [Link to ERD Diagram](https://app.creately.com/d/create?templateId=ib873xm31)

## Postman collection

- Click me to see [postman collection](docs/postman/todo-list-api.postman_collection.json)
- Simply import this [file]() into your [postman]() to see the API documentation and usage information.

# Before Contribution

- Understand [Git Flow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow#:~:text=What%20is%20Gitflow%3F,lived%20branches%20and%20larger%20commits.)
- Use [Semantic Commit Messages](/docs/semantic-commit-message.md)
<!-- - Read [Project Scope]() -->

&copy;todo-api

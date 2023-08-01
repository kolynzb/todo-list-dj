# Local installation for development

## Prerequisites

- _Note_ that the python version used is ![](https://img.shields.io/badge/python-3.11.0-red)

- Clone the repository

```sh
  git clone https://github.com/kolynzb/todo-list-dj.git && cd todo-list-dj
```

## Local Development Setup

- Run `cp .env.example .env` to copy the environment variables to a `.env`
- Fill out the missing environment variables in `.env`
- _Refer to the [.env.example](../.env.example) file at the root of the project to learn more about what variables to add to the file_

- Create a virtual environment with your preferred tool(_either conda ,pipenv,venv_)

  - For `pipenv` (_most preferred for this project_)
    - Run the following commands
    ```bash
    pip install pipenv # install pipenv
    pipenv shell # start virtual environment
    pipenv install # install all packages
    ```
  - For `venv`
    - Run the following commands
    ```bash
     pip install virtualenv
     python3 -m venv <name-of-environment> && source <name-of-environment>/bin/activate
    pip install -r requirements.txt
    ```

- Create and Run migrations

```bash
python manage.py migrate
python manage.py makemigrations
python manage.py runserver
```

- Open [localhost:8000](http://localhost:8000) or [127:0:0:1:8000](http://127:0:0:1:8000) to see the API documentation.

- You're now ready to Work! ✨ 💅 🛳

### Create superuser

If you want, you can create initial super-user with next commad:

```bash
./manage.py createsuperuser
```

## Code formatting using black

To format the code automatically using `black`,
just run it in the project directory:

    black .

-

## Vscode setting

- The vscode settings can be found in the `.vscode` folder
- A list of recommended vscode extensions are included in the `extensions.json` file.

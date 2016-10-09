# django-basic-crm-1.10

Prosty system CRM w technologiach Python/Django oraz przy użyciu twitter bootstrap-a jako frontendu.

System będzie realizować następujące zadania:

1. Strona główna - okno logowania
2. Po zalogowaniu widoczne w menu są dwie sekcje: companies oraz users.
3. W sekcji companies na głównym ekranie jest tabela z listą aktualnie dodanych firm, oraz przycisk umożliwiający dodanie nowej firmy.
4. Sekcja users pozwala na zarządzanie użytkownikami, którzy mogą logować się do systemu.

Installation
------------
    $ sudo apt-get install python3.5-venv

    $ python3 -mvenv myvenvcrm
    $ source myvenvcrm/bin/activate

    $ python3 -m pip install -U pip
    $ python3 -m pip install -U setuptools
    $ python3 -m pip install -r requirements.txt

    $ #deactivate

    $ python3 -m pip freeze > requirements.txt

    $ python3 manage.py migrate
    $ python3 manage.py runserver

    To be able to log in use the following

    user: guest

    password: guestpassword
    
Runner
------

    {
    "cmd": [
        "bash",
        "--login",
        "-c",
        "source myvenvcrm/bin/activate && python manage.py runserver $ip:$port"
    ],
    "working_dir": "$project_path",
    "info": "Your code is running at \\033[01;34m$url\\033[00m.\n\\033[01;31m"
    }
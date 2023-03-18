<h2 align="center">PhotoBlog</h2>

### Description of a project:
Django based simple photoblog (pet-project)

### Stack of technologies:
- Python >= 3.10
- Django == 4.1.7
- SQLite3

## Development:

##### 1) Clone the repository:
    git clone https://github.com/mymotherati/photoblog.git

##### 2) Create a virtual environment:
    cd photoblog
    python -m venv venv

##### 3) Activate the environment:
###### Linux:
    source /venv/bin/activate

###### Windows:
    ./venv/scripts/activate
    
##### 4) Install requierments:
    pip install -r req.txt
    
##### 5) Execute migrations:
    manage.py migrate
    
##### 6) Create superuser:
    manage.py createsuperuser

##### 7) Run server:
    manage.py runserver

##### 8) Links
- Site: http://127.0.0.1:8000/
- Admin-panel: http://127.0.0.1:8000/admin

## License

[The MIT License](https://opensource.org/license/mit/)

Copyright (c) 2023 mymotherati - Maslov Roman

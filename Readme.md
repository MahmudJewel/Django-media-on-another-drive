# Media on another drive
This is a project for changing media route on another drive.
Thange route as bellow:
```sh
$ PATH = '/run/media/mahmud/Project/Practice/Django/storage'
$ MEDIA_ROOT = os.path.join(PATH, 'media')
$ MEDIA_URL = "/media/" 
```

# Tools
### Back-end
#### Language:
	Python (3.10.7)

#### Frameworks:
	Django(4.1.2)
	
#### Other libraries / tools:
	asgiref     3.5.2
	Pillow      9.2.0
	pycodestyle 2.9.1
	setuptools  63.2.0
	sqlparse    0.4.3
	toml        0.10.2

	
### Database:
	SQLite

# Setup
The first thing to do is to clone the repository:
```sh
$ https://github.com/MahmudJewel/Django-media-on-another-drive
```
### Back-end
Create a virtual environment to install dependencies in and activate it:
```sh
$ cd Django-media-on-another-drive
$ python -m venv venv
$ source venv/bin/activate
```
Then install the dependencies:
```sh
(venv)$ pip install -r requirements.txt
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(venv)$ python manage.py migrate
(venv)$ python manage.py runserver 8000
```

# Happy Coding
## From ==> Juwel Mahmud


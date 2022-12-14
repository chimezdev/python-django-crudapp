# MUSICAPP WITH DJANGO - PYTHON
- use  `rm -r -Force .git`
## Create a virtual environment

- Create a virtual environment by running the command, `mkdir <project_name>` to create project folder
- cd into the project folder `cd <project_folder>`
- run `virtualenv <env_name>` to create environment
cd into the environment and run `<env_name>\Scripts\activate` to activate the virtual environment

## Install django in the environment
- run the command, `pip install django` to install django
- You can run, `django-admin --version` to check the installation

## Creating Django project
- run the command, `django-admin startproject <project_name>` to create a django project
- a new folder with the name you have choosen will have appeared in the project directory
- cd into the project directory
To start server run the command, `python manage.py runserver`.

## Creating the *musicapp* application
- run the command, `python manage.py startapp <your_app_name`. remember the server has to be running
- add the *~musicapp~* to the list of installed app in settings.py
To access the admin endpoint, magration has to be applied.
- run the command, `python manage.py migrate` to apply migration.
- go to *~<ip_address:port/admin>~* to access the login page.

To create a user
- run the command, `python manage.py createsuperuser`
Follow the prompt to provide *~username~*, *~email_address~* and *~password~*.
The credentials can then be used to login to the ***musicapp*** admin page.

## Create **requirements.txt** file
While your virtualenv is active, run `pip freeze > requirements.txt`. This will generate a .txt file with the list of packages required to run this project.
- to install the requirement.txt contents run, `pip install -r requirement.txt`

## Configure urls and render views
- Open the musicapp/urls.py and create url path to be rendered by the view
- add the path, ***path('', views.index, name="index")*** to the 'urlpatterns' list. Don't forget to import views .(the same directory)
- goto ***views.py*** file and create your view. In my case, I simply returned an HttpResponse
- goto into songcrud/urls.py and update it to render our musicapp view
- import *include* 
- then do, ***path('', include('musicapp.urls'))***
- save and refresh the homepage.

## Creating Template files
- create a folder *templates* in the *songcrud* django project directory
- go to setting.py and add directory to the templates in the *TEMPLATES* list
- in the *templates* folder, create your *index.html* file
- in views.py, you can instead return render
- follow the steps to add any additional 'html' you intend to include

### Seperate template files
- create a main.html file that will contain the boilerplate of html that other templates will extend from
- create a *navbar.html* file too so we can seperate it from main.
- add this block in the body of the main.html, `{% include 'navbar.html' %}` this tells django to include navbar in this location
- add this block 
    ```{% block content %}

    {% endblock %}```, it is recognized by django and markups will be added.
- also include `{% extends 'main.html' %}` block to other template viles that you want them to inherit the main.html content.

### Styling our templates
I used bootstrap.
- google bootstrap navbar
- copy the styling you like and paste into *navbar.html* file and save.
- get the css file as well, you can paste this in the *main.html* file and every other template will still inherit it.
- if you want to get a dark navbar, change `navbar-dark bg-dark` on the first line of the html, where you have 'light' to dark.
- copy the js link from bootstrap and paste in the bottom section of the *main.html*, to add action to the navbar.

## Adding Static files
The static folder is where we store our css, js and media files including the images and videos
- create a folder *static* in the *songcrud* django project directory
- in it create 3 other folders named *css*, *image*, and *js*
- in the css folder a *main.css* file
- write your main css file here. 
- to link it to your template, first tell django that it exist by going to the *settings.py* file
- scroll down to where you have **STATIC_URL = ...** and add this line of code `STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)`
- add `MEDIA_URL = 'image/'` to reference media files
- remember to import '*os*' at the top
    - ### Linking Static Files
    - add `{% load static %}` at the top of every template file you want to import a static file
    - then a static file is linked using the *link* in this format, `<link rel="stylesheet" href="{% static 'css/main.css' %}">`
    - to link media file use the *img* tag in this format `<img src="{% static "image/logo.jpg" %}" class="logo">`
    - use the *a* link tag `<a class="nav-link" href="{% url 'index' %}">Home<span class="sr-only">(current)</span></a>` to link a clickable link to a page.

## Model Creation
A model refers to a table in the database and it is defined by defining *class* and attributes. The class attributes represent the table columns.
- in the models.py file, define the classes *Artiste*, *Song*, and *Lyric*
- add the following attributes to the *Artiste* class: *first_name, last_name, age*
- remember that django automatically adds the *id* but you can def this as well
- to manually define the id import uuid and use the `UUIDField()` 
- add the following attributes to the *Artiste* class: *title, date released, likes, artiste_id*
- add the following attributes to the *Artiste* class: *content, song_id*
    - ### Tables Relationship
    - the table *Song* has a *one-to-many* relationship with the table *Artiste*
    - this means that an **Artiste can have many songs but a Song should have only one Artiste**
    - to specify this, the *FereignKey()* used, `artiste_id = models.ForeignKey(Artiste, null=True, on_delete=models.SET_NULL)`
    - and this will serve as the *artiste_id* attr of the **Song** class.
    - the *on_delete=models.SET_NULL* tells django to leave the song if the artist is deleted, you can use 'CASCADE' which will delete the song too or 'PROTECTED'
    - run `python manage.py makemigrations` to create migration file out of this model
    - run `python manage.py migrate` to apply this migration. this will create the required tables in our db.
    - visit the '/admin' page to view.
    - run `python manage.py migrate musicapp zero` to reset migration or `python manage.py migrate <app_name> <migration_file_num_code> to undo that particular migration.

## Hiding Sensitive Data using Environment Variable
- run `pip install django-dotenv` 
- do `from dotenv import load_dotenv`in the *settings.py* file 
- below your import; Initialise environment variables by doing:
- `load_dotenv()`
- create *'.env'* file in the same directory as *settings.py*
- Declare your environmental variables here, don't wrap the values with quotation mark.
-   ```
        SECRET_KEY=h^z13$qr_s_wd65@gnj7a=xs7t05$w7q8!x_8zsld#
        DATABASE_NAME=postgresdatabase
        DATABASE_USER=stone
        DATABASE_PASS=supersecretpassword
    ```
- since using sqlite3 this is what i did:
    ```
        SECRET_KEY=h^z13$qr_s_wd65@gnj7a=xs7t05$w7q8!x_8zsld#
        DATABASE_NAME=db.sqlite3
    ```
- and in the *settings* file, I referenced it thus:
-   ```
        DATABASES = {
        ‘default’: {
        ‘ENGINE’: ‘django.db.backends.postgresql_psycopg2’,
        ‘NAME’: 'NAME': BASE_DIR / str(os.getenv('DATABASE_NAME')),

        <!-- ‘USER’: env(‘DATABASE_USER’),
        ‘PASSWORD’: env(‘DATABASE_PASS’), -->
        }
        }
    ```
- add the *.env* file to *.gitignore* using relative path

Visit [Click](https://www.toptal.com/developers/gitignore/api/python) to see more files to add to *.gitignore*

## Querrying the Database
- run the command, `python manage.py shell` to provide interactive shell
- do `from musicapp.models import *` to import all our models
- query commands:
-   ```
    artistes = Artiste.objects.all()
    print(artistes)
    artiste = Artiste(first_name="Zoro", last_name="Swagbagz", age=31) *the id is added by django*
    artiste.save()
    print(artistes.first()) *note that objects are returne FILO and not FIFO*
    artiste1 = Artiste.objects.get(first_name="Burna") *.get() returns only one item*
    print(artiste1.last_name)
    songs = artiste1.song_set.all()  *returns a list of all songs by artist1*
    *say we want to know which artiste own the first song in Song*
    song = Song.objects.first()
    print(song.artiste.first_name)
    lyrics = Lyric.objects.filter()
    print(lyrics)
    artiste2 = Artiste.objects.filter(first_name="Zoro", age=30)
    artiste1 = Artiste.objects.all().order_by('age') *order the artistes by there age*
    artiste1 = Artiste.objects.all().order_by('-age') *reverses the ordering*
    

    ```
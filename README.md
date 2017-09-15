# Week 3 Challenge Code Louisville 2017 Python/Django Cohort
Basic Django Project for the Fall 2017 Python Cohort serving the site from FEWD and extending functionality. louie\_pizza contains the full Django project.

For the original FEWD project see https://github.com/CodeLouisville/May2017-FEWD-Class-Project

# Challenge
The Code Louisville Louies Pizza FEWD project served content on one page. Let's break the various pieces of content (Newsletter, Menu, Contact, Homepage) into separate pages that we can use to learn more about Django. Each page should take advantage of the Django templating engine and inherited layouts with block content. 

The Homepage should be a simple landing page with Louie Pizza's history and operational links to the other pages.

The Newsletter should be it's own page and use the javascript email validation from the FEWD project, but is not functional beyond that at this point.

The Menu should be populated via Django models and categories/menu items should be added and managed via the Django Admin console.

Finally the contact page will not be available and will be setup at a later time using Django Forms.

# Set Up Python:
[https://www.python.org/downloads/](https://www.python.org/downloads/)

For Linux/MacOS you can use apt/yum or [brew to install](http://docs.python-guide.org/en/latest/starting/install3/osx/) also.

## Virtual Environments
We highly recommend using virtual environments for your python projects. Virtual environments isolates Python environments, including their dependencies, which means that if you install different versions of packages (which are dependencies, like Django) for different projects, they will not affect each other.

### Install `virtualenv`
You install `virtualenv` using `pip`. `pip` is a tool included with Python that installs Python packages from the Python Package Index, an online repository of Python packages:

    pip install virtualenv

Virtual environments are stored as regular directories, and it's common practice to create a folder named `virtualenvs` in your home folder or any other folder where you keep your programs.

OS X `virtualenvs` directory creation:

    mkdir ~/.virtualenvs
_Note: Directories starting with a `.` won't show up in the Finder GUI._

Windows `virtualenvs` directory creation:

    cd %HOMEPATH%
    mkdir .virtualenvs
_Note: Directories starting with a `.` won't show up in the Windows GUI._

Once you have a directory to store your virtual environments, you can create a new virtual environment for Louie Pizza:

OS X:

    virtualenv -p python3 ~/.virtualenvs/louie_pizza

Windows:

    virtualenv -p python3 %HOMEPATH%\.virtualenvs\louie_pizza

### Activate `virtualenv`
You will need to activate your virtual environment every time you open a new console. If you don't, `python` will use your system Python and its packages, not the `python` and packages in your virtual environment.

To activate the virtual environment in your console:

OS X:
    
    source ~/.virtualenvs/louie_pizza/bin/activate

Windows:

    source %HOMEPATH%\.virtualenvs\louie_pizza\Scripts\activate

And to deactivate:

    deactivate

## Django project setup
Have you set up a virtual environment? If not, follow the directions above or ask a mentor for help!

The official Django documentation can be found here:
https://docs.djangoproject.com/en/1.11/

The official Django intro tutorial can be found here, but our project is a little different:
https://docs.djangoproject.com/en/1.11/intro/tutorial01/

In your terminal activate your virtual environment and install Django:

    pip install django 

If you want to check if django is installed from the terminal:

    python -m django --version

Once you have Django installed navigate to your project directory in the command line/terminal and once you are in your project directory start your Django project by entering the command:

    django-admin startproject louie_pizza

In your python project directory you should now see a django project directory called louie\_pizza and a manage.py file. Your louie\_pizza project folder should have a subfolder named louie\_pizza as well as some key Python files:

 - \__init__.py
 - settings.py
 - urls.py
 - wsgi.py

Finally lets start the built in Django web server and make sure you can access your site locally.

    python manage.py runserver

You are now ready to take what you have learned from the Django Treehouse modules and convert the FEWD content to be served via the Django backend.

**Advanced project layout**
If you are feeling adventurous, you can use a more advanced project layout with your Django project. The one we'd recommend is from the authors of Two Scoops of Django. To use it, you'll need to install `cookiecutter`:

    pip install cookiecutter

To set up the project layout, run the following command and answer the questions:

    cookiecutter https://github.com/pydanny/cookiecutter-django

The Two Scoops of Django project layout isn't required, but it's more like what you'd see in a professional Django project.

# Solution
**Before proceeding it is suggested you have completed the Python, Python OOP, HTTP and Django Basics courses on treehouse**

You should have the [Code Louisville FEWD Project Content](https://github.com/CodeLouisville/May2017-FEWD-Class-Project) readily available to use for your static content (HTML, CSS, Images) and Javascript. If you have followed the Django setup instructions your will also have a project started where you can add your 

In your parent Django Directory you should begin by creating two HTML pages. One for the homepage, and one that will be a layout template with the header and footer content that all pages will inherit from.

Next we can create a Menu and Newsletter app for us to handle Louie Pizza's menu and newsletter functionality.

Within the Menus app view you should have a content block that will show each category on the menu, and for that category each related item. To accomplish this you can create a model for menu items and a model for categories with a foreign key association. Categories are the parent model and items are the child model. Once you have your models setup make sure to run your migration script and then using the Django Admin setup your menu categories and items. Finally in your view make use of Python script blocks and Django Models to expose the data you added in the Menus view.

One you have this app setup make sure to configure the appropriate URL routing with urls.py/views.py and add the app to settings.py. Start the web server and test that the menus page loads with the correct content and layout.

Within the Newsletters page you should have a content block with the newsletter subscription section from the original FEWD project. It should make use of the javascript email validation script that it was previously using, but as of now does not actually capture the email address.

As with the menus app setup your newsletters app routing and test that the page loads as expected.

# Running the project
If you just want to run the project (assuming Python is on your system and virtualenv) in your terminal:

    git clone https://github.com/AlexHagerman/code_louisville_django.git
    cd code_louisville_django
    virtualenv env
    activate env
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver

And navigate to 127.0.0.1:8000 in your browser
When you are ready to shutdown the server and exit the environment:

    ctrl+c
    exit

# Group9 in course D0020E@LTU
Project called WeBeddit.
## Install virtualenv and Django
First you have to install the virtual environment.
```
1. $ [sudo] pip install virtualenv
```
And then you need to make the directory where ```venv``` is the name of the directory.
```
2. $ python3 -m venv myvenv
```
When that's done, activate the venv, upgrade pip and install Django (we used Django 1.10.0).
```
3. $ source bin/activate
4. (myvenv) ~$ pip install --upgrade
5. (myvenv) ~$ pip install django~=1.10.0
```
For further documentation, visit https://docs.djangoproject.com/en/1.10/
### Installing Channels 

Channels is available on PyPI - to install it, just run::

    pip install -U channels

Once that's done, you should add ``channels`` to your
``INSTALLED_APPS`` setting::

    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        ...
        'channels',
    )
For further documentation, visit https://channels.readthedocs.io/en/stable/index.html

You will also have to install **Redis**.

Run ``python setup.py install`` to install,
or place ``django_redis`` on your Python path.

You can also install it with: ``pip install django-redis``

## Built With

* [Python](https://www.python.org/) - Python3 
* [Django](https://www.djangoproject.com/) - The web framework used.

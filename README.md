# django-orm-autodoc

The purpose of this library is the provide self-generating documenationt for
applications using Django's ORM in a standalone context. 

## Installation

If you connect to GitHub with ssh, install with:
```console
foo@bar:~ $ pipenv install git+ssh://git@github.com/rcarroll901/django-orm-autodoc.git#egg=django_orm_autodoc
```

Or do analgous command for https connection.

## CLI

When installed, an executable `django_autodoc` will be added to your `bin`.
Then we can specify the location where the models.py file is and where we
want our documenation to go. 

```console
foo@bar:~ $ django_autodoc --help
```

yields

![Screen Shot 2021-06-15 at 1 09 05 PM](https://user-images.githubusercontent.com/47673958/122102336-f01e1500-cdda-11eb-8d85-089d7d95f25b.png)

The default for `--models-path` is `"db.models"` and for `--output-path` is `"docs/db/"`. Again, note that `--models-path` should be in the form of a Python import.
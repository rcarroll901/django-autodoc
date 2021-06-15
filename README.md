# django-orm-autodoc

The purpose of this library is the provide self-generating documenationt for
applications using Django's ORM in a standalone context. 

## Installation

If you connect to GitHub with ssh, install with:
```console
foo@bar:~ $ pipenv install git+ssh://git@github.com/rcarroll901/django-orm-autodoc.git#egg=django_orm_autodoc
```

Or do analgous command for https connection.

## Inline Documentation

Documentation is generated from using the `help_text` argument of Django fields. All Django models within that module will be automatically detected, so listing out the models is not requred. For example:

```python
class Offices(models.Model):
    """Information about Offices"""

    name = models.CharField(
        max_length=40,
        unique=True,
        help_text="Name of the office (e.g. OFF01, OFF02, etc...",
    )
    munic_id = models.CharField(
        max_length=8,
        help_text="Name of the municipality that the office is within.",
    )  # should be FK to munic table
    n_workers = models.IntegerField(
        help_text="Number of total workerswithin the office"
    )

    class Meta:
        db_table = "offices"


class Workers(models.Model):
    """Whistleblower complaints filed with the MPT office"""

    office = models.ForeignKey(
        Offices,
        on_delete=models.CASCADE,
        help_text="Primary key of the office to which the complaint was filed.",
    )
    hiring_date = models.DateField(help_text="Date that the worker was hired")
    has_children = models.BooleanField(
        help_text="Whether or not the worker has children"
    )

    class Meta:
        db_table = "workers"
```
 will yield:

 ![Screen Shot 2021-06-15 at 1 19 29 PM](https://user-images.githubusercontent.com/47673958/122103580-666f4700-cddc-11eb-8508-c0c9bb624534.png)

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
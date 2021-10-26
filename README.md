# django-orm-autodoc

The purpose of this library is the provide self-generating documentation for
applications using Django's ORM in a standalone context. 

## Installation

If you connect to GitHub with ssh, install with:

```console
foo@bar:~ $ pipenv install git+ssh://git@github.com/rcarroll901/django-orm-autodoc.git#egg=django_orm_autodoc
```

Or do analgous command for https connection.

In your environment, define the path to the `settings.py` module in the usual Django way. If the app is standalone and you only have a `manage.py` (with `django.setup()` called after configuration is defined), then point to the `manage.py` in the analogous way.

## Inline Documentation

Documentation is generated from using the `help_text` argument of Django fields. All Django models within that module will be automatically detected, so listing out the models is not requred. For example:

```python
class Case(models.Model):
    """Each row in this table represents a single, unique case along with the
    highest level details about it. All updates on this table are done via the
    unique case number (case_num) found in Odyssey."""

    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        help_text="PK of person associated to case",
    )
    case_num = models.CharField(
        max_length=255,
        unique=True,
        help_text="Case identifier number. First two digits typically indicate the year the case was filed. Cases beginning with a letter are typically in Criminal Court as well as cases with IDs that have length > 10.",
    )
    file_date = models.DateField(
        null=True, help_text="Date that the case was created"
    )

    class Meta:
        db_table = "case"

```
 will yield:

![Screenshot from 2021-10-26 00-54-04](https://user-images.githubusercontent.com/47673958/138824403-bc16bafe-2edb-4690-876c-1e6b4436a87b.png)

Also note that the docstring of the model becomes the table description. The
module puts the CSS code next to the HTML, allowing the user to customize the
CSS and will not overwrite it.

## CLI

When installed, an executable `django_autodoc` will be added to your `bin`.
Then we can specify the location where the models.py file is and where we
want our documenation to go. 

```console
foo@bar:~ $ django_autodoc --help
```

yields

```text
Usage: django_autodoc [OPTIONS]

Options:
  -p, --models-path TEXT   Path to the Django models.py file in import 
                           notation (e.g. "db.models")
  -o, --output-path TEXT   Directory of where to output the HTML/CSS 
                           files
  --help                   Show this message and exit
```

The default for `--models-path` is `"db.models"` and for `--output-path` is `"docs/db/"`. Again, note that `--models-path` should be in the form of a Python import.
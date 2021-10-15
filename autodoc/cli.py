import os
import inspect
import sys
import shutil

import jinja2
import django
import click

# tell Django where to look for files and "start" app
sys.path.append(".")
sys.path.append("./package")
sys.path.append(os.getcwd())
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.core.wsgi import get_wsgi_application
from importlib import import_module

application = get_wsgi_application()


@click.command()
@click.option(
    "--models-path",
    "-p",
    default="db.models",
    help="Path to the Django models.py file in import notation (e.g. db.models)",
)
@click.option(
    "--output-path",
    "-o",
    default="docs/db/",
    help="Directory of where to output the documentation",
)
def main(models_path, output_path):
    """Finds the models in a models.py file and creates HTML documentation
    for schema from the help_text argument of Django models
    """

    # import the models module
    models_mod = import_module(models_path)

    # filter in all objects that are inherited from Django models
    my_models = {
        name: obj
        for name, obj in inspect.getmembers(models_mod)
        if type(obj) == django.db.models.base.ModelBase
    }

    # pass those models to a Jinja template to create documentation
    dir_path = os.path.dirname(os.path.realpath(__file__))
    style_path = os.path.join(dir_path, "style/")
    templateLoader = jinja2.FileSystemLoader(searchpath=style_path)
    templateEnv = jinja2.Environment(loader=templateLoader)
    TEMPLATE_FILE = "template.html"
    template = templateEnv.get_template(TEMPLATE_FILE)
    outputText = template.render(models=my_models.values())

    # make sure path to directory exists before writing docs
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # write the output to the html file
    with open(os.path.join(output_path, "docs.html"), "w") as fh:
        fh.write(outputText)

    # copy the style.css file with it so that user can edit CSS as wanted,
    # and also allow the HTML to find it easily
    path_to_style = os.path.join(output_path, "style.css")
    if not os.path.exists(path_to_style):
        shutil.copyfile(os.path.join(style_path, "style.css"), path_to_style)


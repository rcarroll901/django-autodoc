from autodoc.tools import PythonLiteralOption
import os
from datetime import date
import inspect
import sys
import shutil

import jinja2
import django
import click

# tell Django where to look for files and "start" app
sys.path.append(".")
sys.path.append(os.getcwd())
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

# get access to the tables for upload
from .tools import PythonLiteralOption


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

    models = __import__(models_path)

    models_mod = models.models

    my_models = {
        name: obj
        for name, obj in inspect.getmembers(models_mod)
        if type(obj) == django.db.models.base.ModelBase
    }

    dir_path = os.path.dirname(os.path.realpath(__file__))
    style_path = os.path.join(dir_path, "style/")
    templateLoader = jinja2.FileSystemLoader(searchpath=style_path)
    templateEnv = jinja2.Environment(loader=templateLoader)
    TEMPLATE_FILE = "template.html"
    template = templateEnv.get_template(TEMPLATE_FILE)
    outputText = template.render(models=my_models.values())

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    with open(os.path.join(output_path, "docs.html"), "w") as fh:
        fh.write(outputText)

    path_to_style = os.path.join(output_path, "style.css")
    if not os.path.exists(path_to_style):
        shutil.copyfile(os.path.join(style_path, "style.css"), path_to_style)

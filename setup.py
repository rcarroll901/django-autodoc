import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-orm-autodoc",
    author="Ryan Carroll",
    author_email="raec901@gmail.com",
    use_scm_version={
        "local_scheme": "node-and-date",
        "write_to": "autodoc/_version.py",
    },
    description="Package to create HTML documentation of Django models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rcarroll901/django-orm-autodoc",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Operating System :: MacOS",
    ],
    install_requires=["jinja2", "django", "click"],
    python_requires=">=3.6",
    entry_points={"console_scripts": ["django_autodoc=autodoc.cli:main"]},
    setup_requires=[
        "setuptools_scm>=3.3.1",
    ],
)

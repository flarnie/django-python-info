# Django Setup

## Installation

 1. [Install Python 2.6.5+][python-download] (Mac OSX likely has it installed by default.  [Here is a nice guide][get-python] for installing it with homebrew.)
 2. [Set up `pip`][pip-download] ([Installing Python with Homebrew]][homebrew-pip] automatically includes `pip`.)
 3. [Install virtual env with `pip`][install-v-env] and make an environment for your Django project(s).  Example usage:
 
 ```
 $ virtualenv my_django_projects
 $ cd my_django_projects
 $ . bin/activate
 ```
 
 This creates a directory for the `my_django_projects` environment, and
 activates it.  When you are done installing packages and working in that 
 environment, deactivate it with `deactivate`.
 
 4. [Install Django with `pip`][django-download]
 
 ```
 $ pip install Django==1.5.4
 ```
 
[python-download]: http://www.python.org/getit/
[get-python]: http://docs.python-guide.org/en/latest/starting/install/osx/
[pip-download]: http://www.pip-installer.org/en/latest/installing.html#python-os-support
[install-v-env]: https://pypi.python.org/pypi/virtualenv/
[homebrew-pip]: https://github.com/mxcl/homebrew/wiki/Homebrew-and-Python
[django-download]: https://www.djangoproject.com/download/

## Starting a Django Project

 1. In the project directory, with your virtualenv activated, enter `django-admin.py startproject project_title_here` 
 2. `cd` into the newly created project directory.
 3. That's it!  You can start creating models, views, and controllers.  (Although Django doesn't actually have "controllers"; but you get the idea.)
 
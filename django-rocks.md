# Strengths of Django

When considering Django for a project, think about whether you need some of it's most distinct and helpful features:

## Free Admin Interface

It's pretty awesome.  Just by creating the example app, (adding models with some relationships plus a config file), I get a full admin-side interface.

![admin dashboard][admin-ss-1]

![admin dashboard][admin-ss-2]

![admin dashboard][admin-ss-3]

[admin-ss-1]: https://github.com/paradasia/django-python-info/blob/master/django-admin-1.png
[admin-ss-2]: https://github.com/paradasia/django-python-info/blob/master/django-admin-2.png
[admin-ss-3]: https://github.com/paradasia/django-python-info/blob/master/django-admin-3.png

## Customizable Templating

The built-in templating style allows for PHP style inclusion of blocks of markup.  The template system can also be swapped out if you prefer another.

## Modularity

>"Projects vs. apps
>
What’s the difference between a project and an app? An app is a Web application that does something – e.g., a Weblog system, a database of public records or a simple poll app. A project is a collection of configuration and apps for a particular Web site. A project can contain multiple apps. An app can be in multiple projects.
>
>...
>
>Philosophy
>
Django apps are “pluggable”: You can use an app in multiple projects, and you can distribute apps, because they don’t have to be tied to a given Django installation.
"

From Django Tutorial[here][project-vs-app-q] and [here][django-philosophy]

The functionality you write for your app is modular by default.  At a deeper level, most components of Django can be swapped out, from the database query API to the Views.

[project-vs-app-q]: https://docs.djangoproject.com/en/1.5/intro/tutorial01/#creating-models
[django-philosophy]: https://docs.djangoproject.com/en/1.5/intro/tutorial01/#activating-models

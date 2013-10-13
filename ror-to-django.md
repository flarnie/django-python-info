# Ruby on Rails vs. Django

# Similarities

Many things are similar, but have different names and work slightly differently:

| Ruby on Rails          | Django        |
| ------------- |---------------|
| ActiveRecord              | ["database abstraction API"][db-query-api]  |
| Router | [URLConf][urls]; manually maps url strings to python functions, found in `urls.py` |
| transactions; `ActiveRecord::Base.transaction` | [transactions][django-transactions];'@transaction.atomic` |

[db-query-api]: https://docs.djangoproject.com/en/1.5/topics/db/queries/
[urls]: https://docs.djangoproject.com/en/1.5/topics/http/urls/
[django-transactions]: https://docs.djangoproject.com/en/dev/topics/db/transactions/

## Differences

### No DB Migrations

Ruby on Rails has **database migrations** for managing and changing the database.  It gives you a lot of control at the database level.

Django automatically generates tables base on your models.  To make major changes to the table structure, you have to drop the tables and start over.

Seriously.

There is a library called [South][south-package] that may help with this; it seems to implement Rails-like functionality for managing the Django database.

### Simpler Routing

The Django URLConf is much simpler than the Rails Router: it doesn't autogenerate resourceful routes, or nested routes.  You must hand-craft a python regex for each url.  (You can automate nesting somewhat by [including other URLConfs][including-other-url-confs] in the top-level URLConf.)



[south-package]: http://south.aeracode.org/
[including-other-url-confs]: https://docs.djangoproject.com/en/dev/topics/http/urls/#including-other-urlconfs

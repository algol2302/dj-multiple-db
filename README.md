# Dj-multiple-db

## Start:
Just pull and `docker-compose up`.

## Entrypoints:
* http://localhost:8000/csv - to export all readers
* http://localhost:8000/api/v1/reader - to get readers with these books

## Design
There are two databases: `default` and `replica`
Also, there are the most simple 'random'-router between databases to 
decrease load on app and increase performance. 
Requests random get access for one from two databases. 

## Problems: 
* File `gunicorn_run.sh` contains:
```
python manage.py migrate bookreaders 0001_initial
python manage.py migrate bookreaders 0001_initial --database=replica
```
it means that every start `docker-compose up` will run migrations.
it is very bad.

* Migrations are very slow.
* Api is not pretty. it is necessary to use nginx for static.
* Random router isn't good. I think that better way is to use something 
like https://github.com/jbalogh/django-multidb-router.

## Decisions
* I think that replication should use on postgres level, 
but now I don't know how. I need to google it :)
* Second way is to make 2 migrations with database check.
* May be something else... 
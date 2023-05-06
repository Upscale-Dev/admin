inspectdb:
	python manage.py inspectdb > models.py

startapp:
	python manage.py startapp $(appname)

run:
	python manage.py runserver
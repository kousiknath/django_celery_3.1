# django_celery_3.1

This is a very small celery 3.1 integration with django 1.7. The app illustrates automatic task registration from any 'celery_app' packages. Virtually, you can put any number of celery apps with a `celery_tasks/tasks.py` file inside that app. All functions inside that tasks.py file will be loaded as task.

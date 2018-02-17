from celery import Celery

app = Celery('echo')

app.config_from_object('echo.celery_settings')
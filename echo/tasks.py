from .celery_app import app


@app.task(bind=True)
def echo(self):
    return 'Echoing'

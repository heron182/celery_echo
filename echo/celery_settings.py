BROKER_URL = 'sqla+sqlite:///celery_broker.sqlite'
CELERY_RESULT_BACKEND = 'db+sqlite:///celery_results.db'
CELERY_TASK_ROUTES = {'echo.tasks.*': {'queue': 'echo-tasks'}}

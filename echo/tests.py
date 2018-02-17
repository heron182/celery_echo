import pytest

from .celery_app import app
from .celery_settings import (BROKER_URL, CELERY_RESULT_BACKEND,
                              CELERY_TASK_ROUTES)
from .tasks import echo


@pytest.fixture(scope='session')
def celery_config():
    return {
        'broker_url': BROKER_URL,
        'task_routes': CELERY_TASK_ROUTES,
        'result_backend': CELERY_RESULT_BACKEND
    }


def test_task_echo_is_consumed_by_worker(celery_app, celery_worker):
    result = echo.delay().get(timeout=5)
    assert result == 'Echoing'

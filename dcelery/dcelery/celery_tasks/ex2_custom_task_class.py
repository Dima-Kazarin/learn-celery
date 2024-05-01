import logging

from celery import Task
from dcelery.celery_config import app

logging.basicConfig(filename='app.log', level=logging.ERROR,
                    format='%(asctime)s %(levelname)s %(message)s')


class CustomTask(Task):
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        if isinstance(exc, ConnectionError):
            logging.error('Connection error occurred - Admin Notifed')
        else:
            print('{0!r} failed: {1!r}'.format(task_id, exc))


app.Task = CustomTask


@app.task(queue='tasks')
def my_task():
    try:
        raise ConnectionError('Connection Error Occurred...')
    except ConnectionError:
        raise ConnectionError()
    except ValueError:
        logging.error('Value error occurred...')

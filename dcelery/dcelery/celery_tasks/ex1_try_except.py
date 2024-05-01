from dcelery.celery_config import app
import logging

logging.basicConfig(filename='app.log', level=logging.ERROR,
                    format='%(asctime)s %(levelname)s %(message)s')


def perform_specific_error_handling():
    pass


@app.task(queue='tasks')
def my_task():
    try:
        raise ConnectionError('Connection Error Occurred...')
    except ConnectionError:
        logging.error('Connection error occurred...')
        raise ConnectionError()
    except ValueError:
        logging.error('Value error occurred...')
        perform_specific_error_handling()

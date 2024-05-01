from dcelery.celery_config import app
from time import sleep


@app.task(queue='tasks', time_limit=10)
def long_running_task():
    sleep(6)
    return 'Task completed successfully'


def execute_task_example():
    result = long_running_task.delay()
    try:
        task_result = result.get(timeout=40)
    except TimeoutError:
        print('Task timed out')

    task = long_running_task.delay()
    task.revoke(terminate=True)

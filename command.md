pip freeze > requirements.txt
docker-compose up -d --build
docker exec -it django /bin/sh

# Run on Django to inspect task
celery inspect active
celery inspect active_queues


from celery import group
from newapp.tasks import tp1,tp2,tp3,tp4
tasks_group = group(tp1.s(), tp2.s(), tp3.s(), tp4.s())
tasks_group.apply_async()


task_chain = chain(tp1.s(), tp2.s(), tp3.s())
task_chain.apply_async()


t2.apply_async(priority=5)
t1.apply_async(priority=6)
t3.apply_async(priority=9)
t2.apply_async(priority=5)
t1.apply_async(priority=6)
t3.apply_async(priority=9)
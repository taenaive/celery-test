from celery import Celery
from tasks.taskBasic.cel_main import TaskBasicQueue

app = Celery(
    "main",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379"
)

@app.task
def add(a,b):
    return a+b

@app.task
def TaskQueue(message):
    return TaskBasicQueue(message)
    #  return "My TaskBasicQueue: {0}".format(message)

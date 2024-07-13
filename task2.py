from celery import Celery

app = Celery(
    "task2",
    broker="redis://localhost:6379/1",
    backend="redis://localhost:6379"
)

@app.task
def addMoi(a,b):
    return a+b

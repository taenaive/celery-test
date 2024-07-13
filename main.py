from celery import Celery

app = Celery(
    "main",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379"
)

@app.task
def add(a,b):
    return a+b

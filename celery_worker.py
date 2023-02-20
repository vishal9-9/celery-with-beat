from celery_app import celery_app
from function import add_number


@celery_app.task(acks_late=True)
def perform_task():
    return add_number()


@celery_app.task
def check():
    print("I am checking your stuff")

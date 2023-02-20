from fastapi import FastAPI

from celery_worker import perform_task

app = FastAPI()


@app.get('/')
def start_task():
    perform_task.delay()
    return {"status": "Hello World"}

# celery -A celery_worker beat -l info
# celery --broker=redis://127.0.0.1:6379// flower
# python3 -m celery -A celery_worker worker -l info
# uvicorn main:app --reload --port=8001
# python3 -m celery -A celery_worker worker --beat -l info

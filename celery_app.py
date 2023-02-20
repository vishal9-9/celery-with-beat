from celery import Celery

celery_app = Celery('add_number', broker="redis://127.0.0.1:6379//")

celery_app.conf.task_routes = {
    'celery-final.celery_worker.add_number': 'add_number'
}

celery_app.conf.beat_schedule = {"run-me-every-ten-seconds":
                                 {"task": "celery_worker.check", "schedule": 10.0}}

celery_app.conf.update(task_track_started=True)

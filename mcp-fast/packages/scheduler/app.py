from celery import Celery
from env import *
import subprocess

# Celery configuration
scheduler_celery = Celery('scheduler', broker=REDIS_CELERY_BROKER)

# Optional: Add additional Celery configuration
scheduler_celery.conf.update(
    result_backend=REDIS_CELERY_BROKER,
    task_serializer='json',
    accept_content=['json'],
    timezone='UTC',
    enable_utc=True,
)


def start_celery_worker():
    command = [
        "celery",
        "-A",
        "packages.scheduler.app",
        "worker",
        "--loglevel=info"
    ]
    subprocess.run(command, check=True)

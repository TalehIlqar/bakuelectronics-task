from __future__ import absolute_import
from __future__ import unicode_literals

import logging
import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings


logger = logging.getLogger("Celery")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("app")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.beat_schedule = {
    "delete_blocked_ips": {
        "task": "users.tasks.delete_blocked_ips",
        "schedule": crontab(minute="*/1"),
    },
}

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))


app.conf.update(
    BROKER_URL="redis://localhost:6379/0",
    CELERYBEAT_SCHEDULER="django_celery_beat.schedulers:DatabaseScheduler",
    CELERY_DISABLE_RATE_LIMITS=True,
    CELERY_ACCEPT_CONTENT=[
        "json",
    ],
    CELERY_TASK_SERIALIZER="json",
    CELERY_TIMEZONE="Asia/Baku",
    DJANGO_CELERY_BEAT_DB_ALIAS="celery_db",
)

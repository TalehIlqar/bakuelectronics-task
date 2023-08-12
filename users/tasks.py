from .models import BlockedIP
from django.utils import timezone
from celery import shared_task


@shared_task
def delete_blocked_ips():
    time_threshold = timezone.now() - timezone.timedelta(hours=5)
    BlockedIP.objects.using("default").filter(created_at__lt=time_threshold).delete()

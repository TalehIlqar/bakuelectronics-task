from datetime import timedelta
from django.utils import timezone
from django.http import JsonResponse

from .models import BlockedIP


class CheckIPAddressMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        client_ip = self.get_client_ip(request)
        if BlockedIP.objects.filter(
            ip=client_ip,
        ).exists():
            return JsonResponse({"error": "IP is blocked"}, status=403)

        return self.get_response(request)

    @staticmethod
    def get_client_ip(request):
        return request.META.get("REMOTE_ADDR")

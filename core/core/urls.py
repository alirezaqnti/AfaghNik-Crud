import logging

from django.contrib import admin
from django.urls import path

logger = logging.getLogger(__name__)
logger.warning("this is a message")

urlpatterns = [
    path("admin/", admin.site.urls),
]

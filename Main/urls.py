from django.urls import path
from rest_framework import routers

from Main import views
from Main.api import DatasetViewSet

router = routers.DefaultRouter()
router.register("dataset", DatasetViewSet, "dataset")
urlpatterns = [
    path("", views.New_File.as_view(), name="New_File"),
    path("csrf/", views.get_csrf, name="get_csrf"),
    path(
        "new-proccess/",
        views.NewProccessAPIView.as_view(),
        name="NewProccess",
    ),
    path(
        "new-file/",
        views.UploadFiles.as_view(),
        name="UploadFiles",
    ),
]

urlpatterns += router.urls

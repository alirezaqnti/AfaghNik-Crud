import os
import pathlib
import shutil
from time import sleep
from zipfile import ZipFile

from django.conf import settings
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from Main.datasetProccess import NewProccess


def get_csrf(request):
    response = JsonResponse({"Info": "Success - Set CSRF cookie"})
    response["X-CSRFToken"] = get_token(request)
    return response


# region Proccess


class New_File(TemplateView):
    template_name = "index.html"


class UploadFiles(APIView):
    def post(self, request, *args, **kwargs):
        request.data
        return Response(status=status.HTTP_200_OK)


class NewProccessAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        files = data.getlist("files")
        for item in files:
            pathlib.Path(str(item)).suffix
            try:
                os.makedirs(os.path.join(settings.MEDIA_ROOT, "News"))
            except BaseException:
                pass
            output_path = os.path.join(settings.MEDIA_ROOT, "News")
            NewProccess(f"{output_path}/Titanic.xlsx")
            sleep(0.25)

        return Response(status=status.HTTP_200_OK)


# endregion

from typing import Iterable

from django.db import models
from django.utils.translation import gettext_lazy as _


class SingletonModel(models.Model):
    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)


class DataSetFile(SingletonModel):
    File = models.FileField(upload_to="Excel/", max_length=100)

    class Meta:
        verbose_name = _("DataSetFile")
        verbose_name_plural = _("DataSetFiles")


class Dataset(models.Model):
    PassengerId = models.IntegerField(default=0)
    Survived = models.IntegerField(default=0)
    Name = models.CharField(max_length=200, blank=True, null=True)
    Sex = models.CharField(max_length=5, blank=True, null=True)
    Age = models.CharField(max_length=3, blank=True, null=True)
    SibSp = models.CharField(max_length=3, blank=True, null=True)
    Pclass = models.CharField(max_length=2, blank=True, null=True)
    Parch = models.CharField(max_length=1, blank=True, null=True)
    Ticket = models.CharField(max_length=10, blank=True, null=True)
    Fare = models.CharField(max_length=20, blank=True, null=True)
    Cabin = models.CharField(max_length=5, blank=True, null=True)
    Embarked = models.CharField(max_length=1, blank=True, null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Dataset")
        verbose_name_plural = _("Datasets")

    def __str__(self):
        return self.Name
